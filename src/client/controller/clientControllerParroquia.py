from src.heart.heartSistem import *
from src.heart.heartUtil import *
from src.heart.heartServices import *
class ClientControllerParroquia:

        def onGetClientControllerParroquiaModalListView(id):
                parroquiaList = ClientServiceParroquia.ongetClientServiceParroquia(id)
                context = {
                        "listViewParroquia": True,
                        "parroquiaList": parroquiaList
                }
                try: 
                        return render("client/clientCanton.html", **context)
                except SQLAlchemyError as e:
                        return render('errors/error500.html', e) 