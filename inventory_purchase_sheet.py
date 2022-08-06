
from tkinter import *
from tkinter import ttk
import datetime


import inventory_purchase_database
import test3

import databaseinv
import pos



date_and_time = datetime.date.today()
date1 = str(date_and_time)




def inventory_purchase(x, lbl):
    
    
    global my_tree1
    
    label1 = lbl(x, text="Inventory Purchase Daybook")
    label1.grid(column=0, row=0)

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
    my_tree1['columns'] = ("id","date_and_time", "customer_name", "customer_id", "supplier_name", "supplier_id", "inventory_name", "inventory_id", "unit", "total")

    # format our columns
    my_tree1.column("#0", width=0, stretch=NO)
    my_tree1.column("id", anchor=CENTER, width=50)
    my_tree1.column("date_and_time", anchor=W, width=150)
    my_tree1.column("customer_name", anchor=W, width=150)
    my_tree1.column("customer_id", anchor=W, width=150)
    my_tree1.column("supplier_name", anchor=W, width=150)
    my_tree1.column("supplier_id", anchor=CENTER, width=50)
    my_tree1.column("inventory_name", anchor=W, width=160)
    my_tree1.column("inventory_id", anchor=CENTER, width=50 )
    my_tree1.column("unit", anchor=CENTER, width=50)
    # my_tree1.column("qty", anchor=CENTER, width=50)
    # my_tree1.column("price", anchor=CENTER, width=50)
    my_tree1.column("total", anchor=CENTER, width=50)


    # create Headings
    my_tree1.heading("#0", text="", anchor=W)
    my_tree1.heading("id", text="ID", anchor=CENTER)
    my_tree1.heading("date_and_time", text="Date", anchor=W)
    my_tree1.heading("customer_name", text="Customer Name", anchor=W)
    my_tree1.heading("customer_id", text="Customer ID", anchor=W)
    my_tree1.heading("supplier_name", text="Supplier Name", anchor=W)
    my_tree1.heading("supplier_id", text="Supplier ID")
    my_tree1.heading("inventory_name", text="Inventory Name", anchor=W)
    my_tree1.heading("inventory_id", text="Inventory ID", anchor=CENTER)
    my_tree1.heading("unit", text="Unit", anchor=CENTER)
    # my_tree1.heading("qty", text="Quantity", anchor=CENTER)
    # my_tree1.heading("price", text="Price", anchor=CENTER)
    my_tree1.heading("total", text="Total", anchor=CENTER)
    # create striped row tags

    # create striped row tags
    my_tree1.tag_configure('oddrow', background="white", foreground="darkgreen")
    my_tree1.tag_configure('evenrow', background="white", foreground="darkblue")


# foregnkeyid = []
# inv = []
# ttl1 = 0
counter = 0  

def inventory_purchase1(lbl, ent, btn, b, x):
        
    
    
    def datetoday():
        date2 = datetime.date.today()
        date3 = str(date2)
        dateentry.insert(0, date3)
    
    
    
      
    def addinginv():
        # global inv
        
        global ttl1
        global counter
        ttl1 = 0
        ttl = int(inv_amt_entry.get()) * int(inv_count_entry.get())
        inv_tree.insert(parent="", index='end', iid = counter, text="", values=(inv_entry.get(), inv_count_entry.get(), inv_amt_entry.get(), ttl))
        pos.addinginv(inv_entry.get() + ' ' + str(inv_count_entry.get()) + ' ' + str(inv_amt_entry.get()) + ' ' + str(ttl))
        
        counter += 1
        pos.valueadding(ttl)
        
        lb25.delete(0, END)
        inv_entry.delete(0, END)
        inv_count_entry.delete(0, END)
        inv_amt_entry.delete(0, END)




    date_label = lbl(b,
                                              text="Execute Above Mentioned Details Here ------------>",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_label.grid(row=8, column=0,)
    
    date_label = lbl(b,
                                              text="Select the exact item from the list -------->",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_label.grid(row=9, column=0,)
    dateentry = ent(b,
                                             width=10,
                                             placeholder_text="Date")
    dateentry.grid(row=3, column=0, columnspan=1, pady=0, padx=20, sticky="we")
    
    
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


    # name_label = lbl(b,
    #                                           text="Customer Name",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # name_label.grid(row=5, column=0, padx=10, )
    
    customer_name_entry = ent(b,
                                             width=10,
                                             placeholder_text="Customer Name")
    customer_name_entry.grid(row=4, column=0, columnspan=1, pady=5, padx=20, sticky="we")
    
    customer_id_entry = ent(b,
                                             width=10,
                                             placeholder_text="Customer ID")
    customer_id_entry.grid(row=4, column=1, columnspan=1, pady=5, padx=20, sticky="we")
    
    supplier_name_entry = ent(b,
                                             width=10,
                                             placeholder_text="Supplier Name")
    supplier_name_entry.grid(row=5, column=0, columnspan=1, pady=5, padx=20, sticky="we")
    
    supplier_id_entry = ent(b,
                                             width=10,
                                             placeholder_text="Supplier ID")
    supplier_id_entry.grid(row=5, column=1, columnspan=1, pady=5, padx=20, sticky="we")
    
    
    # inventory_entry = ent(b,
    #                                          width=10,
    #                                          placeholder_text="Inventory Name")
    # inventory_entry.grid(row=6, column=0, columnspan=1, pady=5, padx=20, sticky="we")


    # address_label = lbl(b,
    #                                           text="Address",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # address_label.grid(row=6, column=0, padx=10, )
    # inventory_id_entry = ent(b,
    #                                          width=10,
    #                                          placeholder_text="Inventory_id")
    # inventory_id_entry.grid(row=6, column=1, columnspan=1, pady=5, padx=20, sticky="we")
    
    # inv_entrylbl = lbl(b, text="Inventory",
    #                                          width=10,)
    
    # inv_entrylbl.grid(row=6, column=0, columnspan=1, pady=2, padx=20, sticky="we")

    inv_entry = ent(b, placeholder_text="Inventory",
                                             width=10,)
    
    inv_entry.grid(row=6, column=0, columnspan=1, pady=2, padx=20, sticky="we")
    
    inv_count_entry = ent(b, placeholder_text="Quantity")
    inv_count_entry.grid(row = 6, column = 2, )
    
    inv_amtlbl = lbl(b, text="Amount",
                                             width=10,)
    
    inv_amtlbl.grid(row=6, column=3, columnspan=1, pady=2, padx=20, sticky="we")
    
    inv_amt_entry = ent(b)
    inv_amt_entry.grid(row = 6, column = 4, )
    
       
    
    
    
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
                                                
    inv_button.grid(row=6, column=5, padx=10)
    


    # phone_label = lbl(b,
    #                                           text="Phone",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # phone_label.grid(row=4, column=2, padx=10, )
    # unit_entry =ent(b,
    #                                          width=10,
    #                                          placeholder_text="Unit")
    # unit_entry.grid(row=7, column=1, columnspan=1, pady=5, padx=20, sticky="we")
    
    
        


    # pincode_label = lbl(b,
    #                                           text="Pincode",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # pincode_label.grid(row=4, column=4, padx=10, )
    # quantity_entry = ent(b,
    #                                          width=10,
    #                                          placeholder_text="Quantity")
    # quantity_entry.grid(row=7, column=0, columnspan=1, pady=5, padx=20, sticky="we")

    # estimate_label = lbl(b,
    #                                           text="Estimate Amount",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # estimate_label.grid(row=5, column=2, padx=10, )
    # price_entry = ent(b,
    #                                          width=10,
    #                                          placeholder_text="Price")
    # price_entry.grid(row=8, column=0, columnspan=1, pady=5, padx=20, sticky="we")
    
    
    # total_entry = ent(b,
    #                                          width=10,
    #                                          placeholder_text="Total")
    # total_entry.grid(row=8, column=1, columnspan=1, pady=5, padx=20, sticky="we")

    # info_label = customtkinter.CTkLabel(b,
    #                                           text="Date",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # info_label.grid(row=4, column=2)
    # # mylb = Listbox(x, width=90, background="darkgrey", height=8)
    # # mylb.grid(row=5, column=0, columnspan=5, rowspan=4)
    

    # functions

    inventory_purchase_database.dbconnect()

    class InventoryPurchase_handling:
        def select_record(self, e):
            # clear box
            dateentry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            supplier_name_entry.delete(0, END)
            supplier_id_entry.delete(0, END)
            # inventory_entry.delete(0, END)
            # inventory_id_entry.delete(0, END)
            # unit_entry.delete(0, END)
            # quantity_entry.delete(0, END)
            # price_entry.delete(0, END)
            # total_entry.delete(0, END)
            
            
            
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
                # inventory_entry.insert(0, values[4])
                # inventory_id_entry.insert(0, values[5])
                # unit_entry.insert(0, values[6])
                # quantity_entry.insert(0, values[7])
                # price_entry.insert(0, values[8])
                # total_entry.insert(0, values[9])
            
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
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            supplier_name_entry.delete(0, END)
            supplier_id_entry.delete(0, END)
            # inventory_entry.delete(0, END)
            # inventory_id_entry.delete(0, END)
            # unit_entry.delete(0, END)
            # quantity_entry.delete(0, END)
            # price_entry.delete(0, END)
            # total_entry.delete(0, END)
            
            
            
            # mylb.delete(0,END)
            datetoday()
        
        
        def entering(self):
            # try:
           

            # mylb.delete(0, END)
            posdata = pos.printinv()
            
            total = pos.printval()
        
            inventory_purchase_database.dbentry(dateentry.get(),customer_name_entry.get(), customer_id_entry.get(), supplier_name_entry.get(), supplier_id_entry.get(),posdata,0,0, total)
            # mylb.insert(0, "New Data into the Database created")
            pos.delval()
            pos.delinv()
            my_tree1.delete(*my_tree1.get_children())
            inv_tree.delete(*inv_tree.get_children())
            
            
            record1.fetching()
            
            dateentry.delete(0, END)
            supplier_name_entry.delete(0, END)
            supplier_id_entry.delete(0, END)
            
            inv_tree.delete()
            # inventory_entry.delete(0, END)
            # inventory_id_entry.delete(0, END)
            # unit_entry.delete(0, END)
            # quantity_entry.delete(0, END)
            # price_entry.delete(0, END)
            # total_entry.delete(0, END)
            
            
            
            # except:
            #     mylb.insert(0, "Boxes Cannot be Blank")
            datetoday()
            
       
        
        
        def deleting(self):
            
            selected = my_tree1.focus()
            values = my_tree1.item(selected, "values")
            inventory_purchase_database.dbdelete(values[0])
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            supplier_name_entry.delete(0, END)
            supplier_id_entry.delete(0, END)
            # inventory_entry.delete(0, END)
            # inventory_id_entry.delete(0, END)
            # unit_entry.delete(0, END)
            # quantity_entry.delete(0, END)
            # price_entry.delete(0, END)
            # total_entry.delete(0, END)
            
            
            # mylb.delete(0, END)
            # mylb.insert(0, "One item is delted from database")
            datetoday()
        
        # def updating(self):
        #     selected = my_tree1.focus()
        #     values = my_tree1.item(selected, "values")
        
        #     #inventory_purchase_database.dbupdate(dateentry.get(), supplier_name_entry.get(), supplier_id_entry.get(),inventory_entry.get(),inventory_id_entry.get(),unit_entry.get(),quantity_entry.get(),price_entry.get(), total_entry.get(), values[0])
            
        #     my_tree1.delete(*my_tree1.get_children())
            
        #     record1.fetching()
            
        #     dateentry.delete(0, END)
        #     supplier_name_entry.delete(0, END)
        #     supplier_id_entry.delete(0, END)
        #     # inventory_entry.delete(0, END)
        #     # inventory_id_entry.delete(0, END)
        #     # unit_entry.delete(0, END)
        #     # quantity_entry.delete(0, END)
        #     # price_entry.delete(0, END)
        #     # total_entry.delete(0, END)
            
            
        #     # mylb.delete(0, END)
        #     # mylb.insert(0, "One item is updated from database")
        #     datetoday()
        
        def fetching(self):
            data = inventory_purchase_database.dbfetch()
            # mylb.delete(0, END)
            # mylb.insert(0, "Fetched data from database to the table")
            
            count = 0
            
            
            for i in data:
                
                if count % 2 == 0:
                    my_tree1.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]), tags=("evenrow",))
                    
                else:
                    my_tree1.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]), tags=("oddrow",))
                
                # increment counter
                count += 1
            
            
            
        
    record1 = InventoryPurchase_handling()
    # bind
    my_tree1.bind("<ButtonRelease-1>", record1.select_record)

    # buttons

    add_button = btn(b,
                                                 text="Add",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.entering)
    add_button.grid(row=8, column=2, padx=10)

    del_button = btn(b,
                                                 text="Remove",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.deleting)
    del_button.grid(row=8, column=3, padx=10)

    # update_button = btn(b,
    #                                              text="Update",
    #                                              border_width=2,  # <- custom border_width
    #                                              fg_color=None,  # <- no fg_color
    #                                              command=record1.updating)
    # update_button.grid(row=8, column=4, padx=10)

    # show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
    # show_button.grid(row=5, column=5, padx=10)

    record1.fetching()

    clear_button = btn(master=b,
                                                 text="Clear Boxes",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.clearentrybox)
    clear_button.grid(row=8, column=5, padx=10)




    # balance_label = Label(data_frame, text="Balance", background="lightgrey")
    # balance_label.grid(row=4, column=0, padx=10, )
    # balance_entry = Entry(data_frame)
    # balance_entry.grid(row=1, column=3, padx=10, )

    
#     def updatelb1(data):
#         lb16.delete(0, END)
#         for item in data:
#             lb16.insert(END, item)

#     def fillout1(e):
#         li14 = databaseinv.dbfetchinv()
        

        
#         inventory_entry.delete(0, END)
#         inventory_id_entry.delete(0, END)
#         unit_entry.delete(0, END)
#         price_entry.delete(0, END)
        
            
    
        
        
#         # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
#         for i in li14:
#             if lb16.get(ANCHOR) in i:
#                 inventory_entry.insert(0, i[1])
#                 inventory_id_entry.insert(0, i[0])
#                 unit_entry.insert(0, i[4])
#                 price_entry.insert(0, i[3])
        
#         lb16.delete(0, END)
        
    

            
#     def check1(e):
#         global lb16
        
#         li14 = databaseinv.dbfetchinv()
        
#         lb15.destroy()
#         lb16 = Listbox(b)
#         lb16.grid(row=9, column=1, rowspan=4, padx=20, pady=5)
        
#         li16 = []

#         for i in li14:
            
#             li16.append(i[1])
            
            
#         typed = inventory_entry.get()
#         if typed == '':
#             data = li16
#         else:
#             data = []
#             for item in li16:
#                 if typed.lower() in item.lower():
#                     data.append(item)
#         updatelb1(data)
#         lb16.bind("<<ListboxSelect>>", fillout1)
        
        
    
    
        

        


# ###########################################################################
     
    def updatelb2(data):
        lb17.delete(0, END)
        for item in data:
            lb17.insert(END, item)

    def fillout2(e):
        li14 = test3.dbfetch()
        

        
        # inventory_entry.delete(0, END)
        # inventory_id_entry.delete(0, END)
        # unit_entry.delete(0, END)
        # price_entry.delete(0, END)
        
        customer_name_entry.delete(0, END)
        customer_id_entry.delete(0, END)
        
            
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li14:
            if lb17.get(ANCHOR) in i:
                customer_name_entry.insert(0, i[2])
                customer_id_entry.insert(0, i[0])
                # inventory_entry.insert(0, i[1])
                # inventory_id_entry.insert(0, i[0])
                # unit_entry.insert(0, i[4])
                # price_entry.insert(0, i[3])
        
        lb17.delete(0, END)
        
    

            
    def check2(e):
        
        
        li14 = test3.dbfetch()
        
        # lb15.destroy()
        # lb16.destroy()
        
        
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
        updatelb2(data)
        lb17.bind("<<ListboxSelect>>", fillout2)
    
    lb17 = Listbox(b)
    lb17.grid(row=9, column=1, rowspan=4, padx=20, pady=5)

    customer_name_entry.bind("<KeyRelease>", check2)
     

        
# #################################################################


#         # updatelb(li15)



    

#     inventory_entry.bind("<KeyRelease>", check1)
    
#     try:
#         def qtyentry(e):
#             total_entry.delete(0, END)
            
#             total = int(quantity_entry.get()) * int(price_entry.get())
            
#             total_entry.insert(0, total)
            
#             try:
#                 lb15.delete(0, END)
#                 lb16.delete(0, END)
#             except:
#                 pass
#     except:
#         pass
                    
        
        
#     try:
#        quantity_entry.bind("<KeyRelease>", qtyentry)
#     except:
#         pass
    
    
#     try:
#         def qtyentry1(e):
#             total_entry.delete(0, END)
            
#             total = int(quantity_entry.get()) * int(price_entry.get())
            
#             total_entry.insert(0, total)
            
#             try:
#                 lb15.delete(0, END)
#                 lb16.delete(0, END)
#             except:
#                 pass
#     except:
#         pass
    
#     try:
#         price_entry.bind("<KeyRelease>", qtyentry1)
#     except:
#         pass
    # #####################################################################################################################################




    def updatelb(data):
        lb15.delete(0, END)
        for item in data:
            lb15.insert(END, item)

    def fillout(e):
        li20 = test3.dbfetchsup()
        

        
        supplier_name_entry.delete(0, END)
        supplier_id_entry.delete(0, END)
        
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li20:
            if lb15.get(ANCHOR) in i:
                supplier_name_entry.insert(0, i[2])
                supplier_id_entry.insert(0, i[0])
        
        
        lb15.delete(0, END)

        
    def check(e):
        global lb15
        li20 = test3.dbfetchsup()
        li21 = []
        lb17.destroy()
        lb15 = Listbox(b)
        lb15.grid(row=9, column=1, rowspan=4, padx=20, pady=5)
       
        
       


        for i in li20:
            
            li21.append(i[2])
            
            
            
        typed = supplier_name_entry.get()
        if typed == '':
            data = li21
        else:
            data = []
            for item in li21:
                if typed.lower() in item.lower():
                    data.append(item)
        updatelb(data)
        
        

        lb15.bind("<<ListboxSelect>>", fillout)
    
    
     

    supplier_name_entry.bind("<KeyRelease>", check)

    


    

    # updatelb(li15)



    
    
    
    def updatelb5(data):
            lb25.delete(0, END)
            for item in data:
                lb25.insert(END, item)

    def fillout5(e):
        li14 = databaseinv.dbfetchinv()
        

        
        inv_entry.delete(0, END)
        inv_amt_entry.delete(0,END)
        inv_count_entry.delete(0,END)
      
       
            
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li14:
            if lb25.get(ANCHOR) in i:
                inv_entry.insert(0, i[1])
                inv_amt_entry.insert(0, i[3])
             
               
               
          
        
        
        
    

            
    def check5(e):
        global lb25
        
        li14 = databaseinv.dbfetchinv()
        
        lb15.destroy()
        lb25 = Listbox(b)
        lb25.grid(row=9, column=1, rowspan=4, padx=20, pady=5)
        
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
    
#     ##########################################################################