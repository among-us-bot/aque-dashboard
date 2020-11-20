"""
Created by Epic at 11/15/20
"""
from flask import current_app


def has_permissions(guild_id, request):
    splitted = request.headers.split(" ")
    if len(splitted) != 2:
        return False
