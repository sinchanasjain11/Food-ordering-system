from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
from models.models import db
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.customer_login'

# Import models
from models.models import Customer, Owner, Dish, Order, OrderItem

# Import routes
from routes.auth_routes import auth_bp
from routes.customer_routes import customer_bp
from routes.owner_routes import owner_bp
from routes.admin_routes import admin_bp

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(owner_bp)
app.register_blueprint(admin_bp)

@login_manager.user_loader
def load_user(user_id):
    user_type = session.get('user_type')
    if user_type == 'customer':
        return Customer.query.get(int(user_id))
    elif user_type == 'owner':
        return Owner.query.get(int(user_id))
    return None

@app.route('/')
def index():
    dishes = Dish.query.limit(6).all()
    return render_template('index.html', dishes=dishes)

@app.route('/menu')
def menu():
    search = request.args.get('search', '')
    filter_type = request.args.get('filter', 'all')
    
    query = Dish.query
    
    if search:
        query = query.filter(Dish.name.contains(search))
    
    if filter_type == 'veg':
        query = query.filter(Dish.is_veg == True)
    elif filter_type == 'non-veg':
        query = query.filter(Dish.is_veg == False)
    
    dishes = query.all()
    return render_template('menu.html', dishes=dishes, search=search, filter_type=filter_type)

@app.route('/dish/<int:dish_id>')
def dish_detail(dish_id):
    dish = Dish.query.get_or_404(dish_id)
    return render_template('dish_detail.html', dish=dish)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Run seed data if no dishes exist
        if not Dish.query.first():
            from seed.seed import seed_data
            seed_data()
    
    app.run(debug=True)