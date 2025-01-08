import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234qwer@localhost:32770/information_schema'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from sqlalchemy import text

db = SQLAlchemy(app)

@app.route('/databases')
def list_databases():
    try:
        # Create a connection to the database
        with db.engine.connect() as connection:
            # Execute the query to show all databases
            result = connection.execute(text("SHOW TABLES;"))
            databases = [row[0] for row in result]  # Extract the first column (database names)
        return jsonify({"databases": databases})  # Return the databases as JSON
    except Exception as e:
        return 'Internal server error', 500  # Return an error message if the query fails

if __name__ == '__main__':
    app.run(debug=True)
