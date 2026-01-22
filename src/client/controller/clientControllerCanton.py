from src.heart.heartSistem import *
from src.heart.heartUtil import *
from src.heart.heartServices import *
class ClientControllerCanton:

        def onGetClientControllerCanton():

                try:

                        cantonList = ClientServiceCanton.ongetClientServiceCanton()
                        if cantonList != 0:
                                if request.method == 'POST' and 'tag' in request.form:
                                        tag = request.form["tag"]
                                        search = "%{}%".format(tag)
                                        cantonList = ClientServiceCanton.ongetClientServiceCantonName(search)
                                        return render("client/clientCanton.html", cantonList=cantonList, tag = tag)
                                else:
                                #flash('Categorias Listadas', category='success')
                                        return render("client/clientCanton.html", cantonList=cantonList)
                        else:
                                flash('No existe categorias', category='success')
                                return render("client/clientCanton.html", cantonList=cantonList)

                except SQLAlchemyError as e:
                        return render('errors/error500.html', e)
        
        
        
        def onGetClientControllerCantonConJavascript():

                try:
                        termino = request.args.get('q', '').lower()
                        
                        cantonList = ClientServiceCanton.ongetClientServiceCanton()
                        cantonJson = []
                        for item in cantonList:
                                cantonJson.append({
                                        'id':item.pfssateccantonid,
                                        'nombre':item.pfssateccantonnombre, 
                                        'provinciaId':item.pfssatecprovinciaid
                                })
                        if termino:
                                resultados = [canton for canton in cantonJson if termino in canton.get('nombre', '').lower()]
                        else:
                                resultados = cantonJson[:10]

                        return  jsonify(resultados)
                
                except SQLAlchemyError as e:
                        return render('errors/error500.html', e)
        
