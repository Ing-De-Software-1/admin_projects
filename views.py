from flask import Flask, render_template,request, session, redirect, url_for,flash
from config import DevelopmentConfig
#from models import *
import forms

app = Flask(__name__)
app.config.from_object('config')
app.config.from_object(DevelopmentConfig)

   
@app.errorhandler(404)
def not_found(error):
	return "Not Found."

@app.errorhandler(500)
def server_error(e):
    return 'An internal error occurred.', 500

@app.route(r'/')
def index():
#    a=ScanProyect()
#    if a[0]:
#        return render_template('index.html', a=a[1])

    return render_template('index.html')


@app.route(r'/registrar', methods=['GET','POST'])
def registrar():
    form_log = forms.LoginForm(request.form)
    form_reg = forms.RegisterForm(request.form)
    form_equ = forms.EquipoForm(request.form)
    form_pro = forms.ProyectoForm(request.form)
    e = ""
    if request.method== 'POST' and form_log.validate():
        user= form_log.username.data
        password= form_log.password.data
        return redirect(url_for('home'))

    return render_template('registrar.html', login=form_log , registro=form_reg, equipo=form_equ, proyecto=form_pro, e=e)




@app.route(r'/prm', methods=['GET','POST'])
@app.route(r'/prm/<us>/<pas>/<mail>/<int:sem>/<cta>', methods=['GET','POST'])
def prm(us="erick",pas="erick",mail="eric@gmail.com",sem=4,cta="313190944"):
    if SaveProyecto(
            "nombre del proyecto",
            "descripcion del proyecto",
            "equipo"

    ):
        return "yess"
    return "Nooo"



@app.route(r'/login', methods=['GET','POST'])
def login():
    form_log = forms.LoginForm(request.form)
    form_equ = forms.EquipoForm(request.form)
    form_reg = forms.RegisterForm(request.form)
    e = ""
    h=''
    i=''
    b=''
    c=''
    if request.method== 'POST' and form_log.validate():
        user= form_log.username.data
        password= form_log.password.data
        a = LoginModel(str(user))
        if a[2]:
            if a[0] == str(user) and a[1] == str(password):
                session['username'] = user
                return redirect(url_for('home'))
            else:
                e = "usuario o contrasena incorrectos"
        else:
            e = "usuario o contrasena incorrectos"
    return render_template('login.html', login=form_log ,equipo=form_equ, registro=form_reg, e=e)



@app.route(r'/registro/persona', methods=['GET','POST'])
def registroPersona():
    form_log = forms.LoginForm(request.form)
    form_reg = forms.RegisterForm(request.form)
    err=''
    if request.method== 'POST' and form_reg.validate():
        print "ya mero"
        user= (form_reg.username.data).encode('utf-8')
        email= form_reg.email.data
        password= (form_reg.password.data).encode('utf-8')
        semestre= (form_reg.semestre.data).encode('utf-8')
        cuenta= (form_reg.cuenta.data).encode('utf-8')
        print "ya mero2"
        if SaveUser(unicode(str(user), "utf-8"),
                    unicode(str(password), "utf-8"),
                    str(email),
                    int(semestre),
                    unicode(str(cuenta), "utf-8")
                    ):#usernam,passwor,email,semestre,cuenta
            session['username'] = unicode(user,"utf-8")
            return redirect(url_for('home'))
    return render_template('login.html', form=form_log , fo=form_reg, e=err)



@app.route(r'/registro/eq', methods=['GET','POST'])
def registroEquipo():
    form_equ = forms.EquipoForm(request.form)
    e=''
    if request.method== 'POST' and form_equ.validate():

        name =(form_equ.name.data).encode('utf-8')
        nombre=str(unicode(str(name), "utf-8"))
        print nombre
        print type(nombre)
        a=SaveEquipo(nombre,2)
        #b=SaveEquipo("equipo dinamita  ",2)
        session['equipo'] = nombre
        return redirect(url_for('home'))
    return "Error"


@app.route(r'/home', methods=['GET','POST'])
def home():
    form_reg = forms.RegisterForm(request.form)
    form_pro = forms.ProyectoForm(request.form)
    e=''
    return render_template('home.html' ,proyecto=form_pro, registro=form_reg,  e=e)



@app.route(r'/registro/miembro', methods=['GET','POST'])
def registromiembro():
    form_reg = forms.RegisterForm(request.form)
    err=''
    if request.method== 'POST' :
        user= (form_reg.username.data).encode('utf-8')
        email= form_reg.email.data
        password= (form_reg.password.data).encode('utf-8')
        semestre= (form_reg.semestre.data).encode('utf-8')
        cuenta= (form_reg.cuenta.data).encode('utf-8')
        #a=session['equipo']
        if SaveUser(unicode(str(user), "utf-8"),
                    unicode(str(password), "utf-8"),
                    str(email),
                    int(semestre),
                    unicode(str(cuenta), "utf-8"),
                    session['equipo']
                    ):
            return redirect(url_for('home'))
    return "Error"



@app.route(r'/registro/proyecto', methods=['GET','POST'])
def registroproyecto():
    form_pro = forms.ProyectoForm(request.form)
    err=''
    if request.method== 'POST' and form_pro.validate() :
        name= (form_pro.name.data).encode('utf-8')
        desc= (form_pro.descripcion.data).encode('utf-8')
        session['proyecto']=name
        if SaveProyecto(
                unicode(str(name), "utf-8"),
                unicode(str(desc), "utf-8"),
                session['equipo']
                ):
            return redirect(url_for('home'))
    return "Error"



@app.route(r'/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('index'))
