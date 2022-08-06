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
    c.execute('''CREATE TABLE IF NOT EXISTS exp2(id serial primary key, date_and_time TEXT, supplier_name TEXT, supplier_id TEXT, inventory_name TEXT, inv_id TEXT, total INT)''')
    db.commit()
    db.close()





def dbentry(date, supplier_name, supplier_id, inventory_name, inv_id,  total):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  exp2(date_and_time, supplier_name, supplier_id, inventory_name, inv_id,  total) VALUES(%s, %s, %s, %s, %s, %s)''', (date,supplier_name, supplier_id, inventory_name, inv_id,  total))
    db.commit()
    db.close()


def dbupdate(date,supplier_name, supplier_id, inventory_name, inv_id, total, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE exp2 SET date_and_time = %s, supplier_name= %s, supplier_id= %s, inventory_name= %s, inv_id= %s,  total= %s WHERE id = %s''', (date, supplier_name, supplier_id, inventory_name, inv_id, total, id))
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
    c.execute('''DELETE FROM  exp2 WHERE id=''' + id)
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
    c.execute('''SELECT * FROM public.exp2''')
    return c
    