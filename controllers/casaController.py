def index():
    idNum= getId(URL(args=request.args, vars=request.get_vars, host=True))
    casa= db.casa(idNum)
    return dict(casa=casa)

def getId(url):
    cont=0
    cn=0
    for i in url:
        if (i=='='):
            cn=cont
        cont=cont+1
    numId=url[cn+1: len(url)]
    return numId