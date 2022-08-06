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
    c.execute('''CREATE TABLE IF NOT EXISTS cost(id serial primary key, date_and_time TEXT, supplier_name TEXT, supplier_id TEXT, inventory_name TEXT, inv_id TEXT, unit TEXT, qty INT, price INT, total INT)''')
    db.commit()
    db.close()





def dbentry(date, supplier_name, supplier_id, inventory_name, inv_id, unit, qty, price, total):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  cost(date_and_time, supplier_name, supplier_id, inventory_name, inv_id, unit, qty, price, total) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)''', (date,supplier_name, supplier_id, inventory_name, inv_id, unit, qty, price, total))
    db.commit()
    db.close()


def dbupdate(date,supplier_name, supplier_id, inventory_name, inv_id, unit, qty, price, total, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE cost SET date_and_time = %s, supplier_name= %s, supplier_id= %s, inventory_name= %s, inv_id= %s, unit= %s, qty= %s, price= %s, total= %s WHERE id = %s''', (date, supplier_name, supplier_id, inventory_name, inv_id, unit, qty, price, total, id))
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
    c.execute('''DELETE FROM  cost WHERE id=''' + id)
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
    c.execute('''SELECT * FROM public.cost''')
    return c
    