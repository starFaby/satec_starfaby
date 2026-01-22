from src.heart.heartDatabase import *

class ClientServiceCanton:
    
    @classmethod
    def ongetClientServiceCanton(self):
        try:

            #cantonList = Canton.query.join(Parroquia, Canton.pfssateccantonid == Parroquia.pfssateccantonid).join(Provincia, Canton.pfssatecprovinciaid == Provincia.pfssatecprovinciaid).join(Capital, Provincia.pfssatecprovinciaid == Capital.pfssatecprovinciaid).with_entities(Canton.pfssateccantonid, Canton.pfssateccantonnombre, Provincia.pfssatecprovincianombre, Capital.pfssateccapitalnombre)
            #.add_columns( User.pfsusersid,User.pfsuserscedula, User.pfsusersnombres, User.pfsusersapellidos, Canasta.pfscntid, Canasta.pfscntnumpf, Canasta.pfscnttotal, Canasta.pfscntcreatedat).order_by(Canasta.pfscntid.asc()).paginate(page=page, per_page=pages ,error_out=False)
            cantonList = Canton.query.join(Provincia, Canton.pfssatecprovinciaid == Provincia.pfssatecprovinciaid).join(Capital, Capital.pfssatecprovinciaid == Provincia.pfssatecprovinciaid).add_entity(Canton.pfssateccantonnombre).add_entity(Provincia.pfssatecprovincianombre).add_entity(Capital.pfssateccapitalnombre).order_by(Canton.pfssateccantonid.asc())
            return cantonList

        except SQLAlchemyError as e:
            return render('errors/error500.html', e)
        
        
    @classmethod
    def ongetClientServiceCantonName(self, search):
        try:
            cantonList = Canton.query.join(Provincia, Canton.pfssatecprovinciaid == Provincia.pfssatecprovinciaid).join(Capital, Capital.pfssatecprovinciaid == Provincia.pfssatecprovinciaid).add_entity(Canton.pfssateccantonnombre).add_entity(Provincia.pfssatecprovincianombre).add_entity(Capital.pfssateccapitalnombre).filter(Canton.pfssateccantonnombre.like(search)).filter(Canton.pfssateccantonestado == 1)
            return cantonList
        except SQLAlchemyError as e:
            return render('errors/error500.html', e)