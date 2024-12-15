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
    message = {"message": "Hello, World!"}
    return json.dumps(message)


# \end{code}
# ````````  


# run the app
app.run(debug=True)#that when i save the code, the changes are applied into the SERVER