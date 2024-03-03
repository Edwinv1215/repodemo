from . import auth
from . forms import LoginForm, SignupForm
from flask import request, render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from app.models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        queried_user = User.query.filter(User.email == email).first()
        if queried_user and check_password_hash(queried_user.password, password):
            flash(f'wellcome {queried_user.username}!', 'info')
            login_user(queried_user)
            return redirect(url_for('main.home'))
        else: 
            flash('incorrect username, email or password....please try again', 'warning')
            return render_template('login.html', form=form)
    else:
        return render_template('login.html', form=form)
    
  

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        new_user =User(username, email, password)
        new_user.save()
        flash('success thank you for signing up', 'success')
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html', form=form)
    
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))   


        
 
