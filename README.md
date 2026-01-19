# Smart Food - Food Ordering Web Application

A production-ready food ordering web application built with Python Flask and SQLite, featuring customer ordering, restaurant management, and admin controls.

## 🌟 Features

### Customer Features
- **User Registration & Login**: Secure customer authentication
- **Browse Menu**: View dishes with vegetarian/non-vegetarian tags
- **Search & Filter**: Find dishes by name and dietary preferences
- **Shopping Cart**: Add items, modify quantities, and manage cart
- **Order Placement**: Secure checkout process
- **Bill Generation**: Detailed invoice with order history
- **Order History**: View past orders and reorder functionality
- **Dark/Light Mode**: Toggle theme preference (saved in localStorage)

### Restaurant Owner Features
- **Owner Registration**: Apply to join the platform
- **Admin Approval**: Account activation by admin
- **Dish Management**: Add, edit, delete dishes with images
- **Inventory Control**: Manage stock levels
- **Order Tracking**: View orders for their dishes
- **Dashboard**: Comprehensive restaurant management interface

### Admin Features
- **Separate Admin Portal**: Accessible at `/admin-login`
- **Owner Approval**: Approve/reject restaurant applications
- **Content Moderation**: Delete any dish or restaurant
- **Order Overview**: Monitor all platform orders
- **System Management**: Full administrative control

## 🛠 Tech Stack

- **Backend**: Python Flask 2.3.3
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with CSS Variables for theming
- **Icons**: Font Awesome 6.0.0

## 📂 Project Structure

```
smart-food/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── INSTRUCTIONS.md      # Setup and usage guide
├── instance/            # Database storage
│   └── app.sqlite      # SQLite database file
├── static/             # Static assets
│   ├── css/
│   │   └── styles.css  # Main stylesheet
│   ├── js/
│   │   └── app.js      # JavaScript functionality
│   └── img/
│       └── dishes/     # Dish images storage
├── templates/          # Jinja2 templates
│   ├── base.html       # Base template
│   ├── index.html      # Homepage
│   ├── menu.html       # Menu listing
│   ├── dish_detail.html # Individual dish page
│   ├── cart.html       # Shopping cart
│   ├── checkout.html   # Checkout process
│   ├── bill.html       # Order invoice
│   ├── customer_*.html # Customer auth pages
│   ├── owner_*.html    # Owner pages
│   └── admin_*.html    # Admin pages
├── models/             # Database models
│   ├── __init__.py
│   └── models.py       # SQLAlchemy models
├── routes/             # Route handlers
│   ├── __init__.py
│   ├── auth_routes.py  # Authentication routes
│   ├── customer_routes.py # Customer functionality
│   ├── owner_routes.py # Owner dashboard
│   └── admin_routes.py # Admin panel
└── seed/               # Database seeding
    ├── __init__.py
    └── seed.py         # Sample data generator
```

## 🗄 Database Schema

### Tables
- **customers**: Customer accounts and profiles
- **owners**: Restaurant owner accounts
- **dishes**: Menu items with details and pricing
- **orders**: Customer order records
- **order_items**: Individual items within orders

### Relationships
- One-to-Many: Owner → Dishes
- One-to-Many: Customer → Orders
- One-to-Many: Order → OrderItems
- Many-to-One: OrderItem → Dish

## 🍽 Sample Data

The application comes pre-loaded with 5 restaurants:

1. **SpiceHub** (Indian Cuisine)
   - Veg: Paneer Curry, Masala Dosa, Samosa
   - Non-Veg: Biryani, Butter Chicken, Tandoori Chicken

2. **PizzaTown** (Fast Food)
   - Veg: Margherita Pizza, Pasta Alfredo
   - Non-Veg: Pepperoni Pizza, Chicken Burger

3. **SweetCorner** (Desserts)
   - All Veg: Gulab Jamun, Jalebi, Donut, Brownie, Ice Cream

4. **HealthyBites** (Diet Food)
   - Veg: Greek Salad, Idli, Poha
   - Non-Veg: Grilled Chicken Salad, Egg Omelette

5. **GrillHouse** (BBQ)
   - Veg: Grilled Paneer, Veg Manchurian
   - Non-Veg: BBQ Ribs, Shawarma, Buffalo Wings

## 🔐 Security Features

- Password hashing with Werkzeug
- Session-based authentication
- CSRF protection with Flask-WTF
- Input validation and sanitization
- Secure file upload handling
- Role-based access control

## 🎨 UI/UX Features

- Responsive design for all devices
- Dark/Light theme toggle
- Smooth animations and transitions
- Interactive flash messages
- Loading states for better UX
- Print-friendly bill layout

## 📱 Responsive Design

The application is fully responsive and works seamlessly on:
- Desktop computers
- Tablets
- Mobile phones
- Print media (for bills)

## 🚀 Performance Features

- Optimized database queries
- Efficient image handling
- Minimal JavaScript footprint
- CSS Grid and Flexbox layouts
- Debounced search functionality

## 🔧 Customization

The application is built with modularity in mind:
- Easy theme customization via CSS variables
- Modular route structure
- Extensible database models
- Configurable settings in `config.py`

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support and questions, please open an issue in the project repository.