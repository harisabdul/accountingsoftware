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
    c.execute('''CREATE TABLE IF NOT EXISTS construction4(id serial primary key, date_and_time TEXT, customer_name TEXT, address1 TEXT, phone TEXT, pincode TEXT, estimate INT)''')
    db.commit()
    db.close()





def dbentry(date, name, address, phone, pincode, estimate):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  construction4(date_and_time, customer_name, address1, phone, pincode, estimate) VALUES(%s, %s, %s, %s, %s, %s)''', (date, name, address, phone, pincode, estimate))
    db.commit()
    db.close()


def dbupdate(date, customer_name, address, phone, pincode, estimate, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE construction4 SET date_and_time = %s, customer_name = %s, address1 = %s, phone = %s, pincode =%s, estimate = %s WHERE id = %s''', (date, customer_name, address, phone, pincode, estimate, id))
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
    c.execute('''DELETE FROM  construction4 WHERE id=''' + id)
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
    c.execute('''SELECT * FROM public.construction4''')
    return c
    

########################################################################################################################3

# def dbconnect2():
#     db = psycopg2.connect(
#         host = "localhost",
#         database = "kavitha",
#         user = "postgres",
#         password = "goldcoin",
#         port = "5432",
        
#     )
#     c = db.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS receipt(id serial primary key, date_and_time TEXT, customer_fk INT)''')
#     db.commit()
#     db.close()
    
#            estimate INT, received INT, receipt INT, balance INT

# def dbentry2(date, customer_fk):
#     db = psycopg2.connect(
#         host = "localhost",
#         database = "kavitha",
#         user = "postgres",
#         password = "goldcoin",
#         port = "5432",
        
#     )
#     c = db.cursor()
#     c.execute('''INSERT INTO  receipt(date_and_time, customer_fk) VALUES(%s, %s)''', (date, customer_fk))
#     db.commit()
#     db.close()
    


# def dbfetch2():
#     db = psycopg2.connect(
#         host = "localhost",
#         database = "kavitha",
#         user = "postgres",
#         password = "goldcoin",
#         port = "5432",
        
#     )
#     c = db.cursor()
#     c.execute('''SELECT * FROM public.receipt''')
#     return c


# def dbconnect2():
#     db = psycopg2.connect(
#         host = "localhost",
#         database = "kavitha",
#         user = "postgres",
#         password = "goldcoin",
#         port = "5432",
        
#     )
#     c = db.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS reciept2(id serial primary key, date_and_time TEXT, customer_fk INT)''')
#     db.commit()
#     db.close()





# def dbentry2(date, customer_fk):
#     db = psycopg2.connect(
#         host = "localhost",
#         database = "kavitha",
#         user = "postgres",
#         password = "goldcoin",
#         port = "5432",
        
#     )
#     c = db.cursor()
#     c.execute('''INSERT INTO  reciept2(date_and_time, customer_fk) VALUES(%s, %s)''', (date, customer_fk))
#     db.commit()
#     db.close()


# # def dbupdate(date, customer_name, address, phone, pincode, id):
# #     db = psycopg2.connect(
# #         host = "localhost",
# #         database = "kavitha",
# #         user = "postgres",
# #         password = "goldcoin",
# #         port = "5432",
        
# #     )
# #     c = db.cursor()
# #     c.execute('''UPDATE construction2 SET date_and_time = %s, customer_name = %s, address1 = %s, phone = %s, pincode =%s WHERE id = %s''', (date, customer_name, address, phone, pincode, id))
# #     db.commit()
# #     db.close()





# # def dbdelete(id):
# #     db = psycopg2.connect(
# #         host = "localhost",
# #         database = "kavitha",
# #         user = "postgres",
# #         password = "goldcoin",
# #         port = "5432",
        
# #     )
# #     c = db.cursor()
# #     c.execute('''DELETE FROM  construction2 WHERE id=''' + id)
# #     db.commit()
# #     db.close()




# def dbfetch2():
#     db = psycopg2.connect(
#         host = "localhost",
#         database = "kavitha",
#         user = "postgres",
#         password = "goldcoin",
#         port = "5432",
        
#     )
#     c = db.cursor()
#     c.execute('''SELECT * FROM public.reciept2''')
#     return c
    



# Expense handling

def dbconnectexp():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expense1(id serial primary key, expense_name TEXT, discription TEXT)''')
    db.commit()
    db.close()





def dbentryexp(name, discriprion):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  expense1(expense_name, discription) VALUES(%s, %s)''', (name, discriprion))
    db.commit()
    db.close()


def dbupdatexp(expense_name, discription, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE expense1 SET expense_name = %s, discription = %s WHERE id = %s''', (expense_name, discription, id))
    db.commit()
    db.close()





def dbdeleteexp(id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''DELETE FROM  expense1 WHERE id=''' + id)
    db.commit()
    db.close()




def dbfetchexp():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''SELECT * FROM public.expense1''')
    return c
    


##########################################################################################################################################################
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
    c.execute('''CREATE TABLE IF NOT EXISTS employee2(id serial primary key, date_and_time TEXT, employee_name TEXT, address1 TEXT, phone TEXT, pincode TEXT)''')
    db.commit()
    db.close()





def dbentryemp(date, name, address, phone, pincode):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  employee2(date_and_time, employee_name, address1, phone, pincode) VALUES(%s, %s, %s, %s, %s)''', (date, name, address, phone, pincode))
    db.commit()
    db.close()


def dbupdateemp(date, customer_name, address, phone, pincode, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE employee2 SET date_and_time = %s, employee_name = %s, address1 = %s, phone = %s, pincode =%s WHERE id = %s''', (date, customer_name, address, phone, pincode, id))
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
    c.execute('''DELETE FROM  employee2 WHERE id=''' + id)
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
    c.execute('''SELECT * FROM public.employee2''')
    return c
    
    
    
###################################################################################################################
# Reciept handling

def dbconnectreciept():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reciept4(id serial primary key, date1 TEXT, customer_name TEXT, discription TEXT, customer_id TEXT, employee_name TEXT, discription1 TEXT, employee_id TEXT, amount TEXT)''')
    db.commit()
    db.close()





def dbentryreciept(date1, customer_name, discription, customer_id, employee_name, discription1, employee_id, amount):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  reciept4(date1, customer_name, discription, customer_id, employee_name, discription1, employee_id, amount) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)''', (date1, customer_name, discription, customer_id, employee_name, discription1, employee_id, amount))
    db.commit()
    db.close()


def dbupdatereciept(date1, customer_name, discription, customer_id, employee_name, discription1, employee_id, amount, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE reciept4 SET date1 = %s, customer_name = %s, discription = %s, customer_id = %s, employee_name = %s, discription1 = %s, employee_id = %s, amount = %s WHERE id = %s''', (date1, customer_name, discription, customer_id, employee_name, discription1, employee_id, amount, id))
    db.commit()
    db.close()





def dbdeletereciept(id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''DELETE FROM  reciept4 WHERE id=''' + id)
    db.commit()
    db.close()




def dbfetchreciept():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''SELECT * FROM public.reciept4''')
    return c
    


#####################################################################################################3

def dbconnectsup():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS supplier2(id serial primary key, date_and_time TEXT, supplier_name TEXT, address1 TEXT, phone TEXT, pincode TEXT)''')
    db.commit()
    db.close()





def dbentrysup(date, name, address, phone, pincode):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''INSERT INTO  supplier2(date_and_time, supplier_name, address1, phone, pincode) VALUES(%s, %s, %s, %s, %s)''', (date, name, address, phone, pincode))
    db.commit()
    db.close()


def dbupdatesup(date, customer_name, address, phone, pincode, id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''UPDATE supplier2 SET date_and_time = %s, supplier_name = %s, address1 = %s, phone = %s, pincode =%s WHERE id = %s''', (date, customer_name, address, phone, pincode, id))
    db.commit()
    db.close()





def dbdeletesup(id):
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''DELETE FROM  supplier2 WHERE id=''' + id)
    db.commit()
    db.close()




def dbfetchsup():
    db = psycopg2.connect(
        host = "localhost",
        database = dbconinfo.dbname,
        user = "postgres",
        password = "goldcoin",
        port = dbconinfo.portname,
        
    )
    c = db.cursor()
    c.execute('''SELECT * FROM public.supplier2''')
    return c


####################################################################################################