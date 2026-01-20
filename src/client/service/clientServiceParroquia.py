from src.heart.heartDatabase import *

class ClientServiceParroquia:
    
    @classmethod
    def ongetClientServiceParroquia(self):
        try:
            parroquiaList = pd.Series(Parroquia.query.filter(Parroquia.pfssatecparroquiaestado == 1))
            return parroquiaList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)