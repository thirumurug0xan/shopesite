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

github_profile='thirumurug0xan'
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

admin_id = 'admin'
admin_password = 'admin'
#Non routing functions


#Function declaration start from here

@app.route("/")
def home():
    if session.get('uauth',None):
        return redirect('/home')
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
            session['uauth'] = username
            return jsonify({'status': 'success', 'redirect_url': '/home'})#use cookies for best prctices #url_for('welcome', username=username)
        else:
            return jsonify({'status': 'fail', 'message': 'Invalid credentials, please try again.'})
    else:
        if session.get('uauth',None):
           return redirect('/home')
        return render_template('login.html')

# @app.route("/welcome/<username>")
# def welcome(username):
#     return f"Welcome, {username}!"

@app.route("/about_us")
def about_us():
    if not session.get('uauth',None):
      return unauthorized()
    return render_template("about_us.html")

@app.route("/contact_us")
def contact_us():
    if not session.get('uauth',None):
      return unauthorized()
    return render_template("contact_us.html")

@app.route("/home")
def home2():
    if not session.get('uauth',None):
      return unauthorized()
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
      sql_verify = 'select user_name,email from users where user_name=\'{user_name}\' or email = \'{email}\''.format(
         user_name=user_name,
         email=email
      )
      cursor.execute(sql_verify)
      verify_user = cursor.fetchone()
      if verify_user:
         return jsonify({'status':'Failed',
                         'reason':'username or email already exist',
                         'solution':'Try different email or username'})
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

@app.route("/products")
def products():
    if not session.get('uauth',None):
      return unauthorized()
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('select * from products;')
    products_tuble = cursor.fetchall()
    print(products_tuble)
    return render_template("products.html",product_list=products_tuble)

@app.route('/products/<product_name>')
def view_product(product_name):
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('select * from products where product_name = \'{product_name}\''.format(product_name=product_name))
  product_tuple = cursor.fetchone()
  return render_template('/view_product.html',product_tuple=product_tuple)

@app.route('/product/buy/<product_name>',methods=['POST'])
def buy_product(product_name):
   print(request.json)
   return jsonify(confirmation='working')

@app.route('/admin',methods=['GET','POST'])
@app.route("/admin/login",methods=['GET','POST'])
def admin_login():
  if 'POST' == request.method:
    if request.form.get('admin_name') == admin_id and admin_password == request.form.get('password'):
      print(request.form.get('admin_name'))
      session['aauth'] = request.form.get('admin_name')
      return jsonify({'status': 'success', 'redirect_url': '/admin/portal'})
    else:
      print(request.form.get('admin_id'))
      return jsonify({'status': 'fail', 'message': 'Invalid credentials, please try again.'})
  return render_template('/admin_login.html')

@app.route('/admin/portal/update')
def admin_portal_update():
   if not session.get('aauth',None):
    return unauthorized()
   pass

@app.route('/admin/portal/orders')
def admin_portal_orders():
   if not session.get('aauth',None):
    return unauthorized()
   pass

@app.route("/admin/portal/add",methods=['GET','POST'])
def admin_portal_add():
  if not session.get('aauth',None):
     return unauthorized()
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  if request.method == 'POST':
     img = request.files['product_image']
     print(img.content_type[:5])
     if not all(char.isalpha() or char in '-_.1234567890' for char in img.filename) or 'image' != img.content_type[:5] :
        return jsonify({'status':'failled',
                        'reason':'file name should be alphaphet and numeric and following only characters are allowed(-_.)',
                        'reason2':'are you trying to upload non image files'})
     product_tuple = (
     request.form.get('product_name'),
     request.form.get('price'),
     request.form.get('quantity'),
     request.form.get('description'),
     img.filename
     )
     print(product_tuple)
     cursor.execute('select product_name, image_name from products where product_name = \'{product_name}\' or image_name = \'{image_name}\''.format(product_name = product_tuple[0], image_name = product_tuple[4]))
     verify_product = cursor.fetchone()
     if verify_product:
        return jsonify({'status':'failed','reason':'product name or image name already exist'})
     insert_product_quire = 'INSERT INTO products(product_name, price, quantity, describ, image_name) VALUES (\'{product_name}\',\'{price}\',\'{quantity}\',\'{desc}\',\'{img_name}\');'.format(
        product_name=product_tuple[0],
        price=product_tuple[1],
        quantity=product_tuple[2],
        desc = product_tuple[3],
        img_name=product_tuple[4]
        )
     cursor.execute(insert_product_quire)
     mysql.connection.commit()
     cursor.close()
     img.save('static/product_images/{file_name}'.format(file_name=img.filename))
     return 'success'


  return render_template('/admin_add.html')

@app.route("/admin/portal/users")
def admin_portal_users():
  if not session.get('aauth',None):
    return unauthorized()
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('select * from users;')
  user_tuple = cursor.fetchall()
  cursor.close()
  return render_template('/admin_users.html',users=user_tuple)

@app.route("/admin/portal")
def admin_portal():
  #print(url_for('logout',filename='hi')) #@app.route('/logout/<filename>') test purpose : if you didn't use '<filename>' it consider or make url as following /logout?filename=args it wil think of it as args 
  if not session.get('aauth',None):
    return unauthorized()
  return render_template('/admin_portal.html')
@app.route('/admin/portal/settings',methods = ['GET','POST'])
def admin_settings():
  if not session.get('aauth',None):
    return unauthorized()
  global admin_id, admin_password
  print(admin_password)
  if request.method == 'POST':
    print(request.form.get('current_password'))
    if request.form.get('current_password') == admin_password:
      admin_password = request.form.get('confirm_password')
    return redirect('/admin')
  return render_template('admin_settings.html')
  
@app.route('/admin/portal/manage')
def admin_manage():
  if not session.get('aauth',None):
    return unauthorized()
  return render_template('/admin_manage.html')
  
@app.route('/admin/portal/products')
def admin_products():
  if not session.get('aauth',None):
    return unauthorized()
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  cursor.execute('select * from products;')
  products_tuble = cursor.fetchall()
  return render_template('/admin_products.html',products=products_tuble)
  
#@app.route('/admin/portal/product/update',methods = ['GET','POST'])
@app.route('/admin/portal/product/update/<product_name>',methods=['GET','POST'])
def admin_product_update(product_name):
  #print(product_name)
  cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
  if 'POST' == request.method:
    cursor.execute('update products set price = \'{price}\', quantity = \'{quantity}\', describ = \'{describ}\' WHERE product_name = \'{product_name}\';'.format(
    price=request.form.get('price'),
    quantity=request.form.get('quantity'),
    describ=request.form.get('describ'),
    product_name=product_name)
    )
    cursor.connection.commit()
    return jsonify({'status':'success',
      'commit':'success'
    })
  cursor.execute('select * from products where product_name = \'{product_name}\''.format(product_name=product_name))
  edit_product_tuple = cursor.fetchone()
  print(edit_product_tuple)
  return render_template('/admin_update.html',product = edit_product_tuple)

@app.route("/logout/<type_of>") #@app.route('/logout/<filename>')
def logout(type_of):
    if 'admin' == type_of:
      session.pop('aauth','')
    else:
      session.pop('uauth','')
    return redirect('/')

@app.route('/profile')
def profile():
   user_name_or_email_from_session = session['uauth']
   cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   cursor.execute('select user_name,email from users where email=\'{input}\' or user_name=\'{input}\';'.format(input=user_name_or_email_from_session))
   products_tuble = cursor.fetchone()
   user= products_tuble.get('user_name')
   email=products_tuble.get('email')
   cursor.close()
   return render_template('/profile.html',user_name=user,user_email=email)

def unauthorized():
   return render_template('/unauthorized.html'),401
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')


# \hwloc/linux: failed to find sysfs cpu topology directory, aborting linux discovery.
# 1500.858 k/s 

#Development env details
# ┌──(kali㉿localhost)-[~]
# └─$ neofetch
# ..............                                     kali@localhost 
#             ..,;:ccc,.                             -------------- 
#           ......''';lxO.                           OS: Kali GNU/Linux Rolling aarch64 
# .....''''..........,:ld;                           Kernel: 4.19.152-perf-25970710-abE236BXXU4CWI1 
#            .';;;:::;,,.x,                          Uptime: 20080 days, 12 hours, 56 mins 
#       ..'''.            0Xxoc:,.  ...              Packages: 1939 (dpkg) 
#   ....                ,ONkc;,;cokOdc',.            Shell: bash 5.2.21 
#  .                   OMo           ':ddo.          Resolution: 1280x720 
#                     dMc               :OO;         DE: Xfce 4.18 
#                     0M.                 .:o.       WM: Xfwm4 
#                     ;Wd                            WM Theme: Kali-Dark 
#                      ;XO,                          Theme: Kali-Dark [GTK2], adw-gtk3-dark [GTK3] 
#                        ,d0Odlc;,..                 Icons: Flat-Remix-Blue-Dark [GTK2/3] 
#                            ..',;:cdOOd::,.         Terminal: qterminal 
#                                     .:d;.':;.      Terminal Font: FiraCode 10 
#                                        'd,  .'     CPU: Qualcomm LAGOON (8) 
#                                          ;l   ..   Memory: 3208MiB / 5427MiB 
#                                           .o
#                                             c                              
#                                             .'                             
#                                              .

