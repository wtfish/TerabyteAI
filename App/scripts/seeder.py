from App import create_app
from App.db import db
from App.models.user import User

from App.db import db
from App.models.user import User

def seed_database(app):
    with app.app_context():
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', email='admin@example.com')
            admin.set_password('password')
            db.session.add(admin)
            db.session.commit()
            print("Admin user added successfully.")


        # Uncomment to add another user
        if not User.query.filter_by(username='user1').first():
            user1 = User(username='user1', email='user1@terabyteai.com', role=4)
            user1.set_password('1234qwer')
            db.session.add(user1)
            print("User1 added.")

        # Commit changes
        db.session.commit()
        print("Database seeded successfully.")

if __name__ == '__main__':
    seed_database()
