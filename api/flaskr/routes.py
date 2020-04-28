from time import strftime, localtime

from flask import Blueprint

core_api = Blueprint('api', __name__)

@core_api.route('/time')
def get_time():
    return {'time': strftime("%a, %d %b %Y %H:%M:%S", localtime())}

@core_api.route('/queen-bee')
def queen_bee():
    return 'Bzzzzzzzzzzzzzzzzzzz'

@core_api.route('/mistake')
def noobs():
    return 'Your face is a mistake'