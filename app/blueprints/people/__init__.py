from flask import Blueprint, render_template

from ... import SCKT

from flask_socketio import emit


PP = Blueprint('people', __name__, template_folder='templates', static_folder="static", static_url_path='/static/people')


@PP.route('/people', methods=['GET'])
def people():
    return render_template('people.html')

def new_friend(sid):
    print('new friend', sid)
    emit('new_friend_reg', {"peer_id": sid}, broadcast=True)
