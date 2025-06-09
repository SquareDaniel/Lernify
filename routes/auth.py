from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from extensions import db
from models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        is_teacher = 'is_teacher' in request.form
        user = User(username=username, is_teacher=is_teacher)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Регистрация успешна')
        return redirect(url_for('dashboard.index'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard.index'))
        flash('Неверные данные')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('courses.home'))