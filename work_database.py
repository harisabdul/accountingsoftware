import psycopg2
import dbconinfo





def dbconnectexp():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS work(id serial primary key, expense_name TEXT, discription TEXT)''')
    db.commit()
    db.close()





def dbentryexp(name, discriprion):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  work(expense_name, discription) VALUES(%s, %s)''', (name, discriprion))
    db.commit()
    db.close()


def dbupdatexp(expense_name, discription, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE work SET expense_name = %s, discription = %s WHERE id = %s''', (expense_name, discription, id))
    db.commit()
    db.close()





def dbdeleteexp(id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''DELETE FROM  work WHERE id=''' + id)
    db.commit()
    db.close()




def dbfetchexp():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''SELECT * FROM public.work''')
    return c
    
