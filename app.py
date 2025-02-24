from flask import Flask, request, jsonify
from flask_cors import CORS 
import pandas as pd 
import os

app = Flask(__name__)
CORS(app)

EXCEL_FILE = "/Users/USER/OneDrive/Desktop/users.xlsx"

# Initialize Excel file
def init_excel():
    if not os.path.exists(EXCEL_FILE):
        df = pd.DataFrame(columns=["username", "email", "password"])
        df.to_excel(EXCEL_FILE, index=False)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username, email, password = data["username"], data["email"], data["password"]

    # Read existing data
    try:
        df = pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["username", "email", "password"])

    # Check if email already exists
    if email in df["email"].values:
        return jsonify({"message": "Email already registered"}), 400

    # Append new user
    new_user = pd.DataFrame([[username, email, password]], columns=["username", "email", "password"])
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_excel(EXCEL_FILE, index=False)

    return jsonify({"message": "Registration successful"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email, password = data["email"], data["password"]

    # Read stored users
    try:
        df = pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        return jsonify({"message": "Invalid credentials"}), 401

    # Validate login
    user = df[(df["email"] == email) & (df["password"] == password)]
    if not user.empty:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    init_excel()
    app.run(host="0.0.0.0", port=5000, debug=True)
