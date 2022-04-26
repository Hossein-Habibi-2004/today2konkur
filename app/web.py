from flask import Flask, render_template
import logging


def index_view():
    return render_template('index.html')


app = Flask(__name__, template_folder='./web/templates/', static_folder='./web/static/')
log = logging.getLogger('werkzeug')
log.disabled = True

app.add_url_rule('/', 'index', view_func=index_view, methods=['GET'])

