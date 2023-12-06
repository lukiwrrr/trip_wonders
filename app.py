from flask import Flask,redirect,url_for,render_template,request, jsonify
from pymongo import MongoClient

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

app = Flask(__name__)

MONGODB_CONNECTION_STRING = MONGODB_URI

client = MongoClient(MONGODB_CONNECTION_STRING)

db = client[DB_NAME]

client = MongoClient('mongodb+srv://test:<password>@cluster0.o4hcjp6.mongodb.net/?retryWrites=true&w=majority')
db = client['trip_wonders']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.json
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        doc_count = collection.count_documents({})

        # Simpan data ke MongoDB
        if password == confirm_password:
            current_time = datetime.now()
            unique_date = current_time.strftime("%d-%m-%Y | %H.%M.%S")
            
            user_data = {
                '_id': doc_count + 1,
                'email': email,
                'password': password,
                'confirm_password': confirm_password,
                'date': unique_date,
            }
            collection.insert_one(user_data)
            return 'Success'
        else:
            return 'Failed'
    return render_template('register.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port = 5000, debug = True)