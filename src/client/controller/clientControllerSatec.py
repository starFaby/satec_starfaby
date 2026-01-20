from src.heart.heartSistem import *
from src.heart.heartUtil import *
from src.heart.heartServices import *
class ClientControllerSatec:

    def onGetClientControllerSatec():
        satecList = ClientServiceSatec.ongetClientServiceSatec()

        context = {
                    'satecList':satecList
                }
        return render('client/clientSatec.html', **context)