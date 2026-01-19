# Smart Food - Setup and Usage Instructions

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access the Application**
   - Open your web browser
   - Navigate to: `http://localhost:5000`
   - The application will automatically create the database and seed sample data

## 🔑 Default Login Credentials

### Admin Access
- **URL**: `http://localhost:5000/admin-login`
- **Username**: `admin`
- **Password**: `admin123`

### Restaurant Owner Accounts (Pre-created)
| Restaurant | Email | Password |
|FrozenBites|alex@frozenbites.com | password123 |
| SpiceHub| raj@spicehub.com | password123 |
| PizzaTown | maria@pizzatown.com | password123 |
| SweetCorner | amit@sweetcorner.com | password123 |
| HealthyBites | sarah@healthybites.com | password123 |
| GrillHouse | ahmed@grillhouse.com | password123 |

### Customer Account
- Register a new customer account at: `http://localhost:5000/customer-register`
- Or use the customer login page to create an account

## 📋 File and Folder Explanation

### Core Application Files
- **`app.py`**: Main Flask application with routes and configuration
- **`config.py`**: Application configuration settings
- **`requirements.txt`**: Python package dependencies

### Database
- **`instance/app.sqlite`**: SQLite database file (auto-created)
- **`models/models.py`**: Database table definitions using SQLAlchemy

### Routes (URL Handlers)
- **`routes/auth_routes.py`**: Login/logout/registration functionality
- **`routes/customer_routes.py`**: Customer features (cart, orders, checkout)
- **`routes/owner_routes.py`**: Restaurant owner dashboard and dish management
- **`routes/admin_routes.py`**: Admin panel for system management

### Templates (HTML Pages)
- **`templates/base.html`**: Common layout for all pages
- **`templates/index.html`**: Homepage with featured dishes
- **`templates/menu.html`**: Full menu with search and filters
- **`templates/cart.html`**: Shopping cart management
- **`templates/checkout.html`**: Order placement form
- **`templates/bill.html`**: Order invoice/receipt

### Static Assets
- **`static/css/styles.css`**: All styling with dark/light theme support
- **`static/js/app.js`**: JavaScript for interactivity and theme switching
- **`static/img/dishes/`**: Storage folder for dish images

### Data Seeding
- **`seed/seed.py`**: Creates sample restaurants and dishes on first run

## 🏪 How to Add New Restaurants/Owners

### Method 1: Through Admin Panel (Recommended)
1. New restaurant owners register at `/owner-register`
2. Admin logs in at `/admin-login`
3. Admin approves the new owner in the "Pending Approvals" tab
4. Owner can now log in and add dishes

### Method 2: Direct Database Addition
1. Stop the application
2. Add owner data in `seed/seed.py`
3. Delete `instance/app.sqlite`
4. Restart the application (will recreate database with new data)

## 🍽 How to Add New Dishes

### Through Owner Dashboard
1. Log in as a restaurant owner
2. Go to "Add New Dish" tab
3. Fill in dish details:
   - Name and description
   - Price and stock quantity
   - Upload image (optional)
   - Mark as vegetarian/non-vegetarian
4. Click "Add Dish"

### Supported Image Formats
- PNG, JPG, JPEG, GIF
- Maximum file size: 16MB
- Images are automatically renamed to prevent conflicts

## 📸 How to Add Dish Photos

### 📁 Photo Directory Location
All dish images should be placed in: **`static/img/dishes/`**

### Method 1: Direct File Placement (Recommended for Pre-loaded Dishes)

The application comes with pre-loaded sample dishes that reference specific image names. To add real photos for these dishes:

1. **Navigate to the images folder:**
   ```
   c:\Users\vaish\OneDrive\Desktop\food1\static\img\dishes\
   ```

2. **Add images with these exact filenames:**

   **SpiceHub (Indian Restaurant):**
   - `paneer-butter-masala.jpg`
   - `masala-dosa.jpg`
   - `samosa.jpg`
   - `chicken-biryani.jpg`
   - `butter-chicken.jpg`
   - `tandoori-chicken.jpg`

   **PizzaTown (Fast Food):**
   - `margherita-pizza.jpg`
   - `pasta-alfredo.jpg`
   - `pepperoni-pizza.jpg`
   - `chicken-burger.jpg`

   **SweetCorner (Desserts):**
   - `gulab-jamun.jpg`
   - `jalebi.jpg`
   - `chocolate-donut.jpg`
   - `chocolate-brownie.jpg`
   - `vanilla-ice-cream.jpg`

   **HealthyBites (Diet Food):**
   - `greek-salad.jpg`
   - `idli.jpg`
   - `poha.jpg`
   - `grilled-chicken-salad.jpg`
   - `egg-omelette.jpg`

   **GrillHouse (BBQ):**
   - `paneer-tikka.jpg`
   - `veg-manchurian.jpg`
   - `bbq-ribs.jpg`
   - `chicken-shawarma.jpg`
   - `buffalo-wings.jpg`

3. **Restart the application** to see the new images

### Method 2: Upload Through Web Interface

1. **Start the application:** `python app.py`
2. **Login as restaurant owner** (see credentials above)
3. **Go to Owner Dashboard**
4. **Click "Add New Dish" or "Edit" existing dish**
5. **Use the image upload field**
6. **Images appear immediately (no restart needed)**

### 🖼️ Image Requirements

**Supported Formats:**
- PNG, JPG, JPEG, GIF
- Maximum file size: 16MB

**Recommended Specifications:**
- **Resolution:** 800x600 pixels or higher
- **Aspect ratio:** 4:3 or 16:9 (looks best in the layout)
- **File size:** Under 2MB for faster loading
- **Quality:** High quality, well-lit food photos work best

### 📋 Step-by-Step Photo Addition Example

**To add a photo for "Paneer Butter Masala":**

1. **Get your image file** (e.g., `my-paneer-photo.jpg`)
2. **Rename it to:** `paneer-butter-masala.jpg`
3. **Copy it to:** `static\img\dishes\` folder
4. **Restart the application**
5. **Visit the menu page** - your image will now appear

### 🔄 Image Management

**Current Status:**
- All dishes currently use `default.jpg` as placeholder
- You can replace this with actual food photos

**Where Images Appear:**
- Homepage (featured dishes section)
- Menu page (all dishes)
- Individual dish detail pages
- Shopping cart
- Checkout page
- Order history
- Bills/Invoices

**File Organization:**
```
static/
└── img/
    └── dishes/
        ├── default.jpg (placeholder)
        ├── paneer-butter-masala.jpg
        ├── chicken-biryani.jpg
        ├── margherita-pizza.jpg
        └── ... (other dish images)
```

### 🎯 Pro Tips for Adding Photos

1. **Use descriptive filenames** that match your dish names
2. **Optimize images** before uploading (compress to reduce file size)
3. **Consistent styling** - use similar lighting and angles for professional look
4. **Backup originals** - keep original high-resolution images separately
5. **Test on mobile** - ensure images look good on all devices

### 🚨 Troubleshooting Images

**Image not showing?**
- Check filename spelling (case-sensitive)
- Verify file is in correct folder: `static/img/dishes/`
- Ensure supported format (JPG, PNG, GIF)
- Restart application after adding files directly

**Image too large?**
- Resize to max 1200x900 pixels
- Compress using online tools or image editors
- Keep under 2MB for best performance

**Upload not working?**
- Check file size (max 16MB)
- Verify internet connection
- Try different image format
- Clear browser cache and retry

## 🗄 Database Setup Details

### Automatic Setup
- Database is created automatically on first run
- Tables are generated from SQLAlchemy models
- Sample data is seeded if database is empty

### Manual Database Reset
```bash
# Stop the application
# Delete the database file
rm instance/app.sqlite
# Restart the application
python app.py
```

### Database Location
- SQLite file: `instance/app.sqlite`
- Can be opened with any SQLite browser for direct access

## 🎨 Theme Customization

### CSS Variables (in `static/css/styles.css`)
```css
:root {
    --primary-color: #ff6b35;    /* Main brand color */
    --secondary-color: #2c3e50;  /* Secondary brand color */
    --success-color: #27ae60;    /* Success messages */
    --danger-color: #e74c3c;     /* Error messages */
}
```

### Dark Theme
- Automatically switches based on user preference
- Saved in browser localStorage
- Toggle button in navigation bar

## 🔧 Configuration Options

### Environment Variables (Optional)
```bash
export SECRET_KEY="your-secret-key-here"
export DATABASE_URL="sqlite:///path/to/database.db"
```

### Config File (`config.py`)
- `SECRET_KEY`: For session security (change in production)
- `SQLALCHEMY_DATABASE_URI`: Database connection string
- `UPLOAD_FOLDER`: Directory for uploaded images
- `MAX_CONTENT_LENGTH`: Maximum file upload size

## 🚨 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Run on different port
   flask run --port 5001
   ```

2. **Database Errors**
   ```bash
   # Reset database
   rm instance/app.sqlite
   python app.py
   ```

3. **Missing Dependencies**
   ```bash
   # Reinstall requirements
   pip install -r requirements.txt --force-reinstall
   ```

4. **Image Upload Issues**
   - Ensure `static/img/dishes/` directory exists
   - Check file permissions
   - Verify file format is supported

### Debug Mode
- Application runs in debug mode by default
- Automatic reloading on code changes
- Detailed error messages in browser

## 📱 Testing the Application

### Customer Flow
1. Register as customer → Login
2. Browse menu → Search/filter dishes
3. Add items to cart → Modify quantities
4. Checkout → Place order
5. View bill → Check order history

### Owner Flow
1. Register restaurant → Wait for admin approval
2. Login → Add dishes with images
3. Manage inventory → Update prices/stock
4. View orders → Track sales

### Admin Flow
1. Login to admin panel
2. Approve pending restaurant owners
3. Monitor all orders
4. Delete inappropriate content

## 👨‍💼 Admin Panel - How to Approve Restaurant Owners

### 🔐 Admin Access
1. **Navigate to Admin Login:**
   - URL: `http://localhost:5000/admin-login`
   - **Username:** `admin`
   - **Password:** `admin123`

2. **Admin Dashboard Overview:**
   - After login, you'll see the Admin Dashboard with 4 tabs:
     - **Pending Approvals** (new restaurant requests)
     - **Approved Owners** (active restaurants)
     - **All Dishes** (manage all dishes)
     - **All Orders** (view all customer orders)

### 📋 Step-by-Step: Approving New Restaurant Owners

#### Step 1: New Owner Registration Process
1. **Restaurant owner registers** at `/owner-register`
2. **Owner fills registration form:**
   - Owner name
   - Restaurant name
   - Email address
   - Password
3. **System creates account** with `approved = False` status
4. **Owner cannot login** until admin approval

#### Step 2: Admin Reviews Pending Requests
1. **Login to admin panel** (`/admin-login`)
2. **Click "Pending Approvals" tab** (default view)
3. **Review pending restaurant applications:**
   - Owner name
   - Restaurant name
   - Email address
   - Registration date

#### Step 3: Approve or Reject Owners
**To Approve:**
1. **Click "Approve" button** next to the restaurant owner
2. **System updates** `approved = True` in database
3. **Success message** appears: "Owner [Name] approved successfully!"
4. **Owner can now login** and access their dashboard

**To Reject/Delete:**
1. **Click "Delete" button** next to the restaurant owner
2. **Confirm deletion** in popup dialog
3. **Owner account is permanently removed**
4. **Success message** appears: "Owner [Name] deleted successfully!"

### 🏪 Managing Approved Restaurants

#### View Approved Owners
1. **Click "Approved Owners" tab**
2. **See all active restaurants:**
   - Owner details
   - Restaurant name
   - Number of dishes they've added
   - Approval date

#### Remove Approved Owners
1. **In "Approved Owners" tab**
2. **Click "Delete Owner" button**
3. **Confirm deletion** (this removes owner AND all their dishes)
4. **Owner loses access immediately**

### 🍽️ Content Moderation

#### Delete Individual Dishes
1. **Click "All Dishes" tab**
2. **Browse all dishes** from all restaurants
3. **Click "Delete" button** on inappropriate dishes
4. **Dish is removed** from all menus immediately

#### Monitor All Orders
1. **Click "All Orders" tab**
2. **View complete order history:**
   - Customer details
   - Items ordered
   - Restaurant information
   - Order totals and dates

### 🔄 Admin Workflow Example

**Scenario: New Restaurant "Tasty Bites" Wants to Join**

1. **Owner Registration:**
   ```
   Name: John Smith
   Restaurant: Tasty Bites
   Email: john@tastybites.com
   Password: [chosen by owner]
   ```

2. **Admin Review Process:**
   - Admin logs in → sees "Tasty Bites" in Pending Approvals
   - Reviews restaurant name and owner details
   - Decides to approve

3. **Approval Action:**
   - Admin clicks "Approve" button
   - System shows: "Owner John Smith approved successfully!"
   - John can now login at `/owner-login`

4. **Post-Approval:**
   - John logs in → accesses Owner Dashboard
   - John adds dishes with photos and prices
   - Customers can now see and order from Tasty Bites

### 🚨 Admin Best Practices

#### Before Approving:
- **Verify restaurant name** is appropriate and professional
- **Check email format** is valid business email
- **Ensure no duplicate** restaurant names
- **Consider local regulations** if applicable

#### Regular Monitoring:
- **Check pending approvals** daily
- **Review new dishes** for inappropriate content
- **Monitor order patterns** for suspicious activity
- **Maintain approved owner list** up to date

#### Security Measures:
- **Change default admin password** in production
- **Log admin actions** for audit trail
- **Regular database backups**
- **Monitor for spam registrations**

### 📊 Admin Dashboard Features

#### Pending Approvals Tab
```
┌─────────────────────────────────────────────────┐
│ Pending Owner Approvals                         │
├─────────────────────────────────────────────────┤
│ John Smith                                      │
│ Restaurant: Tasty Bites                         │
│ Email: john@tastybites.com                      │
│ Registered: December 15, 2024                   │
│ [Approve] [Delete]                              │
├─────────────────────────────────────────────────┤
│ Maria Garcia                                    │
│ Restaurant: Authentic Tacos                     │
│ Email: maria@authentictacos.com                 │
│ Registered: December 14, 2024                   │
│ [Approve] [Delete]                              │
└─────────────────────────────────────────────────┘
```

#### Approved Owners Tab
```
┌─────────────────────────────────────────────────┐
│ Approved Restaurant Owners                      │
├─────────────────────────────────────────────────��
│ Raj Kumar                                       │
│ Restaurant: SpiceHub                            │
│ Email: raj@spicehub.com                         │
│ Dishes: 6                                       │
│ Approved: December 1, 2024                      │
│ [Delete Owner]                                  │
└─────────────────────────────────────────────────┘
```

### 🔧 Admin Troubleshooting

**Can't see pending approvals?**
- Check if owners completed registration
- Verify admin login credentials
- Refresh the page

**Approval not working?**
- Check database connection
- Verify admin permissions
- Look for error messages in browser console

**Owner still can't login after approval?**
- Confirm approval was successful
- Check owner is using correct credentials
- Verify owner is trying `/owner-login` not `/customer-login`

### 📝 Admin Notes

- **Immediate Effect:** Approvals take effect immediately
- **Email Notifications:** Currently no automatic emails (can be added)
- **Bulk Actions:** Currently one-by-one approval (can be enhanced)
- **Audit Trail:** Admin actions are logged in database
- **Backup Strategy:** Regular database backups recommended

## 🔒 Security Considerations

### For Production Deployment
1. Change default admin credentials
2. Set strong SECRET_KEY
3. Use environment variables for sensitive data
4. Enable HTTPS
5. Set up proper file upload validation
6. Configure database backups

### Current Security Features
- Password hashing (Werkzeug)
- CSRF protection (Flask-WTF)
- Session-based authentication
- Input validation
- File upload restrictions

## 📊 Performance Tips

### For Better Performance
1. Use a production WSGI server (Gunicorn, uWSGI)
2. Set up database connection pooling
3. Implement caching (Redis, Memcached)
4. Optimize images (compression, CDN)
5. Enable gzip compression

### Current Optimizations
- Efficient database queries
- Minimal JavaScript
- CSS Grid/Flexbox layouts
- Debounced search
- Lazy loading considerations

## 🆘 Getting Help

### If You Encounter Issues
1. Check the console for error messages
2. Verify all dependencies are installed
3. Ensure Python version compatibility
4. Check file permissions
5. Review the troubleshooting section

### Development Tips
- Use browser developer tools for debugging
- Check Flask debug output in terminal
- Verify database content with SQLite browser
- Test with different user roles
- Validate responsive design on various devices

## 🎯 Next Steps

After successful setup, you can:
1. Customize the styling and branding
2. Add more restaurant categories
3. Implement payment integration
4. Add email notifications
5. Create mobile app APIs
6. Set up automated testing
7. Deploy to production server

## 📝 Notes

- The application uses SQLite for simplicity
- All uploaded images are stored locally
- Session data is stored server-side
- Theme preference is stored in browser localStorage
- Default images are placeholders (add real images as needed)