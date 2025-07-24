from App.db import db
from App.models.user import User
from App.models.role import Role

def seed_database(app):
    with app.app_context():
        roles = [
            {"id": 1, "name": "Super Admin", "description": "Full control over the application."},
            {"id": 2, "name": "Admin", "description": "Manages users and daily operations."},
            {"id": 3, "name": "Moderator", "description": "Moderates user content and reports."},
            {"id": 4, "name": "User", "description": "Standard user with basic access rights."},
        ]

        for role_data in roles:
            if not Role.query.filter_by(name=role_data['name']).first():
                role = Role(**role_data)
                db.session.add(role)

        db.session.commit()
        print("Role Table seeded successfully.")
    with app.app_context():
        if not User.query.filter_by(username='admin').first():
            admin_role = Role.query.filter_by(name='Super Admin').first()
            admin = User(username='admin', email='admin@terabyteai.com',role=admin_role)
            admin.set_password('password')
            db.session.add(admin)
            db.session.commit()
            print("Super Admin added successfully.")
        # Uncomment to add another user
        if not User.query.filter_by(username='moderator').first():
            moderator_role = Role.query.filter_by(name='Moderator').first()
            user1 = User(username='moderator', email='moderator@terabyteai.com', role=moderator_role)
            user1.set_password('1234qwer')
            db.session.add(user1)
            print("Moderator added.")
        if not User.query.filter_by(username='user').first():
            user_role = Role.query.filter_by(name='User').first()
            user1 = User(username='user', email='user@terabyteai.com', role=user_role)
            user1.set_password('1234qwer')
            db.session.add(user1)
            print("User added.")
        # Commit changes
        db.session.commit()
        print("User Table seeded successfully.")

if __name__ == '__main__':
    from App import create_app
    app=create_app()
    seed_database(app)
