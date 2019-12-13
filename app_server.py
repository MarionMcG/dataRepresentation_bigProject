from flask import Flask, jsonify, abort, request

app = Flask(__name__, static_url_path='', static_folder='.')

from userdao import UserDAO

#@app.route('/')
#def index():
#    return "Hello, World. Why aren't you working?"

#Code to return all users
@app.route('/users')
def getAll():
    result = UserDAO.getAll()
    return jsonify(result)
#CHECK IT WORKS--> curl "http://127.0.0.1:5000/users"

#Code to find users by id
@app.route('/users/<int:id>')
def findById(id):
    foundUser = UserDAO.findByID(id)
    if foundUser == None:
        abort(404)
    else:
        return jsonify(foundUser)

##curl "http://127.0.0.1:5000/users/2"

#Code to add a new user - must include user name and email
# Use dict object would be better - possible extension of project
@app.route('/users', methods = ['POST'])
def create():
    #global newID
    if not request.json:
        abort(400)
    try:
        new_user = request.get_json(force=True)
    except:
        abort(400)
    #if not 'user' in new_user:
        #abort(400)
    #if not 'email' in new_user:
        #abort(400)
    user = {
        "user": new_user['user'],
        "email": new_user['email']
        
        # going to add new users to user_info and user_login at same time
        #"password": new_user['password']
    }
    new_user = (user['user'], user['email'],)
    newId = UserDAO.create(new_user)
    user['id'] = newId
    return jsonify(user)
#curl -i -H "Content-Type:application.json" -X POST -d "{\"email\":\"skippy@hotmail.com\",\"permission\":\"Advanced Editor\",\"user\":\"skippy\"}" http://127.0.0.1:5000/users
#OR 
#curl -i -H "Content-Type:application.json" -X POST -d "{\"email\":\"skippy@hotmail.com\",\"user\":\"skippy\"}" http://127.0.0.1:5000/users

@app.route('/users/<int:id>', methods = ['PUT'])
def update(id):
    foundUser = UserDAO.findByID(id)
    if foundUser==None:
        abort(404)
    if not request.json:
        abort(400)
    #Add code to check that email is in correct format (maybe)
    update_user = request.json

    perms = ['Editor', 'Advanced Editor', 'Gardener']
    if 'edits' in update_user and type(update_user['edits']) is not int:
        abort(400)
    if 'user'in update_user:
        foundUser['user']= update_user['user']
    if 'edits' in update_user:
        foundUser['edits']= update_user['edits']
    if 'email' in update_user:
        foundUser['email']= update_user['email']
    if 'permission' in update_user:
        foundUser['permission']= update_user['permission']
    foundUser['id'] =id
    values = (foundUser['user'], foundUser['email'], foundUser['edits'], foundUser['permission'], foundUser['id'] )
    UserDAO.update(values)
    return jsonify(foundUser)
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"edits\":10,\"email\":\"skippy@hotmail.com\",\"permission\":\"Editor\",\"user\":\"skippy\"}" http://127.0.0.1:5000/users/5
# OR
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"edits\":78}" http://127.0.0.1:5000/users/4

@app.route('/users/<int:id>', methods = ['DELETE'])
def delete(id):
    #OLD CODE -- ignore
    #foundUsers = list(filter(lambda x : x['id'] == id, users))
    #users.remove(foundUsers[0])

    foundUser = UserDAO.findByID(id)
    if foundUser == None:
        abort(404)
    else:
        UserDAO.delete(id)
        return jsonify({"done":True})
#curl -X DELETE "http://127.0.0.1:5000/users/1"

if __name__ == '__main__' :
    app.run(debug= True)
