


import psycopg2
import dbconinfo






###################################################################################################################
# Employee handling

def dbconnectemp():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employee30(id serial primary key, date_and_time TEXT, employee_name TEXT, address1 TEXT, phone TEXT, pincode TEXT, position TEXT)''')
    db.commit()
    db.close()





def dbentryemp(date, name, address, phone, pincode, position):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  employee30(date_and_time, employee_name, address1, phone, pincode, position) VALUES(%s, %s, %s, %s, %s, %s)''', (date, name, address, phone, pincode, position))
    db.commit()
    db.close()


def dbupdateemp(date, customer_name, address, phone, pincode, position, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE employee30 SET date_and_time = %s, employee_name = %s, address1 = %s, phone = %s, pincode =%s, position = %s WHERE id = %s''', (date, customer_name, address, phone, pincode, position, id))
    db.commit()
    db.close()





def dbdeleteemp(id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''DELETE FROM  employee30 WHERE id=''' + id)
    db.commit()
    db.close()




def dbfetchemp():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''SELECT * FROM public.employee30''')
    return c
    
    
    
###################################################################################################################