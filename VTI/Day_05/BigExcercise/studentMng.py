from datetime import datetime
from databaseMng import *
from validInput import *

# Add students
def insertStd():
    # input new students
    while True:
        name = input('Fullname: ')
        if name == "":
            print('Wrong name')
            continue
        else:
            break

    # valid date
    while True:
        birthday = input('Birthday (dd/MM/yyyy): ')
        if validDate(birthday):
            break
        else:
            print('Wrong Date, input again')
            continue
    birthday = datetime.strptime(birthday, "%d/%m/%Y")

    # valid sex
    while True:
        sex = input('Male [0] /Female [1]: ')
        if (sex == '0') | (sex == '1'):
            break
        else:
            print('Wrong sex, input again')
            continue

    # valid phone
    while True:
        phone = input('Phone: ')
        if validPhone(phone):
            break
        else:
            print('Wrong phone number, input again')
            continue

    # valid email
    while True:
        email = input('Email: ')
        if validEmail(email):
            break
        else:
            print('Wrong email, input again')
            continue

    address = input('Address: ')

    sql = "INSERT INTO Students (full_name, birthday, sex, phone, email, address) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (name, birthday, sex, phone, email, address)
    exec(sql, val)

#Edit Student
def editStd():
    name = input('Input name to edit: ')
    sql = "Select * from Students Where instr(Full_name , %s)"
    v = ExecSearch(sql, name)

    if v[0][0] != 0:
        for i in range(len(v)):
            print("Student ID: ", v[i][0], "Student Name: ", v[i][1] )
        vid = input('Please Student ID  to edit: ')

        mylist =[['full_name', 'Name'],
                 ['birthdate', 'Birth day'],
                 ['sex', 'Sex'],
                 ['phone', 'Phone'],
                 ['email', 'Email'],
                 ['address', 'Address']]
        str =input('Please input number to edit: ')

        for i in range(len(str)):
            j = int(str[i])
            if j == 2:
                birthday = input('Birthday (dd/MM/yyyy): ')
                str_input = datetime.strptime(birthday, "%d/%m/%Y")
                sql = "Update Students set birthday = %s where student_Id = {id}".format(id = vid)
                exec(sql,str_input)
            else:
                print('Please input', mylist[j-1][1])
                str_input = input()
                sql = "Update Students set {vcolumn} = %s where student_Id = {id}".format(vcolumn = mylist[j-1][0], id = vid )
                exec(sql,str_input)

# find students
def findStd():
    name = input('Input name to find: ')
    sql = "Select * from Students Where instr(Full_name , %s)"
    mylist = ExecSearch(sql, name)
    for i in mylist:
        print(i)

# delete students
def deleteStd():
    name = input('Input name to delete: ')
    sql = "Select * from Students Where instr(Full_name , %s)"
    v = ExecSearch(sql, name)

    if v[0][0] != 0:
        for i in range(len(v)):
            print("Student ID: ", v[i][0], "Student Name: ", v[i][1])
        vid = input('Please Student ID  to delete: ')

    sql = "Delete from Students where student_id = %s"
    exec(sql, vid)





