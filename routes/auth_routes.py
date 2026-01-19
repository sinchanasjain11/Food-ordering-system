from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import Customer, Owner, db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/customer-login', methods=['GET', 'POST'])
def customer_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        customer = Customer.query.filter_by(email=email).first()
        
        if customer and check_password_hash(customer.password, password):
            login_user(customer)
            session['user_type'] = 'customer'
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('customer_login.html')

@auth_bp.route('/customer-register', methods=['GET', 'POST'])
def customer_register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Check if customer already exists
        if Customer.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return render_template('customer_register.html')
        
        # Create new customer
        hashed_password = generate_password_hash(password)
        customer = Customer(name=name, email=email, password=hashed_password)
        
        db.session.add(customer)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.customer_login'))
    
    return render_template('customer_register.html')

@auth_bp.route('/owner-login', methods=['GET', 'POST'])
def owner_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        owner = Owner.query.filter_by(email=email).first()
        
        if owner and check_password_hash(owner.password, password):
            if not owner.approved:
                flash('Your account is pending approval by admin', 'warning')
                return render_template('owner_login.html')
            
            login_user(owner)
            session['user_type'] = 'owner'
            flash('Login successful!', 'success')
            return redirect(url_for('owner.dashboard'))
        else:
            flash('Invalid email or password', 'error')
    
    return render_template('owner_login.html')

@auth_bp.route('/owner-register', methods=['GET', 'POST'])
def owner_register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        restaurant_name = request.form['restaurant_name']
        
        # Check if owner already exists
        if Owner.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return render_template('owner_register.html')
        
        # Create new owner
        hashed_password = generate_password_hash(password)
        owner = Owner(name=name, email=email, password=hashed_password, 
                     restaurant_name=restaurant_name, approved=False)
        
        db.session.add(owner)
        db.session.commit()
        
        flash('Registration successful! Please wait for admin approval.', 'success')
        return redirect(url_for('auth.owner_login'))
    
    return render_template('owner_register.html')

@auth_bp.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Simple admin credentials (in production, use proper admin model)
        if username == 'admin' and password == 'admin123':
            session['admin_logged_in'] = True
            flash('Admin login successful!', 'success')
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Invalid admin credentials', 'error')
    
    return render_template('admin_login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('index'))