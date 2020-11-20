"""
Created by Epic at 11/15/20
"""
from blueprints.bot_invite import bp as bot_invite
from blueprints.ui_test import bp as ui_test

from flask import Flask
from pymongo import MongoClient
from os import environ as env

app = Flask(__name__)
app.mongo = MongoClient(env["DATABASE_HOST"])
app.db = app.mongo[env["DATABASE_DB"]]
app.whitelisted = app.db["whitelisted"]
app.guild_config = app.db["guild_config"]

# Register blueprints
app.register_blueprint(bot_invite)
app.register_blueprint(ui_test)

if __name__ == '__main__':
    import sass_compile
    app.run(host="0.0.0.0", port=8080, debug=True)

