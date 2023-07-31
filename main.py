from flask import Flask, render_template
from modules.owasptop10 import owasptop10
from modules.owasptop10.a1 import brokenauth as a1_routing
from modules.owasptop10.a2 import cryptofail as a2_routing
from modules.owasptop10.a3 import sqlinjection as a3_routing
from modules.owasptop10.a4 import securitybyobscurity as a4_routing

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


app.register_blueprint(owasptop10.blueprint)
app.register_blueprint(a1_routing.blueprint)
app.register_blueprint(a2_routing.blueprint)
app.register_blueprint(a3_routing.blueprint)
app.register_blueprint(a4_routing.blueprint)
config = {
    "DEBUG": True  # run app in debug mode
}
app.config.from_mapping(config)
