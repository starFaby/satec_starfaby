from src.heart.heartSistem import *
from src.heart.heartUtil import *
from src.heart.heartServices import *
class ClientControllerParroquiaGeneral:

        def onGetClientControllerParroquiaGeneralListView():
                try:
                        parroquiaGeneralList = ClientServiceParroquiaGeneral.ongetClientServiceParroquiaGeneral()
                        
                        if parroquiaGeneralList != 0:
                                if request.method == 'POST' and 'tag' in request.form:
                                        tag = request.form["tag"]
                                        search = "%{}%".format(tag)
                                        parroquiaGeneralList = ClientServiceParroquiaGeneral.ongetClientServiceParroquiaGeneralName(search)
                                        return render("client/clientParroquiaGeneral.html", parroquiaGeneralList=parroquiaGeneralList, tag = tag)
                                else:
                                        #flash('Categorias Listadas', category='success')
                                        return render("client/clientParroquiaGeneral.html", parroquiaGeneralList=parroquiaGeneralList)
                        else:
                                flash('No existe categorias', category='success')
                                return render("client/clientParroquiaGeneral.html", parroquiaGeneralList=parroquiaGeneralList)

                except SQLAlchemyError as e:
                        return render('errors/error500.html', e)                