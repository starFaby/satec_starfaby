#----------
#--Client--
#----------
#Router
#clientControllerStart
from src.client.router.clientRouterStart import crs

#----------
#--AUTH--
#----------
#Router
# Router DataBase 
from src.auth.router.authRouterDataBase import ardbsatec
# Router Login 
from src.auth.router.authRouterUserLoginIn import arulgn 
from src.auth.router.authRouterUserLogout import araulgt

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#------------------------------ADMIN------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#--------------------------
#---ADMIN ROUTER------
#--------------------------

from src.admin.router.adminRouterUser import aru


#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------ADMIN CLIENT------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
from src.client.router.clientRouterSatec import crstc 
from src.client.router.clientRouterParroquia import crparr  
from src.client.router.clientRouterCanton import crcnt  
from src.client.router.clientRouterParroquiaGeneral import crparrg  





