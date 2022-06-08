from db.DB import DB
from flask import (Blueprint, redirect, render_template, request, session,
                   url_for)

from models.user import User

user_services = Blueprint("user_services", __name__)
mydb = DB.connect()


@user_services.route('/login', methods=['GET'])
def login_page():
    if 'username' in session:
        return redirect(url_for('employee_services.index'))
    msg = ''
    return render_template('login.html', msg=msg)


@user_services.route('/login', methods=['POST'])
def login():
    msg = ''
    if 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        is_username = DB.select_query(
            'SELECT COUNT(username) FROM user WHERE username = %s', (username,))
        is_username = is_username[0]['COUNT(username)']

        if is_username == 1:
            stored_password = DB.select_query(
                'SELECT password FROM user WHERE username = %s', (username,))
            stored_password = stored_password[0]['password']

            if User.verify_password(stored_password, password):
                session['loggedin'] = True
                session['username'] = username
                return redirect(url_for('employee_services.index'))
            else:
                msg = 'Username and/or password is not correct!'
                return render_template('login.html', msg=msg)
        else:
            msg = 'Username and/or password is not correct!'
            return render_template('login.html', msg=msg)
    else:
        msg = 'Check your details, and try to login again!'
        return render_template('login.html', msg=msg)
