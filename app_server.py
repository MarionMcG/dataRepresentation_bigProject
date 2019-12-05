from flask import Flask, jsonify, abort, request

app = Flask(__name__, static_url_path='', static_folder='.')

from userdao1 import UserDAO

##TO DO
### Dictionary
### Update and Delete

users = [{"id":1, "User":"EnchantedSleepy", "Email":"sleepy@gmail.com", "Edits":1526, "Permission":"Advanced Editor"}, 
        {"id":2, "User":"MrPotatoHead", "Email":"mph_rocks@gmail.com", "Edits":526, "Permission":"Editor"},
        {"id":3, "User":"AgonyAunt", "Email":"aunty@gmail.com", "Edits":26, "Permission":"Editor"},
        {"id":4, "User":"james_", "Email":"james_notjame@hotmail.com", "Edits":5126, "Permission":"Gardener"}
]
newID = 5

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
    result = UserDAO.findByID(id)
    return jsonify(result)
    #foundUser = list(filter(lambda x : x['id'] == id, users))
    #if len(foundUser)==0:
        #return (jsonify({}), 204)
    #return jsonify(foundUser[0])
##curl "http://127.0.0.1:5000/users/2"

#Code to add a new user - must include user name and email
@app.route('/users', methods = ['POST'])
def create():
    global newID
    try:
        new_user = request.get_json(force=True)
    except:
        abort(400)
    if not 'User' in new_user:
        abort(400)
    if not 'Email' in new_user:
        abort(400)
    user = {
        #Note for new editors, the number of edits is automatically zero
        #and they have editor permissions only
        "Edits": 0,
        "Email": new_user['Email'],
        "Permission": 'Editor',
        "User": new_user['User'],
        "id": newID,
    }
    newID = newID +1
    users.append(user)
    return jsonify({'User': user}), 201
#curl -i -H "Content-Type:application.json" -X POST -d "{\"Email\":\"skippy@hotmail.com\",\"Permission\":\"Advanced Editor\",\"User\":\"skippy\"}" http://127.0.0.1:5000/users
#OR 
#curl -i -H "Content-Type:application.json" -X POST -d "{\"Email\":\"skippy@hotmail.com\",\"User\":\"skippy\"}" http://127.0.0.1:5000/users



@app.route('/users/<int:id>', methods = ['PUT'])
def update(id):
    foundUsers = list(filter(lambda x : x['id'] == id, users))
    if len(foundUsers)==0:
        abort(404)
    foundUser = foundUsers[0]
    if not request.json:
        abort(400)
    update_user = request.json
    perms = ['Editor', 'Advanced Editor', 'Gardener']
    if 'Edits' in update_user and type(update_user['Edits']) is not int:
        abort(400)
    if 'User'in update_user:
        foundUser['User']= update_user['User']
    if 'Edits' in update_user:
        #or we could do , if Edits in update_user
        foundUser['Edits']= update_user['Edits']
    if 'Email' in update_user:
        foundUser['Email']= update_user['Email']
    if 'Permission' in update_user:
        foundUser['Permission']= update_user['Permission']
    return jsonify(foundUser)
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Edits\":10,\"Email\":\"skippy@hotmail.com\",\"Permission\":\"Editor\",\"User\":\"skippy\"}" http://127.0.0.1:5000/users/5
# OR
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Edits\":78}" http://127.0.0.1:5000/users/4

@app.route('/users/<int:id>', methods = ['DELETE'])
def delete(id):
    foundUsers = list(filter(lambda x : x['id'] == id, users))
    if len(foundUsers)==0:
        print('No user with that id')
        abort(404)
    UserDAO.delete(id)
    #users.remove(foundUsers[0])
    return jsonify({"done":True})
#curl -X DELETE "http://127.0.0.1:5000/users/1"

if __name__ == '__main__' :
    app.run(debug= True)
