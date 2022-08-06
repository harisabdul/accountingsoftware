import psycopg2



def dbconnect():
    db = psycopg2.connect(
        host = "localhost",
        database = "kavitha",
        user = "postgres",
        password = "goldcoin",
        port = "5432",
        
    )
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS laborint(id serial primary key, date_and_time TEXT, supplier_name TEXT, supplier_id TEXT, inventory_name TEXT, inv_id TEXT, sup_name TEXT, emp_name TEXT, qty INT, price INT, total INT)''')
    db.commit()
    db.close()





def dbentry(date, supplier_name, supplier_id, inventory_name, inv_id, unit, emp_name, qty, price, total):
    db = psycopg2.connect(
        host = "localhost",
        database = "kavitha",
        user = "postgres",
        password = "goldcoin",
        port = "5432",
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  laborint(date_and_time, supplier_name, supplier_id, inventory_name, inv_id, sup_name, emp_name, qty, price, total) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (date,supplier_name, supplier_id, inventory_name, inv_id, unit, emp_name, qty, price, total))
    db.commit()
    db.close()


def dbupdate(date,supplier_name, supplier_id, inventory_name, inv_id, unit, emp_name, qty, price, total, id):
    db = psycopg2.connect(
        host = "localhost",
        database = "kavitha",
        user = "postgres",
        password = "goldcoin",
        port = "5432",
        
    )
    c = db.cursor()
    c.execute('''UPDATE laborint SET date_and_time = %s, supplier_name= %s, supplier_id= %s, inventory_name= %s, inv_id= %s, sup_name= %s, emp_name= %s, qty= %s, price= %s, total= %s WHERE id = %s''', (date, supplier_name, supplier_id, inventory_name, inv_id, unit, emp_name, qty, price, total, id))
    db.commit()
    db.close()





def dbdelete(id):
    db = psycopg2.connect(
        host = "localhost",
        database = "kavitha",
        user = "postgres",
        password = "goldcoin",
        port = "5432",
        
    )
    c = db.cursor()
    c.execute('''DELETE FROM  laborint WHERE id=''' + id)
    db.commit()
    db.close()




def dbfetch():
    db = psycopg2.connect(
        host = "localhost",
        database = "kavitha",
        user = "postgres",
        password = "goldcoin",
        port = "5432",
        
    )
    c = db.cursor()
    c.execute('''SELECT * FROM public.laborint''')
    return c
    