from src.heart.heartDatabase import *

class ClientServiceParroquiaGeneral:
    
    @classmethod
    def ongetClientServiceParroquiaGeneral(self):
        try:
            #parroquiaList = pd.Series(Parroquia.query.filter(Parroquia.pfssatecparroquiaestado == 1).filter(Parroquia.pfssateccantonid == id))
            parroquiaGeneralList = Parroquia.query.join(Tipozona, Parroquia.pfssatectipozonaid == Tipozona.pfssatectipozonaid).join(Canton, Parroquia.pfssateccantonid == Canton.pfssateccantonid).join(Provincia, Canton.pfssatecprovinciaid == Provincia.pfssatecprovinciaid).add_entity(Provincia.pfssatecprovincianombre).add_entity(Parroquia.pfssatecparroquianombre).add_entity(Tipozona.pfssatectipozonanombre).add_entity(Canton.pfssateccantonnombre).filter(Parroquia.pfssatecparroquiaestado == 1)
            return parroquiaGeneralList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
    @classmethod
    def ongetClientServiceParroquiaGeneralName(self, search):
        try:
            parroquiaGeneralList = Parroquia.query.join(Tipozona, Parroquia.pfssatectipozonaid == Tipozona.pfssatectipozonaid).join(Canton, Parroquia.pfssateccantonid == Canton.pfssateccantonid).join(Provincia, Canton.pfssatecprovinciaid == Provincia.pfssatecprovinciaid).add_entity(Provincia.pfssatecprovincianombre).add_entity(Parroquia.pfssatecparroquianombre).add_entity(Tipozona.pfssatectipozonanombre).add_entity(Canton.pfssateccantonnombre).filter(Parroquia.pfssatecparroquianombre.like(search)).filter(Parroquia.pfssatecparroquiaestado == 1)
            return parroquiaGeneralList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)