from flask import render_template, redirect, url_for, flash, request
from App.models.user import User
from flask_login import login_required, current_user
from App.db import db

@login_required
def index():
    return render_template('dashboard/dashboard.html',user=current_user)