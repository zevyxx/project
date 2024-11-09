from flask import *
from flask_mysqldb import *

app = Flask(_name_)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "pc_db"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "" 

mysql = MySQL(app)

@app.route('/') 
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/simpan', methods = ["POST", "GET"] )
def simpan():
    nama_komputer = request.form["nama_komputer"]
    cpu_komputer = request.form["cpu_komputer"]
    rom_komputer = request.form["rom_komputer"]
    cursor = mysql.connection.cursor()
    query = ("insert into 40mil_pc values( %s, %s, %s, %s, %s )")
    data = ( "", nama_komputer, cpu_komputer, rom_komputer )
    cursor.execute( query, data )
    mysql.connection.commit()
    cursor.close()
    return f"sukses disimpan.."

@app.route('/tampil')
def tampil():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from 40mil_pc")
    data = cursor.fetchall()
    cursor.close()
    return render_template('tampil.html',data=data) 

@app.route('/hapus/<id_komputer>')
def hapus(id_komputer):
    cursor = mysql.connection.cursor()
    query = ("delete from 40mil_pc where id = %s")
    data = (id_komputer,)
    cursor.execute( query, data )
    mysql.connection.commit()
    cursor.close()
    return redirect('/tampil')

@app.route('/update/<id>')
def update(id_komputer):
    cursor = mysql.connection.cursor()
    sql = ("select * from 40mil_pc where id = %s")
    data = (id_komputer,)
    cursor.execute( sql, data )
    value = cursor.fetchone()
    return render_template('update.html',value=value) 


@app.route('/aksiupdate', methods = ["POST", "GET"] )
def aksiupdate():
    id_komputer = request.form["id_komputer"]
    nama_komputer = request.form["nama_komputer"]
    cpu_komputer = request.form["cpu_komputer"]
    rom_komputer = request.form["rom_komputer"]
    cursor = mysql.connection.cursor()
    query = ("update 40mil_pc set nama_komputer = %s, cpu_komputer = %s, rom_komputer = %s where id_komputer = %s")
    data = ( nama_komputer,cpu_komputer,rom_komputer, id_komputer ,)
    cursor.execute( query, data )
    mysql.connection.commit()
    cursor.close()
    return redirect('/tampil')


if _name_ == "_main_":
    app.run(debug=True)