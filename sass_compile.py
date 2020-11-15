"""
Created by Epic at 11/15/20
"""
from os import system
from pathlib import Path

sass_directory = Path("sass/")
css_directory = Path("static/css")

if not css_directory.is_dir():
    css_directory.mkdir()

for sass_file in sass_directory.glob("*.scss"):
    system(f"sass {sass_file} {css_directory}/{str(sass_file).split('/')[-1][:-4] + 'css'}")
