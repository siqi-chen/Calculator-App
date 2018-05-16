# Web-App-Calculator


## What is this?

This is a simple calculator. You can perform basic calculations, such as adding, subtracting, multiplying, dividing and modulo operations, between any two numbers x and y.



## How to use it?

Enter two numbers x and y, which can be integers or decimals, and a valid operator such as +, -, *, / and %.
The output will be shown after you hit the "Compute" botton.

##
## Setting up a wsgi server by using Apache

### 1. Install prerequisite packages.
Flask: a web microframework for Python.
virtualenv: a tool to create isolated Python environments.
mod_wsgi: an Apache module implementing the WSGI specification.

### 2. Put the web application file under the path /var/www/html.

### 3. Creat a virtual environment using virtualenv.
Virtual environments have the advantage that they never install the required dependencies system wide so you have a better control over what is used where. 

### 4. Create a .wsgi file
The .wsgi file contains the code mod_wsgi is executing on startup to get the application object. 


### 5. Create an Apache configuration file.

```
The configuration file should be located at /etc/httpd/conf.d/.
LoadModule wsgi_module modules/mod_wsgi.so
WSGISocketPrefix run/wsgis

<virtualhost *:80>
    ServerName ec2-18-218-153-199.us-east-2.compute.amazonaws.com
    WSGIDaemonProcess app threads=5 python-path=/var/www/html/Web-App-Calculator:/var/www/html/Web-App-Calculator/venv/lib/python2.7/site-packages
    WSGIScriptAlias / /var/www/html/Web-App-Calculator/app.wsgi

    <directory /var/www/html/Web-App-Calculator>
        WSGIProcessGroup app
        WSGIApplicationGroup %{GLOBAL}
        WSGIScriptReloading On
        Order deny,allow
        Allow from all
    </directory>
</virtualhost>／
 ```
 
### 6. Restart the Apache.

```
sudo service httpd restart
```
Now you can access the web application in the browser by accessing the domain without additional ports. Check the error_log for diagnosing issues.


###
### References:
Running a Flask application under the Apache WSGI module
https://www.jakowicz.com/flask-apache-wsgi/

SETTING UP A WEB-SERVER FOR FLASK-APP DEPLOYMENT IN MOD_WSGI
https://codeflu.blog/2014/10/11/setting-up-a-web-server-for-flask-app-deployment-in-mod_wsgi-part-2/

Serving a Python Flask Web Application via Apache Webserver in Raspberry Pi
http://www.ashokraja.me/post/Serving-a-Python-Flask-Web-Application-via-Apache-Webserver-in-Raspberry-Pi.aspx

Running a Flask app on AWS EC2
https://www.datasciencebytes.com/bytes/2015/02/24/running-a-flask-app-on-aws-ec2/

##
## Running the web application on HTTPS

### 1. Install OpenSSL package in the virtual environment.

### 2. Generate self-signed certificates.
Generate a certificate with its corresponding private key from the command line.
```
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout key.key -out cert.crt

```

### 3. Adding the ssl_context argument in the application.
Use the new self-signed certificate in the Flask application by setting the ssl_context argument to the filenames of the certificate and private key files.

```
ssl_context=('cert.pem', 'key.pem')
```
###
### References:
Running Your Flask Application Over HTTPS
https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

Python Flask API in HTTPS
https://udaraliyanage.wordpress.com/2015/10/21/python-flask-api-in-https/
