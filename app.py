# app.py

# Import Flask and jsonify to return JSON responses
from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# A simple route to test if the app is working
@app.route('/')
def home():
    return jsonify({"message": "Welcome to User Management API!"})

# A simple in-memory user storage (list of users)
users = []

# Route to create a new user (POST request)
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()  # Get the request data
    user = {
        "id": len(users) + 1,  # Generate a new ID based on the current number of users
        "name": data["name"],
        "email": data["email"]
    }
    users.append(user)  # Add the user to the list
    return jsonify({"message": "User created", "user": user}), 201

# Route to get all users (GET request)
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": users})

# Route to get a specific user by ID (GET request)
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify({"user": user})
    else:
        return jsonify({"message": "User not found"}), 404

# Route to update an existing user (PUT request)
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user["name"] = data["name"]
        user["email"] = data["email"]
        return jsonify({"message": "User updated", "user": user})
    else:
        return jsonify({"message": "User not found"}), 404

# Route to delete a user (DELETE request)
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)  # Enable debugging
