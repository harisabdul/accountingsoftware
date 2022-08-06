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
    c.execute('''CREATE TABLE IF NOT EXISTS labor_purchase1(id serial primary key, date_and_time TEXT,customer_name TEXT, customer_id TEXT, supplier_name TEXT, supplier_id TEXT, inventory_name TEXT, inv_id TEXT, qty INT, price INT, total INT)''')
    db.commit()
    db.close()





def dbentry(date, customer_name, customer_id, supplier_name, supplier_id, inventory_name, inv_id, qty, price, total):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  labor_purchase1(date_and_time, customer_name, customer_id, supplier_name, supplier_id, inventory_name, inv_id, qty, price, total) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (date, customer_name, customer_id, supplier_name, supplier_id, inventory_name, inv_id, qty, price, total))
    db.commit()
    db.close()


def dbupdate(date, customer_name, customer_id, supplier_name, supplier_id, inventory_name, inv_id, qty, price, total, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE labor_purchase1 SET date_and_time = %s,customer_name= %s, customer_id= %s, supplier_name= %s, supplier_id= %s, inventory_name= %s, inv_id= %s, qty= %s, price= %s, total= %s WHERE id = %s''', (date, customer_name, customer_id,  supplier_name, supplier_id, inventory_name, inv_id, qty, price, total, id))
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
    c.execute('''DELETE FROM  labor_purchase1 WHERE id=''' + id)
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
    c.execute('''SELECT * FROM public.labor_purchase1''')
    return c
    