import payment_database
import reciept_database





def get_reciept(fromdate, todate):
    
    date = []
    reciept = []
    
    
    data = reciept_database.dbfetch()
    
    for i in data:
        if i[1] >= fromdate and i[1] <= todate:
            date.append(i[1])
            reciept.append(i[6])
    
    
    
    return date, reciept
    
    
def get_payment(fromdate, todate):
    
    date = []
    payment = []
    
    
    data = payment_database.dbfetch()
    
    for i in data:
        if i[1] >= fromdate and i[1] <= todate:
            date.append(i[1])
            payment.append(i[10])
    
    
    return date, payment