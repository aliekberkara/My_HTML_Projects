from flask import Flask,render_template,flash,redirect,url_for,session,request
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps
from werkzeug.utils import secure_filename
import pdfkit
from flask import make_response
# User Login Control

def cvlogin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Giriş Yapmak Gerekli!", "danger")
            return redirect(url_for("cvlogin"))
    return decorated_function

def bloglogin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_out" in session:
            return f(*args, **kwargs)
        else:
            flash("Giriş Yapmak Gerekli!", "danger")
            return redirect(url_for("bloglogin"))
    return decorated_function

# Article

class ArticleForm(Form):
    title = StringField("Makale Başlığı", validators=[validators.Length(min = 5, max = 100, message = "5-100 karakter olacak şekilde Makale Başlığı giriniz...")])
    content = TextAreaField("Makale İçeriği", validators=[validators.Length(min = 10, message = "En az 10 karakter olacak şekilde Makale İçeriği giriniz...")])

# Personal Informations

class PersonalForm(Form):
    name = StringField("İsim*", validators=[validators.DataRequired("Lütfen Adınızı Giriniz...")])
    surname = StringField("Soyad*", validators=[validators.DataRequired("Lütfen Soyadınızı Giriniz...")])
    email = StringField("E-posta Adresi*", validators=[validators.Email("Lütfen Geçerli Bir Email Adresi Giriniz...")])
    phone = StringField("Telefon Numarası", validators=[validators.Length(min=11, max=11, message="Geçerli bir Telefon numarası giriniz...")])
    address = StringField("Adres")
    post_code=StringField("Posta Kodu", validators=[validators.Length(min=5,max=5,message="Geçerli bir posta kodu giriniz...")])
    city = StringField("Şehir/İlçe")
    birthplace = StringField("Doğum Yeri")
    license = StringField("Sürücü Ehliyeti")
    military = StringField("Askerlik Durumu")
    linkedin = StringField("LinkedIn")
    instagram = StringField("Instagram")
    github = StringField("Github")
    website = StringField("Web Sitesi")

# Profil Informations

class ProfilForm(Form):
    about = TextAreaField("", validators=[validators.Length(min = 10, message = "En az 10 karakter olacak şekilde Özet giriniz...")])
    work_title = StringField("İş Başlığı", validators=[validators.Length(min = 5, message = "En az 5 karakter olacak şekilde İş Başlığı giriniz...")])
    company_name = StringField("Şirket Adı", validators=[validators.Length(min = 5, message = "En az 5 karakter olacak şekilde Şirket Adı giriniz...")])
    city = StringField("Şehir", validators=[validators.Length(min = 5, message = "En az 5 karakter olacak şekilde Şehir giriniz...")])
    country = StringField("Ülke", validators=[validators.Length(min = 5, message = "En az 5 karakter olacak şekilde Ülke giriniz...")])
    work_about = TextAreaField("",  validators=[validators.Length(min = 10, message = "En az 10 karakter olacak şekilde İş Deneyimi giriniz...")])
    school_name = StringField("Okul Adı", validators=[validators.Length(min = 5, message = "En az 5 karakter olacak şekilde Okul Adı giriniz...")])
    school_location = StringField("Okul Konumu", validators=[validators.Length(min = 5, message = "En az 5 karakter olacak şekilde Konum giriniz...")])
    degree = StringField("Derece", validators=[validators.Length(min = 5, message = "En az 5 karakter olacak şekilde Derece giriniz...")])
    work_area = StringField("Çalışma Alanı", validators=[validators.Length(min = 5, message = "En az 5 karakter olacak şekilde Çalışma Alanı giriniz...")])
    language = StringField("Dil", validators=[validators.Length(min = 5, message = "En az 5 karakter olacak şekilde Dil giriniz...")])
    skill = StringField("Beceri", validators=[validators.Length(min = 5, message = "En az 5 karakter olacak şekilde Beceri giriniz...")])

# User Register Form

class RegisterForm(Form):
    name = StringField("Ad", validators=[validators.Length(min = 3, max = 25, message = "3-25 karakter olacak şekilde Adınızı giriniz...")])
    surname = StringField("Soyad", validators=[validators.Length(min = 2, max = 25, message = "2-25 karakter olacak şekilde Soyadınızı giriniz...")])
    email = StringField("Email Adresi", validators=[validators.Email("Lütfen Geçerli Bir Email Adresi Giriniz..."), validators.DataRequired("Lütfen Bir Email Adresi Giriniz...")])
    username = StringField("Kullanıcı Adı", validators=[validators.Length(min = 5, max = 35), validators.DataRequired("Lütfen Kullanıcı Adı Giriniz...")])
    password = PasswordField("Parola", validators=[
        validators.DataRequired("Lütfen Bir Parola Giriniz..."),
        validators.EqualTo("confirm", "Parolanız Uyuşmuyor...")
    ])
    confirm = PasswordField("Parola(Tekrar)")

# User Login Form

class LoginForm(Form):
    username = StringField("Kullanıcı Adı", validators=[validators.DataRequired("Lütfen Kullanıcı Adı Giriniz...")])
    password = PasswordField("Parola", validators = [validators.DataRequired("Lütfen Bir Parola Giriniz...")])

# Article Form

class ContactForm(Form):
    name = StringField("Adınız", validators=[validators.Length(min = 2, max = 30, message = "2-30 karakter olacak şekilde Adınızı giriniz...")])
    surname = StringField("Soyadınız", validators=[validators.Length(min = 2, max = 20, message = "2-20 karakter olacak şekilde Soyadınızı giriniz...")])
    email = StringField("Email Adresi", validators=[validators.Email("Lütfen Geçerli Bir Email Adresi Giriniz..."), validators.DataRequired("Lütfen Bir Email Adresi Giriniz...")])
    message = TextAreaField("Mesajınız", validators=[validators.Length(min = 10, message = "En az 10 karakter olacak şekilde Mesajınızı giriniz...")])

app = Flask(__name__)

app.secret_key = ""

app.config["MYSQL_HOST"]=""
app.config["MYSQL_USER"]=""
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]=""
app.config["MYSQL_CURSORCLASS"]=""
app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)

mysql = MySQL(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    complete = db.Column(db.Boolean)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods = ["GET", "POST"])
def contact():
    form = ContactForm(request.form)

    if request.method == "POST" and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        message = form.message.data

        cursor = mysql.connection.cursor()
        query = "Insert into messages(name,surname,email,message) VALUES (%s,%s,%s,%s)"

        cursor.execute(query, (name, surname, email, message))

        mysql.connection.commit()
        cursor.close()

        flash("Mesajınız Gönderildi...", "success")

        return redirect(url_for("contact"))

    return render_template("contact.html", form = form)

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/cvbuilder")
def cvbuilder():
    return render_template("cvbuilder.html")

@app.route("/cvabout")
def cvabout():
    return render_template("cvabout.html")

@app.route("/cvlogin", methods = ["GET","POST"])
def cvlogin():
    form = LoginForm(request.form)

    if request.method == "POST":
        username_entered = form.username.data
        password_entered = form.password.data

        cursor = mysql.connection.cursor()

        query = "Select * from cv_users where username = %s"

        result = cursor.execute(query, (username_entered,))

        if result > 0:
            data = cursor.fetchone()
            password = data["password"]
            if sha256_crypt.verify(password_entered, password):
                flash("Giriş Başarılı!", "success")

                session["logged_in"] = True
                session["username"] = username_entered

                return redirect(url_for("cvbuilder"))
            else:
                flash("Kullanıcı Adı veya Parola Hatalı!", "danger")
                return redirect(url_for("cvlogin"))
        else:
            flash("Böyle bir kullanıcı bulunmuyor...", "danger")
            return redirect(url_for("cvlogin"))

    return render_template("cvlogin.html", form = form)

@app.route("/cvregister", methods = ["GET","POST"])
def cvregister():
    form = RegisterForm(request.form)
    
    if request.method == "POST" and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()

        query = "Insert into cv_users(name, surname, email, username, password) VALUES(%s,%s,%s,%s,%s)"

        cursor.execute(query, (name, surname, email, username, password))

        mysql.connection.commit()

        cursor.close()
        
        flash("Kayıt Başarılı!", "success")

        return redirect(url_for("cvlogin"))
    else:
        return render_template("cvregister.html", form = form)

@app.route("/cvlogout")
@cvlogin_required
def cvlogout():
    session.clear()
    return redirect(url_for("cvbuilder"))

@app.route("/cvpersonal", methods = ["GET", "POST"])
@cvlogin_required
def cvpersonal():
    form = PersonalForm(request.form)
    if request.method == "POST" and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        phone = form.phone.data
        address = form.address.data
        post_code = form.post_code.data
        city = form.city.data
        birthday = request.form.get('yillar') + '-' + request.form.get('aylar') + '-' + request.form.get('days')
        birthplace = form.birthplace.data
        license = form.license.data
        gender = request.form.get('gender')
        military = form.military.data
        marital = request.form.get("marital")
        linkedin = form.linkedin.data
        instagram = form.instagram.data
        github = form.github.data
        website = form.website.data
        file = request.files["file"]
        
        img_name = secure_filename(file.filename)
        mimetype = file.mimetype
        img = file.read()

        cursor = mysql.connection.cursor()
        query = "Insert into personal_infos(name,surname,email,phone,address,post_code,city,birthday,birthplace,license,gender,military,marital,linkedin,instagram,github,website, img_name, img,username) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(query, (name,surname,email,phone,address,post_code,city,birthday,birthplace,license,gender,military,marital,linkedin,instagram,github,website,img_name,img,session["username"]))

        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("cvprofile"))

    return render_template("cvpersonal.html", form = form)

@app.route("/cvprofile", methods = ["GET", "POST"])
@cvlogin_required
def cvprofile():
    form = ProfilForm(request.form)

    if request.method == "POST" and form.validate():
        about = form.about.data
        work_title = form.work_title.data
        company_name = form.company_name.data
        city = form.city.data
        country = form.country.data
        start_date = request.form.get("years") + '-' + request.form.get("months") + '-' + '01'
        finish_date = request.form.get("year") + '-' + request.form.get("month") + '-' + '01'
        work_about = form.work_about.data
        school_name = form.school_name.data
        school_location = form.school_location.data
        degree = form.degree.data
        work_area = form.work_area.data
        school_start = request.form.get("yearss") + '-' + request.form.get("monthss") + '-' + '01'
        school_finish = request.form.get("yearsss") + '-' + request.form.get("monthsss") + '-' +  '01'
        language = form.language.data
        lang_degree = request.form.get("level")
        skill = form.skill.data
        skill_degree = request.form.get("level1")

        cursor = mysql.connection.cursor()
        query = "Insert into profile_infos(about,work_title,company_name,city,country,start_date,finish_date,work_about,school_name,school_location,degree,work_area,school_start,school_finish,language,lang_degree,skill,skill_degree,username) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(query, (about,work_title,company_name,city,country,start_date,finish_date,work_about,school_name,school_location,degree,work_area,school_start,school_finish,language,lang_degree,skill,skill_degree,session["username"]))

        mysql.connection.commit()
        cursor.close()

        return redirect(url_for("cvdashboard"))
    
    return render_template("cvprofile.html", form = form)

@app.route("/cv-<string:id>")
@cvlogin_required
def cv(id):
    cursor = mysql.connection.cursor()
    cursor1 = mysql.connection.cursor()
    query = "Select * from personal_infos where id = %s"
    query1 = "Select * from profile_infos where id = %s"
    result = cursor.execute(query, (id,))
    result1 = cursor1.execute(query1, (id,))

    if result > 0 and result1 > 0:
        personal = cursor.fetchone()
        profile = cursor1.fetchone()
        return render_template("cv.html", personal = personal, profile = profile)
    else:
        return render_template("cv.html")

@app.route("/download-<string:id>")
@cvlogin_required
def download(id):
    cursor = mysql.connection.cursor()
    cursor1 = mysql.connection.cursor()
    query = "Select * from personal_infos where id = %s"
    query1 = "Select * from profile_infos where id = %s"
    result = cursor.execute(query, (id,))
    result1 = cursor1.execute(query1, (id,))

    if result > 0 and result1 > 0:
        personal = cursor.fetchone()
        profile = cursor1.fetchone()
        path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
        html = render_template("download.html",personal=personal, profile = profile)
        html.encode('utf-8')
        pdf = pdfkit.from_string(html, False, configuration=config)
        response = make_response(pdf)
        response.headers["Content-Type"] = "application/pdf"
        response.headers["Content-Disposition"] = "inline; filename=output.pdf"
        return response
    else:
        return render_template("cv.html")

@app.route("/cvdashboard")
@cvlogin_required
def cvdashboard():
    cursor = mysql.connection.cursor()
    query = "Select * from personal_infos where username = %s"
    result = cursor.execute(query, (session["username"],))

    if result > 0:
        CVs = cursor.fetchall()
        return render_template("cvdashboard.html", CVs = CVs)
    else:
        return render_template("cvdashboard.html")

@app.route("/cvdelete-<string:id>")
@cvlogin_required
def cvdelete(id):
    cursor = mysql.connection.cursor()
    cursor1 = mysql.connection.cursor()
    query = "Select * from personal_infos where username = %s and id = %s"
    query1 = "Select * from profile_infos where username = %s and id = %s"
    result = cursor.execute(query, (session["username"], id))
    result1 = cursor1.execute(query1, (session["username"], id))

    if result > 0 and result1 > 0:
        query = "Delete from personal_infos where id = %s"
        query1 = "Delete from profile_infos where id = %s"
        cursor.execute(query, (id,))
        cursor1.execute(query1, (id,))
        mysql.connection.commit()

        return redirect(url_for("cvdashboard"))
    else:
        flash("Bu işleme yetkiniz yok!","danger")
        return redirect(url_for("cvbuilder"))

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/blogabout")
def blogabout():
    return render_template("blogabout.html")

@app.route("/articles")
def articles():
    cursor = mysql.connection.cursor()
    query = "Select * from articles"
    result = cursor.execute(query)

    if result > 0:
        articles = cursor.fetchall()
        return render_template("articles.html", articles = articles)
    else:
        return render_template("articles.html")

@app.route("/blogdashboard")
@bloglogin_required
def blogdashboard():
    cursor = mysql.connection.cursor()
    query = "Select * from articles where author = %s"
    result = cursor.execute(query, (session["username"],))

    if result > 0:
        articles = cursor.fetchall()
        return render_template("blogdashboard.html", articles = articles)
    else:
        return render_template("blogdashboard.html")

@app.route("/blogregister", methods = ["GET","POST"])
def blogregister():
    form = RegisterForm(request.form)
    
    if request.method == "POST" and form.validate():
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(form.password.data)

        cursor = mysql.connection.cursor()

        query = "Insert into blog_users(name, surname, email, username, password) VALUES(%s,%s,%s,%s,%s)"

        cursor.execute(query, (name, surname, email, username, password))

        mysql.connection.commit()

        cursor.close()
        
        flash("Kayıt Başarılı!", "success")

        return redirect(url_for("bloglogin"))
    else:
        return render_template("blogregister.html", form = form)

@app.route("/bloglogin", methods = ["GET","POST"])
def bloglogin():
    form = LoginForm(request.form)

    if request.method == "POST":
        username_entered = form.username.data
        password_entered = form.password.data

        cursor = mysql.connection.cursor()

        query = "Select * from blog_users where username = %s"

        result = cursor.execute(query, (username_entered,))

        if result > 0:
            data = cursor.fetchone()
            password = data["password"]
            if sha256_crypt.verify(password_entered, password):
                flash("Giriş Başarılı!", "success")

                session["logged_out"] = True
                session["username"] = username_entered

                return redirect(url_for("blog"))
            else:
                flash("Kullanıcı Adı veya Parola Hatalı!", "danger")
                return redirect(url_for("bloglogin"))
        else:
            flash("Böyle bir kullanıcı bulunmuyor...", "danger")
            return redirect(url_for("bloglogin"))

    return render_template("bloglogin.html", form = form)

@app.route("/article-<string:id>")
def article(id):
    cursor = mysql.connection.cursor()
    query = "Select * from articles where id = %s"

    result = cursor.execute(query, (id,))

    if result > 0:
        article = cursor.fetchone()
        return render_template("article.html", article = article)
    else:
        return render_template("article.html")

@app.route("/bloglogout")
@bloglogin_required
def bloglogout():
    session.clear()
    return redirect(url_for("blog"))

@app.route("/addarticle", methods = ["GET", "POST"])
@bloglogin_required
def addarticle():
    form = ArticleForm(request.form)

    if request.method == "POST" and form.validate():
        title = form.title.data
        content = form.content.data

        cursor = mysql.connection.cursor()
        query = "Insert into articles(title,author,content) VALUES (%s,%s,%s)"

        cursor.execute(query, (title, session["username"], content))

        mysql.connection.commit()
        cursor.close()

        flash("Makale Başarıyla Eklendi...", "success")

        return redirect(url_for("blogdashboard"))

    return render_template("addarticle.html", form = form)

@app.route("/blogdelete-<string:id>")
@bloglogin_required
def blogdelete(id):
    cursor = mysql.connection.cursor()
    query = "Select * from articles where author = %s and id = %s"
    result = cursor.execute(query, (session["username"], id))

    if result > 0:
        query1 = "Delete from articles where id = %s"
        cursor.execute(query1, (id,))
        mysql.connection.commit()

        return redirect(url_for("blogdashboard"))
    else:
        flash("Bu işleme yetkiniz yok!","danger")
        return redirect(url_for("blog"))

@app.route("/update-<string:id>", methods = ["GET","POST"])
@bloglogin_required
def update(id):
    if request.method == "GET":
        cursor = mysql.connection.cursor()
        query = "Select * from articles where author = %s and id = %s"
        result = cursor.execute(query, (session["username"], id))

        if result == 0:
            flash("Bu işleme yetkiniz yok!", "danger")
            return redirect(url_for("blog"))
        else:
            article = cursor.fetchone()
            form = ArticleForm()

            form.title.data = article["title"]
            form.content.data = article["content"]

            return render_template("update.html", form = form)

    else:
        # POST Request
        form = ArticleForm(request.form)

        newTitle = form.title.data
        newContent = form.content.data

        cursor = mysql.connection.cursor()
        query1 = "Update articles Set title = %s, content = %s where id = %s"
        cursor.execute(query1, (newTitle, newContent, id))
        mysql.connection.commit()

        flash("Makale Başarıyla Güncellendi!","success")

        return redirect(url_for("blogdashboard"))

@app.route("/search", methods = ["GET","POST"])
def search():
    if request.method == "GET":
        return redirect(url_for("blog"))
    else:
        keyword = request.form.get("keyword")

        cursor = mysql.connection.cursor()
        query = "Select * from articles where title like '%" + keyword + "%'"
        result = cursor.execute(query)

        if result > 0:
            articles = cursor.fetchall()

            return render_template("articles.html", articles = articles)
        else:
            flash("Sonuç Bulunamadı...","warning")
            return redirect(url_for("articles"))

@app.route("/todoapp")
def todoapp():
    todos = Todo.query.all()
    return render_template("todoapp.html", todos = todos)

@app.route("/add", methods = ["POST"])
def add():
    title = request.form.get("title")
    newTodo = Todo(title = title, complete = False)
    db.session.add(newTodo)
    db.session.commit()

    return redirect(url_for("todoapp"))

@app.route("/complete-<string:id>")
def complete(id):
    todo = Todo.query.filter_by(id = id).first()
    todo.complete = not todo.complete

    db.session.commit()
    return redirect(url_for("todoapp"))

@app.route("/delete-<string:id>")
def delete(id):
    todo = Todo.query.filter_by(id = id).first()
    
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todoapp"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)