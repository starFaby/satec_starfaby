from flask import Blueprint
from src.heart.heartController import *
crstc= Blueprint('crstc', __name__)
crstc.route('/crstc', methods=['GET', 'POST'])(ClientControllerSatec.onGetClientControllerSatec)