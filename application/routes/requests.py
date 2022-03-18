from application import app
from application.database import database
from flask import request, jsonify
from functools import wraps

user_name = 'admin'
pass_word = 'password'
def protected(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == user_name and auth.password == pass_word:
            return f(*args, **kwargs)
        return jsonify({'Error': 'The username or password is incorrect'}), 401
    return decorated

@app.route('/member', methods=['GET'])
@protected
def get_members():
    db = database.get_db()
    return_values = []
    members_curr = db.execute('select id, name, email, level from members')
    members = members_curr.fetchall()
    for foo in members:
        member_dict = {'id': foo['id'], 'name': foo['name'], 'email': foo['email'], 'level': foo['level']}
        return_values.append(member_dict)
    return jsonify({'members: ': return_values})

@app.route('/member/<member_id>', methods=['GET'])
def get_member(member_id):
    db = database.get_db()
    member_curr = db.execute('select id, name, email, level from members where id = ?', [member_id])
    member_result = member_curr.fetchone()
    return jsonify({'members': {'id': member_result['id'], 'name': member_result['name'],
                                'email': member_result['email'], 'level': member_result['level']}})


@app.route('/member', methods=['POST'])
def add_member():
    db = database.get_db()
    new_member_data = request.get_json()
    name = new_member_data['name']
    email = new_member_data['email']
    level = new_member_data['level']
    db.execute('insert into members (name, email, level) values (?, ?, ?)', [name, email, level])
    db.commit()
    user_curr = db.execute('select id, name, email, level from members where name = ?', [name])
    user_result = user_curr.fetchone()
    return jsonify({'members: ', {'id': user_result['id'], 'name': user_result['name'], 'email': user_result['email'],
                                  'level': user_result['level']}})


@app.route('/member/<member_id>', methods=['PUT', 'PATCH'])
def edit_member(member_id):
    db = database.get_db()
    user_update = request.get_json()
    name = user_update['name']
    email = user_update['email']
    level = user_update['level']
    db.execute('update members set name = ?, email = ?, level = ? where id = ?', [name, email, level, member_id])
    db.commit()


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    db = database.get_db()
    db.execute('delete from members where id = ?', [member_id])
    db.commit()
