# Shopesite  

Shopesite is a dynamic, user-friendly e-commerce platform designed for modern businesses. It enables seamless online shopping experiences, robust product management.  

## Features  
- **User-Friendly Interface**:  
  - Intuitive navigation for customers.  
  - Responsive design optimized for all devices.  
- **Product Management**:  
  - Add, edit, and categorize products with ease.  
  - Very simple user-friendly Environment 
- **Admin Dashboard**:  
  - Comprehensive sales analytics.  
  - Order management and fulfillment tools.  
- **Customer Accounts**:  
  - Secure user registration and login.  
  - Order history and wishlist features.    
- **Bandwidth**
  - Very less Bandwidth and latency
  - Rich experience

## Specification   
- Python 3.12.8
- Database: MySQL
- Frontend: HTML, CSS, JavaScript
- Backend: Python Flask

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/thirumurug0xan/shopesite.git  
   cd shopesite
   python3 -m venv .venv
   source .venv/bin/activate
   pip install flask,flask_mysqldb,MySQLdb
   ```
2. Database connection:
   ```python
   #File : app.py
   app.config['MYSQL_HOST'] = 'YOUR_HOST_ADDRESS' #Example:'127.0.0.1'
   app.config['MYSQL_USER'] = 'DBUSER' #Example:'kali'
   app.config['MYSQL_PASSWORD'] = 'DBUSER_PASSWORD'#Example:'kali'
   app.config['MYSQL_DB'] = 'YOUR_DB_NAME' #Example:'shopesite'(recommended)
   ```
3. Make you sure mysql server is up in running
   ```bash
   service mysql status
   ```
4. It is important to mention change the following in app.py for more security
   ```python
   app.secret_key = 'YOUR_SUPER_SECRET_KEY' #Default : 'super_secret'
   ```
5. Finally
   ```bash
   flask run
   ```
6. Thats all.

## Credentials 
1. Default admin Credentials are
   ```
      admin_id = admin
      admin_password = admin
   ```
2. You can also able to change password once you get into the application

## Error Handling
You most probably encounter the following error while executing pip
That is because you either forget to create a venv or activating venv
   ```bash
   ┌──(kali㉿localhost)-[~/Projects/shopesite]
   └─$ pip install flask,flask_mysqldb,MySQLdb
   error: externally-managed-environment

   × This environment is externally managed
   ╰─> To install Python packages system-wide, try apt install
        python3-xyz, where xyz is the package you are trying to
        install.

        If you wish to install a non-Debian-packaged Python package,
        create a virtual environment using python3 -m venv path/to/venv.
        Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
        sure you have python3-full installed.

        If you wish to install a non-Debian packaged Python application,
        it may be easiest to use pipx install xyz, which will manage a
        virtual environment for you. Make sure you have pipx installed.

        See /usr/share/doc/python3.12/README.venv for more information.

    note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
    hint: See PEP 668 for the detailed specification.
```
## Contact
[Linkedin](https://linkedin.com/in/thirumurug0xan)\
[Instagram](https://Instagram.com/thirumurug0xan)
