from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__,template_folder='./')

# Route for the homepage
@app.route("/")
@app.route("/login.html",methods=['GET','POST'])
def login():
  if request.method == 'POST':
    print(request.form['username'])
    username = request.form['username']
    password = request.form['password']

    # Check if the entered credentials match the hardcoded ones
    if username == 'admin' and password == 'admin':
        return redirect(url_for('welcome', username=username))
    else:
        print(username)
        return {"error":"Invalid credentials, please try again."}
  else:
    return render_template('login.html')

@app.route("/about_us.html")
def about_us():
    return render_template("about_us.html")
    
@app.route("/contact_us.html")
def contact_us():
    return render_template("contact_us.html")
    
@app.route("/home.html")
def home_():
    return render_template("home.html")
    
@app.route("/home2.html")
def home2():
    return render_template("home2.html")
    
@app.route("/register.html")
def register():
    return render_template("register.html")

@app.route("/view_product.html")
def view_product():
    return render_template("view_product.html")
@app.route("/admin/<filename>")
def admin(filename):
    print(filename)
    return render_template("view_product.html")
if __name__ == "__main__":
    app.run(debug=True)
