from flask import Flask, render_template, flash,redirect,url_for,session,request
#from flask_sqlalchemy import SQLAlchemy
#from flask_mysqldb import MySQL
#from passlib.hash import sha256_crypt
from functools import wraps
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = "pcman"

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="neusiber"
app.config["MYSQL_CURSORCLASS"]="DictCursor"

#mysql = MySQL(app)

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        query = "Insert into activities(name,email) VALUES (%s,%s)"

        cursor.execute(query, (name, email))

        mysql.connection.commit()
        cursor.close()

        flash("Kaydınız Alınmıştır...", "success")

        return redirect(url_for("index"))

    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods = ["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        cursor = mysql.connection.cursor()
        query = "Insert into messages(name,email,message) VALUES (%s,%s,%s)"

        cursor.execute(query, (name, email, message))

        mysql.connection.commit()
        cursor.close()

        flash("Mesajınız Gönderildi...", "success")

        return redirect(url_for("contact"))

    return render_template("contact.html")

@app.route('/trainings')
def trainings():
    return render_template('trainings.html')

@app.route('/network')
def network():
    return render_template('network.html')

@app.route('/network/network_video')
def network_video():
    return render_template('network_video.html')

@app.route('/windows')
def windows():
    return render_template('windows.html')

@app.route('/windows/windows_video')
def windows_video():
    return render_template('windows_video.html')

@app.route('/linux-1')
def linux_1():
    return render_template('linux_1.html')

@app.route('/linux-1/linux_video1')
def linux1_video():
    return render_template('linux1_video.html')

@app.route('/linux-2')
def linux_2():
    return render_template('linux_2.html')

@app.route('/linux-2/linux_video2')
def linux2_video():
    return render_template('linux2_video.html')

@app.route('/nmap')
def nmap():
    return render_template('nmap.html')

@app.route('/nmap/nmap_video')
def nmap_video():
    return render_template('nmap_video.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/article-1')
def article():
    return render_template('article.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username_entered = request.form['email']
        password_entered =  request.form['password']

        cursor = mysql.connection.cursor()

        query = "Select * from users where email = %s"

        result = cursor.execute(query, (username_entered,))

        if result > 0:
            data = cursor.fetchone()
            password = data["password"]
            if password_entered==password:
                flash("Giriş Başarılı!", "success")

                session["logged_in"] = True
                session["email"] = username_entered

                return redirect(url_for("dashboard"))
            else:
                flash("Kullanıcı Adı veya Parola Hatalı!", "danger")
                return redirect(url_for("login"))
        else:
            flash("Böyle bir kullanıcı bulunmuyor...", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route('/register',  methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor()
        query = "Insert into users(name,email,username,password) VALUES (%s,%s,%s,%s)"

        cursor.execute(query, (name, email, username, password))

        mysql.connection.commit()
        cursor.close()

        flash("Kayıt Başarılı...", "success")

        return redirect(url_for("register"))

    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)
    