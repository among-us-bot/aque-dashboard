"""
Created by Epic at 11/15/20
"""
from flask import Blueprint, render_template
from os import environ as env

bp = Blueprint("UI Test", __name__)


@bp.route("/dev/template/<path:template>")
def show_template(template: str):
    return render_template(template, env=env)
