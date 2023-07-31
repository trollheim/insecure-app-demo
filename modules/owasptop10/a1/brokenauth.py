import base64

from flask import Blueprint, render_template, abort, redirect, make_response
from modules.shared.flagloader import OWASP_TOP_FLAGS

blueprint = Blueprint('owasptop10_a1', __name__,
                        template_folder='templates')

from flask import request, jsonify

COOKIE = "session_a1"

users = [
    {

        "username" : "admin",
        "password" : "f1e069787ece74531d112559945c6871",
    },
{
        "username" : "test_user",
        "password" : "test_password",
    },
]


@blueprint.route('/owasptop10/a1')
def loginPage():
    return  render_template('owasptop10/a1/login.html')


@blueprint.route('/owasptop10/a1/user')
def userPage():
    cookie = request.cookies.get(COOKIE)
    user = base64.b64decode(cookie. encode("ascii")).decode()
    if user == "admin":
        message = OWASP_TOP_FLAGS.get("A1")
    elif user == "test_user":
        message = "To get the flag, log in as an admin, you must."
    else:
        message = "warmer... warmer..."

    return render_template('owasptop10/a1/user.html', user = user, message = message)



@blueprint.route('/owasptop10/a1/login', methods = ["POST"])
def loginForm():
    login = request.form

    for user in users:
        print(user)
        if user.get("username") == login.get("username") and user.get("password") == login.get("password"):
            resp = make_response(redirect('/owasptop10/a1/user'))
            resp.set_cookie(COOKIE, base64.b64encode(user.get("username"). encode("ascii")).decode())
            return resp

    print("user not found "+ login.get("username"))
    return redirect('/owasptop10/a1?nouser')
