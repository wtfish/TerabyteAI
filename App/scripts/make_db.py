from sqlalchemy import create_engine, inspect
from App.db import db

def make_db(app):
    with app.app_context():
        # Create an engine for the database
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        
        # Check if the database exists
        inspector = inspect(engine)
        if 'terabyteAI' not in inspector.get_schema_names():
            # Create the database
            db.create_all()
            print("Database 'terabyteAI' initialized.")
        else:
            print("Database 'terabyteAI' already exists.")
        
        print("Run 'flask seed' to seed database with initial data.")
        print("Run 'flask run' to start the application.")
        print("Run 'flask init db' to seed database with initial data.")

if __name__ == '__main__':
    from App import create_app
    app = create_app()
    make_db(app)