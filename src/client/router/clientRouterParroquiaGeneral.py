from flask import Blueprint
from src.heart.heartController import *
crparrg= Blueprint('crparrg', __name__)
crparrg.route('/crparrg', methods=['GET', 'POST'])(ClientControllerParroquiaGeneral.onGetClientControllerParroquiaGeneralListView)