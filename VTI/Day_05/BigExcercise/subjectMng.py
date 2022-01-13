from databaseMng import *

# Add subject
def insertSbj():
    sql = "Select * from Subjects Where subject_name = %s "
    while True:
        subject = input('Input new subject: ')
        if subject == "":
            print('subject not blank!')
            continue
        if ExecSearch(sql, subject) == 0:
            break
        else:
            print('Subject exists')
            continue
    sql = "INSERT INTO Subjects (subject_name) VALUES (%s)"
    exec(sql, subject)

# Edit Subject
def editSbj():
    while True:
        subject = input('Input subject to edit: ')
        if subject == "":
            print('subject not blank!')
            continue
        else:
            break
    sql = "Select * from Subjects where instr(subject_name , %s)"
    v = ExecSearch(sql, subject)
    if v == 0:
        print('No found')
    else:
        for i in range(len(v)):
            print("Subject ID: ", v[i][0], "Subject Name: ", v[i][1] )
        id = input('Please input ID subject to change: ')
        str_input = input('Please input new name to change: ')
        sql = "Update Subjects set subject_name = %s where subject_id = %s"
        val = (str_input, id)
        exec(sql, val)

# find subject
def findSbj():
    while True:
        subject = input('Input subject to find: ')
        if subject == "":
            print('subject not blank!')
            continue
        else:
            break
    sql = "Select * from Subjects Where instr(subject_name , %s)"
    mylist = ExecSearch(sql, subject)
    if mylist == 0:
        print("No found")
    else:
        for i in mylist:
            print(i)

# delete subject
def deleteSbj():
    while True:
        subject = input('Input Subject to delete: ')
        if subject == "":
            print('subject not blank!')
            continue
        else:
            break
    sql = "Delete from Subjects where subject_name = %s"
    exec(sql, subject)




