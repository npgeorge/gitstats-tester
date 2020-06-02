import os
from dotenv import load_dotenv
import requests
from pprint import pprint
import base64
import json
from github import Github
from flask import Flask, request, jsonify, render_template, Response
import pandas as pd
import numpy as np
from pprint import pformat
import plotly.express as px
# current app ppints to config in app.py
from flask import Blueprint, jsonify, request, render_template, current_app

# import database models.py to link class tables
#from git_app.models import db, migrate, User, Repos
#from git_app.services import github_api_client

#rearranging for Heroku
from git_app.models import db, migrate, User, Repos
from git_app.services import github_api_client

load_dotenv()

# can make client global variable if you want to
client = github_api_client()

#
# ROUTING
#

# specifying for Blueprint to be used in app.py
my_routes = Blueprint('my_routes', __name__)

@my_routes.route("/")
def index():
    # return "Example"
    return render_template("homepage.html")

@my_routes.route("/ds")
def ds_index():
    # return "Example"
    return render_template("ds.html")


# gathering all the repos and displaying what is stored in the Repos database
@my_routes.route("/ds/repos")
@my_routes.route("/ds/repos.json")
def repos():
    repos = Repos.query.all()
    #print(len(users))
    print(type(repos))
    print(type(repos[0]))
    repos_response = []
    for repo in repos:
        repos_dict = repo.__dict__
        del repos_dict["_sa_instance_state"]
        repos_response.append(repos_dict)
    return jsonify(repos_response)

# user is able to input reposiotry names and they'll be added to the Repos database
@my_routes.route("/ds/repos/add", methods=["POST"])
def add_repos():
    print("ADD A NEW REPO....")
    print("FROM DATA:", dict(request.form)) # detects what information was sent to server when a POST request was made
    # something
    # return jsonify({"message": "CREATED OK"})
    if "repo" in request.form:
        repo = request.form["repo"]
        print(repo)
        db.session.add(Repos(repo=repo))
        db.session.commit()
        return jsonify({"message": "CREATED OK", "repo": repo})
    else:
        return jsonify({"message": "OOPS PLEASE SPECIFY A REPOSITORY!"})

# ------- repo commit response --------
@my_routes.route('/repos/commits', methods=['POST', 'GET'])
def commits():
    
    # user inputs repo name
    ui_commit = request.form['repo_commits']
    URL = f"https://api.github.com/repos/{ui_commit}/commits?per_page=100"
    response = requests.get(URL)
    data = response.json()
    data = pformat(data)
    return data

#
#
#
# ----- WEB ROUTES -----
#
#
#

@my_routes.route("/web")
def web_index():
    # return "Example"
    return render_template("web.html")

# J's endpoint
@my_routes.route('/web/kubernetes_test', methods=['GET'])
def display_graph():
    # api-endpoint 
    URL = "https://api.github.com/repos/kubernetes/kubernetes/issues?page=1"
    URL2 = "https://api.github.com/repos/kubernetes/kubernetes/issues?page=2"
    URL3 = "https://api.github.com/repos/kubernetes/kubernetes/issues?page=3"
    # sending get request and saving the response as response object 
    r = requests.get(url = URL) 
    r2 = requests.get(url = URL2)
    r3 = requests.get(url = URL3)
    # extracting data in json format 
    data1 = r.json() 
    data2 = r2.json()
    data3 = r3.json()  
    issues1 = pd.DataFrame(data1)
    issues2 = pd.DataFrame(data2)
    issues3 = pd.DataFrame(data3)
    issues = issues1.append(issues2)
    issues = issues.append(issues3)
    fig = px.line(issues, x='created_at', y='comments')
    fig.show()