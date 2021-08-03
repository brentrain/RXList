from flask import Blueprint, render_template, request, flash

auth = Blueprint('views', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # messages won't flash - takke up here tomorrow 
        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(fname) < 2:
            flash('First name must be greater than 2 characters', category='error')
        elif len(lname) < 2:
            flash('Last name must be greater than 2 characters', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif password1 < 8:
            flash('Password is too short.  Must be greater than 8 characters', category='error')
        else:
            flash('Account created', category = 'success')
            pass
        
            
    return render_template('signup.html')