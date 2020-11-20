"""
Created by Epic at 11/15/20
"""
from flask import Blueprint, current_app, request
from yaml import dump

bp = Blueprint("Config API", __name__)


@bp.route("/api/config/<int:guild_id>")
def get_config(guild_id: int):
    display_type = request.args.get("format", "json")
    config = current_app.guild_config.find_one({"_id": guild_id})
    if display_type == "json":
        return config
    elif display_type == "yaml":
        return dump(config)
    else:
        return "Invalid guild config"

