from src.heart.heartSistem import *
from src.heart.heartUtil import *
from src.heart.heartServices import *
class ClientControllerParroquia:

    def onGetClientControllerParroquia():
        ParroquiaList = ClientServiceParroquia.ongetClientServiceParroquia()

        return ParroquiaList