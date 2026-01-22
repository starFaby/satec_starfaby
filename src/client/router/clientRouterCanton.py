from flask import Blueprint
from src.heart.heartController import *
crcnt= Blueprint('crcnt', __name__)
crcnt.route('/crcnt', methods=['GET', 'POST'])(ClientControllerCanton.onGetClientControllerCanton)