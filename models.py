from google.appengine.ext import ndb

class User(ndb.Model):
    username = ndb.StringProperty(indexed=True, required=True)
    password = ndb.StringProperty(indexed=True, required=True)
    email = ndb.StringProperty(indexed=True, required=True)
    semestre = ndb.IntegerProperty(indexed= True, required=True)
    cuenta = ndb.IntegerProperty(indexed= True, required=True)



#nombre, #integrantes, logo, proyecto, horario, alumnos
class Equipo(ndb.Model):
    nombre = ndb.StringProperty(indexed= True, required=True)
    integrantes = ndb.IntegerProperty(indexed= True, required=True)



#nombre,descripcion,duracion,equipo
class Proyecto(ndb.Model):
    nombre = ndb.StringProperty(indexed= True, required=True)
    descripcion = ndb.TextProperty(indexed= True, required=True)



def SaveUser(usernam,passwor,email,semestre,cuenta):
    try:
        a=User(
            cuenta=cuenta,
            semestre=semestre,
            email=email,
            password=passwor,
            username=usernam

        )
        a.put()
        return True
    except:
        return False



def SaveEquipo(nombre,integrantes):
    try:
        a=User(
            nombre=nombre,
            integrantes=integrantes

        )
        a.put()
        return True
    except:
        return False


def SaveProyecto(nombre,descripcion):
    try:
        a=User(
            nombre=nombre,
            descripcion=descripcion

        )
        a.put()
        return True
    except:
        return False
