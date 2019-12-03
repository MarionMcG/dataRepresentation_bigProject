from zstudentDAO import studentDAO


latestid = studentDAO.create(('mark', 45))
result = studentDAO.findbyID(latestid);
print(result)

#Update
studentDAO.update(('Fred', 21, latestid))
result = studentDAO.findbyID(latestid);
print(result)

#Get all users
allstudents = studentDAO.getAll()
for student in allstudents:
    print(student)

#delete
studentDAO.delete(latestid)