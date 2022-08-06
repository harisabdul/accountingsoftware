import test3
import inventory_purchase_database
import payment_database
import construction_cost_database
import labor_allocation_database
import expdatabase




def revenue(fromdate, todate):
    total_reveue = 0
    revenue = []
    data = test3.dbfetch()
    for i in data:
        if i[1] > fromdate and i[1] < todate:
            revenue.append(i[6])
    for i in revenue:
        total_reveue += i
        
    return total_reveue


def purchases(fromdate, todate):
    total_purchases = 0
    purchases = []
    
    data = inventory_purchase_database.dbfetch()
    for i in data:
        if i[1] > fromdate and i[1] < todate:
            purchases.append(i[9])
        
    
    # data1 = payment_database.dbfetch()
    # for i in data1:
    #     if i[1] > fromdate and i[1] < todate:
    #         purchases.append(i[10])
    
    
    for i in purchases:
        total_purchases += i
        
    return total_purchases


def sold_inv(fromdate, todate):
    total_sold_inv = 0
    sold_inv = []
    
    data = construction_cost_database.dbfetch()
    
    for i in data:
        if i[1] > fromdate and i[1] < todate:
            sold_inv.append(i[9])
        
    for i in sold_inv:
        total_sold_inv += i
    
    
    return total_sold_inv


def deduction_data(fromdate, todate):
    
    total_inv_allocation = 0
    total_labor_allocation = 0
    total_exp_allocation = 0
    total_customer_payment = 0
    
    inventory_allocation = []
    labor_allocation = []
    expense_allocation = []
    customer_payment = []
    
    
    data = construction_cost_database.dbfetch()
    labor = labor_allocation_database.dbfetch()
    expense = expdatabase.dbfetch()
    payment = payment_database.dbfetch()
    
    for i in data:
        if i[1] >= fromdate and i[1] <= todate:
            inventory_allocation.append(i[9])
    
    for i in inventory_allocation:
        total_inv_allocation += i

    
    for i in labor:
        if i[1] >= fromdate and i[1] <= todate:
            labor_allocation.append(i[10])
    
    for i in labor_allocation:
        total_labor_allocation += i
            
    for i in expense:
        if i[1] >= fromdate and i[1] <= todate:
            expense_allocation.append(i[6])
    
    for i in expense_allocation:
        total_exp_allocation += i
            
    for i in payment:
        if i[1] >= fromdate and i[1] <= todate:
            customer_payment.append(i[10])
    
    for i in customer_payment:
        total_customer_payment += i

    
    
    return total_inv_allocation, total_labor_allocation, total_exp_allocation, total_customer_payment