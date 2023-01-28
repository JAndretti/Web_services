import cgi
import pymysql
import json


def connect(log,mdp):

    # Adaptez le contenu en bleu à votre cas particulier
    connection = pymysql.connect(host='localhost',
                user=log,
                password=mdp,
                db=log,
                charset='utf8mb4',
                port=3306,
                cursorclass=pymysql.cursors.DictCursor)
    return connection


def returnHttpData(): # Fonction retournant le dictionnaire qui contient les données http
    formData = cgi.FieldStorage()
    httpData = {}
    httpDataKeys = []
    httpDataKeys = list(formData)
    for key in httpDataKeys:
        httpData[key] = (formData[key].value)
    return httpData

def getStudent(dest,connection):
    student=dest.get('student')
    with connection.cursor() as cursor:
            sql = "SELECT Id_Student FROM `Student` WHERE `Number` = '"+student+"'"
            cursor.execute(sql)
    output = cursor.fetchall()
    return output[0].get('Id_Student')

def getExam(dest,connection):
    exam=dest.get('exam')
    with connection.cursor() as cursor:
            sql = "SELECT Id_Exam FROM `Exam` WHERE `Name` = '"+exam+"'"
            cursor.execute(sql)
    output = cursor.fetchall()
    return output[0].get('Id_Exam')

def getSensor(dest,connection):
    sensor=dest.get('sensor')
    with connection.cursor() as cursor:
            sql = "SELECT Id_Sensor FROM `Sensor` WHERE `Short_Name` = '"+sensor+"'"
            cursor.execute(sql)
    output = cursor.fetchall()
    return output[0].get('Id_Sensor')

def readRessource(dest,connection):
    try:
        student=int(getStudent(dest,connection))
        exam=int(getExam(dest,connection))
        sensor=int(getSensor(dest,connection))
    except:
        return

    if student and exam and sensor:
        clauseWhere = "WHERE `Id_Student` = "+str(student)+" AND `Id_Exam` = "+str(exam)+" AND `Id_Sensor` = "+str(sensor)
        with connection.cursor() as cursor:
            sql = "SELECT Measurement_value, Acquisition_time FROM `Measurements` "+clauseWhere
            cursor.execute(sql)
        output = cursor.fetchall()
        return output


def PostRessource(dest,connection):
    #
    output=readRessource(dest,connection)
    if output:
        return {'code': 'ALREADY_EXIST', 'text': 'this data already exist in the DB', 'data': None}
    else :
        try:
            student = int(dest.get('student'))
            exam=int(dest.get('exam'))
            sensor=int(dest.get('sensor'))
            time=dest.get('time')
            measurement = dest.get('measure')            
        except:
            return {'code': 'FAILED', 'text': 'Missing data', 'data': None}
        value = "('"+str(student)+"', '"+str(exam)+"', '"+str(sensor)+"', '"+str(time)+"', '"+str(measurement)+"')"
        with connection.cursor() as cursor:
            sql = "INSERT INTO `Measurements` (Id_Student, Id_Exam, Id_Sensor, Acquisition_time, Measurement_value) VALUES "+value
            cursor.execute(sql)
        connection.commit()
        if cursor.rowcount>0:
            return {'code': 'SUCCESS', 'text': 'Data added successfully', 'data': dest}
        else:
            return {'code': 'FAILED', 'text': 'Failed to add data', 'data': None}

def droit(connection, loginMdp):
    with connection.cursor() as cursor:
        sql = "SELECT `rights` FROM `users` WHERE `loginUser` = '" + loginMdp[0] + "' AND `pwdUser` = PASSWORD('" +loginMdp[1] + "')"        
        cursor.execute(sql)
        right = cursor.fetchone()
    if right is not None:
        return right
    else:
        return 'error'