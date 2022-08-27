import csv
def write():

    f=open('stud4.csv','a',newline='')
    w=csv.writer(f)
    n=int(input('enter number of students '))
    for x in range(n):
        name=input('Enter your name : ')
        age=input('Enter your age : ')
        mob_num=int(input('Enter your mobile num : '))
        email_id=input('Enter your email id : ')
        roll_no=input('Enter your roll no : ')
        l=[name,age,mob_num,email_id,roll_no]
        w.writerow(l)
    f.close()
def display():
    f=open('stud4.csv','r',newline='')
    stud=csv.reader(f)
    for i in stud:
        print(i)
    f.close()


# main
while True:
    print('MENU \n 1-WRITE \n 2-DISPLAY  \n 3-exit')
    ch=int(input('Enter your choice : '))
    if ch ==1:
        write()
    if ch==2:
        display()
    
    if ch==3:
        print('************ END OF THE PROGRAM ********** \n  ************** THANK YOU FOR USIMG THIS SOFTWARE **********')
        break
