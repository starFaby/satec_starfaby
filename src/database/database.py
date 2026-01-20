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
    
    

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        
    pfsusersid = ma.auto_field()
    pfsuserscedula = ma.auto_field()
    pfsusersnombres = ma.auto_field()
    pfsusersapellidos = ma.auto_field()
    pfsusersusername = ma.auto_field()
    pfsusersemail = ma.auto_field()
    pfsuserspassword = ma.auto_field()
    pfsusersdireccion = ma.auto_field()
    pfsuserscelular = ma.auto_field()
    pfsuserstelefono = ma.auto_field()
    pfsusersisadmin = ma.auto_field()
    pfsusersavatar = ma.auto_field()
    pfsusersestado = ma.auto_field()
    pfsuserscreatedat = ma.auto_field()

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
    pfssatecregionubicacion = db.Column(db.String(500), nullable=False)
    pfssatecregionestado = db.Column(db.String(1), nullable=True)
    pfssatecregioncreatedat = db.Column(db.String(11), nullable=True) 


    def __init__(self, pfssatecregionnombre, pfssatecregionimage, pfssatecregiondetalle ,pfssatecregionubicacion, pfssatecregionestado, pfssatecregioncreatedat):
        self.pfssatecregionnombre = pfssatecregionnombre
        self.pfssatecregionimage = pfssatecregionimage
        self.pfssatecregiondetalle = pfssatecregiondetalle
        self.pfssatecregionubicacion = pfssatecregionubicacion
        self.pfssatecregionestado = pfssatecregionestado
        self.pfssatecregioncreatedat = pfssatecregioncreatedat

class RegionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Region

    pfssatecregionid = ma.auto_field()
    pfssatecregionnombre = ma.auto_field()
    pfssatecregionimage = ma.auto_field()
    pfssatecregiondetalle = ma.auto_field()
    pfssatecregionubicacion = ma.auto_field()
    pfssatecregionestado = ma.auto_field()
    pfssatecregioncreatedat = ma.auto_field()

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
    pfssatecprovinciadetalle = db.Column(db.String(200), nullable=False)
    pfssatecprovinciaubicacion = db.Column(db.String(500), nullable=False)
    pfssatecprovinciacodigo = db.Column(db.String(120), nullable=False)
    pfssatecprovinciaestado = db.Column(db.String(1), nullable=True)
    pfssatecprovinciacreatedat = db.Column(db.String(11), nullable=True) 

    pfssatecregionid = db.Column(db.Integer, db.ForeignKey('pfssatecregion.pfssatecregionid',ondelete='CASCADE'), nullable=False)
    pfssatecregion = db.relationship('Region',backref=db.backref('pfssatecprovincia',lazy=True))

    def __init__(self, pfssatecprovincianombre,pfssatecprovinciaimage,pfssatecprovinciadetalle, pfssatecprovinciaubicacion, pfssatecprovinciacodigo,pfssatecprovinciaestado, pfssatecprovinciacreatedat, pfssatecregionid):
        self.pfssatecprovincianombre = pfssatecprovincianombre
        self.pfssatecprovinciaimage = pfssatecprovinciaimage
        self.pfssatecprovinciadetalle = pfssatecprovinciadetalle
        self.pfssatecprovinciaubicacion = pfssatecprovinciaubicacion
        self.pfssatecprovinciacodigo = pfssatecprovinciacodigo
        self.pfssatecprovinciaestado = pfssatecprovinciaestado
        self.pfssatecprovinciacreatedat = pfssatecprovinciacreatedat
        self.pfssatecregionid = pfssatecregionid

class ProvinciaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Provincia

    pfssatecprovinciaid = ma.auto_field()
    pfssatecprovincianombre = ma.auto_field()
    pfssatecprovinciaimage = ma.auto_field()
    pfssatecprovinciadetalle = ma.auto_field()
    pfssatecprovinciaubicacion = ma.auto_field()
    pfssatecprovinciacodigo = ma.auto_field()
    pfssatecprovinciaestado = ma.auto_field()
    pfssatecprovinciacreatedat = ma.auto_field()

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
    pfssateccapitaldetalle = db.Column(db.String(120), nullable=False)
    pfssateccapitalubicacion = db.Column(db.String(500), nullable=False)
    pfssateccapitalcodigo = db.Column(db.String(120), nullable=False)
    pfssateccapitalestado = db.Column(db.String(1), nullable=True)
    pfssateccapitalcreatedat = db.Column(db.String(11), nullable=True) 

    pfssatecprovinciaid = db.Column(db.Integer, db.ForeignKey('pfssatecprovincia.pfssatecprovinciaid',ondelete='CASCADE'), nullable=False)
    pfssatecprovincia = db.relationship('Provincia',backref=db.backref('pfssateccapital',lazy=True))

    def __init__(self, pfssateccapitalnombre,pfssateccapitalimage,pfssateccapitaldetalle,pfssateccapitalubicacion, pfssateccapitalcodigo,pfssateccapitalestado, pfssateccapitalcreatedat, pfssatecprovinciaid):
        self.pfssateccapitalnombre = pfssateccapitalnombre
        self.pfssateccapitalimage = pfssateccapitalimage
        self.pfssateccapitaldetalle = pfssateccapitaldetalle
        self.pfssateccapitalubicacion = pfssateccapitalubicacion
        self.pfssateccapitalcodigo = pfssateccapitalcodigo
        self.pfssateccapitalestado = pfssateccapitalestado
        self.pfssateccapitalcreatedat = pfssateccapitalcreatedat
        self.pfssatecprovinciaid = pfssatecprovinciaid

class CapitalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Capital

    pfssateccapitalid = ma.auto_field()
    pfssateccapitalnombre = ma.auto_field()
    pfssateccapitalimage = ma.auto_field()
    pfssateccapitaldetalle = ma.auto_field()
    pfssateccapitalubicacion = ma.auto_field()
    pfssateccapitalcodigo = ma.auto_field()
    pfssateccapitalestado = ma.auto_field()
    pfssateccapitalcreatedat = ma.auto_field()
    pfssatecprovinciaid = ma.auto_field()

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
    pfssateccantondetalle = db.Column(db.String(120), nullable=False)
    pfssateccantonubicacion = db.Column(db.String(500), nullable=False)
    pfssateccantoncodigo = db.Column(db.String(120), nullable=False)
    pfssateccantonestado = db.Column(db.String(1), nullable=True)
    pfssateccantoncreatedat = db.Column(db.String(11), nullable=True) 

    pfssatecprovinciaid = db.Column(db.Integer, db.ForeignKey('pfssatecprovincia.pfssatecprovinciaid',ondelete='CASCADE'), nullable=False)
    pfssatecprovincia = db.relationship('Provincia',backref=db.backref('pfssateccanton',lazy=True))


    def __init__(self, pfssateccantonnombre,pfssateccantonimage, pfssateccantoncodigo,pfssateccantondetalle,pfssateccantonubicacion,pfssateccantonestado, pfssateccantoncreatedat, pfssatecprovinciaid):
        self.pfssateccantonnombre = pfssateccantonnombre
        self.pfssateccantonimage = pfssateccantonimage
        self.pfssateccantondetalle = pfssateccantondetalle
        self.pfssateccantonubicacion = pfssateccantonubicacion
        self.pfssateccantoncodigo = pfssateccantoncodigo
        self.pfssateccantonestado = pfssateccantonestado
        self.pfssateccantoncreatedat = pfssateccantoncreatedat
        self.pfssatecprovinciaid = pfssatecprovinciaid

class CantonSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Canton 
    
    pfssateccantonid = ma.auto_field()
    pfssateccantonnombre = ma.auto_field()
    pfssateccantonimage = ma.auto_field()
    pfssateccantondetalle = ma.auto_field()
    pfssateccantonubicacion = ma.auto_field()
    pfssateccantoncodigo = ma.auto_field()
    pfssateccantonestado = ma.auto_field()
    pfssateccantoncreatedat = ma.auto_field()
    pfssatecprovinciaid = ma.auto_field()

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

class TipozonaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tipozona

    pfssatectipozonaid = ma.auto_field()
    pfssatectipozonanombre = ma.auto_field()
    pfssatectipozonadetalle = ma.auto_field()
    pfssatectipozonaestado = ma.auto_field()
    pfssatectipozonacreatedat = ma.auto_field()   

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
    pfssatecparroquiadetalle = db.Column(db.String(120), nullable=False)
    pfssatecparroquiaubicacion = db.Column(db.String(120), nullable=False)
    pfssatecparroquiacodigo = db.Column(db.String(120), nullable=False)
    pfssatecparroquiaestado = db.Column(db.String(1), nullable=True)
    pfssatecparroquiacreatedat = db.Column(db.String(11), nullable=True) 

    pfssateccantonid = db.Column(db.Integer, db.ForeignKey('pfssateccanton.pfssateccantonid',ondelete='CASCADE'), nullable=False)
    pfssateccanton = db.relationship('Canton',backref=db.backref('pfssatecparroquia',lazy=True))

    pfssatectipozonaid = db.Column(db.Integer, db.ForeignKey('pfssatectipozona.pfssatectipozonaid',ondelete='CASCADE'), nullable=False)
    pfssatectipozona = db.relationship('Tipozona',backref=db.backref('pfssatecparroquia',lazy=True))

    def __init__(self, pfssatecparroquianombre,pfssatecparroquiaimage,pfssatecparroquiadetalle,pfssatecparroquiaubicacion, pfssatecparroquiacodigo,pfssatecparroquiaestado, pfssatecparroquiacreatedat, pfssateccantonid, pfssatectipozonaid):
        self.pfssatecparroquianombre = pfssatecparroquianombre
        self.pfssatecparroquiaimage = pfssatecparroquiaimage
        self.pfssatecparroquiadetalle = pfssatecparroquiadetalle
        self.pfssatecparroquiaubicacion = pfssatecparroquiaubicacion
        self.pfssatecparroquiacodigo = pfssatecparroquiacodigo
        self.pfssatecparroquiaestado = pfssatecparroquiaestado
        self.pfssatecparroquiacreatedat = pfssatecparroquiacreatedat
        self.pfssateccantonid = pfssateccantonid
        self.pfssatectipozonaid = pfssatectipozonaid

class ParroquiaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Parroquia

    pfssatecparroquiaid = ma.auto_field() 
    pfssatecparroquianombre = ma.auto_field() 
    pfssatecparroquiaimage = ma.auto_field() 
    pfssatecparroquiadetalle = ma.auto_field() 
    pfssatecparroquiaubicacion = ma.auto_field() 
    pfssatecparroquiacodigo = ma.auto_field() 
    pfssatecparroquiaestado = ma.auto_field() 
    pfssatecparroquiacreatedat = ma.auto_field()  
    pfssateccantonid = ma.auto_field()  
    pfssatectipozonaid = ma.auto_field()  


parroquiaSchema = ParroquiaSchema()
parroquiaSchema = ParroquiaSchema(many=True)







