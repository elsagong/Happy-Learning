# app/home/views.py
# coding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import abort, render_template
from flask_login import current_user, login_required

from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Welcome")

@home.route('/dashboard')#登录需求加或者不加，均显示"login_manager.login_message”信息,bug??
@login_required#It's must...the reason is server delay or partial page caching???
def dashboard():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/dashboard.html', title="Dashboard")


#add admin dashboard view
@home.route('/admin/dashboard')#登录需求加或者不加，均显示"login_manager.login_message”信息,bug??
@login_required#It's must...the reason is server delay or partial page caching???
def admin_dashboard():
    """
     prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")
