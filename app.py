from util import *
print("----------------------Welcome To Hospital Management System----------------------\n")
opt = 1
while(opt != 0):
    print("\n\n\t\t\tPlease choose an opttion from the menu below.")
    print("1. Add Test Information.")
    print("2. Add Doctor Information.")
    print("3. Add Patient Information.")
    print("4. Add test record to Patient.")
    print("5. Delete Test Information.")
    print("6. Delete Doctor Information.")
    print("7. Delete Patient Information.")
    print("8. Make an appointment.")
    print("9. Show appointments.")
    print("10. Show Tests.")
    print("11. Show Docs.")
    print("0. Exit")

    print("\nYour Choice: ", end='')

    opt = int(input())
    if opt == 1:
        addTestInfo()
    elif opt == 2:
        addDocInfo()
    elif opt == 3:
        addPatInfo()
    elif opt == 4:
        addTestRec()
    elif opt == 5:
        delTestInfo()
    elif opt == 6:
        delDocInfo()
    elif opt == 7:
        delPatInfo()
    elif opt == 8:
        makeAnAppo()
    elif opt == 9:
        showAppointments()
    elif opt == 10:
        showTests()
    elif opt == 11:
        showDocs()
    else:
        print("\nWhat the hell did you enter.")
