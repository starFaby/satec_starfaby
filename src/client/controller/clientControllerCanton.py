from src.heart.heartSistem import *
from src.heart.heartUtil import *
from src.heart.heartServices import *
class ClientControllerCanton:

        def onGetClientControllerCanton():

                try:
                        cantonList = ClientServiceCanton.ongetClientServiceCanton()
                        cantonJson = []
                        for item in cantonList:
                                cantonJson.append({
                                        'id':item.pfssateccantonid,
                                        'nombre':item.pfssateccantonnombre, 
                                        'provinciaId':item.pfssatecprovinciaid
                                })
                        return  jsonify(cantonJson)
                
                except SQLAlchemyError as e:
                        return render('errors/error500.html', e)
        
