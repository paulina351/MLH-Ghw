# importing flask
from flask import Flask, redirect


# creating the application
app = Flask(__name__)

app.route("/")
def get_RickRolled():
    """
    Function to RickRoll an individual using Rick Astley Song from Youtube.
    """
    return redirect("https://youtu.be/dQw4w9WgXcQ?si=u5gVOx0Z0p3XBtSY")

app.run(host='0.0.0.0', port=8080)