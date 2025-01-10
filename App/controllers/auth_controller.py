from flask import render_template, redirect, url_for, flash, session
from App.models.user import User
from App.forms.auth_forms import LoginForm
from App.db import db

def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Query the database for the user
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            # Save user information in the session
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('general_bp.index'))  # Redirect to home page
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('auth/login.html', form=form)
