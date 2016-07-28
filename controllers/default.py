# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
from gluon.serializers import loads_json

def index():
    return dict()



def galeriaCasas():
    return dict()



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

def registrarse():
    form=SQLFORM(db.usuario)
    if form.accepts(request.vars,session):
        response.flash='Usuario Registrado'
    return dict(form=form)

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def getMarkers():
    mapas = []
    casas = db().select(db.casa.ALL)
    for casa in casas:
        markers=db(db.marker.id==casa.id_marker).select()
        if(casa.disponible=="Disponible"):
            mapa = {
                'lat': markers[0].lat,
                'lng': markers[0].lng,
                'title': casa.nombre,
                'infoWindow': { 'content': "<h4>" + casa.nombre +"</h4>"},
                'icon':'../static/icons/icon_green32.png',
            }
        else:
            mapa = {
            'lat': markers[0].lat,
            'lng': markers[0].lng,
            'title': casa.nombre,
            'infoWindow': { 'content': '<h3>' + casa.nombre +'</h3>' },
            'icon':'../static/icons/icon_pink32.png',
            }
        mapas.append(mapa)
    return response.json(mapas)     

def getAll():
    mapas =[]
    rows = db(db.casa.id_marker == db.marker.id).select()
    for row in rows:
        mapa={
            'lat': marker.lat,
            'lng': marker.lng,
            'title': casa.nombre,
            'infoWindow': { 'content': "<h4>" + casa.disponible},
            'icon':'../static/icons/icon_yellow32.png',
        }
        mapas.append(mapa)
    return response.json(mapas)