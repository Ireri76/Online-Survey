import os
from flask import Flask, request, render_template, flash, redirect, url_for
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

# Get the MongoDB URI and database name from environment variables
uri = os.getenv('MONGODB_URI')
database_name = os.getenv('MONGODB_NAME')

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Initialize the MongoDB client and specify the database and collection
db = client[database_name]  # Use the database specified in environment variables
collection = db['Survey 2024']  # Use a collection named 'Survey 2024'

# Route to render the study overview and consent
@app.route('/')
def overview():
    return render_template('consent.html')

# Route to render the actual form after consent
@app.route('/form')
def form():
    return render_template('index.html')

# Data collection route
@app.route('/collect_data', methods=['POST'])
def collect_data():
    try:
        # Get user input
        age = int(request.form['age'])
        gender = request.form['gender']
        total_income = float(request.form['total_income'])
        
        # Gather expenses from the form
        expenses = {
            'utilities': float(request.form['utilities']) if request.form.get('utilities') else 0,
            'entertainment': float(request.form['entertainment']) if request.form.get('entertainment') else 0,
            'school_fees': float(request.form['school_fees']) if request.form.get('school_fees') else 0,
            'shopping': float(request.form['shopping']) if request.form.get('shopping') else 0,
            'healthcare': float(request.form['healthcare']) if request.form.get('healthcare') else 0
        }

        # Create a dictionary of the data
        BAN6420_data = {
            'age': age,
            'gender': gender,
            'total_income': total_income,
            'expenses': expenses
        }

        # Insert the data into MongoDB
        collection.insert_one(BAN6420_data)

        # Redirect to a success page after data submission
        return redirect(url_for('success'))

    except ValueError:
        # Flash a message if invalid data is entered
        flash("Please enter valid values for all fields.", "error")
        return redirect('/form')

# Success route to show the success message and provide a button to return to the form
@app.route('/success')
def success():
    return render_template('success.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
