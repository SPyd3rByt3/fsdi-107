from flask import Flask
import json

app = Flask(__name__) 
# must be 2 underscores on both sides eg.(12name12)
@app.get("/")
def home():
    return {"message": "Hello, World, from FLASK!"}

@app.get("/test")
def test():
    return "Hello, from the TEST page!"

@app.get("/about")
def about():
    return "Seth Patterson"

@app.get("/hello")
def hello():
    message = {"message": "Hello, World!!"}
    return json.dumps(message)


# \end{code}
# ````````  


# run the app
app.run(debug=True)#that when i save the code, the changes are applied into the SERVER

# MINI CHALLENGE : that says HELLO using a variable instead of a string.
@app.get("/hello")
def hello():
    message = {"message":"hello there!"}
    return json.dumps(message)
#
# 
#  Add a new endpoint to the app that returns a list of all the endpoints available in the app


#``````````
# From flask import Flask, jsonify

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return jsonify(message="Hello, World, from FLASK!")

# if __name__ == "__main__":
#     app.run(debug=True)
# Improvements Made:
# Use of jsonify: Instead of returning a dictionary directly, we use jsonify to create a JSON response. This is a best practice in Flask as it sets the correct content type for the response.

# Route Decorator: Changed @app.get("/") to @app.route("/"), which is more general and can handle different HTTP methods if needed in the future.

# Main Guard: Added the if __name__ == "__main__": guard. This ensures that the Flask app runs only when the script is executed directly, which is a common practice in Python scripts.

# These changes make the code cleaner and more maintainable while keeping the same functionality.
