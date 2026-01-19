from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.models import Owner, Dish, Order, Customer, db

admin_bp = Blueprint('admin', __name__)

def admin_required(f):
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            flash('Admin access required', 'error')
            return redirect(url_for('auth.admin_login'))
        return f(*args, **kwargs)
    decorated_function.__name__ = f.__name__
    return decorated_function

@admin_bp.route('/admin-dashboard')
@admin_required
def dashboard():
    pending_owners = Owner.query.filter_by(approved=False).all()
    approved_owners = Owner.query.filter_by(approved=True).all()
    all_dishes = Dish.query.all()
    all_orders = Order.query.order_by(Order.created_at.desc()).all()
    
    return render_template('admin_dashboard.html', 
                         pending_owners=pending_owners,
                         approved_owners=approved_owners,
                         all_dishes=all_dishes,
                         all_orders=all_orders)

@admin_bp.route('/approve-owner/<int:owner_id>', methods=['POST'])
@admin_required
def approve_owner(owner_id):
    owner = Owner.query.get_or_404(owner_id)
    owner.approved = True
    db.session.commit()
    
    flash(f'Owner {owner.name} approved successfully!', 'success')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/delete-owner/<int:owner_id>', methods=['POST'])
@admin_required
def delete_owner(owner_id):
    owner = Owner.query.get_or_404(owner_id)
    db.session.delete(owner)
    db.session.commit()
    
    flash(f'Owner {owner.name} deleted successfully!', 'success')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/admin-delete-dish/<int:dish_id>', methods=['POST'])
@admin_required
def delete_dish(dish_id):
    dish = Dish.query.get_or_404(dish_id)
    db.session.delete(dish)
    db.session.commit()
    
    flash(f'Dish {dish.name} deleted successfully!', 'success')
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/admin-logout')
@admin_required
def logout():
    session.pop('admin_logged_in', None)
    flash('Admin logged out successfully', 'info')
    return redirect(url_for('index'))