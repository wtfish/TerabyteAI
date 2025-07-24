from App.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from App.models.role import Role

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # 
    # 0=highest; 3=lowest
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"),unique=False, nullable=False,default=3)
    role = db.relationship('Role', back_populates='users')

    password_hash = db.Column(db.Text(), nullable=False)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def has_permission(self, required_level):
        return self.role.level <= required_level

    def __repr__(self):
        return f"<User {self.username}>"