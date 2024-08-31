from flask import Flask, render_template, flash,redirect,url_for,session,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "pcman"

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="quiz"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

mysql = MySQL(app)

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        q1 = request.form['question1']
        q2 = request.form['question2']
        

        if q1 == "tensorflow" and q2 == "noron":
            point = 100
        elif q1 == "tensorflow" and q2 != "noron":
            point = 75
        elif q1 != "tensorflow" and q2 == "noron":
            point = 75
        else:
            point = 50

        cursor = mysql.connection.cursor()
        query = "Select MAX(point) from questions"
        cursor.execute(query)
        data = cursor.fetchone()
        if data:
            big_point = data['MAX(point)']
            
            if point >= big_point:
                big_point = point
                query = "insert into questions(point) values(%s)"
                cursor.execute(query, (big_point,))
                mysql.connection.commit()
        else:
            query = "insert into questions(point) values(%s)"
            cursor.execute(query, (point, ))
            mysql.connection.commit()
        cursor.close()

        return render_template("result.html", point=point, big_point = big_point)
    cursor = mysql.connection.cursor()
    query = "Select MAX(point) from questions"
    cursor.execute(query)
    data = cursor.fetchone()
    big_point = data['MAX(point)']
    return render_template("index.html", big_point = big_point)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)