import mysql.connector as sql
import TablePrint as tp

database = sql.connect(host='localhost',user='root',password='root',database='Library')
dbms = database.cursor()

def close():
    dbms.close()
    database.close()
    
def purchase(name,author,qty):
    dbms.execute("SELECT name,author FROM Books WHERE name = '{}' AND author = '{}';".format(name,author))
    if dbms.fetchone() is None:
        dbms.execute("INSERT INTO Books (name,author,qty) VALUES ('{}','{}',{});".format(name,author,qty))
    else:
        dbms.execute("UPDATE Books SET qty = qty + {}, qty_in_library = qty_in_library + {} WHERE name = '{}' AND author = '{}';".format(qty,qty,name,author))
    database.commit()
    
def issue(bname, bauthor,sname,sclass,sid):
    dbms.execute("SELECT id FROM Books WHERE name = '{}' AND author = '{}';".format(bname,bauthor))
    out = dbms.fetchone()
    if out is None:
        print('Can`t issue books,-')
        print('Book not available..')
        return
    out = out[0] # to get id extracted from tuple.
    dbms.execute("UPDATE Books SET qty_in_library = qty_in_library - 1 WHERE id = {};".format(out))
    database.commit()
    dbms.execute("INSERT INTO Issued VALUES ({},'{}','{}',{});".format(out,sname,sclass,sid))
    database.commit()
    
def book_back(bname,bauthor,sid):
    dbms.execute("SELECT id,qty-qty_in_library FROM Books WHERE name = '{}' AND author = '{}';".format(bname,bauthor))
    out = dbms.fetchone()
    if out is None:
        print('Can`t get book back book,-')
        print('Book neither issued nor available..')
        return
    elif out[0]:
        print('Can`t issue book,-')
        print('Book not issued..')
    out = out[0] # to get id extracted from tuple.
    dbms.execute("UPDATE Books SET qty_in_library = qty_in_library + 1 WHERE id = {};".format(out))
    database.commit()
    dbms.execute('DELETE FROM Issued WHERE book_id ={} , s_id ={};'.format(out,sid))
    database.commit()
    
def remove(name,author,qty,reason):
    dbms.execute("SELECT count(*),qty,qty_in_library,id FROM Books WHERE name = '{}' ,author = '{}';".format(name,author))
    out = dbms.fetchone()
    count = out[0] # to get count.
    if count == 0:
        print('Book already not available.')
        return
    elif out[2] < qty:
        print('Only {} books in library out of {}.'.format(out[1],out[2]))
        return
    elif out[2] == qty:
        dbms.execute("DELETE FROM Books WHERE id = {};".format(out[3]))
    else:
        dbms.execute("UPDATE Books SET qty = aty - {}, qty_in_library = qty_in_library -{} WHERE id = {};".format(qty,qty,out[3]))
    database.commit()
    dbms.execute("INSERT INTO Removed VALUES ('{}','{}',{},'{}');".format(name,author,qty,reason))
    database.commit()
    
def all_books():
    dbms.execute("SELECT *,qty-qty_in_library FROM Books;")
    head = ['Serial / Id','Book Name','Author','Total Books','Books in Library','Books Issued']
    tp.from_cursor(dbms,head)
    temp = input('Enter to [CONTINUE] - - -')
    
def books():
    dbms.execute("SELECT name,author,qty_in_library FROM Books;")
    head = ['Book Name','Author','Books in Library']
    tp.from_cursor(dbms,head)
    temp = input('Enter to [CONTINUE] - - -')
    
def all_issued():
    dbms.execute("SELECT s_id,name,author FROM Issued INNER JOIN Books WHERE book_id = id;")
    head = ['Student Id','Book Name','Author']
    tp.from_cursor(dbms,head)
    temp = input('Enter to [CONTINUE] - - -')
    
def issued():
    dbms.execute("SELECT s_id,s_name,s_class,name,author FROM Issued INNER JOIN Books WHERE book_id = id;")
    head = ['Student Id','Student Name','Student Class','Book Name','Author']
    tp.from_cursor(dbms,head)
    temp = input('Enter to [CONTINUE] - - -')