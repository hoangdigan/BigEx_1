# VALIDATE USER INPUT

import re
from datetime import datetime
from databaseMng import *


# Email validate
def validEmail(email):
    regex = r'\b[A-Za-z0-9.]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    else:
        return False


# Phone validate
def validPhone(phoneNumber):
    pattern = r"^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$"

    if re.match(pattern, phoneNumber):
        return True
    else:
        return False


# Date validate
def validDate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%d/%m/%Y").strftime('%d/%m/%Y'):
            raise ValueError
        return True
    except ValueError:
        return False


def validStudentIDExist(studentID):
    try:
        idStudent = int(studentID)
        sql = "Select * from Students Where student_id = %s"
        v = ExecSearch(sql, idStudent)
        if v == 0:
            print('Student ID not in the list')
            return False
        else:
            return True
    except:
        print('Student ID must be number')
        return False


# Check subject exists
def validSubjectIDExist(id):
    try:
        idSubject = int(id)
        sql = "Select * from Subjects Where subject_id = %s"
        v = ExecSearch(sql, idSubject)
        if v == 0:
            print('Subject ID not in the list')
            return False
        else:
            return True
    except:
        print('Subject ID must be number')
        return False


# Scores input validate
def validInputScore(score):
    try:
        score = int(score)
        if (score >= 0) & (score <= 100):
            return True
        else:
            print(' 0 <= score must be <= 100')
            return False
    except:
        print('Scores must be number')
        return False
