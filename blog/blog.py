from flask import render_template, url_for, flash, session, redirect, request, Blueprint
from flask_wtf import FlaskForm
from wtforms import  StringField, PasswordField, TextAreaField, validators
from flask_wtf.file import FileField, FileAllowed, FileRequired
from passlib.hash import sha256_crypt
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
from functools import wraps
from werkzeug.utils import secure_filename
import os

upload_folder='/Users/samrajyathapa/Environments/blogApp/blog/static/'
bp = Blueprint('blog', __name__)

mysql=MySQL(cursorclass=DictCursor)


####wtforms for the app#####

#register form
class RegisterForm(FlaskForm):
    name= StringField('Name', [validators.Length(min=1, max=50)])
    username= StringField('Username', [validators.Length(min=4, max=25)])
    email= StringField('Email', [validators.Length(min=6, max=50), validators.Regexp('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$', message='Enter valid email')])
    password= PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match'
    )])
    confirm= PasswordField('Confirm Password')

#add blog post Form
class addPostForm(FlaskForm):
    title = StringField('Title', [validators.Length(min=1, max=50)])
    body = TextAreaField('Body', [validators.Length(min=15)])
    blog_img = FileField('Image', [FileRequired(), FileAllowed(['jpg', 'png'])])


###forms end here

####routes start here#######

#home
@bp.route('/')
def home():
    return render_template('home.html')

#about
@bp.route('/about')
def about():
    return render_template('about.html')

#register route
@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)

        #create cursor
        cur = mysql.get_db().cursor()

        #check if username Exists
        count = cur.execute("SELECT * FROM users WHERE username = %s", [username])
        if count !=0:
            flash('Username Already Exists', 'danger')
            return redirect(url_for('blog.register'))

        #check if email exists
        count1 = cur.execute("SELECT * FROM users WHERE email = %s", [email])
        if count1 !=0:
            flash('Email Already Exists', 'danger')
            return redirect(url_for('blog.register'))


        cur.execute("INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)", (name, email, username, password))

        mysql.get_db().commit()
        cur.close()
        flash('You are registered. You can now Log In.', 'success')

        return redirect(url_for('blog.register'))

    return render_template('register.html', form=form)


#check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized. Please Log In', 'danger')
            return redirect(url_for('blog.login'))
    return wrap

#login route
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password_candidate = request.form['password']

        cur = mysql.get_db().cursor()

        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:

            data = cur.fetchone()

            password = data['password']


            if sha256_crypt.verify(password_candidate, password):

                session['logged_in'] = True
                session['username'] = username

                flash('Success! you are logged in.', 'success')
                return redirect(url_for('blog.dashboard'))

            else:
                flash('Login Failed!', 'danger')
                return redirect(url_for('blog.login'))
        else:
            flash('User Does Not Exist', 'danger')
            return redirect(url_for('blog.login'))

    return render_template('login.html')


#logout
@bp.route('/logout')
def logout():
    session.clear()
    flash('You are Logged Out.', 'success')
    return redirect(url_for('blog.login'))


#dashboard route
@bp.route('/dashboard')
@is_logged_in
def dashboard():
    cur = mysql.get_db().cursor()
    result= cur.execute("SELECT * FROM blogpost WHERE author=%s",(session['username']))
    data = cur.fetchall()
    if result > 0:
        return render_template('dashboard.html', data=data)
    else:
        msg = 'no blog posts'
        return render_template('dashboard.html', msg=msg)
    cur.close()

#add post route
@bp.route('/addPost', methods=['GET', 'POST'])
@is_logged_in
def addPost():
    form = addPostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        file = form.blog_img.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(upload_folder, filename))
        cur = mysql.get_db().cursor()

        cur.execute("INSERT INTO blogpost(title, author, body, blog_img) VALUES(%s, %s, %s, %s)", (title, session['username'], body, filename))
        mysql.get_db().commit()
        cur.close()
        flash('Post Created!', 'success')
        return redirect(url_for('blog.dashboard'))

    return render_template('addPostForm.html', form=form)

#view all blog posts
@bp.route('/posts')
@is_logged_in
def posts():
    cur = mysql.get_db().cursor()
    result1= cur.execute("SELECT * FROM blogpost WHERE author=%s",(session['username']))
    data1 = cur.fetchall()
    if result1 > 0:
        return render_template('posts.html', data1=data1)
    else:
        msg = 'no posts'
        return render_template('posts.html', msg=msg)


    cur.close()

#go to a specific blog post
@bp.route('/posts/<string:id>')
@is_logged_in
def view_post(id):
    cur = mysql.get_db().cursor()
    result = cur.execute("SELECT * FROM blogpost WHERE id=%s", [id])
    data = cur.fetchone()
    if result > 0:
        return render_template('viewPost.html', data=data)
    else:
        msg = "error"
        return redirect(url_for('blog.posts'))

    cur.close()

@bp.route('/del_post/<string:id>')
@is_logged_in
def del_post(id):
    cur = mysql.get_db().cursor()
    cur.execute("DELETE FROM blogpost WHERE id=%s", [id])
    mysql.get_db().commit()

    flash('Successfully Deleted Post', 'success')

    cur.execute("ALTER TABLE blogpost DROP id")
    cur.execute("ALTER TABLE blogpost ADD id INT AUTO_INCREMENT PRIMARY KEY FIRST")
    mysql.get_db().commit()
    return redirect(url_for('blog.dashboard'))

    cur.close()

@bp.route('/edit_post/<string:id>', methods=['GET', 'POST'])
@is_logged_in
def edit_post(id):
    cur = mysql.get_db().cursor()
    cur.execute("SELECT * FROM blogpost WHERE id=%s", [id])
    data = cur.fetchone()
    cur.close()

    form = addPostForm()
    form.title.data = data['title']
    form.body.data = data['body']

    if form.validate_on_submit():
        title = request.form['title']
        body = request.form['body']
        file = form.blog_img.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(upload_folder, filename))

        cur = mysql.get_db().cursor()
        cur.execute("UPDATE blogpost SET title=%s, body=%s WHERE id=%s", (title, body, id))
        mysql.get_db().commit()
        cur.close()

        flash('Post Updated', 'success')
        return redirect(url_for('blog.dashboard'))

    return render_template('edit_post.html', form=form)

@bp.route('/find')
def find():
    username_candidate = request.args.get('search')
    if username_candidate is not None:
        cur = mysql.get_db().cursor()
        result = cur.execute("SELECT * FROM blogpost WHERE author = %s", [username_candidate])
        if result > 0 :
            data = cur.fetchall()
            return render_template('find.html', data=data)
        else:
            flash('No Match Found', 'danger')
        return redirect(url_for('blog.find'))

    return render_template('find.html')
