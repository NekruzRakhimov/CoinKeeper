import random
import repository
#from models import Accounts 
#giving error because of not exists class
from flask import jsonify, request, render_template, Blueprint


app = Blueprint('routes', __name__)


@app.route('/', methods=['GET'])
def index():
    return {"Status": "Up"}, 200
