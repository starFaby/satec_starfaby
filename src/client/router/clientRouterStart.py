from flask import Blueprint
from src.heart.heartController import *
crs= Blueprint('crs', __name__)
crs.route('/crs', methods=['GET', 'POST'])(ClientControllerStart.onGetClientControllerStart)
