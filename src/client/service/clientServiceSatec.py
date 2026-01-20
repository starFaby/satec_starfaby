from src.heart.heartDatabase import *

class ClientServiceSatec:
    
    @classmethod
    def ongetClientServiceSatec(self):
        try:
            satecList = pd.Series(Canton.query.filter(Canton.pfssateccantonestado == 1))
            return satecList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)