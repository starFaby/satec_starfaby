from src.heart.heartSistem import *

#----------------------------
#----------ROL----------
#--------------------------


#----------------------------
#----------usuario----------
#--------------------------
class User(db.Model):
    __tablename__='pfsusers'

    pfsusersid = db.Column(db.Integer, primary_key=True)
    pfsuserscedula = db.Column(db.String(80), nullable=False)
    pfsusersnombres = db.Column(db.String(80), nullable=False)
    pfsusersapellidos = db.Column(db.String(80), nullable=False)
    pfsusersusername = db.Column(db.String(30), nullable=False)
    pfsusersemail = db.Column(db.String(120), nullable=False)
    pfsuserspassword = db.Column(db.String(250), nullable=True)
    pfsusersdireccion = db.Column(db.String(100), nullable=True)
    pfsuserscelular = db.Column(db.String(25), nullable=False)
    pfsuserstelefono = db.Column(db.String(20), nullable=False)
    pfsusersisadmin = db.Column(db.Boolean, default=False)
    pfsusersavatar = db.Column(db.String(250), nullable=True)
    pfsusersestado = db.Column(db.String(1), nullable=True)
    pfsuserscreatedat = db.Column(db.Date, nullable=True) 

    def onGetSetPassword(self, pfsuserspassword):
        self.pfsuserspassword = generate_password_hash(pfsuserspassword)

    def onGetCheckPassword(self, pfsuserspassword):
        return check_password_hash(self.pfsuserspassword, pfsuserspassword)

    def __init__(self, pfsuserscedula, pfsusersnombres, pfsusersapellidos, pfsusersusername, pfsusersemail, pfsuserspassword, pfsusersdireccion,  pfsuserscelular, pfsuserstelefono, pfsusersisadmin, pfsusersavatar, pfsusersestado, pfsuserscreatedat):
        self.pfsuserscedula = pfsuserscedula
        self.pfsusersnombres = pfsusersnombres
        self.pfsusersapellidos = pfsusersapellidos
        self.pfsusersusername = pfsusersusername
        self.pfsusersemail = pfsusersemail
        self.pfsuserspassword = pfsuserspassword 
        self.pfsusersdireccion = pfsusersdireccion 
        self.pfsuserscelular = pfsuserscelular
        self.pfsuserstelefono = pfsuserstelefono
        self.pfsusersavatar = pfsusersavatar
        self.pfsusersisadmin = pfsusersisadmin
        self.pfsusersestado = pfsusersestado
        self.pfsuserscreatedat = pfsuserscreatedat 
    
    

class UserSchema(ma.Schema):
    class Meta:
        fields = ('pfsusersid', 'pfsuserscedula', 'pfsusersnombres', 'pfsusersapellidos', 'pfsusersusername', 'pfsusersemail', 'pfsuserspassword', 'pfsusersdireccion',  'pfsuserscelular', 'pfsuserstelefono','pfsusersisadmin', 'pfsusersavatar', 'pfsusersestado', 'pfsuserscreatedat')

userSchema = UserSchema()
usersSchema = UserSchema(many=True)

#----------------------------------------------------------
#---------------Region----------------------------
#----------------------------------------------------------

class Region(db.Model): 
    __tablename__='pfssatecregion'

    pfssatecregionid = db.Column(db.Integer, primary_key=True)
    pfssatecregionnombre = db.Column(db.String(120), nullable=False)
    pfssatecregionimage = db.Column(db.String(300), nullable=False)
    pfssatecregiondetalle = db.Column(db.String(300), nullable=False)
    pfssatecregionestado = db.Column(db.String(1), nullable=True)
    pfssatecregioncreatedat = db.Column(db.String(11), nullable=True) 


    def __init__(self, pfssatecregionnombre, pfssatecregionimage, pfssatecregiondetalle , pfssatecregionestado, pfssatecregioncreatedat):
        self.pfssatecregionnombre = pfssatecregionnombre
        self.pfssatecregionimage = pfssatecregionimage
        self.pfssatecregiondetalle = pfssatecregiondetalle
        self.pfssatecregionestado = pfssatecregionestado
        self.pfssatecregioncreatedat = pfssatecregioncreatedat

class RegionSchema(ma.Schema):
    class Meta:
        fields = ('pfssatecregionid', 'pfssatecregionnombre', 'pfssatecregionimage', 'pfssatecregiondetalle' , 'pfssatecregionestado', 'pfssatecregioncreatedat')

regionSchema = RegionSchema()
regionSchema = RegionSchema(many=True)
#-----------------------------------------------------------
#--------------------PROVINCIA-------------------------------
#----------------------------------------------------------
class Provincia(db.Model):
    __tablename__='pfssatecprovincia'

    pfssatecprovinciaid = db.Column(db.Integer, primary_key=True)
    pfssatecprovincianombre = db.Column(db.String(150), nullable=False)
    pfssatecprovinciaimage = db.Column(db.String(300), nullable=False)
    pfssatecprovinciacodigo = db.Column(db.String(120), nullable=False)
    pfssatecprovinciaestado = db.Column(db.String(1), nullable=True)
    pfssatecprovinciacreatedat = db.Column(db.String(11), nullable=True) 

    pfssatecregionid = db.Column(db.Integer, db.ForeignKey('pfssatecregion.pfssatecregionid',ondelete='CASCADE'), nullable=False)
    pfssatecregion = db.relationship('Region',backref=db.backref('pfssatecprovincia',lazy=True))

    def __init__(self, pfssatecprovincianombre,pfssatecprovinciaimage, pfssatecprovinciacodigo,pfssatecprovinciaestado, pfssatecprovinciacreatedat):
        self.pfssatecprovincianombre = pfssatecprovincianombre
        self.pfssatecprovinciaimage = pfssatecprovinciaimage
        self.pfssatecprovinciacodigo = pfssatecprovinciacodigo
        self.pfssatecprovinciaestado = pfssatecprovinciaestado
        self.pfssatecprovinciacreatedat = pfssatecprovinciacreatedat

class ProvinciaSchema(ma.Schema):
    class Meta:
        fields = ('pfssatecprovinciaid', 'pfssatecprovincianombre','pfssatecprovinciaimage', 'pfssatecprovinciacodigo', 'pfssatecprovinciaestado' , 'pfssatecprovinciacreatedat', 'pfssatecregionid')

provinciaSchema = ProvinciaSchema()
provinciaSchema = ProvinciaSchema(many=True)

#-----------------------------------------------------------
#---------------CAPITAL-------------------------------------
#-----------------------------------------------------------

class Capital(db.Model):
    __tablename__='pfssateccapital'

    pfssateccapitalid = db.Column(db.Integer, primary_key=True)
    pfssateccapitalnombre = db.Column(db.String(150), nullable=False)
    pfssateccapitalimage = db.Column(db.String(300), nullable=False)
    pfssateccapitalcodigo = db.Column(db.String(120), nullable=False)
    pfssateccapitalestado = db.Column(db.String(1), nullable=True)
    pfssateccapitalcreatedat = db.Column(db.String(11), nullable=True) 

    pfssatecprovinciaid = db.Column(db.Integer, db.ForeignKey('pfssatecprovincia.pfssatecprovinciaid',ondelete='CASCADE'), nullable=False)
    pfssatecprovincia = db.relationship('Provincia',backref=db.backref('pfssateccapital',lazy=True))

    def __init__(self, pfssateccapitalnombre,pfssateccapitalimage, pfssateccapitalcodigo,pfssateccapitalestado, pfssateccapitalcreatedat):
        self.pfssateccapitalnombre = pfssateccapitalnombre
        self.pfssateccapitalimage = pfssateccapitalimage
        self.pfssateccapitalcodigo = pfssateccapitalcodigo
        self.pfssateccapitalestado = pfssateccapitalestado
        self.pfssateccapitalcreatedat = pfssateccapitalcreatedat

class CapitalSchema(ma.Schema):
    class Meta:
        fields = ('pfssateccapitalid', 'pfssateccapitalnombre','pfssateccapitalimage', 'pfssateccapitalcodigo', 'pfssateccapitalestado' , 'pfssateccapitalcreatedat', 'pfssatecprovinciaid')

capitalSchema = CapitalSchema()
capitalSchema = CapitalSchema(many=True)

#-----------------------------------------------------------
#-----------------CANTON------------------------------------
#-----------------------------------------------------------

class Canton(db.Model):
    __tablename__='pfssateccanton'

    pfssateccantonid = db.Column(db.Integer, primary_key=True)
    pfssateccantonnombre = db.Column(db.String(150), nullable=False)
    pfssateccantonimage = db.Column(db.String(300), nullable=False)
    pfssateccantoncodigo = db.Column(db.String(120), nullable=False)
    pfssateccantonestado = db.Column(db.String(1), nullable=True)
    pfssateccantoncreatedat = db.Column(db.String(11), nullable=True) 

    pfssateccapitalid = db.Column(db.Integer, db.ForeignKey('pfssateccapital.pfssateccapitalid',ondelete='CASCADE'), nullable=False)
    pfssateccapital = db.relationship('Capital',backref=db.backref('pfssateccanton',lazy=True))

    def __init__(self, pfssateccantonnombre,pfssateccantonimage, pfssateccantoncodigo,pfssateccantonestado, pfssateccantoncreatedat):
        self.pfssateccantonnombre = pfssateccantonnombre
        self.pfssateccantonimage = pfssateccantonimage
        self.pfssateccantoncodigo = pfssateccantoncodigo
        self.pfssateccantonestado = pfssateccantonestado
        self.pfssateccantoncreatedat = pfssateccantoncreatedat

class CantonSchema(ma.Schema):
    class Meta:
        fields = ('pfssateccantonid', 'pfssateccantonnombre','pfssateccantonimage', 'pfssateccantoncodigo', 'pfssateccantonestado' , 'pfssateccantoncreatedat', 'pfssateccapitalid')

cantonSchema = CantonSchema()
cantonSchema = CantonSchema(many=True)

#-----------------------------------------------------------
#-----------------TIPO DE ZONA---------------------------------
#-----------------------------------------------------------

class Tipozona(db.Model):
    __tablename__='pfssatectipozona'

    pfssatectipozonaid = db.Column(db.Integer, primary_key=True)
    pfssatectipozonanombre = db.Column(db.String(20), nullable=False)
    pfssatectipozonadetalle = db.Column(db.String(200), nullable=False)
    pfssatectipozonaestado = db.Column(db.String(1), nullable=True)
    pfssatectipozonacreatedat = db.Column(db.String(11), nullable=True) 


    def __init__(self, pfssatectipozonanombre,pfssatectipozonadetalle, pfssatectipozonaestado,pfssatectipozonacreatedat):
        self.pfssatectipozonanombre = pfssatectipozonanombre
        self.pfssatectipozonadetalle = pfssatectipozonadetalle
        self.pfssatectipozonaestado = pfssatectipozonaestado
        self.pfssatectipozonacreatedat = pfssatectipozonacreatedat

class TipozonaSchema(ma.Schema):
    class Meta:
        fields = ('pfssatectipozonaid', 'pfssatectipozonanombre','pfssatectipozonadetalle', 'pfssatectipozonaestado', 'pfssatectipozonacreatedat')

tipozonaSchema = TipozonaSchema()
tipozonaSchema = TipozonaSchema(many=True)

#-----------------------------------------------------------
#-----------------PARROQUIA---------------------------------
#-----------------------------------------------------------

class Parroquia(db.Model):
    __tablename__='pfssatecparroquia'

    pfssatecparroquiaid = db.Column(db.Integer, primary_key=True)
    pfssatecparroquianombre = db.Column(db.String(150), nullable=False)
    pfssatecparroquiaimage = db.Column(db.String(300), nullable=False)
    pfssatecparroquiacodigo = db.Column(db.String(120), nullable=False)
    pfssatecparroquiaestado = db.Column(db.String(1), nullable=True)
    pfssatecparroquiacreatedat = db.Column(db.String(11), nullable=True) 

    pfssateccantonid = db.Column(db.Integer, db.ForeignKey('pfssateccanton.pfssateccantonid',ondelete='CASCADE'), nullable=False)
    pfssateccanton = db.relationship('Canton',backref=db.backref('pfssatecparroquia',lazy=True))

    pfssatectipozonaid = db.Column(db.Integer, db.ForeignKey('pfssatectipozona.pfssatectipozonaid',ondelete='CASCADE'), nullable=False)
    pfssatectipozona = db.relationship('Tipozona',backref=db.backref('pfssatecparroquia',lazy=True))

    def __init__(self, pfssatecparroquianombre,pfssatecparroquiaimage, pfssatecparroquiacodigo,pfssatecparroquiaestado, pfssatecparroquiacreatedat):
        self.pfssatecparroquianombre = pfssatecparroquianombre
        self.pfssatecparroquiaimage = pfssatecparroquiaimage
        self.pfssatecparroquiacodigo = pfssatecparroquiacodigo
        self.pfssatecparroquiaestado = pfssatecparroquiaestado
        self.pfssatecparroquiacreatedat = pfssatecparroquiacreatedat

class ParroquiaSchema(ma.Schema):
    class Meta:
        fields = ('pfssatecparroquiaid', 'pfssatecparroquianombre','pfssatecparroquiaimage', 'pfssatecparroquiacodigo', 'pfssatecparroquiaestado' , 'pfssatecparroquiacreatedat', 'pfssateccantonid', 'pfssatectipozonaid')

parroquiaSchema = ParroquiaSchema()
parroquiaSchema = ParroquiaSchema(many=True)







