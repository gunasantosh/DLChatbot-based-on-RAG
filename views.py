from flask import Blueprint
from flask import render_template, jsonify, request, redirect, url_for
from dotenv import load_dotenv
import os

views = Blueprint("views", __name__)

load_dotenv("../.env")

API_KEY = os.getenv("API_KEY")


@views.route("/")
@views.route("/home")
def home():
    return render_template("index.html", API_KEY=API_KEY)
