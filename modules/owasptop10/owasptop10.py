from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

blueprint = Blueprint('owasptop10', __name__,
                        template_folder='templates')



@blueprint.route('/owasptop10/test')
def owasptop10test():
    return "test"

owasp = [
    {"url" : "/owasptop10/a1" , "doc": "https://owasp.org/Top10/A01_2021-Broken_Access_Control/", "name": "A01:2021 – Broken Access Control"},
    {"url" : "/owasptop10/a2" ,"doc": "https://owasp.org/Top10/A02_2021-Cryptographic_Failures/", "name": " A02:2021 – Cryptographic Failures"},
    {"url": "/owasptop10/a3", "doc": "https://owasp.org/Top10/A03_2021-Injection/",
     "name": "A03:2021 – Injection"},
    {"url": "/owasptop10/a4", "doc": "https://owasp.org/Top10/A04_2021-Insecure_Design/",
     "name": "A04_2021-Insecure_Design"},

{"url" : "/owasptop10/a5" , "doc": "https://owasp.org/Top10/A05_2021-Security_Misconfiguration/", "name": "A05:2021 – Security Misconfiguration"},
    {"url" : "/owasptop10/a6" ,"doc": "https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/", "name": "A07:2021 – Identification and Authentication Failures"},

    {"url": "/owasptop10/a7", "doc": "https://owasp.org/Top10/A07_2021-Identification_and_Authentication_Failures/",
     "name": "A07:2021 – Identification and Authentication Failures"},
    {"url": "/owasptop10/a8", "doc": "https://owasp.org/Top10/A08_2021-Software_and_Data_Integrity_Failures/",
     "name": "A08:2021 – Software and Data Integrity Failures"},
    {"url": "/owasptop10/a9", "doc": "https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/",
     "name": "A09:2021 – Security Logging and Monitoring Failures"},
    {"url": "/owasptop10/a10", "doc": "https://owasp.org/Top10/A10_2021-Server-Side_Request_Forgery_%28SSRF%29/",
     "name": "A10:2021 – Server-Side Request Forgery (SSRF)"}


]




@blueprint.route('/owasptop10')
def owasptop10Index():
    return render_template('owasptop10/index.html', members=owasp)







@blueprint.route('/owasptop10/a5')
def owasptop10a5():
    return "test"
@blueprint.route('/owasptop10/a6')
def owasptop10a6():
    return "test"
@blueprint.route('/owasptop10/a7')
def owasptop10a7():
    return "test"
@blueprint.route('/owasptop10/a8')
def owasptop10a8():
    return "test"
@blueprint.route('/owasptop10/a9')
def owasptop10a9():
    return "test"
@blueprint.route('/owasptop10/a10')
def owasptop10a10():
    return "test"