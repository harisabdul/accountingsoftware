

from tkinter import *
from tkinter import ttk
import datetime

import cashflow_check


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


date_and_time = datetime.date.today()
date1 = str(date_and_time)
import test3
import payment_database
import reciept_database


     
def searchentry(ent, b, btn, x, lbl):
    fromdate = ent(b, placeholder_text="From Date",
                                             width=10,)
    
    fromdate.grid(row=3, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    todate = ent(b, placeholder_text="To Date",
                                             width=10,)
    
    todate.grid(row=4, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    format = lbl(b, text = "Date format: yyyy-mm-dd",
                                             width=10,)
    
    format.grid(row=5, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    
    todate.insert(0, date_and_time)
    
    opening_Balance_entry = ent(b, placeholder_text="Opening Balance",
                                             width=10,)
    
    opening_Balance_entry.grid(row=6, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
   
    data = []
    
    def getestimate():
        my_tree1.delete(*my_tree1.get_children())
  
        
        # estimate, date1 = checking.estimatecollection(customer_name_entry.get())
        # data.append(date1)
        # data.append(estimate)
       
    
       
        
        count = 0
                
                
                
                
        if count == 0:
            my_tree1.insert(parent="", index="end", iid=count, text="", values=(fromdate.get(), opening_Balance_entry.get()), tags=("evenrow",))
        
        
        date1, reciept = cashflow_check.get_reciept(fromdate.get(), todate.get())
        date2, payment = cashflow_check.get_payment(fromdate.get(), todate.get())
        
        count = 1
        
        for i in range(len(date1)):
            my_tree1.insert(parent="", index="end", iid=count, text="", values=(date1[i], '', reciept[i]), tags=("evenrow",))
            count += 1
            
        for i in range(len(date2)):
            my_tree1.insert(parent="", index="end", iid=count, text="", values=(date2[i], '', '', payment[i]), tags=("evenrow",))
            count += 1
            
        total_reciept = 0
        total_payment = 0
        for i in reciept:
            total_reciept += i
        
        for i in payment:
            total_payment += i
        
        closing_balance = (int(opening_Balance_entry.get()) + total_reciept) - total_payment
        
        count = count + 1
        
        my_tree1.insert(parent="", index="end", iid=count, text="", values=("Closing Balance", '', '', "", closing_balance), tags=("evenrow",))
        
            
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
                                                    command=getestimate
                                                    )
    submit_button.grid(row=3, column=1, padx=10)
    
    
    
    label1 = lbl(x, text="Cash Flow Statement")
    label1.grid(column=0, row=0)
    
    
    style = ttk.Style()


    # pick a theme
    style.theme_use('default')


    # configure the treeview colors
    style.configure("Treeview", background="lightblue", foreground="black", rowheight=25, fieldbackground="grey")

    # change selected color
    style.map("Treeview", background=[('selected', "green")])

    # create a treeview
    

    tree_frame1 = Frame(x)
    tree_frame1.grid(padx=10, pady=10, row=1, column=0, rowspan=11)


    # create scroll bar
    tree_scroll1 = Scrollbar(tree_frame1)
    tree_scroll1.pack(side=RIGHT, fill=Y)


    # create the treeview
    my_tree1 = ttk.Treeview(tree_frame1, yscrollcommand=tree_scroll1.set, selectmode="extended")
    my_tree1.pack()



    # configure the scroll bar
    tree_scroll1.config(command=my_tree1.yview)

    # define our columns
    my_tree1['columns'] = ("date_and_time","opening_balance", "cash_inflow", "cash_outflow","closing_balance")

    # format our columns
    my_tree1.column("#0", width=0, stretch=NO)
    my_tree1.column("date_and_time", anchor=W, width=150)
    my_tree1.column("opening_balance", anchor=W, width=150)
    my_tree1.column("cash_inflow", anchor=W, width=150)
    my_tree1.column("cash_outflow", anchor=W, width=150)
    my_tree1.column("closing_balance", anchor=W, width=150)
   
  
    

    # create Headings
    my_tree1.heading("#0", text="", anchor=W)
    my_tree1.heading("date_and_time", text="Date", anchor=W)
    my_tree1.heading("opening_balance", text="Opening Balance", anchor=W)
    my_tree1.heading("cash_inflow", text="Cash Inflow", anchor=W)
    my_tree1.heading("cash_outflow", text="Cash Outflow", anchor=W)
    my_tree1.heading("closing_balance", text="Closing Balance", anchor=W)

   
    # create striped row tags

    # create striped row tags
    # my_tree1.tag_configure('oddrow', background="white", foreground="darkgreen")
    # my_tree1.tag_configure('evenrow', background="white", foreground="darkblue")
    
    
    
    

    
  



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
    

      
            
    
        
  
        
        
 