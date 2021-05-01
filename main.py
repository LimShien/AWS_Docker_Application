from flask import *
from flask_fontawesome import FontAwesome
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user,login_required,logout_user
import random
import time
import cus_func
app = Flask(__name__)
app.secret_key = 's3cr3tK3y'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db'
db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager= LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class users(UserMixin,db.Model):
    id = db.Column("id", db.Integer, primary_key=True) 
    userid = db.Column("userid", db.String(64), unique=True, nullable=False ) 
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    email=db.Column(db.String(300), nullable=True)
    score=db.Column(db.Integer,  nullable=True)
    completedlab=db.Column(db.String(),  nullable=True, default=0)

    def __init__(self, username, password):
        self.userid = random.getrandbits(32)
        self.username=username
        self.password=password
        

class labs(db.Model):
    id = db.Column("id", db.Integer, primary_key=True) 
    title = db.Column(db.String(5000))
    content = db.Column(db.String(5000)) 
    answer = db.Column(db.String(5000))
    completedby = db.Column(db.String(5000)) 

class openvpn_config(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    path = db.Column(db.String(5000))



@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        if 'userid' in session:  
            cus_func.create_user(session['userid'])

    return render_template("index.html")

@app.route('/index')
def rhome():
    return redirect(url_for("home"))

@app.route('/index/download')
def download_file():
	path = "/home/kali/College/AWS_Docker/web/static/openvpn/client.ovpn" ##absolute path for the file
	return send_file(path, as_attachment=True)

@login_manager.user_loader
def load_user(id):
    return users.query.get(int(id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        #retrieve credentials from the login form
        username = request.form['login']
        password = request.form['password']

        user =  users.query.filter_by(username=username).first() #query database

        if not user or not bcrypt.check_password_hash(user.password, password): #no user found or invalid pasword
            flash("Invalid login, please try again!")
            return redirect(url_for('login'))

        session['userid']= user.userid
        session['username']=user.username
        login_user(user)
        flash("Login Successfully!")
        return redirect(url_for('home'))

    if 'user' in session:
        return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == 'POST':
        #retrieve value from form 
        username = request.form['login']
        password = request.form['password']
        password2 = request.form['comfirmpassword']

        if(users.query.filter_by(username=username).first()): #if exist in database
            flash("Username already exist!")
            return redirect(url_for('register'))
        else: # user not in database
            #if only both password are same -> simple verification
            if password == password2: 
                #create model for user
                usr = users(username, password=bcrypt.generate_password_hash(password,))
                db.session.add(usr)  # add to database
                db.session.commit()

                flash("Account created successfully")
                return redirect(url_for("login"))
            else:
                flash("Password not the same! Try Again") 
                return redirect(url_for('register'))
    else:
         return render_template('register.html')


@app.route('/pentest')
@login_required
def selectlab():
    return render_template("pentest.html") 

@app.route('/pentest/lab<int:i>', methods=['GET'])
@login_required
def lab(i):
    session['task-list']=0
    template = "lab" + str(i) + ".html"
    return render_template(template, tasklist=labs.query.all())    

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", user =users.query.filter_by(userid=session['userid']).first()) 


@app.route('/admin')
@login_required
def admin_dashboard():
    if session['username'] == 'admin':
        return render_template("admin.html", user =users.query.all(), lab=labs.query.all()) 
    else: 
        return redirect(url_for("dashboard"))



@app.route('/pentest/lab1/task-<int:tid>')
def update(tid):
    ##update the completedby user array in labs table
    userid = str(session['userid']) ##get current userid 

    user= users.query.filter_by(userid=userid).first() ##The userobject => to append the score/completed lab

    userarray =labs.query.filter_by(id=tid).first().completedby ##query lab table --> filter by lab id

    userarray += ','   ##append the user array
    userarray += userid
    labs.query.filter_by(id=tid).first().completedby = userarray  ##update the user array in lab

    print(userarray)

    ##add certain mark for completing the task/lab
    user.score += 5

    ##update the users table completed lab/task
    user.completedlab += ":"
    user.completedlab += str(tid)
    

    db.session.commit()
    return ''

@app.route('/logout')
@login_required
def logout():
    logout_user()
    for key in list(session.keys()):
        session.pop(key)
    return redirect(url_for("home"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)