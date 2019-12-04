from userdao1 import userDAO


latestid = userDAO.create(('JKMan', 'jkfanman@hotmail.com'))
result = userDAO.findbyID(latestid);
print(result)

#Update
userDAO.update(('briarpatch', 'briarpatch@live.org', latestid))
result = userDAO.findbyID(latestid);
print(result)

#Get all users
allusers = userDAO.getAll()
for user in allusers:
    print(user)

#delete
userDAO.delete(latestid)