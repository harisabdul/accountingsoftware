


from tkinter import *
from tkinter import ttk
import datetime




import inventory_purchase_database
import test3

import databaseinv
import checking

import construction_cost_database
import labor_allocation_database
import work_database
import interior_designing_labor_database
import reciept_database
import payment_database
import paymentposdb
import balance_sheet_check

date_and_time = datetime.date.today()
date1 = str(date_and_time)
import test3
import payment_database
import reciept_database
import income_statement_check
import income_statement
import cashflow_check


     
def searchentry(ent, b, btn, x, lbl):
    
    
    fromdate = ent(b, placeholder_text="From Date",
                                             width=10,)
    
    fromdate.grid(row=3, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    
    todate = ent(b, placeholder_text="To Date",
                                             width=10,)
    
    todate.grid(row=4, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    

    
    todate.insert(0, date_and_time)
    
    long_term_assets_entry = ent(b, placeholder_text="Long Term Assets",
                                             width=10,)
    
    long_term_assets_entry.grid(row=6, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    opening_inv_entry = ent(b, placeholder_text="Opening Inventorys",
                                             width=10,)
    
    opening_inv_entry.grid(row=7, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    opening_cash_entry = ent(b, placeholder_text="Opening Cash Balance",
                                             width=10,)
    
    opening_cash_entry.grid(row=8, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    
    
    
    
    def get_data():
        
        date = todate.get()
        
        label2 = lbl(x, text=f"as at {date}")
        label2.grid(column=0, row=1, columnspan = 2)
        
        
        fixed_asset1 = lbl(x, text=long_term_assets_entry.get())
        fixed_asset1.grid(column=1, row=3)
        
        equity1 = lbl(x, text=long_term_assets_entry.get())
        equity1.grid(column=1, row=11)
        
        
        opening_date = fromdate.get()
        
        purchases = income_statement_check.purchases(opening_date, date)
        
        opening_inv = opening_inv_entry.get()
        
        sold_inv = income_statement_check.sold_inv(opening_date, date)
        
        closing_inv = (int(opening_inv) + int(purchases)) - sold_inv
        
        
        closing_inventory1 = lbl(x, text=closing_inv)
        closing_inventory1.grid(column=1, row=5)
        
        opening_cash = opening_cash_entry.get()
        
        date3, reciept = cashflow_check.get_reciept(opening_date, date)
        date4, payement = cashflow_check.get_payment(opening_date, date)
        
        reciept_total = 0
        payment_total = 0
        
        for i in reciept:
            reciept_total += i
            
        for i in payement:
            payment_total += i
        closing_cash = (int(opening_cash) + reciept_total) - payment_total
        
        cash1 = lbl(x, text=closing_cash)
        cash1.grid(column=1, row=6)
        
        payables = balance_sheet_check.get_payables()
        
        payables1 = lbl(x, text=payables)
        payables1.grid(column=1, row=14)
        
        
        recievables = balance_sheet_check.get_recievables()
        
        recievables1 = lbl(x, text=recievables)
        recievables1.grid(column=1, row=7)
        
        
        asset_total = int(long_term_assets_entry.get()) + closing_inv + closing_cash + recievables
        
        total_assets1 = lbl(x, text=asset_total)
        total_assets1.grid(column=1, row=8, sticky = W)
        
        retained = asset_total - (int(long_term_assets_entry.get()) + payables)
        
        retained_earnings1 = lbl(x, text = retained)
        retained_earnings1.grid(column=1, row=12)
        
        total_liabilities = int(long_term_assets_entry.get()) + retained + payables
        
        total_el1 = lbl(x, text = total_liabilities)
        total_el1.grid(column=1, row=15, sticky = W)
        
        
        
        
        # revenue = income_statement_check.revenue(fromdate.get(), todate.get())
        # Revenue1 = lbl(x, text= revenue)
        # Revenue1.grid(column=1, row=2)
        
        # opening_inventory1 = lbl(x, text=opening_inventory_entry.get())
        # opening_inventory1.grid(column=1, row=3)
        
        # purchases = income_statement_check.purchases(fromdate.get(), todate.get())
        
        # purchases1 = lbl(x, text= purchases)
        # purchases1.grid(column=1, row=4)
        
        # sold_inv = income_statement_check.sold_inv(fromdate.get(), todate.get())
        
        # closing_inv = int(opening_inventory_entry.get()) + int(purchases) - int(sold_inv)
        
        # closing_inventory1 = lbl(x, text=closing_inv)
        # closing_inventory1.grid(column=1, row=5)
        
        # cgs = (int(opening_inventory_entry.get()) + purchases) - closing_inv
        
        # cgs1 = lbl(x, text=cgs)
        # cgs1.grid(column=1, row=6)
        
        # gp = revenue - cgs
        
        # gp1 = lbl(x, text=gp)
        # gp1.grid(column=1, row=7)
        
        
        # inv, labor, exp, payment = income_statement_check.deduction_data(fromdate.get(), todate.get())
    
        # inv_allocation1 = lbl(x, text=inv)
        # inv_allocation1.grid(column=1, row=8)
        
        
        # labor_allocation1 = lbl(x, text=labor)
        # labor_allocation1.grid(column=1, row=9)
        
        
        # exp_allocation1 = lbl(x, text=exp)
        # exp_allocation1.grid(column=1, row=10)
        
        # customer_payment1 = lbl(x, text=payment)
        # customer_payment1.grid(column=1, row=11)
        
        # np = gp - (inv + labor + exp + payment)
        
        # np1 = lbl(x, text=np)
        # np1.grid(column=1, row=12)
            
   
    # data = []
    
    # def getestimate():
        
        
        
        
    #     my_tree1.delete(*my_tree1.get_children())
  
        
    #     estimate, date1 = checking.estimatecollection(customer_name_entry.get())
    #     data.append(date1)
    #     data.append(estimate)
       
    
       
        
    #     count = 0
                
                
                
                
    #     if count == 0:
    #         my_tree1.insert(parent="", index="end", iid=count, text="", values=(date1, estimate), tags=("evenrow",))
            
    #     # else:
    #     #     my_tree1.insert(parent="", index="end", iid=count, text="", values=(date1, estimate), tags=("oddrow",))
        
    #     # increment counter
    #     count = 1
        
    #     date2, reciept = checking.reciept_collection(customer_name_entry.get())
        
    #     for i in range(len(date2)):
    #         my_tree1.insert(parent="", index="end", iid=count, text="", values=(date2[i],'', reciept[i]), tags=("evenrow",))
    #         count += 1
    #     # print(date2)
    #     # print(reciept)
        
        
    #     date3, payment = checking.payment_collection(customer_name_entry.get())
        
    #     for i in range(len(date3)):
    #         my_tree1.insert(parent="", index="end", iid=count, text="", values=(date3[i],'','', payment[i]), tags=("evenrow",))
    #         count += 1
            
            
    #     date4, material_allocation = checking.material_allocation_collection(customer_name_entry.get())
        
    #     for i in range(len(date4)):
    #         my_tree1.insert(parent="", index="end", iid=count, text="", values=(date4[i],'','','', material_allocation[i]), tags=("evenrow",))
    #         count += 1
            
        
    #     total_reciept = 0
        
    #     for i in reciept:
    #         total_reciept += i
    
        
    #     balance = estimate - total_reciept
        
    #     count = count + 1
    #     if balance == 0:
    #         my_tree1.insert(parent="", index="end", iid=count, text="", values=('Balance due','','','', '', "Closed"), tags=("evenrow",))
    #     else:
    #         my_tree1.insert(parent="", index="end", iid=count, text="", values=('Balance due','','','', '', balance), tags=("evenrow",))
        
        
        

    
    
    
    
    submit_button = btn(b,
                                                    text="Submit",
                                                    border_width=2,  # <- custom border_width
                                                    fg_color=None,  # <- no fg_color
                                                    command=get_data
                                                    )
    submit_button.grid(row=9, column=0, padx=10)
    
    
    
    label1 = lbl(x, text="Statement of Financial Position")
    label1.grid(column=0, row=0, columnspan = 2)
    
    
    asset_head = lbl(x, text="ASSETS")
    asset_head.grid(column=0, row=2, sticky = W)
    
    fixed_asset = lbl(x, text="Long Term Assets :")
    fixed_asset.grid(column=0, row=3)
    
    current_asset = lbl(x, text="Current Assets")
    current_asset.grid(column=0, row=4)
    
    
    closing_inventory = lbl(x, text="Closing Inventory :")
    closing_inventory.grid(column=0, row=5)
    
    
    cash = lbl(x, text="Cash Balance :")
    cash.grid(column=0, row=6)
    
    recievables = lbl(x, text="Recievables :")
    recievables.grid(column=0, row=7)
    
    total_assets = lbl(x, text="TOTAL ASSETS")
    total_assets.grid(column=0, row=8, sticky = W)
    
    
    inv_allocation = lbl(x, text="")
    inv_allocation.grid(column=0, row=9)
    
    
    el_head = lbl(x, text="EQUITIES AND LIABILITIES")
    el_head.grid(column=0, row=10, sticky = W)
    
    
    equity = lbl(x, text="Owners Equity :")
    equity.grid(column=0, row=11)
    
    retained_earnings = lbl(x, text="Retained Earnings :")
    retained_earnings.grid(column=0, row=12)
    
    
    liabilities_head = lbl(x, text="LIABILITIES")
    liabilities_head.grid(column=0, row=13, sticky = W)
    
    
    payables = lbl(x, text="Payables :")
    payables.grid(column=0, row=14)
    
    total_el = lbl(x, text="TOTAL EQUITIES AND LIABILITIES")
    total_el.grid(column=0, row=15, sticky = W)
    
    
    
    
    
################################################################################    
    
    
    
    
    
    
    
    

    
   
    
    
    
    
    
    
    
    
    
    # style = ttk.Style()


    # # pick a theme
    # style.theme_use('default')


    # # configure the treeview colors
    # style.configure("Treeview", background="lightblue", foreground="black", rowheight=25, fieldbackground="grey")

    # # change selected color
    # style.map("Treeview", background=[('selected', "green")])

    # # create a treeview
    

    # tree_frame1 = Frame(x)
    # tree_frame1.grid(padx=10, pady=10, row=1, column=0, rowspan=11)


    # # create scroll bar
    # tree_scroll1 = Scrollbar(tree_frame1)
    # tree_scroll1.pack(side=RIGHT, fill=Y)


    # # create the treeview
    # my_tree1 = ttk.Treeview(tree_frame1, yscrollcommand=tree_scroll1.set, selectmode="extended")
    # my_tree1.pack()



    # # configure the scroll bar
    # tree_scroll1.config(command=my_tree1.yview)

    # # define our columns
    # my_tree1['columns'] = ("date_and_time","estimate", "reciept", "payments","spending_allocation","balance")

    # # format our columns
    # my_tree1.column("#0", width=0, stretch=NO)
    # my_tree1.column("date_and_time", anchor=W, width=150)
    # my_tree1.column("estimate", anchor=W, width=150)
    # my_tree1.column("reciept", anchor=W, width=150)
    # my_tree1.column("payments", anchor=W, width=150)
    # my_tree1.column("spending_allocation", anchor=W, width=150)
    # my_tree1.column("balance", anchor=W, width=160)
  
    

    # # create Headings
    # my_tree1.heading("#0", text="", anchor=W)
    # my_tree1.heading("date_and_time", text="Date", anchor=W)
    # my_tree1.heading("estimate", text="Estimate", anchor=W)
    # my_tree1.heading("reciept", text="Reciept", anchor=W)
    # my_tree1.heading("payments", text="Payments", anchor=W)
    # my_tree1.heading("spending_allocation", text="Spending", anchor=W)
    # my_tree1.heading("balance", text="Balance", anchor=W)
   
   
    # # create striped row tags

    # # create striped row tags
    # # my_tree1.tag_configure('oddrow', background="white", foreground="darkgreen")
    # # my_tree1.tag_configure('evenrow', background="white", foreground="darkblue")
    
    
    
    

    
  



    # class Autofill:
        
    #     lb15 = Listbox(b)
    #     lb15.grid(row=4, column=0, rowspan=3, padx=20, pady=5)
        
    #     def updatelb(self,data):
    #         self.lb15.delete(0, END)
    #         for item in data:
    #             self.lb15.insert(END, item)

    #     def fillout(self, e):
    #         li14 = test3.dbfetch()        
    #         customer_name_entry.delete(0, END)
     
    #         # supplier_name_entry.insert(0, lb15.get(ANCHOR))
    #         for i in li14:
    #             if self.lb15.get(ANCHOR) in i:
    #                 customer_name_entry.insert(0, i[2])
                   
    #         self.lb15.delete(0, END)
        

            
    #     def check(self, e):
    #         li14 = test3.dbfetch()
    #         li15 = []
    #         for i in li14:
    #             li15.append(i[2])   
    #         typed = customer_name_entry.get()
    #         if typed == '':
    #             data = li15
    #         else:
    #             data = []
    #             for item in li15:
    #                 if typed.lower() in item.lower():
    #                     data.append(item)
    #         self.updatelb(data)
            
            
        
    

            
            
            
            

        

    # customer = Autofill()
    
    # customer.lb15.bind("<<ListboxSelect>>", customer.fillout)
    # customer_name_entry.bind("<KeyRelease>", customer.check)



    #     # # updatelb(li15)



    #     # lb15.bind("<<ListboxSelect>>", fillout)

    #     # supplier_name_entry.bind("<KeyRelease>", check)
    

      
            
    
        
  