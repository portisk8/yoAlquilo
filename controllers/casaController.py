from gluon.serializers import loads_json
import os

def index():
    idNum= getId2(URL(args=request.args, vars=request.get_vars, host=True))
    idCasa = idNum
    casa= db.casa(idNum)
    marker= db.marker(casa.id_marker)
    contacto = db.auth_user(marker.id_user)
    return dict(casa=casa, contacto=contacto)

def agregarCasa():
    if auth.user!=None:
        form=SQLFORM.factory(db.marker,db.casa, Field('file', 'upload', uploadfolder=os.path.join(request.folder, 'uploads')),
        table_name='casa')
        if form.accepts(request.vars):
            id_marker = db.marker.insert(**db.marker._filter_fields(form.vars))
            form.vars.id_marker=id_marker
            db.casa.insert(**db.casa._filter_fields(form.vars))
            response.flash='Thanks for filling the form'
        return dict(form=form)
    else:
        return redirect(URL('default','index'))

def getId(url):
    cont=0
    cn=0
    for i in url:
        if (i=='='):
            cn=cont
        cont=cont+1
    numId=url[cn+1: len(url)]
    return numId

def getId2(url):
    longitud=len(url)
    c=longitud
    cont=0
    for i in range(longitud):
        c=c-1
        if (url[c]!='/'):
            cont+=1
        else:
            break
    ini=longitud - cont
    numId = url[ini:longitud]
    return numId


def getMarker():
    idNum= getId(URL(args=request.args, vars=request.get_vars, host=True))
    idNum = getId2(idNum)
    casa= db.casa(idNum)
    marker= db.marker(casa.id_marker)
    if(casa.disponible=="Disponible"):
        icono = '../../static/icons/icon_green32.png'
        disp ="<p><font color='green'>"+casa.disponible+"</font></p>"
    else:
        icono = '../../static/icons/icon_pink32.png'
        disp ="<p><font color='red'>"+casa.disponible+"</font></p>"
    mapa = {
        'lat': marker.lat,
        'lng': marker.lng,
        'title': casa.nombre,
        'infoWindow': { 'content': '<h4>' + casa.nombre +"</h4>"+disp },
        'icon':icono,
        }
    return response.json(mapa)

def download():
    return response.download(request, db)