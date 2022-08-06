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
    c.execute('''CREATE TABLE IF NOT EXISTS supplier_settlement(id serial primary key, date_and_time TEXT, supplier_name TEXT, supplier_id TEXT, outstanding INT, current_payment INT, balance INT)''')
    db.commit()
    db.close()





def dbentry(date, name, id, outstanding, current_payment, balance):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  supplier_settlement(date_and_time, supplier_name, supplier_id, outstanding, current_payment, balance) VALUES(%s, %s, %s, %s, %s, %s)''', (date, name, id, outstanding, current_payment, balance))
    db.commit()
    db.close()


def dbupdate(date, supplier_name, supplier_id, outstanding, current_payment, balance, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE supplier_settlement SET date_and_time = %s, supplier_name = %s, supplier_id = %s, outstanding = %s, current_payment =%s, balance = %s WHERE id = %s''', (date, supplier_name, supplier_id, outstanding, current_payment, balance, id))
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
    c.execute('''DELETE FROM  supplier_settlement WHERE id=''' + id)
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
    c.execute('''SELECT * FROM public.supplier_settlement''')
    return c
    