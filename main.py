"""
Created by Epic at 11/15/20
"""
from flask import Flask
from os import environ as env

app = Flask(__name__)
app.config.from_object({
    "CLIENT_ID": env["CLIENT_ID"],
    "CLIENT_SECRET": env["CLIENT_SECRET"]
})

if __name__ == '__main__':
    app.run(port=5050, debug=True)
