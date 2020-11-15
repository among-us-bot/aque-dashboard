"""
Created by Epic at 11/15/20
"""
from flask import Blueprint, redirect, current_app, request, render_template
from os import environ as env
from requests import post

bp = Blueprint("Bot invite", __name__)


@bp.route("/invite")
def invite_url():
    return redirect("https://discord.com/api/oauth2/authorize?"
                    f"client_id={env['CLIENT_ID']}&"
                    f"redirect_uri={env['REDIRECT_URL_ENCODED']}&"
                    "scope=bot&"
                    "response_type=code")


@bp.route("/invite/callback")
def invite_bot_callback():
    args = request.args
    code = args.get("code")
    guild_id = args.get("guild_id")
    if code is None:
        return redirect("/invite")
    guild = current_app.whitelisted.find_one({"_id": guild_id})
    if guild is None:
        return render_template("invite/not_whitelisted.html")
    if guild["invited"]:
        # To people who try to abuse bugs, fuck you.
        return render_template("invite/not_whitelisted.html")
    current_app.whitelisted.update_one({"_id": guild_id}, {"$set": {"invited": True}})

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    invite_data = {
        "client_id": env["CLIENT_ID"],
        "client_secret": env["CLIENT_SECRET"],
        "grant_type": "authorization_code",
        "redirect_uri": env["REDIRECT_URL"],
        "scope": "bot",
        "code": args.get("code")
    }
    post(f"https://discord.com/api/v8/oauth2/token", data=invite_data, headers=headers)
    return render_template("invite/success.html")
