from google.appengine.ext import ndb

class User(ndb.Model):
    username = ndb.StringProperty(indexed=True, required=True)
    password = ndb.StringProperty(indexed=True, required=True)
    email = ndb.StringProperty(indexed=True, required=True)
    semestre = ndb.IntegerProperty(indexed= True, required=True)
    cuenta = ndb.IntegerProperty(indexed= True, required=True)


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
