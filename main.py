from flask import *
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='harsh@777'
app.config['MYSQL_DB']='form'
mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def form():
    if request.method=='POST':
        email=request.form['Email']
        password=request.form['Password']
        cur=mysql.connection.cursor()
        cur.execute('insert into i(email,password) values(%s,%s)',(email,password))
        mysql.connection.commit()
        cur.close()
        return 'Success'
    return render_template('form.html')
if __name__=='__main__':
    app.run(debug=True)