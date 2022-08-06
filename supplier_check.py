import inventory_purchase_database
import labour_purchase_database
import supplier_settlement_database



def get_purchase(supplier_name):
    date = []
    purchase = []
    
    data = inventory_purchase_database.dbfetch()
    
    for i in data:
        if supplier_name in i[4]:
            date.append(i[1])
            purchase.append(i[9])
    
    
    data1 = labour_purchase_database.dbfetch()
    
    for i in data1:
        if supplier_name in i[4]:
            date.append(i[1])
            purchase.append(i[10])
    
    
    return date, purchase


def get_settlement(supplier_name):
    date = []
    payment = []
    
    data = supplier_settlement_database.dbfetch()
    
    for i in data:
        if supplier_name in i[2]:
            date.append(i[1])
            payment.append(i[5])
        
        
    return date, payment
        