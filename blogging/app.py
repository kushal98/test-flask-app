from flask import Flask , render_template,json,request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Kushal@123'
app.config['MYSQL_DATABASE_DB'] = {'webapp'}
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route('/show')
def showsignup():
    return render_template('signUp.htm')

@app.route('/signUp',methods=['POST'])
def signUp():
        #reading the posted values
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_createUser',(_name,_email,_password))

        data = cursor.fetchall()
 
        if len(data) is 0:
            conn.commit()
            return json.dumps({'message':'User created successfully !'})
        else:
            return json.dumps({'error':str(data[0])})

        


@app.route('/signin')
def signin():
    return render_template('')

if( __name__ == "__main__"):
    app.run()