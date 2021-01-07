import db
import time

print(
    '''
            +--------------------+
            |     Welcome to     |
            | LIBRARY MANAGEMENT |
            +--------------------+
        
    LIBRARAY MANAGEMENT deals with databases
    required.
    It works with User friendly CLI.
    
    '''
    )


def controll(i):
    if i in [0,7]:
        i = input('Sure to exit..[y/m] ').strip().lower()
        if i == 'y':
            db.close()
            exit()
        else:
            print('Exit Canceled.')
    elif i == 1:
        book = input('Name of book-> ')
        author = input('Author of book-> ') 
        try:
            qty = int(input('Quantity purchased-> ').strip())
        except:
            print('Input should be integer for quantity.')
            print('Retry the purchase entry (1).')
            return
        db.purchase(book,author,qty)
    elif i == 2:
        s_name = input('Student Getting Name-> ').strip()
        s_class = input("Class of Student-> ").strip()
        s_id = input('Id of Student-> ').strip()
        b_name = input('Nmae of book issued-> ').strip()
        b_author = input('Author of Issued book-> ').strip()
        db.issue(b_name,b_author,s_name,s_class,s_id)
    elif i == 3:
        bname = input('Nmae of book returned-> ').strip()
        bauthor = input('Author of book returned-> ').strip()
        sid = int(input('Id of student returned book-> ').strip())
        db.book_back(bname,bauthor,sid)
    elif i == 4:
        bname = input('Nmae of book removed-> ').strip()
        bauthor = input('Author of book removed-> ').strip()
        bqty = int(input('Quantity of book removed-> ').strip())
        breason = int(input('Reason for removal-> ').strip())
        db.remove(bname,bauthor,bqty,reason)
        
    elif i in (50,5):
        db.all_books()
    elif i == 51:
        db.books()
    elif i in (60,6):
        db.all_issued()
    elif i == 61:
        db.issued()
    
    for a in range(1,21):
        print()
        time.sleep(1/a)
    print()

#-----------------------------------

while True:
    print(
        '''
    +  --------------------------  +
    1. Purchased books entry.
    2. Book issued to student.
    3. Book taken back from student.
    4. Book removed.
    ~~~~~~~~~~~~~~~
    5. Check Book list.
        50. (Default) all books.
        51. Books with Library.
    6. Check Book given to student.
        60. (Default) with student id only.
        61. with student complete details.
    ~~~~~~~~~~~~~~~
    (7). Exit.
    (0). Exit.
    
        '''
        )
    try:
        I = input('what to do-> ').strip()
        i = int(I)
        if not (0 <= i < 8 or i in [50,51,60,61]):
            print()
            print('++++++++++++++++++++++++++++++++')
            print('Value out of range...(Try Again)')
            continue
    except:
        print()
        print('++++++++++++++++++++++++++++++++++++++++')
        print('Your option not an Integer...(Try Again)')
        continue
    controll(i)