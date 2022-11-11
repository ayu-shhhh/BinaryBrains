
import mysql.connector as c
con=c.connect(host='localhost',user='root',passwd='1234',database='freetime')
cursor=con.cursor()

#menu functions

def s_va():
    global cursor
    query=("select * from s")
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(i)
    
def s_vo():
    global cursor
    s_name=input("enter the name of the student who's record you want to view: ")
    query=("select * from s where s_name='{}'".format(s_name))
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(i)


def s_a():
    global cursor
    s_no=int(input("enter the id of the student: "))
    s_name=input("enter the name of the student: ")

    query=("insert into s values({},'{}', NULL, NULL, NULL, NULL)" .format(s_no,s_name))
    cursor.execute(query)
    print("|student record added|")

def s_d():
    global cursor
    s_va()
    s_no=input("enter the serial no. of the student who's record you want to delete: ")
    query=("delete from s where s_no='{}'".format(s_no))
    cursor.execute(query)
    con.commit()
    print("|record deleted|") 

def f_va():
    global cursor
    query=("select * from f")
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(i)

def f_vo():
    global cursor
    f_name=input("enter the name of the faculty who's record you want to view: ")
    query=("select * from f where f_name='{}'".format(f_name))
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        print(i)

def f_a():
    global cursor
    f_no=int(input("enter the id of the faculty: "))
    f_name=input("enter the name of the faculty: ")

    query=("insert into f values({},'{}',NULL)" .format(f_no,f_name))
    cursor.execute(query)
    print("|faculty record added|")

def f_d():
    global cursor
    f_no=input("enter the serial no. of the faculty who's record you want to delete: ")
    query=("delete from f where f_no='{}'".format(f_no))
    cursor.execute(query)
    con.commit()
    print("|record deleted|")


            
#print('')                    #title



    




def menu():
    while True:
        print("\n\n\n\nAre you a Student or Faculty Member?")
        c=input("Enter choice: ")
        if c=="Student":
            student()
        elif c=="Faculty":
            faculty()
        else:
            print("there was a mistake please try again...\n\n\n\n")
                


def student():
    print("1: Student Record")
    print("2: Check Free Time Slots")
    c=int(input("Enter choice: "))
    if c==1:
        stu_rec()
    elif c==2:
        stu_slot()


def stu_rec():
    while True:
        print("1: Add Record")
        print("2: Delete Record")
        print("3: View One Record")
        print("4: View All Record")
        print("5: Go back to the last menu")
        c=int(input("Enter choice: "))
        if c==1:
            s_a()
        elif c==2:
            s_d()
        elif c==3:
            s_vo()
        elif c==4:
            s_va()
        elif c==5:
            print("\n\n")
            student()

def stu_slot():
    b=input("Enter Faculty's Name: ")
    query=("select * from f where f_name='{}' ".format(b))
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    a=input("Enter Student's Name: ")
    query2=("update s set f_as='{}' where s_name='{}' ".format(b,a))
    cursor.execute(query2)
    
    x=input("Want to apply for the slot? Y/N? :")
    if x=='Y':
        y=input("Enter the topic you want to study: ")
        query3=("update s,f set s.sts = f.fs , s.topic='{}' where s_name='{}' ".format(y,a))
    else:
        student()

        

def faculty():
    print("1: Faculty Record")
    print("2: Edit Free Time Slots")
    c=int(input("Enter choice: "))
    if c==1:
        fac_rec()
    elif c==2:
        fac_slot()


def fac_rec():
    while True:
        print("1: Add Record")
        print("2: Delete Record")
        print("3: View One Record")
        print("4: View All Record")
        print("5: Go back to the last menu")
        c=int(input("Enter choice: "))
        if c==1:
            f_a()
        elif c==2:
            f_d()
        elif c==3:
            f_vo()
        elif c==4:
            f_va()
        elif c==5:
            print("\n\n\n\n")
            faculty()

def fac_slot():
    global cursor
    
    a=input("Enter Faculty Name: ")
    query=("select * from f where f_name='{}'".format(a))
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    print("\n\n")
    print("1: Add Slot")
    print("2: Delete Slot")
    print("3: Show Students' Query")
    c=int(input("Enter Choice: "))
    if c==1:
        _1=input('Enter Time Slot: ')
        query=("update f set fs='{}' where f_name='{}' ".format(_1,a))
        cursor.execute(query)
        print("slot added")
    elif c==2:
        query=("update f set fs='NULL' where f_name='{}' ".format(a))
        cursor.execute(query)
        print("slot deleted")
    
    elif c==3:
        query=("select * from s,f where s.sts = f.fs AND f_name= '{}' ".format(a))
        cursor.execute(query)
        data=cursor.fetchall()
        for i in data:
            print(i)
        x=int(input("Enter the student's id that you want to approve:"))
        query5=("update s set f_as = '{}' , approved = 1 where s_id".format(a))
        cursor.execute(query5)


menu()
