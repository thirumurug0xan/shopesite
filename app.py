from flask import (Flask, 
                   render_template, 
                   request, 
                   jsonify, 
                   url_for, 
                   redirect, 
                   make_response,
                   session)
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os 

# admin_name = input('Enter name for admin:')
# admin_password = input('Enter password for admin:')
# if not (admin_name and admin_password):
#     admin_name = admin_password = 'admin'

app = Flask(__name__, template_folder='./templates')

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'kali'
app.config['MYSQL_PASSWORD'] = 'kali'
app.config['MYSQL_DB'] = 'shopesite'
app.secret_key = 'super_secret'
mysql = MySQL(app)

#Function declaration start from here

@app.route("/")
def home():
    return render_template("home.html")


# def view_orders():
#   pass

# def view_status():
#   pass

# def add_products():
#   pass

# Route for the login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        sql_select = 'select email,password from users where email=\'{ps}\';'.format(ps=username) \
        if '@' in username \
        else 'select user_name,password from users where user_name=\'{ps}\';'.format(ps=username)
        print(sql_select)
        cursor.execute(sql_select)
        print('{p}'.format(p='hu'))
        print(username)
        account = cursor.fetchone()
        if not account:
          account = dict()
        print(account)
        # Check if the entered credentials match the hardcoded ones
        print(account.get('email','not_found'),account.get('password','not_found'))
        if (username == account.get('email','not_found') or username == account.get('user_name','not_found'))\
        and \
        password == account.get('password','not_found'):
            return jsonify({'status': 'success', 'redirect_url': '/home2.html'})#use cookies for best prctices #url_for('welcome', username=username)
        else:
            return jsonify({'status': 'fail', 'message': 'Invalid credentials, please try again.'})
    else:
        return render_template('login.html')

# @app.route("/welcome/<username>")
# def welcome(username):
#     return f"Welcome, {username}!"

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")

@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")

@app.route("/home2")
def home2():
    return render_template("home2.html")
    
@app.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'POST':
      cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
      first_name = request.form.get('first_name')
      last_name = request.form.get('last_name')
      user_name = request.form.get('username')
      phone_no = request.form.get('phone_number')
      email = request.form.get('email')
      password = request.form.get('password')
      #ensure the user_name and email are unique
      sql_insert = 'insert into users value(\'{first_name}\',\'{last_name}\',\'{user_name}\',\'{phone_no}\',\'{email}\',\'{password}\');'.format(first_name=first_name,
         last_name=last_name,
         user_name=user_name,
         phone_no=phone_no,
         email=email,
         password=password)
      print(sql_insert)
      cursor.execute(sql_insert)
      mysql.connection.commit()
      cursor.close()
      #print(cursor.fetchone())
      #cursor.execute('select * from users;')
      #print(cursor.fetchone())
      return redirect(url_for('login'))
    return render_template("register.html")

@app.route("/view_product")
def view_product():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('select * from products;')
    products_tuble = cursor.fetchall()
    print(products_tuble)
    return render_template("view_product.html",product_list=products_tuble)

@app.route("/admin/login",methods=['GET','POST'])
def admin_login():
  if 'POST' == request.method:
    if request.form.get('admin_id') == 'admin' or 'admin'== request.form.get('password'):
      return 'success'
    else:
      return 'failed'
  return render_template('/admin_login.html')

@app.route('/admin/portal/update')
def admin_portal_update():
   pass

@app.route('/admin/portal/orders')
def admin_portal_orders():
   pass

@app.route("/admin/portal/add")
def admin_portal_add():
  return render_template('/admin_add.html')

@app.route("/admin/portal/users")
def admin_portal_add():
  return render_template('/admin_users.html')

@app.route("/admin/portal")
def admin_portal_add():
  return render_template('/admin_portal.html')

@app.route("/logout")
def logout():
    return redirect('/home')

@app.route('/profile')
def profile():
   return render_template('/profile.html',user_name='sample',user_email='sample@email.com')


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')


# \hwloc/linux: failed to find sysfs cpu topology directory, aborting linux discovery.
# 1500.858 k/s 
