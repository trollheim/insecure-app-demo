import sqlite3
import os
from flask import Blueprint, render_template, abort, redirect, make_response, send_from_directory
from modules.shared.flagloader import OWASP_TOP_FLAGS

blueprint = Blueprint('owasptop10_a3', __name__,
                        template_folder='templates')

from flask import request



@blueprint.route('/owasptop10/a3')
def index():
    return  render_template('owasptop10/a3/index.html')





@blueprint.route('/owasptop10/a3/data')
def data():
    try:
        args = request.args


        db_file = os.path.join(blueprint.root_path,"database.db")
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        pagenumber = args.get("pagenumber", default = "0")
        search = args.get("search", default =  "").upper()

        query = "SELECT * FROM tblusers where (fname like '%" + search + "%') or (sname  like '%" + search + "%') LIMIT " + pagenumber + ",10"
        print(query)
        cur.execute(query)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append({
                'id': str(row[0]),
                'fname': row[1],
                'sname': row[2],
                'credits': row[3]
            })
        return result
    finally:
        if conn is not None:
            conn.close()



