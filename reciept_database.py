import psycopg2
import dbconinfo



def dbconnect():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reciept53(id serial primary key, date_and_time TEXT, customer_name TEXT, customer_id TEXT, employee_name TEXT, employee_id TEXT, amount INT, estimate INT, balance INT, cat INT, cat1 TEXT)''')
    db.commit()
    db.close()





def dbentry(date, customer_name, customer_id, employee_name, employee_id, amount, estimate, balance, cat, cat1):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  reciept53(date_and_time, customer_name, customer_id, employee_name, employee_id, amount, estimate, balance, cat, cat1) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (date, customer_name, customer_id, employee_name, employee_id, amount, estimate, balance, cat, cat1))
    db.commit()
    db.close()


def dbupdate(date, customer_name, customer_id, employee_name, employee_id, amount, estimate, balance, cat, cat1, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE reciept53 SET date_and_time = %s, customer_name= %s, customer_id= %s, employee_name= %s, employee_id= %s, amount= %s, estimate= %s, balance= %s, cat= %s, cat1=%s WHERE id = %s''', (date, customer_name, customer_id, employee_name, employee_id, amount, estimate, balance, cat, cat1, id))
    db.commit()
    db.close()





def dbdelete(id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''DELETE FROM  reciept53 WHERE id=''' + id)
    db.commit()
    db.close()




def dbfetch():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''SELECT * FROM public.reciept53''')
    return c
    