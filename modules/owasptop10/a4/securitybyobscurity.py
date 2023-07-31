import sqlite3
import os
from flask import Blueprint, render_template, abort, redirect, make_response, send_from_directory
from modules.shared.flagloader import OWASP_TOP_FLAGS

blueprint = Blueprint('owasptop10_a4', __name__,
                        template_folder='templates')

from flask import request



@blueprint.route('/owasptop10/a4')
def index():
    return  render_template('owasptop10/a4/index.html')





@blueprint.route('/owasptop10/a4/admin')
def step1():
    msg = "warm..."
    return render_template('owasptop10/a4/step.html', message = msg)

@blueprint.route('/owasptop10/a4/admin/backup')
def step2():
    msg = "warmer..."
    return render_template('owasptop10/a4/step.html', message=msg)


@blueprint.route('/owasptop10/a4/admin/backup/00')
def step3():
    msg = "almost there..."
    return render_template('owasptop10/a4/step.html', message=msg)

@blueprint.route('/owasptop10/a4/admin/backup/00')
def step4():
    msg = "and one more..."
    return render_template('owasptop10/a4/step.html', message=msg)


@blueprint.route('/owasptop10/a4/admin/backup/00/china')
def step5():
    msg = OWASP_TOP_FLAGS.get("A4")
    return render_template('owasptop10/a4/step.html', message=msg)