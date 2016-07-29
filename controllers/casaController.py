def index():
    idNum= getId(URL(args=request.args, vars=request.get_vars, host=True))
    casa= db.casa(idNum)
    marker= db.marker(casa.id_marker)
    contacto = db.usuario(marker.id_user)
    return dict(casa=casa, contacto=contacto)

def getId(url):
    cont=0
    cn=0
    for i in url:
        if (i=='='):
            cn=cont
        cont=cont+1
    numId=url[cn+1: len(url)]
    return numId

def download():
    return response.download(request, db)