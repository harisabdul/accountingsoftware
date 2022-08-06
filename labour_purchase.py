
from tkinter import *
from tkinter import ttk
import datetime


import inventory_purchase_database
import test3

import labour_purchase_database

import work_database

date_and_time = datetime.date.today()
date1 = str(date_and_time)




def labor(x, lbl):
    
    
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
    my_tree1['columns'] = ("id","date_and_time","customer_name", "customer_id", "supplier_name", "supplier_id", "work_name", "work_id", "nos", "price", "total")

    # format our columns
    my_tree1.column("#0", width=0, stretch=NO)
    my_tree1.column("id", anchor=CENTER, width=50)
    my_tree1.column("date_and_time", anchor=W, width=150)
    my_tree1.column("customer_name", anchor=W, width=150)
    my_tree1.column("customer_id", anchor=CENTER, width=50)
    my_tree1.column("supplier_name", anchor=W, width=150)
    my_tree1.column("supplier_id", anchor=CENTER, width=50)
    my_tree1.column("work_name", anchor=W, width=160)
    my_tree1.column("work_id", anchor=CENTER, width=50 )
    my_tree1.column("nos", anchor=CENTER, width=50)
    my_tree1.column("price", anchor=CENTER, width=50)
    my_tree1.column("total", anchor=CENTER, width=50)


    # create Headings
    my_tree1.heading("#0", text="", anchor=W)
    my_tree1.heading("id", text="ID", anchor=CENTER)
    my_tree1.heading("date_and_time", text="Date", anchor=W)
    my_tree1.heading("customer_name", text="Customer Name", anchor=W)
    my_tree1.heading("customer_id", text="Customer ID")
    my_tree1.heading("supplier_name", text="Supplier Name", anchor=W)
    my_tree1.heading("supplier_id", text="Supplier ID")
    my_tree1.heading("work_name", text="Work Name", anchor=W)
    my_tree1.heading("work_id", text="Work ID", anchor=CENTER)
    my_tree1.heading("nos", text="Number of workers", anchor=CENTER)
    my_tree1.heading("price", text="Wage", anchor=CENTER)
    my_tree1.heading("total", text="Total", anchor=CENTER)
    # create striped row tags

    # create striped row tags
    my_tree1.tag_configure('oddrow', background="white", foreground="darkgreen")
    my_tree1.tag_configure('evenrow', background="white", foreground="darkblue")




def labor1(lbl, ent, btn, b):
    def datetoday():
        date2 = datetime.date.today()
        date3 = str(date2)
        dateentry.insert(0, date3)
    
    




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
    
    
    work_entry = ent(b,
                                             width=10,
                                             placeholder_text="Work Name")
    work_entry.grid(row=6, column=0, columnspan=1, pady=5, padx=20, sticky="we")


    # address_label = lbl(b,
    #                                           text="Address",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # address_label.grid(row=6, column=0, padx=10, )
    work_id_entry = ent(b,
                                             width=10,
                                             placeholder_text="Work_id")
    work_id_entry.grid(row=6, column=1, columnspan=1, pady=5, padx=20, sticky="we")


    # phone_label = lbl(b,
    #                                           text="Phone",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # # phone_label.grid(row=4, column=2, padx=10, )
    # unit_entry =ent(b,
    #                                          width=10,
    #                                          placeholder_text="Unit")
    # unit_entry.grid(row=6, column=1, columnspan=1, pady=5, padx=20, sticky="we")
    
    


    # pincode_label = lbl(b,
    #                                           text="Pincode",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # pincode_label.grid(row=4, column=4, padx=10, )
    quantity_entry = ent(b,
                                             width=10,
                                             placeholder_text="Number of workers")
    quantity_entry.grid(row=7, column=0, columnspan=1, pady=5, padx=20, sticky="we")

    # estimate_label = lbl(b,
    #                                           text="Estimate Amount",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # estimate_label.grid(row=5, column=2, padx=10, )
    price_entry = ent(b,
                                             width=10,
                                             placeholder_text="Wage")
    price_entry.grid(row=7, column=1, columnspan=1, pady=5, padx=20, sticky="we")
    
    
    total_entry = ent(b,
                                             width=10,
                                             placeholder_text="Total")
    total_entry.grid(row=8, column=1, columnspan=1, pady=5, padx=20, sticky="we")

    # info_label = customtkinter.CTkLabel(b,
    #                                           text="Date",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # info_label.grid(row=4, column=2)
    # # mylb = Listbox(x, width=90, background="darkgrey", height=8)
    # # mylb.grid(row=5, column=0, columnspan=5, rowspan=4)
    

    # functions

    labour_purchase_database.dbconnect()

    class LaborPurchase_handling:
        def select_record(self, e):
            # clear box
            
            dateentry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            supplier_name_entry.delete(0, END)
            supplier_id_entry.delete(0, END)
            work_entry.delete(0, END)
            work_id_entry.delete(0, END)
            quantity_entry.delete(0, END)
            price_entry.delete(0, END)
            total_entry.delete(0, END)
            
            
            
            # Grab record number
            selected = my_tree1.focus()
            values = my_tree1.item(selected, "values")
            
            #output entrybox
            dateentry.insert(0, values[1])
            customer_name_entry.insert(0, values[2])
            customer_id_entry.insert(0, values[3])
            supplier_name_entry.insert(0, values[2])
            supplier_id_entry.insert(0, values[3])
            work_entry.insert(0, values[4])
            work_id_entry.insert(0, values[5])
            quantity_entry.insert(0, values[6])
            price_entry.insert(0, values[7])
            total_entry.insert(0, values[8])
            
            
            
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
            work_entry.delete(0, END)
            work_id_entry.delete(0, END)
            quantity_entry.delete(0, END)
            price_entry.delete(0, END)
            total_entry.delete(0, END)
            
            
            
            # mylb.delete(0,END)
            datetoday()
        
        
        def entering(self):
            # try:

            # mylb.delete(0, END)
            
            
            labour_purchase_database.dbentry(dateentry.get(), customer_name_entry.get(), customer_id_entry.get(), supplier_name_entry.get(), supplier_id_entry.get(),work_entry.get(),work_id_entry.get(),quantity_entry.get(),price_entry.get(), total_entry.get())
            # mylb.insert(0, "New Data into the Database created")
            
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            supplier_name_entry.delete(0, END)
            supplier_id_entry.delete(0, END)
            work_entry.delete(0, END)
            work_id_entry.delete(0, END)
            quantity_entry.delete(0, END)
            price_entry.delete(0, END)
            total_entry.delete(0, END)
            
            
            # except:
            #     mylb.insert(0, "Boxes Cannot be Blank")
            datetoday()
        
        
        def deleting(self):
            
            selected = my_tree1.focus()
            values = my_tree1.item(selected, "values")
            labour_purchase_database.dbdelete(values[0])
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            supplier_name_entry.delete(0, END)
            supplier_id_entry.delete(0, END)
            work_entry.delete(0, END)
            work_id_entry.delete(0, END)
            quantity_entry.delete(0, END)
            price_entry.delete(0, END)
            total_entry.delete(0, END)
            
            
            # mylb.delete(0, END)
            # mylb.insert(0, "One item is delted from database")
            datetoday()
        
        def updating(self):
            selected = my_tree1.focus()
            values = my_tree1.item(selected, "values")
        
            labour_purchase_database.dbupdate(dateentry.get(), customer_name_entry.get(), customer_id_entry.get(), supplier_name_entry.get(), supplier_id_entry.get(),work_entry.get(),work_id_entry.get(),quantity_entry.get(),price_entry.get(), total_entry.get(), values[0])
            
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            supplier_name_entry.delete(0, END)
            supplier_id_entry.delete(0, END)
            work_entry.delete(0, END)
            work_id_entry.delete(0, END)
            quantity_entry.delete(0, END)
            price_entry.delete(0, END)
            total_entry.delete(0, END)
            
            
            # mylb.delete(0, END)
            # mylb.insert(0, "One item is updated from database")
            datetoday()
        
        def fetching(self):
            data = labour_purchase_database.dbfetch()
            # mylb.delete(0, END)
            # mylb.insert(0, "Fetched data from database to the table")
            
            count = 0
            
            
            for i in data:
                
                if count % 2 == 0:
                    my_tree1.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]), tags=("evenrow",))
                    
                else:
                    my_tree1.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10]), tags=("oddrow",))
                
                # increment counter
                count += 1
            
            
            
        
    record1 = LaborPurchase_handling()
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

    update_button = btn(b,
                                                 text="Update",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.updating)
    update_button.grid(row=8, column=4, padx=10)

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
    
    
    
    
  # #####################################################################################################################################




    def updatelb2(data):
        lb17.delete(0, END)
        for item in data:
            lb17.insert(END, item)

    def fillout2(e):
        li21 = test3.dbfetch()
        

        
        customer_name_entry.delete(0, END)
        customer_id_entry.delete(0, END)
        
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li21:
            if lb17.get(ANCHOR) in i:
                customer_name_entry.insert(0, i[2])
                customer_id_entry.insert(0, i[0])
        
        
        lb17.delete(0, END)

        
    def check2(e):
        li20 = test3.dbfetch()
        li21 = []

        for i in li20:
            
            li21.append(i[2])
            
            
        typed = customer_name_entry.get()
        if typed == '':
            data = li21
        else:
            data = []
            for item in li21:
                if typed.lower() in item.lower():
                    data.append(item)
        updatelb2(data)
        
        

    

    


    lb17 = Listbox(b)
    lb17.grid(row=9, column=1, rowspan=4, padx=20, pady=5)


    # updatelb(li15)



    lb17.bind("<<ListboxSelect>>", fillout2)

    customer_name_entry.bind("<KeyRelease>", check2)
    
    
    
    
    
    ##########################################################################
    # #####################################################################################################################################




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
        
        
        lb15.delete(0, END)

        
    def check(e):
        global lb15
        li14 = test3.dbfetchsup()
        li15 = []

        for i in li14:
            
            li15.append(i[2])
            
        lb15 = Listbox(b)
        lb15.grid(row=9, column=1, rowspan=4, padx=20, pady=5)
        typed = supplier_name_entry.get()
        if typed == '':
            data = li15
        else:
            data = []
            for item in li15:
                if typed.lower() in item.lower():
                    data.append(item)
        updatelb(data)
        
        
        lb15.bind("<<ListboxSelect>>", fillout)
    

    


    


    # updatelb(li15)



    

    supplier_name_entry.bind("<KeyRelease>", check)
    
    
    
    
    
    ##########################################################################
    
    def updatelb1(data):
        lb16.delete(0, END)
        for item in data:
            lb16.insert(END, item)

    def fillout1(e):
        li14 = work_database.dbfetchexp()
        

        
        work_entry.delete(0, END)
        work_id_entry.delete(0, END)
        # price_entry.delete(0, END)
        
            
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        try:
            for i in li14:
                if lb16.get(ANCHOR) in i:
                    work_entry.insert(0, i[1])
                    work_id_entry.insert(0, i[0])
                    price_entry.insert(0, i[3])
            
            lb16.delete(0, END)
        except:
            pass
            
    

            
    def check1(e):
        global lb16
        
        li14 = work_database.dbfetchexp()
        
        lb15.destroy()
        lb16 = Listbox(b)
        lb16.grid(row=9, column=1, rowspan=4, padx=20, pady=5)
        
        li16 = []

        for i in li14:
            
            li16.append(i[1])
            
            
        typed = work_entry.get()
        if typed == '':
            data = li16
        else:
            data = []
            for item in li16:
                if typed.lower() in item.lower():
                    data.append(item)
        updatelb1(data)
        lb16.bind("<<ListboxSelect>>", fillout1)

        

        


       


        # updatelb(li15)



    

    work_entry.bind("<KeyRelease>", check1)
    
    try:
        def qtyentry(e):
            total_entry.delete(0, END)
            
            try:
                
                
                
                total = int(quantity_entry.get()) * int(price_entry.get())
                
                total_entry.insert(0, total)
            except:
                pass
            
            try:
                lb16.delete(0, END)
                total_entry.delete(0, END)
            except:
                pass
            
            
            try:
                lb15.delete(0, END)
                lb16.delete(0, END)
            except:
                pass
                    
    except:
        pass
        
        

    try:
        price_entry.bind("<KeyRelease>", qtyentry)
    except:
        pass
    
    
    try:
        def dellb(e):
            
            try:
                lb16.delete(0,END)
                total_entry.delete(0, END)
            except:
                pass
            try:
                total = int(quantity_entry.get()) * int(price_entry.get())
            except:
                pass
            try:
                total_entry.insert(0, total)
            except:
                pass
    except:
        pass
        # def qtyentry(e):
        #     lb16.delete(0, END)
        #     total_entry.delete(0, END)
        #     try:
        #         total = int(quantity_entry.get()) * int(price_entry.get())
        #     except:
        #         pass
            
        #     total_entry.insert(0, total)
            
        #     try:
        #         lb15.delete(0, END)
        #         lb16.delete(0, END)
        #     except:
        #         pass
                    
    
        
        

    
    price_entry.bind("<KeyRelease>", dellb)
   