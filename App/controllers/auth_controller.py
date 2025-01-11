from flask import render_template, redirect, url_for, flash, request
from App.models.user import User
from App.forms.auth_forms import LoginForm, RegisterForm
from flask_login import login_user
from App.db import db

def login():
    # Initialize both forms
    login_form = LoginForm()
    register_form = RegisterForm()

    # Handle Login Form Submission
    if login_form.validate_on_submit() and 'login' in request.form:
        username = login_form.username.data
        password = login_form.password.data

        # Query the database for the user
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)  # Log the user in
            flash('Login successful!', 'success')
            return redirect(url_for('general_bp.index'))  # Redirect to home page
        else:
            flash('Invalid username or password.', 'danger')

    # Handle Register Form Submission
    if register_form.validate_on_submit() and 'register' in request.form:
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data

        # Check if the user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
        elif User.query.filter_by(email=email).first():
            flash('Email already registered.', 'danger')
        else:
            # Create a new user
            new_user = User(username=username, email=email)
            new_user.set_password(password)

            # Save the new user to the database
            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth_bp.login'))

    # Render the template with both forms
    return render_template(
        'auth/login.html',
        form=login_form,
        register=register_form
    )
