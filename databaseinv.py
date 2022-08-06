
import psycopg2
import dbconinfo



# Expense handling

def dbconnectinv():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS inventory1(id serial primary key, inventory_name TEXT, discription TEXT, cost TEXT, unit TEXT)''')
    db.commit()
    db.close()





def dbentryinv(name, discriprion, cost, unit):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  inventory1(inventory_name, discription, cost, unit) VALUES(%s, %s, %s, %s)''', (name, discriprion, cost, unit))
    db.commit()
    db.close()


def dbupdatinv(inventory_name, discription, cost, unit, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE inventory1 SET inventory_name = %s, discription = %s, cost = %s, unit = %s WHERE id = %s''', (inventory_name, discription, cost, unit, id))
    db.commit()
    db.close()





def dbdeleteinv(id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''DELETE FROM  inventory1 WHERE id=''' + id)
    db.commit()
    db.close()




def dbfetchinv():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''SELECT * FROM public.inventory1''')
    return c