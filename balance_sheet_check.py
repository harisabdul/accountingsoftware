

import inventory_purchase_database
import labour_purchase_database
import supplier_settlement_database

import test3
import reciept_database



def get_payables():
    
    purchase = []
    paid = []
    
    data = inventory_purchase_database.dbfetch()
    data1 = labour_purchase_database.dbfetch()
    data2 = supplier_settlement_database.dbfetch()
    
    for i in data:
        purchase.append(i[9])
        
    for i in data1:
        purchase.append(i[10])
    
    for i in data2:
        paid.append(i[5])
        
    
    total_purcahse = 0
    total_paid = 0
    
    for i in purchase:
        total_purcahse += i
        
    for i in paid:
        total_paid += i
        
    
    payables = total_purcahse - total_paid
    
    return payables
    

    
    
        
def get_recievables():
    
    estimate = []
    total_estimate = 0
    
    reciept = []
    total_reciept = 0
    
    
        
    data = test3.dbfetch()
    data1 = reciept_database.dbfetch()
    
    for i in data:
        estimate.append(i[6])
    
    for i in estimate:
        total_estimate += i
    
    for i in data1:
        reciept.append(i[6])
    
    for i in reciept:
        total_reciept += i
    
    recievables = total_estimate - total_reciept
    
    return recievables