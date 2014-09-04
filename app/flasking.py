__author__ = 'Liew'

from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
import database
import json
import collections


Result = ""
Image = ""
dataDict = {}


def setvalues(pid, ipadd, operatingsystem, port, method, attackduration, sensitivity,
            maxpacket, fixapplied, pie, filename, time):
    global distData, dataDict, solution
    dataDict['primaryID'] = pid
    dataDict['ipAddress'] = ipadd
    dataDict['OperatingSystem'] = operatingsystem
    dataDict['Port'] = port
    dataDict['Method'] = method
    dataDict['AttackDuration'] = attackduration
    dataDict['Sensitive'] = sensitivity
    dataDict['MaxPacketSent'] = maxpacket
    dataDict['FixApplied'] = fixapplied
    dataDict['log'] = filename
    dataDict['DateTime'] = time
    dataDict['Pie'] = pie
    dataDict['Result'] = getResult(pid, fixapplied)[1]
    dataDict['Resultnum'] = getResult(pid, fixapplied)[0]
    dataDict['Resultcolor'] = getResult(pid, fixapplied)[2]
    dataDict['DoSDefinition'] = database.getDef(method)
    distData = getScore(pid)
    solution = getSolution(operatingsystem, method)

def getScore(pid):
    b = json.loads(database.getScore(pid)[0])
    data = [dict(num=row[0], imgpath=row[1])
             for row in collections.OrderedDict(sorted(json.loads(database.getimage(pid)[0]).items())).items()]
    data1 = [dict(oncount=(row[1].count('ON')), length=(float(len(row[1]))),
                 score=(row[1].count('ON')/float(len(row[1]))))
                for row in collections.OrderedDict(sorted(b.items())).items()]
    for i in range(0, len(data1)):
        data[i].update(data1[i])
    return data

app = Flask(__name__)

def getResult(pid, fix):
    b = collections.OrderedDict(sorted(json.loads(database.getScore(pid)[0]).items()))
    total = len(b)
    grandScore = 0
    i = 1

    for row in b.items():
        score = row[1].count('ON')/float(len(row[1]))
        if i <= 1:
            if score > 0.9:
                grandScore += 1
        elif 1 < i <= 2:
            if score > 0.8:
                grandScore += 1
        elif 2 < i <= 3:
            if score > 0.7:
                grandScore += 1
        elif 4 < i <= 5:
            if score > 0.5:
                grandScore += 1
        else:
            if score > 0.2:
                grandScore += 1
        i += 1

    if fix == "NO":
        if grandScore <= 1:
            return [grandScore, "VERY CRITICAL", "RED"]
        elif 1 < grandScore <= 2:
            return [grandScore, "CRITICAL", "Orange"]
        elif 2 < grandScore <= 3:
            return [grandScore, "VERY VULNERABLE", "Orange"]
        elif 3 < grandScore <= 4:
            return [grandScore, "VULNERABLE", "Yellow"]
        elif grandScore >= 5:
            return [grandScore, "SAFE", "Green"]

    else:
        if grandScore <= 1:
            return [grandScore, "SAFE", "Green"]
        elif 1 < grandScore <= 2:
            return [grandScore, "VULNERABLE", "Yellow"]
        elif 2 < grandScore <= 3:
            return [grandScore, "VERY VULNERABLE", "Orange"]
        elif 3 < grandScore <= 4:
            return [grandScore, "CRITICAL", "Orange"]
        elif grandScore >= 5:
            return [grandScore, "VERY CRITICAL", "RED"]

def getSolution(os, atk):
    return [dict(number=row[0], entry=row[1]) for row in database.getSolutions(os,atk)]

@app.route("/")
def launchreport():
    global distData, dataDict, solution
    return render_template('report.html', dataDisplay=distData, dataDicts=dataDict, solutions=solution)

@app.route("/<numbers>")
def setid(numbers):
    global distData, dataDict, solution
    dbRec = database.getOneRecord(numbers)
    if dbRec:
        setvalues(dbRec[0], dbRec[1], dbRec[2], dbRec[3], dbRec[4],
              dbRec[5], dbRec[6], dbRec[7], dbRec[8], dbRec[11], dbRec[12], dbRec[13])
        return render_template('report.html', dataDisplay=distData, dataDicts=dataDict, solutions=solution)
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

def starting():
    # setvalues('1', '192.168.56.102', 'Ubuntu', '80', 'HTTP ATTACK',
    #            '60', '500', 'YES', 'b66f6ba2-00e4-4d49-8fca-2e5e31ce9a20.svg', '0210')
    app.run()


