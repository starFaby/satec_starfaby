from flask import Blueprint
from src.migrate.migrate import initDB

ardbsatec= Blueprint('ardbsatec', __name__)

ardbsatec.route('/ardbsatec', methods=['GET'])(initDB)