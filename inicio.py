
from flask import Flask, g, session, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
import pymysql
app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'rh'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/minigame')
def minigame():
    return render_template("minigame.html")




@app.route('/videos')
def videos():
    return render_template("videos.html")
@app.route('/comentarios')
def comentarios():
    return render_template("comentarios.html")
@app.route('/register')
def register():
    return render_template("register.php")
@app.route('/login')
def login():
    return render_template("login.php")



@app.route('/contactos')
def contactos():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port='')
    cursor = conn.cursor()
    cursor.execute('select id,correo,comentarios,telefono,asunto from comenta order by id')
    datos = cursor.fetchall()
    return render_template("contactos.html", comentarios= datos)

@app.route('/agrega_contactos',methods={"post"})

def agrega_contactos():
    if request.method == 'POST':
      
        aux_usuario = request.form['introducir_nombre']
        aux_correo = request.form['introducir_email']
        aux_comentarios = request.form['introducir_mensaje']
        aux_telefono= request.form['introducir_telefono']
        aux_asunto= request.form['introducir_asunto']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
        cursor = conn.cursor()
        cursor.execute('insert into comenta (usuario,correo,comentarios,telefono,asunto) values (%s,%s,%s,%s,%s)',(aux_usuario,aux_correo,aux_comentarios,aux_telefono,aux_asunto))
        conn.commit()
    return redirect(url_for('index'))


@app.route('/crud')
def crud():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port='')
    cursor = conn.cursor()
    cursor.execute('select id, usuario,correo,comentarios,telefono,asunto from comenta order by id')
    datos = cursor.fetchall()
    return render_template("crud.html", usuario = datos)

@app.route('/editar/<string:id>')
def editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port='')
    cursor = conn.cursor()
    cursor.execute('select id,usuario,correo,comentarios,telefono,asunto from comenta where id = %s', (id))
    dato  = cursor.fetchall()
    return render_template("editar.html", comentar=dato[0])

@app.route('/editar_comenta/<string:id>',methods=['POST'])
def editar_comenta(id):
    if request.method == 'POST':
     
        aux_usuario = request.form['introducir_nombre']
        aux_correo = request.form['introducir_email']
        aux_comentarios = request.form['introducir_mensaje']
        aux_telefono= request.form['introducir_telefono']
        aux_asunto= request.form['introducir_asunto']
        
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port='')
        cursor = conn.cursor()
        cursor.execute('update comenta set usuario = %s,correo = %s,comentarios = %s,telefono = %s,asunto = %s where id = %s',(aux_usuario,aux_correo,aux_comentarios,aux_telefono,aux_asunto,id))
        conn.commit()
        return redirect(url_for('crud'))

@app.route('/borrar/<string:id>')
def borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='agenda', port='')
    cursor = conn.cursor()
    cursor.execute('delete from comenta where id = {0}'.format(id))
    conn.commit()
    return redirect(url_for('crud'))

@app.route('/insertar')
def insertar():
    return render_template("insertar.html")
@app.route('/agrega_comenta', methods=['POST'])
def agrega_comenta():
    if request.method == 'POST':
      
        aux_Descripcion = request.form['Descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
        cursor = conn.cursor()
        cursor.execute('insert into area (Descripcion) values (%s)',(aux_Descripcion))
        conn.commit()
    return redirect(url_for('index'))

@app.route('/comentariosescolaridad')
def comentariosescolaridad():
    return render_template("comentariosescolaridad.html")
@app.route('/escolaridad')
def escolaridad():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh', port='')
    cursor = conn.cursor()
    cursor.execute('select idescolaridad, descripcionescolaridad,edad,genero,correo,fecha from escolaridad order by idescolaridad')
    datos = cursor.fetchall()
    return render_template("escolaridad.html", descripcionescolaridad = datos)

@app.route('/editarescolaridad/<string:idescolaridad>')
def editarescolaridad(idescolaridad):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh', port='')
    cursor = conn.cursor()
    cursor.execute('select idescolaridad, descripcionescolaridad,edad,genero,correo,fecha from escolaridad where idescolaridad = %s', (idescolaridad))
    dato  = cursor.fetchall()
    return render_template("editarescolaridad.html", comentar=dato[0])

@app.route('/editar_escolaridad/<string:idescolaridad>',methods=['POST'])
def editar_escolaridad(idescolaridad):
    if request.method == 'POST':

        aux_descripcionescolaridad = request.form['descripcionescolaridad']
        edad = request.form['edad']
        gen = request.form['genero']
        correo = request.form['correo']
        fech = request.form['fecha']
      
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh', port='')
        cursor = conn.cursor()
        cursor.execute('update escolaridad set descripcionescolaridad= %s,edad = %s,genero = %s,correo = %s,fecha = %s where idescolaridad = %s',(aux_descripcionescolaridad,edad,gen,correo,fech,idescolaridad))
        conn.commit()
    return redirect(url_for('escolaridad'))

@app.route('/borrarescolaridad/<string:idescolaridad>')
def borrarescolaridad(idescolaridad):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh', port='')
    cursor = conn.cursor()
    cursor.execute('delete from escolaridad where idescolaridad = {0}'.format(idescolaridad))
    conn.commit()
    return redirect(url_for('escolaridad'))

@app.route('/insertarescolaridad')
def insertarescolaridad():
    return render_template("insertarescolaridad.html")

@app.route('/agrega_escolaridad', methods=['POST'])
def agrega_escolaridad():
    if request.method == 'POST':
      
        aux_descripcionescolaridad = request.form['descripcionescolaridad']
        edad = request.form['edad']
        gen = request.form['genero']
        correo = request.form['correo']
        fech = request.form['fecha']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
        cursor = conn.cursor()
        cursor.execute('insert into escolaridad (descripcionescolaridad,edad,genero,correo,fecha) values (%s,%s,%s,%s,%s)',(aux_descripcionescolaridad,edad,gen,correo,fech))
        conn.commit()
    return redirect(url_for('index'))
    
@app.route('/comentariosdocumentos')
def comentariosdocumentos():
    return render_template("comentariosdocumentos.html")
@app.route('/documentos')
def documentos():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh', port='')
    cursor = conn.cursor()
    cursor.execute('select iddocumentos, descripciondocumentos,juego,usuario,discord,tipo,horario from documentos order by iddocumentos')
    datos = cursor.fetchall()
    return render_template("documentos.html", descripciondocumentos = datos)

@app.route('/editardocumentos/<string:iddocumentos>')
def editardocumentos(iddocumentos):
    
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh', port='')
    cursor = conn.cursor()
    cursor.execute('select iddocumentos, descripciondocumentos,juego,usuario,discord,tipo,horario from documentos where iddocumentos = %s', (iddocumentos))
    dato  = cursor.fetchall()
    return render_template("editardocumentos.html", comentar=dato[0])

@app.route('/editar_documentos/<string:iddocumentos>',methods=['POST'])
def editar_documentos(iddocumentos):
    if request.method == 'POST':
        aux_descripciondocumentos = request.form['descripciondocumentos']
        jueg = request.form['juego']
        usu = request.form['usuario']
        disc = request.form['discord']
        tipo = request.form['tipo']
        hora = request.form['horario'] 
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh', port='')
        cursor = conn.cursor()
        cursor.execute('update documentos set descripciondocumentos= %s,juego = %s,usuario = %s,discord = %s,tipo = %s,horario = %s where iddocumentos = %s',(aux_descripciondocumentos,jueg,usu,disc,tipo,hora,iddocumentos))
        conn.commit()
    return redirect(url_for('documentos'))

@app.route('/borrardocumentos/<string:iddocumentos>')
def borrardocumentos(iddocumentos):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh', port='')
    cursor = conn.cursor()
    cursor.execute('delete from documentos where iddocumentos = {0}'.format(iddocumentos))
    conn.commit()
    return redirect(url_for('documentos'))

@app.route('/insertardocumentos')
def insertardocumentos():
    return render_template("insertardocumentos.html")

@app.route('/agrega_documentos', methods=['POST'])
def agrega_documentos():
    if request.method == 'POST':
      
        aux_descripciondocumentos = request.form['descripciondocumentos']
        jueg = request.form['juego']
        usu = request.form['usuario']
        disc = request.form['discord']
        tipo = request.form['tipo']
        hora = request.form['horario']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh' )
        cursor = conn.cursor()
        cursor.execute('insert into documentos (descripciondocumentos,juego,usuario,discord,tipo,horario) values (%s,%s,%s,%s,%s,%s)',(aux_descripciondocumentos,jueg,usu,disc,tipo,hora))
        conn.commit()
    return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)


