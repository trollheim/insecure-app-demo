import base64
import os
import binascii

from flask import Blueprint, render_template, abort, redirect, make_response, send_from_directory
from modules.shared.flagloader import OWASP_TOP_FLAGS

blueprint = Blueprint('owasptop10_a2', __name__,
                        template_folder='templates')

from flask import request, jsonify

COOKIE = "session_a2"
TOKEN = binascii.hexlify(os.urandom(24)).decode()



user = {
        "username" : "gil.snyder@acme.io",
        "password" : "gaudencio",
       }

@blueprint.route('/owasptop10/a2')
def index():
    return  render_template('owasptop10/a2/index.html')

@blueprint.route('/owasptop10/a2/login',methods =["GET"])
def loginPage():
    return  render_template('owasptop10/a2/login.html')



@blueprint.route('/owasptop10/a2/user')
def userPage():
    cookie = request.cookies.get(COOKIE)

    if cookie != TOKEN:
        return redirect("/owasptop10/a2")
    message = OWASP_TOP_FLAGS.get("A2")
    return render_template('owasptop10/a2/user.html', user = user.get("username"), message = message)



@blueprint.route('/owasptop10/a2/login', methods = ["POST"])
def loginForm():
    login = request.form

    if user.get("username") != login.get("username"):
        return redirect('/owasptop10/a2/login?error=noUser')

    if user.get("password") != login.get("password"):
        return redirect('/owasptop10/a2/login?error=invalidPassword')

    resp = make_response(redirect('/owasptop10/a2/user'))
    resp.set_cookie(COOKIE, TOKEN)
    return resp



@blueprint.route('/owasptop10/a2/file')
def fileDownload():
    return send_from_directory(blueprint.root_path, "hackedusers.txt")




