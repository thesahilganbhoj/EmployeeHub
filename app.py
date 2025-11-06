import os
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, Employee
from sqlalchemy import or_

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SESSION_SECRET', 'dev-secret-key-change-in-production')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///E:/Tata Work Stuff/WorkingApp/SkillMatrix/instance/employees.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        employee_id = request.form.get('employee_id')
        employee = Employee.query.filter_by(employee_id=employee_id).first()
        
        if employee:
            login_user(employee)
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Invalid Employee ID. Please try again.', 'error')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.name = request.form.get('name')
        current_user.email = request.form.get('email')
        current_user.role = request.form.get('role')
        current_user.location = request.form.get('location')
        current_user.skills = request.form.get('skills')
        
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))
    
    return render_template('profile.html')

@app.route('/api/employees')
def get_employees():
    search = request.args.get('search', '').strip()
    available_only = request.args.get('available') == 'true'
    
    query = Employee.query
    
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                Employee.name.ilike(search_term),
                Employee.email.ilike(search_term),
                Employee.skills.ilike(search_term)
            )
        )
    
    if available_only:
        query = query.filter_by(is_available=True)
    
    employees = query.all()
    return jsonify([emp.to_dict() for emp in employees])

@app.route('/api/toggle-availability', methods=['POST'])
@login_required
def toggle_availability():
    current_user.is_available = not current_user.is_available
    db.session.commit()
    return jsonify({
        'success': True,
        'is_available': current_user.is_available
    })

@app.after_request
def add_header(response):
    if response.content_type and 'text/html' in response.content_type:
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
