from src.heart.heartDatabase import *

class ClientServiceParroquia:
    
    @classmethod
    def ongetClientServiceParroquia(self, id):
        try:
            #parroquiaList = pd.Series(Parroquia.query.filter(Parroquia.pfssatecparroquiaestado == 1).filter(Parroquia.pfssateccantonid == id))
            parroquiaList = Parroquia.query.join(Tipozona, Parroquia.pfssatectipozonaid == Tipozona.pfssatectipozonaid).add_entity(Parroquia.pfssatecparroquianombre).add_entity(Tipozona.pfssatectipozonanombre).filter(Parroquia.pfssatecparroquiaestado == 1).filter(Parroquia.pfssateccantonid == id)
            return parroquiaList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)