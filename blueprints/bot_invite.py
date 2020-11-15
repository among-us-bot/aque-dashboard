"""
Created by Epic at 11/15/20
"""
from flask import Blueprint

bp = Blueprint("Bot invite", __name__)

@bp.route("/invite")
def