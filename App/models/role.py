from App.db import db
from werkzeug.security import generate_password_hash, check_password_hash

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    users = db.relationship('User', back_populates='role', lazy='dynamic')
    def __repr__(self):
        return f"<Role {self.role}>"