from flask import render_template, redirect, url_for, flash, request
from App.models.user import User
from App.forms.auth_forms import LoginForm, RegisterForm
from flask_login import login_user,current_user,logout_user
from App.db import db

def login():
    # Initialize both forms
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_bp.index'))  # Redirect to a default page, e.g., the dashboard
    login_form = LoginForm(prefix='login')
    register_form = RegisterForm(prefix='register')
    

    # Handle Login Form Submission
    if request.method == 'POST' :

        if  'login-submit' in request.form and login_form.validate_on_submit():
            username = login_form.username.data
            password = login_form.password.data

            # Query the database for the user
            user = User.query.filter_by(username=username).first()

            if user and user.check_password(password):
                login_user(user)  # Log the user in
                # flash('Login successful!', 'success')
                # Handle the "next" parameter
                next_page = request.args.get('next')  # Get the 'next' parameter from the query string
                if next_page:
                    return redirect(next_page)  # Redirect to the original page
                return redirect(url_for('dashboard_bp.index'))  # Redirect to home page
            else:
                flash('Invalid username or password.', 'danger')

        # Handle Register Form Submission
        if 'register-submit' in request.form and register_form.validate_on_submit()  :
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
        login=login_form,
        register=register_form,
        request=request.form.to_dict(),
        stat='register-submit' in request.form
    )
def logout():
    if current_user.is_authenticated:
        logout_user()
        flash('You have been logged out.', 'success')
        return redirect(url_for('auth_bp.login'))
    else:
        flash('You are not logged in.', 'warning')
        return redirect(url_for('auth_bp.login'))
