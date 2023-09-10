from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.user import User

@app.route('/')
def all_users():
    all_users = User.get_all()
    print(all_users)
    return render_template("read_all.html",users=all_users)

@app.route('/create_user')
def new_user():
    return render_template("create.html")


@app.route('/create', methods=["POST"])
def create_user():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.create_user(data)
    return redirect('/')

@app.route('/one_user/<int:id>')
def show_one_user(id):
    user = User.get_one(id)
    return render_template("one_user.html", user=user)

@app.route('/update_user/<int:id>')
def change_info(id):
    user = User.get_one(id)
    return render_template("update.html", user=user)

@app.route('/update_user/<int:id>', methods=['POST'])
def update(id):
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'id' : id
    }
    User.update(data)
    return redirect('/')

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    User.delete_user(user_id)
    return redirect('/')

@app.route('/end')
def end():
    return redirect('/')
