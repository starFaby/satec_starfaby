from src.heart.heartDatabase import *

class ClientServiceCanton:
    
    @classmethod
    def ongetClientServiceCanton(self):
        try:
            cantonList = pd.Series(Canton.query.filter(Canton.pfssateccantonestado == 1))
            return cantonList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)