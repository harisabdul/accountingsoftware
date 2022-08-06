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
    c.execute('''CREATE TABLE IF NOT EXISTS tesingpos(id serial primary key, obname TEXT, qty_or_id TEXT, price INT, total INT)''')
    db.commit()
    db.close()





def dbentry(obname, qty, price, total):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  testingpos(obname, qty_or_id, price, total) VALUES(%s, %s, %s, %s)''', (obname, qty, price, total))
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
    c.execute('''DELETE FROM  testingpos WHERE id=''' + id)
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
    c.execute('''SELECT * FROM public.testingpos''')
    return c
    