from flask import Blueprint
from src.heart.heartController import *
crparr= Blueprint('crparr', __name__)
crparr.route('/crparr', methods=['GET', 'POST'])(ClientControllerParroquia.onGetClientControllerParroquia)