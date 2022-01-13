from databaseMng import *
from validInput import *
import pandas as pd

# Add score
def insertScr():
    # Validate ID student
    while True:
        vid = input('Input student ID: ')
        if validStudentIDExist(vid):
            break
        else:
            continue
    # Validate ID subject
    while True:
        idSubject = input('Input subject ID: ')
        if validSubjectIDExist(idSubject):
            break
        else:
            continue
    # Validate process scores
    while True:
        processScore = input('Input process score: ')
        if validInputScore(processScore):
            break
        else:
            continue
    # Validate exam scores
    while True:
        examScore = int(input('Input exam score: '))
        if validInputScore(processScore):
            break
        else:
            continue
    sql = "INSERT INTO Scores (student_id, subject_id, process_scores, exam_scores) VALUES (%s, %s, %s, %s)"
    val = (vid, idSubject, processScore, examScore)

    check = exec(sql, val)
    if check == 0:
        print("No record process, maybe double")
    else:
        print("Successfull")

# Edit Score
def editScr():
    studentName = input('Input student Name to edit: ')
    ml1 = findScrName(studentName)

    studentid = input('Input student ID to edit: ')
    ml2 = findScrID(studentid)

    while True:
        SubjectID = input('Input Subject ID to edit: ')
        processScore = input('Input process score to edit: ')
        examScore = input('Input exam score to edit: ')
        sql = "Update Scores set process_scores = %s, exam_scores = %s where (student_Id = %s) & (subject_Id = %s)"
        val = (processScore, examScore, studentid, SubjectID)
        exec(sql, val)
        checkContinue = input("Press N to end, other to continue? ")
        if checkContinue.upper() == "N":
            break
        else:
            continue

#find score by student ID
def findScrID(Sid):
    while True:
        try:
            studentid = int(Sid)
            sql = "Select * from Students Where student_id = %s"
            vid = ExecSearch(sql, studentid)
            if vid == 0:
                print('Student ID not exists, input again')
                continue
            else:
                sql = "Select * from Scores Where student_id = %s"
                mylist = ExecSearch(sql, vid[0][0])
                list_header = ['Student ID', 'Subject ID', 'Process scores', 'Exam scores', 'Final scores']
                mylist.insert(0, list_header)
                for row in mylist:
                    print("{: >12} {: >12} {: >15} {: >15} {: >15}".format(*row))
                return mylist
                break
        except:
            print('Wrong Type ID, INPUT again')
            continue

# find score by student name
def findScrName(Sname):
    sql = "Select * from Students Where instr(Full_name, %s)"
    listID = ExecSearch(sql,Sname)

    if listID == 0:
        print('No name found')
    else:
        sql = "Select * from Scores Where student_id in %s"
        list_tmp = []
        for i in range(len(listID)):
            list_tmp.append(listID[i][0])
        tuple_tmp = tuple(list_tmp)
        mylist = ExecSearch(sql, (tuple_tmp,))

        list_header = ['Student ID', 'Subject ID', 'Process scores', 'Exam scores', 'Final scores']
        mylist.insert(0, list_header)
        for row in mylist:
            print("{: >12} {: >12} {: >15} {: >15} {: >15}".format(*row))
        return mylist

# score statistics
def statisticScr():
    sql = 'Select * from scores'
    mylist = ExecSearch(sql,None)
    print(mylist)
    for i in range(len(mylist)):
        if mylist[i][4] >= 90:
            mylist[i].append('A')
        elif mylist[i][4] <50:
            mylist[i].append('D')
        elif (mylist[i][4]>=50) & (mylist[i][4]<70):
            mylist[i].append('C')
        else:
            mylist[i].append('B')
    l = ['Student ID', 'Subject ID', 'Process scores', 'Exam scores', 'Final scores', 'Category Final']
    mylist.insert(0, l)
    for row in mylist:
        print("{: >12} {: >12} {: >15} {: >15} {: >15} {: >15}".format(*row))

def processExportToExcel():
    sql = 'SELECT full_name, birthday, sex, phone, email, address, subject_name, process_scores, exam_scores, final_scores \
               FROM students st \
               LEFT JOIN scores sc \
               ON st.student_id = sc.student_id \
               LEFT JOIN subjects su \
               ON sc.subject_id = su.subject_id'

    ml = ExecSearch(sql, None)
    mylist = []
    for i in range(len(ml)):
        list_tmp = []
        for j in range(10):
            if j == 1:
                v = ml[i][j].strftime(format='%d/%m/%Y')
                list_tmp.append(v)
            elif j in (6, 7, 8):
                if ml[i][j] != None:
                    list_tmp.append(ml[i][j])
                else:
                    list_tmp.append(0)
            elif j == 9:
                if ml[i][j] != None:
                    list_tmp.append(round(ml[i][j], 2))
                else:
                    list_tmp.append(0)
            else:
                list_tmp.append(ml[i][j])
        mylist.append(list_tmp)
    for v in mylist:
        print(v)
    df = pd.DataFrame()
    selected_column = ['Full name', 'Birthday', 'Sex', 'Phone', 'Email', 'Address',\
                       'Subject name', 'Process scores', 'Exam scores', 'Final scores']
    df = pd.DataFrame(columns=selected_column)
    for i in range(len(mylist)):
        df = df.append(pd.Series(mylist[i], index =selected_column), ignore_index = True)

    df.to_excel('FinalList.xlsx', index = False)
    print('DataFrame is written to Excel File successfully.')

