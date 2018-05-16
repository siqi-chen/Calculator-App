#!/var/www/html/Web-App-Calculator/venv/bin/python2.7
# app.wsgi
import sys

activate_this = '/var/www/html/Web-App-Calculator/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))


# expand python classes path with your app's path
# sys.path.append('/var/www/html/Web-App-Calculator')
sys.path.insert(0, '/var/www/html/Web-App-Calculator/')

from app import app as application
