import json


def addTestInfo():
    f = open('tests.json', 'a')
    f.close()
    test = {
        'name': '',
        'price': 0,
        'roomNum': 0
    }
    print("\n\t\tAdding a test info.")
    print('\tEnter test name: ', end='')
    test['name'] = input()

    print('\tEnter test price: ', end='')
    test['price'] = input()

    print('\tEnter test room #: ', end='')
    test['roomNum'] = input()
    fr = open('tests.json', 'r')

    prevTests = fr.read()

    allTests = [test]
    if prevTests != '':
        prevTests = json.loads(prevTests)
        prevTests.append(test)
        allTests = prevTests

    f = open('tests.json', 'w')
    f.write(json.dumps(allTests))
    f.close()
    fr.close()


def addDocInfo():
    f = open('doctor.json', 'a')
    f.close()
    doc = {
        'name': '',
        'specialization': 0,
        'timing': {'from': 0, 'to': 2},
        'venue': 0,
        'daysAvailable': {'from': 0, 'to': 5},
        'appointments': []
    }
    print("\n\t\tAdding a Doctor info.")
    print('\tEnter Doctor\'s name: ', end='')
    doc['name'] = input()

    print('\tEnter Doctor\'s specilization: ', end='')
    doc['specialization'] = input()

    print('\tEnter Doctor\'s timimg (0 == 12:00 am and 23 == 12: 00 pm )')
    print('\tFrom = ', end='')
    doc['timing']['from'] = input()
    print('\tTo = ', end='')
    doc['timing']['to'] = input()

    print('\tEnter Doctor\'s Venue (room #): ', end='')
    doc['venue'] = input()

    print("\tEnter Doctor's available days (0 == Monday, 1 == Tues and so on)")
    print("\tFrom: ", end='')
    doc['daysAvailable']['from'] = input()
    print('\tTo: ', end='')
    doc['daysAvailable']['to'] = input()

    fr = open('doctor.json', 'r')

    prevData = fr.read()

    allData = [doc]
    if prevData != '':
        prevData = json.loads(prevData)
        prevData.append(doc)
        allData = prevData

    f = open('doctor.json', 'w')
    f.write(json.dumps(allData))

    f.close()
    fr.close()


def addPatInfo():
    f = open('patient.json', 'a')
    f.close()
    pat = {
        'name': '',
        'age': 0,
        'gender': 0,
        "address": '',
        "date": '',
        "disease": '',
        'tests': []
    }
    print("\n\t\tAdding a patient info.")
    print('\tEnter patient\'s name: ', end='')
    pat['name'] = input()

    print('\tEnter patient\'s age: ', end='')
    pat['age'] = input()

    print('\tEnter patient\'s gender: ', end='')
    pat['gender'] = input()

    print('\tEnter Date: ', end='')
    pat['date'] = input()

    print('\tEnter patient\'s address: ', end='')
    pat['address'] = input()

    print('\tEnter patient\'s diseases name: ', end='')
    pat['disease'] = input()

    fr = open('patient.json', 'r')

    preData = fr.read()

    allData = [pat]
    if preData != '':
        preData = json.loads(preData)
        preData.append(pat)
        allData = preData

    f = open('patient.json', 'w')
    f.write(json.dumps(allData))
    f.close()
    fr.close()


def addTestRec():
    f = open('patient.json', 'a')
    f.close()
    test = {
        'name': '',
        'price': 0,
    }
    print("\n\t\tAdding a test record in patient.")

    print('\tEnter Patient\'s name: ', end='')
    patName = input()

    print('\tEnter test name: ', end='')
    test['name'] = input()

    print('\tEnter test price: ', end='')
    test['price'] = input()

    fr = open('patient.json', 'r')
    prevData = fr.read()

    if prevData != '':
        prevData = json.loads(prevData)
        for patient in prevData:
            if patient['name'] == patName:
                patient['tests'].append(test)

        allData = prevData

    f = open('patient.json', 'w')
    f.write(json.dumps(allData))
    f.close()
    fr.close()


def delTestInfo():
    print("\t\tDeleting a test info.")
    print("\tEnter test's name: ", end="")

    name = input()

    f = open('tests.json', 'r')
    data = json.loads(f.read())
    f.close()
    newData = []
    for test in data:
        if test['name'] == name:
            print("Successfully deleted the test")
            continue
        else:
            newData.append(test)
    fr = open('tests.json', 'w')
    fr.write(json.dumps(newData))
    fr.close()


def delDocInfo():
    print("\t\tDeleting a Doctors info.")
    print("\tEnter Doctor's name: ", end="")

    name = input()

    f = open('doctor.json', 'r')
    data = json.loads(f.read())
    f.close()
    newData = []
    for test in data:
        if test['name'] == name:
            print("Successfully deleted the test")
            continue
        else:
            newData.append(test)
    fr = open('doctor.json', 'w')
    fr.write(json.dumps(newData))
    fr.close()


def delPatInfo():
    print("\t\tDeleting a Patient info.")
    print("\tEnter patient's name: ", end="")

    name = input()

    f = open('patient.json', 'r')
    data = json.loads(f.read())
    f.close()
    newData = []
    for test in data:
        if test['name'] == name:
            print("Successfully deleted the test")
            continue
        else:
            newData.append(test)
    fr = open('patient.json', 'w')
    fr.write(json.dumps(newData))
    fr.close()


def makeAnAppo():
    print('\t\tMaking an appointment.')
    print("\tEnter day (0 == Mon, 1 == Tues and so on)", end='')
    day = int(input())

    print("\tEnter Doc's name: ", end='')
    name = input()

    f = open('doctor.json', 'r')
    doctors = json.loads(f.read())
    f.close()

    for doc in doctors:
        if doc['name'] == name and day >= int(doc['daysAvailable']['from']) and day <= int(doc['daysAvailable']['to']):
            print("\tEnter Patient name: ", end='')
            patName = input()

            print('\tEnter Patient Disease: ', end='')
            patDis = input()
            doc['appointments'].append({'name': patName, 'disease': patDis})

            print("\n\nSuccessfully made an appointment.")

    fr = open('doctor.json', 'w')
    fr.write(json.dumps(doctors))


def showAppointments():
    print('\t\tShowing Doctors appointments.')
    print('\tEnter Doctors name: ', end='')
    name = input()

    f = open('doctor.json', 'r')
    allData = json.loads(f.read())
    for doc in allData:
        if doc['name'] == name:
            for app in doc['appointments']:
                print(app)

    f.close()
