from models.models import Owner, Dish, db
from werkzeug.security import generate_password_hash

def seed_data():
    """Seed the database with sample restaurants and dishes"""
    
    # Create sample restaurant owners
    owners_data = [
        {
            'name': 'Raj Kumar',
            'email': 'raj@spicehub.com',
            'password': 'password123',
            'restaurant_name': 'SpiceHub',
            'approved': True
        },
        {
            'name': 'Maria Giuseppe',
            'email': 'maria@pizzatown.com',
            'password': 'password123',
            'restaurant_name': 'PizzaTown',
            'approved': True
        },
        {
            'name': 'Amit Sharma',
            'email': 'amit@sweetcorner.com',
            'password': 'password123',
            'restaurant_name': 'SweetCorner',
            'approved': True
        },
        {
            'name': 'Dr. Sarah Wilson',
            'email': 'sarah@healthybites.com',
            'password': 'password123',
            'restaurant_name': 'HealthyBites',
            'approved': True
        },
        {
            'name': 'Ahmed Hassan',
            'email': 'ahmed@grillhouse.com',
            'password': 'password123',
            'restaurant_name': 'GrillHouse',
            'approved': True
        }
    ]
    
    owners = []
    for owner_data in owners_data:
        owner = Owner(
            name=owner_data['name'],
            email=owner_data['email'],
            password=generate_password_hash(owner_data['password']),
            restaurant_name=owner_data['restaurant_name'],
            approved=owner_data['approved']
        )
        db.session.add(owner)
        owners.append(owner)
    
    db.session.flush()  # Get owner IDs
    
    # Create sample dishes
    dishes_data = [
        # SpiceHub (Indian) - Owner ID 1
        {
            'name': 'Paneer Butter Masala',
            'description': 'Creamy and rich paneer curry with aromatic spices and butter',
            'price': 280.00,
            'stock': 25,
            'image_path': 'paneer-butter-masala.jpg',
            'is_veg': True,
            'owner_id': 1
        },
        {
            'name': 'Masala Dosa',
            'description': 'Crispy South Indian crepe filled with spiced potato filling',
            'price': 120.00,
            'stock': 30,
            'image_path': 'masala-dosa.jpg',
            'is_veg': True,
            'owner_id': 1
        },
        {
            'name': 'Samosa (2 pieces)',
            'description': 'Deep-fried pastry with spiced potato and pea filling',
            'price': 60.00,
            'stock': 50,
            'image_path': 'samosa.jpg',
            'is_veg': True,
            'owner_id': 1
        },
        {
            'name': 'Chicken Biryani',
            'description': 'Fragrant basmati rice cooked with tender chicken and aromatic spices',
            'price': 350.00,
            'stock': 20,
            'image_path': 'chicken-biryani.jpg',
            'is_veg': False,
            'owner_id': 1
        },
        {
            'name': 'Butter Chicken',
            'description': 'Tender chicken in creamy tomato-based curry sauce',
            'price': 320.00,
            'stock': 18,
            'image_path': 'butter-chicken.jpg',
            'is_veg': False,
            'owner_id': 1
        },
        {
            'name': 'Tandoori Chicken',
            'description': 'Marinated chicken grilled in traditional tandoor oven',
            'price': 380.00,
            'stock': 15,
            'image_path': 'tandoori-chicken.jpg',
            'is_veg': False,
            'owner_id': 1
        },
        
        # PizzaTown (Fast Food) - Owner ID 2
        {
            'name': 'Margherita Pizza',
            'description': 'Classic pizza with fresh tomatoes, mozzarella, and basil',
            'price': 250.00,
            'stock': 20,
            'image_path': 'margherita-pizza.jpg',
            'is_veg': True,
            'owner_id': 2
        },
        {
            'name': 'Pasta Alfredo',
            'description': 'Creamy fettuccine pasta with parmesan cheese and herbs',
            'price': 220.00,
            'stock': 25,
            'image_path': 'pasta-alfredo.jpg',
            'is_veg': True,
            'owner_id': 2
        },
        {
            'name': 'Pepperoni Pizza',
            'description': 'Classic pizza topped with spicy pepperoni and mozzarella',
            'price': 320.00,
            'stock': 18,
            'image_path': 'pepperoni-pizza.jpg',
            'is_veg': False,
            'owner_id': 2
        },
        {
            'name': 'Chicken Burger',
            'description': 'Juicy grilled chicken patty with lettuce, tomato, and mayo',
            'price': 180.00,
            'stock': 30,
            'image_path': 'chicken-burger.jpg',
            'is_veg': False,
            'owner_id': 2
        },
        
        # SweetCorner (Desserts) - Owner ID 3
        {
            'name': 'Gulab Jamun (4 pieces)',
            'description': 'Soft milk dumplings soaked in rose-flavored sugar syrup',
            'price': 80.00,
            'stock': 40,
            'image_path': 'gulab-jamun.jpg',
            'is_veg': True,
            'owner_id': 3
        },
        {
            'name': 'Jalebi',
            'description': 'Crispy spiral-shaped sweet soaked in sugar syrup',
            'price': 100.00,
            'stock': 35,
            'image_path': 'jalebi.jpg',
            'is_veg': True,
            'owner_id': 3
        },
        {
            'name': 'Chocolate Donut',
            'description': 'Soft glazed donut with rich chocolate coating',
            'price': 60.00,
            'stock': 25,
            'image_path': 'chocolate-donut.jpg',
            'is_veg': True,
            'owner_id': 3
        },
        {
            'name': 'Chocolate Brownie',
            'description': 'Rich and fudgy chocolate brownie with nuts',
            'price': 120.00,
            'stock': 20,
            'image_path': 'chocolate-brownie.jpg',
            'is_veg': True,
            'owner_id': 3
        },
        {
            'name': 'Vanilla Ice Cream',
            'description': 'Creamy vanilla ice cream made with real vanilla beans',
            'price': 90.00,
            'stock': 30,
            'image_path': 'vanilla-ice-cream.jpg',
            'is_veg': True,
            'owner_id': 3
        },
        
        # HealthyBites (Diet Food) - Owner ID 4
        {
            'name': 'Greek Salad Bowl',
            'description': 'Fresh mixed greens with feta cheese, olives, and olive oil dressing',
            'price': 180.00,
            'stock': 25,
            'image_path': 'greek-salad.jpg',
            'is_veg': True,
            'owner_id': 4
        },
        {
            'name': 'Steamed Idli (4 pieces)',
            'description': 'Soft and fluffy South Indian rice cakes served with chutney',
            'price': 80.00,
            'stock': 35,
            'image_path': 'idli.jpg',
            'is_veg': True,
            'owner_id': 4
        },
        {
            'name': 'Poha',
            'description': 'Light and healthy flattened rice with vegetables and spices',
            'price': 70.00,
            'stock': 30,
            'image_path': 'poha.jpg',
            'is_veg': True,
            'owner_id': 4
        },
        {
            'name': 'Grilled Chicken Salad',
            'description': 'Protein-rich salad with grilled chicken breast and fresh vegetables',
            'price': 250.00,
            'stock': 20,
            'image_path': 'grilled-chicken-salad.jpg',
            'is_veg': False,
            'owner_id': 4
        },
        {
            'name': 'Egg Omelette',
            'description': 'Fluffy omelette with herbs and vegetables',
            'price': 100.00,
            'stock': 25,
            'image_path': 'egg-omelette.jpg',
            'is_veg': False,
            'owner_id': 4
        },
        
        # GrillHouse (BBQ) - Owner ID 5
        {
            'name': 'Grilled Paneer Tikka',
            'description': 'Marinated paneer cubes grilled with bell peppers and onions',
            'price': 220.00,
            'stock': 20,
            'image_path': 'paneer-tikka.jpg',
            'is_veg': True,
            'owner_id': 5
        },
        {
            'name': 'Veg Manchurian',
            'description': 'Deep-fried vegetable balls in tangy Indo-Chinese sauce',
            'price': 160.00,
            'stock': 25,
            'image_path': 'veg-manchurian.jpg',
            'is_veg': True,
            'owner_id': 5
        },
        {
            'name': 'BBQ Ribs',
            'description': 'Tender pork ribs glazed with smoky barbecue sauce',
            'price': 450.00,
            'stock': 12,
            'image_path': 'bbq-ribs.jpg',
            'is_veg': False,
            'owner_id': 5
        },
        {
            'name': 'Chicken Shawarma',
            'description': 'Middle Eastern wrap with grilled chicken and garlic sauce',
            'price': 180.00,
            'stock': 22,
            'image_path': 'chicken-shawarma.jpg',
            'is_veg': False,
            'owner_id': 5
        },
        {
            'name': 'Buffalo Wings (6 pieces)',
            'description': 'Spicy chicken wings with buffalo sauce and blue cheese dip',
            'price': 280.00,
            'stock': 18,
            'image_path': 'buffalo-wings.jpg',
            'is_veg': False,
            'owner_id': 5
        }
    ]
    
    # Create dishes
    for dish_data in dishes_data:
        dish = Dish(**dish_data)
        db.session.add(dish)
    
    db.session.commit()
    print("Database seeded successfully with sample data!")
    print(f"Created {len(owners)} restaurant owners")
    print(f"Created {len(dishes_data)} dishes")
    
    # Print owner credentials for testing
    print("\n=== Test Credentials ===")
    print("Restaurant Owner Logins:")
    for owner_data in owners_data:
        print(f"Email: {owner_data['email']} | Password: password123")
    
    print("\nAdmin Login:")
    print("Username: admin | Password: admin123")
    
    print("\nCustomer Registration:")
    print("Register as a customer to place orders")