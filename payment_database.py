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
    c.execute('''CREATE TABLE IF NOT EXISTS payment53(id serial primary key, date_and_time TEXT, customer_name TEXT, customer_id TEXT, supplier_name TEXT, supplier_id TEXT, employee_name TEXT, employee_id TEXT, work_name TEXT, work_id TEXT, amount INT, estimate INT, balance INT, cat TEXT, pos TEXT)''')
    db.commit()
    db.close()





def dbentry(date, customer_name, customer_id, supplier_name, supplier_id, employee_name, employee_id, work_name, work_id, amount, estimate, balance, cat, pos):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  payment53(date_and_time, customer_name, customer_id, supplier_name, supplier_id, employee_name, employee_id, work_name, work_id, amount, estimate, balance, cat, pos) VALUES(%s, %s, %s, %s, %s, %s, %s, %s,%s,%s, %s, %s, %s, %s)''', (date, customer_name, customer_id,supplier_name, supplier_id, employee_name, employee_id, work_name, work_id, amount, estimate, balance, cat, pos))
    db.commit()
    db.close()


# def dbupdate(date, customer_name, customer_id,supplier_name, supplier_id, employee_name, employee_id,work_name, work_id, amount, estimate, balance, cat, id):
#     db = psycopg2.connect(
#         host = "localhost",
#         database = "kavitha",
#         user = "postgres",
#         password = "goldcoin",
#         port = "5432",
        
#     )
#     c = db.cursor()
#     c.execute('''UPDATE payment52 SET date_and_time = %s, customer_name= %s, customer_id= %s, supplier_name =%s, supplier_id = %s, employee_name= %s, employee_id= %s, work_name= %s, work_id= %s, amount= %s, estimate= %s, balance= %s, cat= %s WHERE id = %s''', (date, customer_name, customer_id,supplier_name, supplier_id, employee_name, employee_id,work_name,work_id, amount, estimate, balance, cat, id))
#     db.commit()
#     db.close()





def dbdelete(id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''DELETE FROM  payment53 WHERE id=''' + id)
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
    c.execute('''SELECT * FROM public.payment53''')
    return c
    