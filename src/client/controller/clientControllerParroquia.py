from src.heart.heartSistem import *
from src.heart.heartUtil import *
from src.heart.heartServices import *
class ClientControllerParroquia:

    
    def onGetClientControllerParroquiaModalListView():
                parroquiaList = ClientServiceParroquia.ongetClientServiceParroquia()
                context = {
                        "listViewParroquia": True,
                        "parroquiaList": parroquiaList
                }
                try: 
                        return render("client/clientCanton.html", **context)
                except SQLAlchemyError as e:
                        return render('errors/error500.html', e) 