from flask import Blueprint
from src.heart.heartController import *
crparr= Blueprint('crparr', __name__)
crparr.route('/crparr/<int:id>', methods=['GET', 'POST'])(ClientControllerParroquia.onGetClientControllerParroquiaModalListView)