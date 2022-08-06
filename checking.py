import test3
import reciept_database
import payment_database
import construction_cost_database
import labour_purchase_database
import inventory_purchase_database
import supplier_settlement_database
import labor_allocation_database
import expdatabase


def estimatecollection(customer_name):
    estimate = 0
    date = ''
    
    data = test3.dbfetch()
    for i in data:
        if customer_name in i[2]:
            estimate = i[6]
            date = i[1]
    
    return estimate, date


def reciept_collection(customer_name):
    date = []
    reciept = []
    employee = []
    
    data = reciept_database.dbfetch()
    for i in data:
        if customer_name in i[2]:
            date.append(i[1])
            reciept.append(i[6])
            employee.append(i[4])
    
    return date, reciept, employee


def payment_collection(customer_name):
    date = []
    payment = []
    employee = []
    work = []
    
    data = payment_database.dbfetch()
    for i in data:
        if customer_name in i[2]:
            date.append(i[1])
            payment.append(i[10])
            employee.append(i[6])
            work.append(i[8])
    
    return date, payment, employee, work


def material_allocation_collection(customer_name):
    date = []
    material_allocation = []
    
    data = construction_cost_database.dbfetch()
    for i in data:
        if customer_name in i[2]:
            date.append(i[1])
            material_allocation.append(i[9])
    
    
    data1 = labor_allocation_database.dbfetch()
    
    for i in data1:
        if customer_name in i[2]:
            date.append(i[1])
            material_allocation.append(i[10])
    
    
    data3 = expdatabase.dbfetch()
    for i in data3:
        if customer_name in i[2]:
            date.append(i[1])
            material_allocation.append(i[6])
            
    return date, material_allocation







def supplier_balance(supplier_name):
    supplier_grand_total = 0
    supplier_paid = []
    supplier_paid_total = 0
    supplier_net_balance = 0
    supplier_total = []
    
    data = inventory_purchase_database.dbfetch()
    for i in data:
        if supplier_name in i[4]:
            supplier_total.append(i[9])
        
    data1 = labour_purchase_database.dbfetch()
    for i in data1:
        if supplier_name in i[4]:
            supplier_total.append(i[10])
    
    
    for i in supplier_total:
        supplier_grand_total += i
        
    data2 = supplier_settlement_database.dbfetch()
    for i in data2:
        if supplier_name in i[2]:
            supplier_paid.append(i[5])
    
    for i in supplier_paid:
        supplier_paid_total += i
        
    
    supplier_net_balance = supplier_grand_total - supplier_paid_total
    
        
    
    return supplier_net_balance
            