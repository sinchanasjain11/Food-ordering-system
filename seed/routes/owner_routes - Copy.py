from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from models.models import Dish, Order, OrderItem, db
import os

owner_bp = Blueprint('owner', __name__)

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@owner_bp.route('/owner-dashboard')
@login_required
def dashboard():
    if session.get('user_type') != 'owner':
        flash('Access denied', 'error')
        return redirect(url_for('index'))
    
    dishes = Dish.query.filter_by(owner_id=current_user.id).all()
    
    # Get orders for owner's dishes
    order_items = db.session.query(OrderItem).join(Dish).filter(Dish.owner_id == current_user.id).all()
    orders_data = {}
    
    for item in order_items:
        order_id = item.order_id
        if order_id not in orders_data:
            orders_data[order_id] = {
                'order': item.order,
                'items': [],
                'total': 0
            }
        orders_data[order_id]['items'].append(item)
        orders_data[order_id]['total'] += item.price * item.quantity
    
    return render_template('owner_dashboard.html', dishes=dishes, orders_data=orders_data)

@owner_bp.route('/add-dish', methods=['GET', 'POST'])
@login_required
def add_dish():
    if session.get('user_type') != 'owner':
        flash('Access denied', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = float(request.form['price'])
        stock = int(request.form['stock'])
        is_veg = 'is_veg' in request.form
        
        # Handle file upload
        image_path = 'default.jpg'
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Create unique filename
                import uuid
                filename = f"{uuid.uuid4().hex}_{filename}"
                
                # Ensure upload directory exists
                upload_dir = os.path.join('static', 'img', 'dishes')
                os.makedirs(upload_dir, exist_ok=True)
                
                file_path = os.path.join(upload_dir, filename)
                file.save(file_path)
                image_path = filename
        
        dish = Dish(
            name=name,
            description=description,
            price=price,
            stock=stock,
            image_path=image_path,
            is_veg=is_veg,
            owner_id=current_user.id
        )
        
        db.session.add(dish)
        db.session.commit()
        
        flash('Dish added successfully!', 'success')
        return redirect(url_for('owner.dashboard'))
    
    return render_template('add_dish.html')

@owner_bp.route('/edit-dish/<int:dish_id>', methods=['GET', 'POST'])
@login_required
def edit_dish(dish_id):
    if session.get('user_type') != 'owner':
        flash('Access denied', 'error')
        return redirect(url_for('index'))
    
    dish = Dish.query.get_or_404(dish_id)
    
    # Ensure owner can only edit their own dishes
    if dish.owner_id != current_user.id:
        flash('Access denied', 'error')
        return redirect(url_for('owner.dashboard'))
    
    if request.method == 'POST':
        dish.name = request.form['name']
        dish.description = request.form['description']
        dish.price = float(request.form['price'])
        dish.stock = int(request.form['stock'])
        dish.is_veg = 'is_veg' in request.form
        
        # Handle file upload
        if 'image' in request.files:
            file = request.files['image']
            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # Create unique filename
                import uuid
                filename = f"{uuid.uuid4().hex}_{filename}"
                
                # Ensure upload directory exists
                upload_dir = os.path.join('static', 'img', 'dishes')
                os.makedirs(upload_dir, exist_ok=True)
                
                file_path = os.path.join(upload_dir, filename)
                file.save(file_path)
                dish.image_path = filename
        
        db.session.commit()
        flash('Dish updated successfully!', 'success')
        return redirect(url_for('owner.dashboard'))
    
    return render_template('edit_dish.html', dish=dish)

@owner_bp.route('/delete-dish/<int:dish_id>', methods=['POST'])
@login_required
def delete_dish(dish_id):
    if session.get('user_type') != 'owner':
        flash('Access denied', 'error')
        return redirect(url_for('index'))
    
    dish = Dish.query.get_or_404(dish_id)
    
    # Ensure owner can only delete their own dishes
    if dish.owner_id != current_user.id:
        flash('Access denied', 'error')
        return redirect(url_for('owner.dashboard'))
    
    db.session.delete(dish)
    db.session.commit()
    
    flash('Dish deleted successfully!', 'success')
    return redirect(url_for('owner.dashboard'))