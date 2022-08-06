

from logging import PlaceHolder
from tkinter import *
from tkinter import ttk
import datetime
from turtle import width


import inventory_purchase_database
import test3

import databaseinv

import construction_cost_database
import labor_allocation_database
import work_database
import interior_designing_labor_database
import reciept_database
import payment_database
import paymentposdb
import inventory_purchase_database
import labour_purchase_database
import empdatabase


date_and_time = datetime.date.today()
date1 = str(date_and_time)




def paymentfn(x, lbl):
    
    
    global my_tree1
    
    label1 = lbl(x, text="Cash Payment")
    label1.grid(column=0, row=0)
    
    label2 = lbl(x, text="Inventory")
    label2.grid(column=2, row=0)

    # add some style
    style = ttk.Style()


    # pick a theme
    style.theme_use('default')


    # configure the treeview colors
    style.configure("Treeview", background="black", foreground="white", rowheight=25, fieldbackground="grey")

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
    my_tree1['columns'] = ("id","date_and_time","customer_name", "customer_id", "supplier_name","supplier_id","employee_name","employee_id", "work_name", "work_id", "amount", "outstanding", "balance", "catogory", "pos")

    # format our columns
    my_tree1.column("#0", width=0, stretch=NO)
    my_tree1.column("id", anchor=CENTER, width=50)
    my_tree1.column("date_and_time", anchor=W, width=150)
    my_tree1.column("customer_name", anchor=W, width=150)
    my_tree1.column("customer_id", anchor=CENTER, width=50)
    my_tree1.column("supplier_name", anchor=W, width=150)
    my_tree1.column("supplier_id", anchor=CENTER, width=50)
    my_tree1.column("employee_name", anchor=W, width=160)
    my_tree1.column("employee_id", anchor=CENTER, width=50 )
    my_tree1.column("work_name", anchor=W, width=160)
    my_tree1.column("work_id", anchor=CENTER, width=50 )
    my_tree1.column("amount", anchor=CENTER, width=50)
    my_tree1.column("outstanding", anchor=CENTER, width=100)
    my_tree1.column("balance", anchor=CENTER, width=50)
    my_tree1.column("catogory", anchor=CENTER, width=50)
    my_tree1.column("pos", anchor=CENTER, width=50)
    

    # create Headings
    my_tree1.heading("#0", text="", anchor=W)
    my_tree1.heading("id", text="ID", anchor=CENTER)
    my_tree1.heading("date_and_time", text="Date", anchor=W)
    my_tree1.heading("customer_name", text="Customer Name", anchor=W)
    my_tree1.heading("customer_id", text="Customer ID")
    my_tree1.heading("supplier_name", text="Supplier Name", anchor=W)
    my_tree1.heading("supplier_id", text="Supplier ID")
    my_tree1.heading("employee_name", text="Employee Name", anchor=W)
    my_tree1.heading("employee_id", text="Employee ID", anchor=CENTER)
    my_tree1.heading("work_name", text="Work Name", anchor=W)
    my_tree1.heading("work_id", text="Work ID", anchor=CENTER)
    my_tree1.heading("amount", text="Amount", anchor=CENTER)
    my_tree1.heading("outstanding", text="Oustanding", anchor=CENTER)
    my_tree1.heading("balance", text="Balance", anchor=CENTER)
    my_tree1.heading("catogory", text="Catogory", anchor=CENTER)
    my_tree1.heading("pos", text="POS data", anchor=CENTER)
   
    # create striped row tags

    # create striped row tags
    my_tree1.tag_configure('oddrow', background="white", foreground="darkgreen")
    my_tree1.tag_configure('evenrow', background="white", foreground="darkblue")


inv = []

exp = []





foregnkeyid = []
ttl1 = 0
counter = 0    
def addinginv():
    global inv
    global ttl1
    global counter
    ttl = int(inv_amt_entry.get()) * int(inv_count_entry.get())
    inv_tree.insert(parent="", index='end', iid = counter, text="", values=(inv_entry.get(), inv_count_entry.get(), inv_amt_entry.get(), ttl))
    inv.append(inv_entry.get() + ' ' + str(inv_count_entry.get()) + ' ' + str(inv_amt_entry.get()) + ' ' + str(ttl))
    
    counter += 1
    ttl1 = ttl1 + ttl
    
   
    
    
    # paymentposdb.dbentry(inv_entry.get(), inv_count_entry.get(), inv_amt_entry.get(), ttl)
    # f1 = paymentposdb.dbfetch()
    # for i in f1:
    #     foregnkeyid.append(i[0])
    inv_entry.delete(0, END)
    inv_count_entry.delete(0, END)
    inv_amt_entry.delete(0, END)
    
    
   
def addingexp():
    global exp
    global ttl1
    global counter
    ttl = int(exp_amt_entry.get()) * int(exp_count_entry.get())
    inv_tree.insert(parent="", index='end', iid = counter, text="", values=(exp_entry.get(), exp_count_entry.get(), exp_amt_entry.get(), ttl))
    counter += 1
    
    exp.append(exp_entry.get() + " " + str(exp_count_entry.get()) + " " + str(exp_amt_entry.get()) + " " + str(ttl))
    # paymentposdb.dbentry(exp_entry.get(), exp_count_entry.get(), exp_amt_entry.get(), ttl)
    # f1 = paymentposdb.dbfetch()
    # for i in f1:
    #     foregnkeyid.append(i[0])
    
    ttl1 = ttl1 + ttl
    
      
        
     
    exp_entry.delete(0, END)
    exp_count_entry.delete(0, END)
    exp_amt_entry.delete(0, END)
    
def addingsup():
    global counter
    inv_tree.insert(parent="", index='end', iid = counter, text="", values=(supplier_name_entry.get(), supplier_id_entry.get(), None, None))
    counter += 1
    
def addingwork():
    global counter
    inv_tree.insert(parent="", index='end', iid = counter, text="", values=(work_name_entry.get(), work_id_entry.get(), None, None))
    counter += 1
    
    
def addingcus():
    global counter
    inv_tree.insert(parent="", index='end', iid = counter, text="", values=(customer_name_entry.get(), customer_id_entry.get(), None, None))
    counter += 1

# def enteramt(e):
    
    
    
    
def paymentfn1(lbl, ent, btn, b, x, cb):
    global inv_amt_entry
    global inv_count_entry
    global inv_tree
    global inv_entry
    
    global work_name_entry
    global work_id_entry
    
    global supplier_name_entry
    global supplier_id_entry
    
    global amount_entry
    
    global exp_amt_entry
    global exp_count_entry
    global exp_entry
    
    global customer_name_entry
    global customer_id_entry
    
    def datetoday():
        date2 = datetime.date.today()
        date3 = str(date2)
        dateentry.insert(0, date3)
    
    
    
    
    
    tree_frame2 = Frame(x)
    tree_frame2.grid(padx=10, pady=10, row=1, column=1, rowspan=11)


    # create scroll bar
    tree_scroll1 = Scrollbar(tree_frame2)
    tree_scroll1.pack(side=RIGHT, fill=Y)


    # create the treeview
    inv_tree = ttk.Treeview(tree_frame2, yscrollcommand=tree_scroll1.set, selectmode="extended")
    inv_tree.pack()



    # configure the scroll bar
    tree_scroll1.config(command=inv_tree.yview)




    date_label = lbl(b,
                                              text="Execute Above Mentioned Details Here ------------>",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_label.grid(row=11, column=0,)
    
    date_label = lbl(b,
                                              text="Select the exact item from the list -------->",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_label.grid(row=13, column=0,)
    dateentry = ent(b,
                                             width=10,
                                             placeholder_text="Date")
    dateentry.grid(row=12, column=0, columnspan=1, pady=0, padx=20, sticky="we")
    
    
    datetoday()
    

    # def set_time():
    #     dateentry.delete(0, END)
    #     dateentry.insert(0, date1)
    # timebtn = Button(x, text="Today", command=set_time, background="darkgrey", foreground="blue")
    # timebtn.grid(row=0, column=2)
    # date_inst = lbl(b,
    #                                           text="Date",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # date_inst.grid(row=6, column=0)



    # date_entry = ent(b,
    #                                          width=10,
    #                                          placeholder_text="Date")
    # date_entry.grid(row=6, column=1, columnspan=1, pady=20, padx=20, sticky="we")
    
    inv_entrylbl = lbl(b, text="Inventory",
                                             width=10,)
    
    inv_entrylbl.grid(row=4, column=0, columnspan=1, pady=2, padx=20, sticky="we")

    inv_entry = ent(b, placeholder_text="Inventory",
                                             width=10,)
    
    inv_entry.grid(row=4, column=1, columnspan=1, pady=2, padx=20, sticky="we")
    
    inv_count_entry = ent(b, placeholder_text="Quantity")
    inv_count_entry.grid(row = 4, column = 2, )
    
    inv_amtlbl = lbl(b, text="Amount",
                                             width=10,)
    
    inv_amtlbl.grid(row=4, column=3, columnspan=1, pady=2, padx=20, sticky="we")
    
    inv_amt_entry = ent(b)
    inv_amt_entry.grid(row = 4, column = 4, )
    
    
    
    
    
    
    
    exp_entrylbl = lbl(b, text="Expense",
                                             width=10,)
    
    exp_entrylbl.grid(row=5, column=0, columnspan=1, pady=2, padx=20, sticky="we")

    exp_entry = ent(b, placeholder_text="Expense",
                                             width=10,)
    
    exp_entry.grid(row=5, column=1, columnspan=1, pady=2, padx=20, sticky="we")
    
    
    exp_count_entry = ent(b, placeholder_text="Quantity")
    
    exp_count_entry.grid(row=5, column=2, columnspan=1, pady=2, padx=20, sticky="we")
    
    
    exp_amtlbl = lbl(b, text="Amount",
                                             width=10,)
    
    exp_amtlbl.grid(row=5, column=3, columnspan=1, pady=2, padx=20, sticky="we")
    
    exp_amt_entry = ent(b)
    exp_amt_entry.grid(row = 5, column = 4, )
    
    
    
    
    
    
    
    
    inv_tree['columns'] = ("name", "qty/id", "price", "total")    
    
    
    inv_tree.column("#0", width=1)
    inv_tree.column("name", width=150)
    inv_tree.column("qty/id", width=50)
    inv_tree.column("price", width=100)
    inv_tree.column("total", width=100)
    
    inv_tree.heading("#0")
    inv_tree.heading("name", text="Name")
    inv_tree.heading("qty/id", text="Quantity")
    inv_tree.heading("price", text="Price")
    inv_tree.heading("total", text="Total")


    
    
    inv_button = btn(b,
                                                 text="Add inventory",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=addinginv)
    inv_button.grid(row=4, column=5, padx=10)
    
    
    
    
    
    
    exp_button = btn(b,
                                                 text="Add Expense",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=addingexp)
    exp_button.grid(row=5, column=5, padx=10)
    
    
    
    # inv_listbox = Listbox(b)
    # inv_tree.grid(row=1, column=1, padx=10, pady=10, columnspan=2, rowspan=2)
    






    # name_label = lbl(b,
    #                                           text="Customer Name",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # name_label.grid(row=5, column=0, padx=10, )
    
    sup_entrylbl = lbl(b, text="Supplier",
                                             width=10,)
    
    sup_entrylbl.grid(row=6, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    supplier_name_entry = ent(b,
                                             width=10,
                                             placeholder_text="Supplier Name")
    supplier_name_entry.grid(row=6, column=1, columnspan=1, pady=2, padx=20, sticky="we")
    
    supplier_id_entry = ent(b,
                                             width=10,
                                             placeholder_text="Supplier ID")
    supplier_id_entry.grid(row=6, column=2, columnspan=1, pady=2, padx=20, sticky="we")
    
    
    # supplier_button = btn(b,
    #                                              text="Add Supplier",
    #                                              border_width=2,  # <- custom border_width
    #                                              fg_color=None,  # <- no fg_color
    #                                              command=addingsup)
    # supplier_button.grid(row=5, column=5, padx=10)
    
    
    
    
    cus_entrylbl = lbl(b, text="Customer",
                                             width=10,)
    
    cus_entrylbl.grid(row=3, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    customer_name_entry = ent(b,
                                             width=10,
                                             placeholder_text="Customer Name")
    customer_name_entry.grid(row=3, column=1, columnspan=1, pady=2, padx=20, sticky="we")
    
    customer_id_entry = ent(b,
                                             width=10,
                                             placeholder_text="Customer ID")
    customer_id_entry.grid(row=3, column=2, columnspan=1, pady=2, padx=20, sticky="we")
    
    
    # customer_button = btn(b,
    #                                              text="Add Customer",
    #                                              border_width=2,  # <- custom border_width
    #                                              fg_color=None,  # <- no fg_color
    #                                              command=addingcus)
    # customer_button.grid(row=6, column=5, padx=10)
    
    # worklist = []
    
    # fetchwork = work_database.dbfetchexp()
    
    # for i in fetchwork:
    #     worklist.append(i[1])
    emp_entrylbl = lbl(b, text="Employee",
                                             width=10,)
    
    emp_entrylbl.grid(row=7, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    employee_name_entry = ent(b,
                                             width=10,
                                             placeholder_text="Employee Name")
    employee_name_entry.grid(row=7, column=1, columnspan=1, pady=2, padx=20, sticky="we")
    
    employee_id_entry = ent(b,
                                             width=10,
                                             placeholder_text="Employee ID")
    employee_id_entry.grid(row=7, column=2, columnspan=1, pady=2, padx=20, sticky="we")
    
    
    # employee_button = btn(b,
    #                                              text="Employee Customer",
    #                                              border_width=2,  # <- custom border_width
    #                                              fg_color=None,  # <- no fg_color
    #                                              command=addingcus)
    # employee_button.grid(row=7, column=5, padx=10)
    
    # optionmenu_3 = opt(b,
    #                                                         values=worklist)
    # optionmenu_3.grid(row=5, column=0, pady=10, padx=20, sticky="w")
    
    work_entrylbl = lbl(b, text="Work",
                                             width=10,)
    
    work_entrylbl.grid(row=8, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    work_name_entry = ent(b,
                                             width=10,
                                             placeholder_text="Work Name")
    work_name_entry.grid(row=8, column=1, columnspan=1, pady=2, padx=20, sticky="we")
    


    # address_label = lbl(b,
    #                                           text="Address",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # address_label.grid(row=6, column=0, padx=10, )
    
    
    work_id_entry = ent(b,
                                             width=10,
                                             placeholder_text="Work ID")
    work_id_entry.grid(row=8, column=2, columnspan=1, pady=2, padx=20, sticky="we")
    
    
    # work_button = btn(b,
    #                                              text="Add work",
    #                                              border_width=2,  # <- custom border_width
    #                                              fg_color=None,  # <- no fg_color
    #                                              command=addingwork)
    # work_button.grid(row=8, column=5, padx=10)
    


    # phone_label = lbl(b,
    #                                           text="Phone",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # phone_label.grid(row=4, column=2, padx=10, )
    amount_entry =ent(b,
                                             width=10,
                                             placeholder_text="Amount")
    amount_entry.grid(row=9, column=1, columnspan=1, pady=2, padx=20, sticky="we")
    
    # outstanding_entry =ent(b,
    #                                          width=10,
    #                                          placeholder_text="Outstanding")
    # outstanding_entry.grid(row=9, column=2, columnspan=1, pady=2, padx=20, sticky="we")
    
    
    


    # # pincode_label = lbl(b,
    # #                                           text="Pincode",
    # #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # # pincode_label.grid(row=4, column=4, padx=10, )
    # balance_entry = ent(b,
    #                                          width=10,
    #                                          placeholder_text="balance")
    # balance_entry.grid(row=9, column=3, columnspan=1, pady=2, padx=20, sticky="we")

    # estimate_label = lbl(b,
    #                                           text="Estimate Amount",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # estimate_label.grid(row=5, column=2, padx=10, )
 
    # info_label = customtkinter.CTkLabel(b,
    #                                           text="Date",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # info_label.grid(row=4, column=2)
    # # mylb = Listbox(x, width=90, background="darkgrey", height=8)
    # # mylb.grid(row=5, column=0, columnspan=5, rowspan=4)
    

    # functions

    payment_database.dbconnect()

    class Reciept_handling:
        try:
            def select_record(self, e):
                # clear box
                dateentry.delete(0, END)
                supplier_name_entry.delete(0, END)
                supplier_id_entry.delete(0, END)
                work_name_entry.delete(0, END)
                work_id_entry.delete(0, END)
                amount_entry.delete(0, END)
                # outstanding_entry.delete(0, END)
                # balance_entry.delete(0, END)
                
                
                # Grab record number
                selected = my_tree1.focus()
                values = my_tree1.item(selected, "values")
                
                #output entrybox
                try:
                    dateentry.insert(0, values[1])
                    customer_name_entry.insert(0, values[2])
                    customer_id_entry.insert(0, values[3])
                    supplier_name_entry.insert(0, values[4])
                    supplier_id_entry.insert(0, values[5])
                    employee_name_entry.insert(0, values[6])
                    employee_id_entry.insert(0, values[7])
                    work_name_entry.insert(0, values[8])
                    work_id_entry.insert(0, values[9])
                    amount_entry.insert(0, values[10])
                    # outstanding_entry.insert(0, values[11])
                    # balance_entry.insert(0, values[12])
                except:
                    pass
                
                
        except:
            pass
                #output listbox
                
                # mylb.delete(0, END)
                # mylb.insert(0, f"Customer Details {values}")
                # mylb.insert(1, values[2])
                # mylb.insert(2, values[3])
            

        def clearentrybox(self):
            # clear box
            
            dateentry.delete(0, END)
            supplier_name_entry.delete(0, END)
            supplier_id_entry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            employee_name_entry.delete(0, END)
            employee_id_entry.delete(0, END)
            work_name_entry.delete(0, END)
            work_id_entry.delete(0, END)
            amount_entry.delete(0, END)
            # outstanding_entry.delete(0, END)
            # balance_entry.delete(0, END)
            
            
            # mylb.delete(0,END)
            datetoday()
        
        
        def entering(self):
            global inv
            global exp
            
            # mylb.delete(0, END)
            posdata = str(inv) + str(exp)
            
            payment_database.dbentry(dateentry.get(), customer_name_entry.get(), customer_id_entry.get(), supplier_name_entry.get(), supplier_id_entry.get(), employee_name_entry.get(), employee_id_entry.get(), work_name_entry.get(), work_id_entry.get(), amount_entry.get(), 0, 0, combobox_2.get(), posdata )
            # mylb.insert(0, "New Data into the Database created")
            inv = []
            exp = []
            
            inv_tree.delete(*inv_tree.get_children())
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            supplier_name_entry.delete(0, END)
            supplier_id_entry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            employee_name_entry.delete(0, END)
            employee_id_entry.delete(0, END)
            work_name_entry.delete(0, END)
            work_id_entry.delete(0, END)
            amount_entry.delete(0, END)
            # outstanding_entry.delete(0, END)
            # balance_entry.delete(0, END)
            # # except:
            #     mylb.insert(0, "Boxes Cannot be Blank")
            
            
            
            
            datetoday()
        
        
        def deleting(self):
            
            selected = my_tree1.focus()
            values = my_tree1.item(selected, "values")
            payment_database.dbdelete(values[0])
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            supplier_name_entry.delete(0, END)
            supplier_id_entry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            employee_name_entry.delete(0, END)
            employee_id_entry.delete(0, END)
            work_name_entry.delete(0, END)
            work_id_entry.delete(0, END)
            amount_entry.delete(0, END)
            # outstanding_entry.delete(0, END)
            # balance_entry.delete(0, END)
            # mylb.delete(0, END)
            # mylb.insert(0, "One item is delted from database")
            datetoday()
        
        # def updating(self):
        #     selected = my_tree1.focus()
        #     values = my_tree1.item(selected, "values")
        
        #     payment_database.dbupdate(dateentry.get(),customer_name_entry.get(), customer_id_entry.get(), supplier_name_entry.get(),supplier_id_entry.get(), employee_name_entry.get(), employee_id_entry.get(), work_name_entry.get(), work_id_entry.get(), amount_entry.get(), outstanding_entry.get(), balance_entry.get(), combobox_2.get(), values[0])
            
        #     my_tree1.delete(*my_tree1.get_children())
            
        #     record1.fetching()
            
        #     dateentry.delete(0, END)
        #     supplier_name_entry.delete(0, END)
        #     supplier_id_entry.delete(0, END)
        #     work_name_entry.delete(0, END)
        #     work_id_entry.delete(0, END)
        #     amount_entry.delete(0, END)
        #     outstanding_entry.delete(0, END)
        #     balance_entry.delete(0, END)
            
        #     # mylb.delete(0, END)
        #     # mylb.insert(0, "One item is updated from database")
        #     datetoday()
        
        def fetching(self):
            data = payment_database.dbfetch()
            # mylb.delete(0, END)
            # mylb.insert(0, "Fetched data from database to the table")
            
            count = 0
            
            
            for i in data:
                
                if count % 2 == 0:
                    my_tree1.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14]), tags=("evenrow",))
                    
                else:
                    my_tree1.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14]), tags=("oddrow",))
                
                # increment counter
                count += 1
            
            
            
        
    record1 = Reciept_handling()
    # bind
    my_tree1.bind("<ButtonRelease-1>", record1.select_record)

    # buttons

    add_button = btn(b,
                                                 text="Add",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.entering)
    add_button.grid(row=11, column=2, padx=10)

    # del_button = btn(b,
    #                                              text="Remove",
    #                                              border_width=2,  # <- custom border_width
    #                                              fg_color=None,  # <- no fg_color
    #                                              command=record1.deleting)
    # del_button.grid(row=11, column=3, padx=10)
    
    
    def btndiable(combobox="Remove Disable"):
            
    
        if combobox == "Remove Disable":
            del_button = btn(b,
                                                    text="Remove",
                                                    border_width=2,  # <- custom border_width
                                                    fg_color=None,  # <- no fg_color
                                                    command=record1.deleting)
            del_button.grid(row=11, column=3, padx=10)
            del_button.configure(state="disabled", text="Disabled Remove Btn")
        elif combobox == "Remove Enable":
            del_button = btn(b,
                                                    text="Remove",
                                                    border_width=2,  # <- custom border_width
                                                    fg_color=None,  # <- no fg_color
                                                    command=record1.deleting)
            del_button.grid(row=11, column=3, padx=10)
    
    
    btndiable()
    def selection():
        combobox_1 = cb(b,
                                                        values=["Remove Disable", "Remove Enable"],
                                                        command = btndiable)
        combobox_1.grid(row=12, column=3, columnspan=1, pady=10, padx=20, sticky="we")
    
    combobox_2 = cb(b,
                                                        values=["Construction", "Interior Designing"],)
    combobox_2.grid(row=12, column=4, columnspan=1, pady=10, padx=20, sticky="we")
    
            
    selection()
    
    
    
    
    
    
    
    

    # update_button = btn(b,
    #                                              text="Update",
    #                                              border_width=2,  # <- custom border_width
    #                                              fg_color=None,  # <- no fg_color
    #                                              command=record1.updating)
    # update_button.grid(row=11, column=4, padx=10)
    
    # update_button.configure(state="disabled", text="Disabled Remove Btn")

    # show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
    # show_button.grid(row=5, column=5, padx=10)

    record1.fetching()

    clear_button = btn(master=b,
                                                 text="Clear Boxes",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.clearentrybox)
    clear_button.grid(row=11, column=5, padx=10)




    # balance_label = Label(data_frame, text="Balance", background="lightgrey")
    # balance_label.grid(row=4, column=0, padx=10, )
    # balance_entry = Entry(data_frame)
    # balance_entry.grid(row=1, column=3, padx=10, )
    # #####################################################################################################################################


    ########################################################################################################
    #######################################################################################################
    # #########################################################################################################3

    def updatelb(data):
        lb15.delete(0, END)
        for item in data:
            lb15.insert(END, item)

    def fillout(e):
        li14 = test3.dbfetchsup()
        

        
        supplier_name_entry.delete(0, END)
        supplier_id_entry.delete(0, END)
        
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li14:
            if lb15.get(ANCHOR) in i:
                supplier_name_entry.insert(0, i[2])
                supplier_id_entry.insert(0, i[0])
               
        
        
        # lb15.delete(0, END)

        
    def check(e):
        
       
        
        
        li14 = test3.dbfetchsup()
        li15 = []

        for i in li14:
            
            li15.append(i[2])
            
            
        typed = supplier_name_entry.get()
        if typed == '':
            data = li15
        else:
            data = []
            for item in li15:
                if typed.lower() in item.lower():
                    data.append(item)
        updatelb(data)
        
        

        
        
        
        

    

    


    lb15 = Listbox(b)
    lb15.grid(row=11, column=1, rowspan=3, padx=20, pady=5)


    # updatelb(li15)



    lb15.bind("<<ListboxSelect>>", fillout)

    supplier_name_entry.bind("<KeyRelease>", check)
    
    
    
    
    
    ##########################################################################
    
    def updatelb1(data):
        lb16.delete(0, END)
        for item in data:
            lb16.insert(END, item)

    def fillout1(e):
        li14 = work_database.dbfetchexp()
        

        exp_amt_entry.delete(0, END)
        work_name_entry.delete(0, END)
        work_id_entry.delete(0, END)
       
            
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li14:
            if lb16.get(ANCHOR) in i:
                work_name_entry.insert(0, i[1])
                work_id_entry.insert(0, i[0])
               
          
        
        lb16.delete(0, END)
        
    

            
    def check1(e):
        global lb16
        
        li14 = work_database.dbfetchexp()
        
        lb15.destroy()
        lb16 = Listbox(b)
        lb16.grid(row=11, column=1, rowspan=4, padx=20, pady=5)
        
        li16 = []

        for i in li14:
            
            li16.append(i[1])
            
            
        typed = work_name_entry.get()
        if typed == '':
            data = li16
        else:
            data = []
            for item in li16:
                if typed.lower() in item.lower():
                    data.append(item)
        updatelb1(data)
        lb16.bind("<<ListboxSelect>>", fillout1)
        
        
    work_name_entry.bind("<KeyRelease>", check1)

        
    # ############################################################
    
    def updatelb2(data):
            lb17.delete(0, END)
            for item in data:
                lb17.insert(END, item)

    def fillout2(e):
        li14 = test3.dbfetchsup()
        

        
        supplier_name_entry.delete(0, END)
       
            
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li14:
            if lb17.get(ANCHOR) in i:
                supplier_name_entry.insert(0, i[2])
                supplier_id_entry.insert(0, i[0])
              
               
          
        
        lb17.delete(0, END)
        
    

            
    def check2(e):
        global lb17
        amount_entry.delete(0, END)
        amount_entry.insert(0, ttl1)
        
        
        
        # print(type(inv))
        # print(inv)
        
       
        
        li14 = test3.dbfetchsup()
        
        lb15.destroy()
        lb17 = Listbox(b)
        lb17.grid(row=11, column=1, rowspan=4, padx=20, pady=5)
        
        li16 = []

        for i in li14:
            
            li16.append(i[2])
            
            
        typed = supplier_name_entry.get()
        if typed == '':
            data = li16
        else:
            data = []
            for item in li16:
                if typed.lower() in item.lower():
                    data.append(item)
        updatelb2(data)
        lb17.bind("<<ListboxSelect>>", fillout2)
        
       
    
    
    ############################################################
    
    
    def updatelb3(data):
            lb18.delete(0, END)
            for item in data:
                lb18.insert(END, item)

    def fillout3(e):
        li14 = test3.dbfetch()
        

        
        customer_name_entry.delete(0, END)
        customer_id_entry.delete(0, END)
       
            
    
        
        
        # customer_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li14:
            if lb18.get(ANCHOR) in i:
                customer_name_entry.insert(0, i[2])
                customer_id_entry.insert(0, i[0])
          
        try:
            lb17.delete(0, END)
        except:
            pass
    

            
    def check3(e):
        global lb18
        
        li14 = test3.dbfetch()
        
        # lb17.destroy()
        lb18 = Listbox(b)
        lb18.grid(row=11, column=1, rowspan=4, padx=20, pady=5)
        
        li16 = []

        for i in li14:
            
            li16.append(i[2])
            
            
        typed = customer_name_entry.get()
        if typed == '':
            data = li16
        else:
            data = []
            for item in li16:
                if typed.lower() in item.lower():
                    data.append(item)
        updatelb3(data)
        lb18.bind("<<ListboxSelect>>", fillout3)
    
        
        
    ###############################################################


       


        # updatelb(li15)



    

    work_name_entry.bind("<KeyRelease>", check1)
    
    supplier_name_entry.bind("<KeyRelease>", check2)
    
    customer_name_entry.bind("<KeyRelease>", check3)
    
    
    
    
    # def qtyentry(e):
    #     balance_entry.delete(0, END)
        
    #     balance = int(estimate_entry.get()) - int(amount_entry.get())
        
    #     balance_entry.insert(0, balance)
        
    #     try:
    #         lb15.delete(0, END)
    #         lb16.delete(0, END)
    #     except:
    #         pass
                
        
        
    
    # amount_entry.bind("<KeyRelease>", qtyentry)
    
    
    
    def updatelb5(data):
            lb25.delete(0, END)
            for item in data:
                lb25.insert(END, item)

    def fillout5(e):
        li14 = databaseinv.dbfetchinv()
        

        
        inv_entry.delete(0, END)
        inv_amt_entry.delete(0, END)
      
       
            
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li14:
            if lb25.get(ANCHOR) in i:
                inv_entry.insert(0, i[1])
                inv_amt_entry.insert(0, i[3])
             
               
               
          
        
        lb25.delete(0, END)
        
    

            
    def check5(e):
        global lb25
        
        li14 = databaseinv.dbfetchinv()
        
        lb15.destroy()
        lb25 = Listbox(b)
        lb25.grid(row=11, column=1, rowspan=4, padx=20, pady=5)
        
        li16 = []

        for i in li14:
            
            li16.append(i[1])
            
            
        typed = inv_entry.get()
        if typed == '':
            data = li16
        else:
            data = []
            for item in li16:
                if typed.lower() in item.lower():
                    data.append(item)
        updatelb5(data)
        lb25.bind("<<ListboxSelect>>", fillout5)
        
        
    inv_entry.bind("<KeyRelease>", check5)












     ##########################################
   
    
    def updatelb6(data):
            lb26.delete(0, END)
            for item in data:
                lb26.insert(END, item)

    def fillout6(e):
        li14 = test3.dbfetchexp()
        

        
        exp_entry.delete(0, END)
    
    
            
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li14:
            if lb26.get(ANCHOR) in i:
                exp_entry.insert(0, i[1])
                
            
            
        
        
        lb26.delete(0, END)
        
    

            
    def check6(e):
        global lb26
        
        li14 = test3.dbfetchexp()
        lb25.destroy()
        

        lb26 = Listbox(b)
        lb26.grid(row=11, column=1, rowspan=4, padx=20, pady=5)
        
        li16 = []

        for i in li14:
            
            li16.append(i[1])
            
            
        typed = exp_entry.get()
        if typed == '':
            data = li16
        else:
            data = []
            for item in li16:
                if typed.lower() in item.lower():
                    data.append(item)
        updatelb6(data)
        lb26.bind("<<ListboxSelect>>", fillout6)
        
        
    exp_entry.bind("<KeyRelease>", check6)
       
            

            
        
        
        #########################################################33
        
    def updatelb7(data):
            lb27.delete(0, END)
            for item in data:
                lb27.insert(END, item)

    def fillout7(e):
        li14 = empdatabase.dbfetchemp()
        

        
        employee_name_entry.delete(0, END)


            

        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li14:
            if lb27.get(ANCHOR) in i:
                employee_name_entry.insert(0, i[2])
                employee_id_entry.insert(0, i[0])
                
            
            
        
        
        lb27.delete(0, END)
        


            
    def check7(e):
        global lb27
        
        li14 = empdatabase.dbfetchemp()
        
        # lb26.destroy()
        lb27 = Listbox(b)
        lb27.grid(row=11, column=1, rowspan=4, padx=20, pady=5)
        
        li16 = []

        for i in li14:
            
            li16.append(i[2])
            
            
            
        typed = employee_name_entry.get()
        if typed == '':
            data = li16
        else:
            data = []
            for item in li16:
                if typed.lower() in item.lower():
                    data.append(item)
        updatelb7(data)
        lb27.bind("<<ListboxSelect>>", fillout7)
        # outstanding_entry.delete(0, END)
        # outs = []
        # totalouts = 0
        # data5 = inventory_purchase_database.dbfetch()
        # for item in data5:
        #     if supplier_name_entry.get() in item[2]:
        #         outs.append(item[9])
        
        # data6 = labour_purchase_database.dbfetch()
        
        # for item in data6:
        #     if supplier_name_entry.get() in item[2]:
        #         outs.append(item[8])
        
        
        # for item in outs:
        #     totalouts = int(totalouts) + int(item)
        
        
        # outstanding_entry.insert(0, totalouts)
        
        # bala = totalouts - int(ttl1)
        # balance_entry.delete(0, END)
        # balance_entry.insert(0, bala)
            
    employee_name_entry.bind("<KeyRelease>", check7)
    