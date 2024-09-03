from flask import Flask, jsonify
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

@app.route('/')
def home():
    return 'Welcome to the Flask app!'

@app.route('/test-env')
def test_env():
    secret_key = os.getenv('SECRET_KEY')
    return jsonify({'SECRET_KEY': secret_key})

if __name__ == '__main__':
    app.run(debug=True)
