from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from flask_login import login_required, current_user
from models.models import Dish, Order, OrderItem, db
from datetime import datetime

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/cart')
@login_required
def cart():
    if session.get('user_type') != 'customer':
        flash('Access denied', 'error')
        return redirect(url_for('index'))
    
    cart_items = session.get('cart', {})
    cart_data = []
    total = 0
    
    for dish_id, quantity in cart_items.items():
        dish = Dish.query.get(int(dish_id))
        if dish:
            subtotal = dish.price * quantity
            cart_data.append({
                'dish': dish,
                'quantity': quantity,
                'subtotal': subtotal
            })
            total += subtotal
    
    return render_template('cart.html', cart_data=cart_data, total=total)

@customer_bp.route('/add-to-cart', methods=['POST'])
@login_required
def add_to_cart():
    if session.get('user_type') != 'customer':
        return jsonify({'success': False, 'message': 'Access denied'})
    
    dish_id = request.json.get('dish_id')
    quantity = request.json.get('quantity', 1)
    
    dish = Dish.query.get(dish_id)
    if not dish:
        return jsonify({'success': False, 'message': 'Dish not found'})
    
    if dish.stock < quantity:
        return jsonify({'success': False, 'message': 'Insufficient stock'})
    
    cart = session.get('cart', {})
    cart[str(dish_id)] = cart.get(str(dish_id), 0) + quantity
    session['cart'] = cart
    
    return jsonify({'success': True, 'message': 'Added to cart'})

@customer_bp.route('/update-cart', methods=['POST'])
@login_required
def update_cart():
    if session.get('user_type') != 'customer':
        return jsonify({'success': False, 'message': 'Access denied'})
    
    dish_id = request.json.get('dish_id')
    quantity = request.json.get('quantity')
    
    cart = session.get('cart', {})
    
    if quantity <= 0:
        cart.pop(str(dish_id), None)
    else:
        dish = Dish.query.get(dish_id)
        if dish and dish.stock >= quantity:
            cart[str(dish_id)] = quantity
        else:
            return jsonify({'success': False, 'message': 'Insufficient stock'})
    
    session['cart'] = cart
    return jsonify({'success': True})

@customer_bp.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    if session.get('user_type') != 'customer':
        flash('Access denied', 'error')
        return redirect(url_for('index'))
    
    cart_items = session.get('cart', {})
    if not cart_items:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('menu'))
    
    if request.method == 'POST':
        # Create order
        total_price = 0
        order_items_data = []
        
        for dish_id, quantity in cart_items.items():
            dish = Dish.query.get(int(dish_id))
            if dish and dish.stock >= quantity:
                subtotal = dish.price * quantity
                total_price += subtotal
                order_items_data.append({
                    'dish': dish,
                    'quantity': quantity,
                    'price': dish.price
                })
                # Update stock
                dish.stock -= quantity
            else:
                flash(f'Insufficient stock for {dish.name if dish else "unknown dish"}', 'error')
                return redirect(url_for('customer.cart'))
        
        # Create order record
        order = Order(
            customer_id=current_user.id,
            total_price=total_price,
            status='confirmed'
        )
        db.session.add(order)
        db.session.flush()  # Get order ID
        
        # Create order items
        for item_data in order_items_data:
            order_item = OrderItem(
                order_id=order.id,
                dish_id=item_data['dish'].id,
                quantity=item_data['quantity'],
                price=item_data['price']
            )
            db.session.add(order_item)
        
        db.session.commit()
        
        # Clear cart
        session['cart'] = {}
        
        flash('Order placed successfully!', 'success')
        return redirect(url_for('customer.bill', order_id=order.id))
    
    # GET request - show checkout page
    cart_data = []
    total = 0
    
    for dish_id, quantity in cart_items.items():
        dish = Dish.query.get(int(dish_id))
        if dish:
            subtotal = dish.price * quantity
            cart_data.append({
                'dish': dish,
                'quantity': quantity,
                'subtotal': subtotal
            })
            total += subtotal
    
    return render_template('checkout.html', cart_data=cart_data, total=total)

@customer_bp.route('/bill/<int:order_id>')
@login_required
def bill(order_id):
    if session.get('user_type') != 'customer':
        flash('Access denied', 'error')
        return redirect(url_for('index'))
    
    order = Order.query.get_or_404(order_id)
    
    # Ensure customer can only view their own bills
    if order.customer_id != current_user.id:
        flash('Access denied', 'error')
        return redirect(url_for('index'))
    
    return render_template('bill.html', order=order)

@customer_bp.route('/order-history')
@login_required
def order_history():
    if session.get('user_type') != 'customer':
        flash('Access denied', 'error')
        return redirect(url_for('index'))
    
    orders = Order.query.filter_by(customer_id=current_user.id).order_by(Order.created_at.desc()).all()
    return render_template('order_history.html', orders=orders)