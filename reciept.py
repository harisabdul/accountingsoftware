
from tkinter import *
from tkinter import ttk
import datetime


import inventory_purchase_database
import test3

import databaseinv

import construction_cost_database
import labor_allocation_database
import work_database
import interior_designing_labor_database
import reciept_database
import empdatabase


date_and_time = datetime.date.today()
date1 = str(date_and_time)




def recieptfn(x, lbl):
    
    
    global my_tree1
    
    label1 = lbl(x, text="Cash Reciept")
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
    my_tree1['columns'] = ("id","date_and_time","customer_name","customer_id","employee_name","employee_id", "current_reciept", "estimate", "recieved", "balance", "cat")

    # format our columns
    my_tree1.column("#0", width=0, stretch=NO)
    my_tree1.column("id", anchor=CENTER, width=50)
    my_tree1.column("date_and_time", anchor=W, width=150)
    my_tree1.column("customer_name", anchor=W, width=150)
    my_tree1.column("customer_id", anchor=CENTER, width=50)
    my_tree1.column("employee_name", anchor=W, width=160)
    my_tree1.column("employee_id", anchor=CENTER, width=50 )
    my_tree1.column("current_reciept", anchor=CENTER, width=50)
    my_tree1.column("estimate", anchor=CENTER, width=100)
    my_tree1.column("recieved", anchor=CENTER, width=50)
    my_tree1.column("balance", anchor=CENTER, width=50)
    my_tree1.column("cat", anchor=CENTER, width=50)
    

    # create Headings
    my_tree1.heading("#0", text="", anchor=W)
    my_tree1.heading("id", text="ID", anchor=CENTER)
    my_tree1.heading("date_and_time", text="Date", anchor=W)
    my_tree1.heading("customer_name", text="Customer Name", anchor=W)
    my_tree1.heading("customer_id", text="Customer ID")
    my_tree1.heading("employee_name", text="Employee Name", anchor=W)
    my_tree1.heading("employee_id", text="Employee ID", anchor=CENTER)
    my_tree1.heading("current_reciept", text="Current Reciept", anchor=CENTER)
    my_tree1.heading("estimate", text="Estimate", anchor=CENTER)
    my_tree1.heading("recieved", text="Recieved", anchor=CENTER)
    my_tree1.heading("balance", text="Balance", anchor=CENTER)
    my_tree1.heading("cat", text="Catogory", anchor=CENTER)
   
    # create striped row tags

    # create striped row tags
    my_tree1.tag_configure('oddrow', background="white", foreground="darkgreen")
    my_tree1.tag_configure('evenrow', background="white", foreground="darkblue")




def recieptfn1(lbl, ent, btn, b, cb):
    def datetoday():
        date2 = datetime.date.today()
        date3 = str(date2)
        dateentry.insert(0, date3)
    
    




    date_label = lbl(b,
                                              text="Execute Above Mentioned Details Here ------------>",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_label.grid(row=7, column=0,)
    
    date_label = lbl(b,
                                              text="Select the exact item from the list -------->",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_label.grid(row=8, column=0,)
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
    
    
    employee_name_entry = ent(b,
                                             width=10,
                                             placeholder_text="Employee Name")
    employee_name_entry.grid(row=5, column=0, columnspan=1, pady=5, padx=20, sticky="we")
    


    # address_label = lbl(b,
    #                                           text="Address",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # address_label.grid(row=6, column=0, padx=10, )
    employee_id_entry = ent(b,
                                             width=10,
                                             placeholder_text="Employee ID")
    employee_id_entry.grid(row=5, column=1, columnspan=1, pady=5, padx=20, sticky="we")


    # phone_label = lbl(b,
    #                                           text="Phone",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # phone_label.grid(row=4, column=2, padx=10, )
    amount_entry =ent(b,
                                             width=10,
                                             placeholder_text="Current Reciept")
    amount_entry.grid(row=6, column=0, columnspan=1, pady=5, padx=20, sticky="we")
    
    estimate_entry =ent(b,
                                             width=10,
                                             placeholder_text="Estimate")
    estimate_entry.grid(row=6, column=1, columnspan=1, pady=5, padx=20, sticky="we")
    
    
    recieved_entry =ent(b,
                                             width=10,
                                             placeholder_text="Recieved")
    recieved_entry.grid(row=6, column=2, columnspan=1, pady=5, padx=20, sticky="we")


    # pincode_label = lbl(b,
    #                                           text="Pincode",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # pincode_label.grid(row=4, column=4, padx=10, )
    balance_entry = ent(b,
                                             width=10,
                                             placeholder_text="balance")
    balance_entry.grid(row=6, column=3, columnspan=1, pady=5, padx=20, sticky="we")

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

    reciept_database.dbconnect()

    class Reciept_handling:
        def select_record(self, e):
            # clear box
            dateentry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            employee_name_entry.delete(0, END)
            employee_id_entry.delete(0, END)
            amount_entry.delete(0, END)
            estimate_entry.delete(0, END)
            balance_entry.delete(0, END)
            
            
            # Grab record number
            selected = my_tree1.focus()
            values = my_tree1.item(selected, "values")
            try:
                #output entrybox
                dateentry.insert(0, values[1])
                customer_name_entry.insert(0, values[2])
                customer_id_entry.insert(0, values[3])
                employee_name_entry.insert(0, values[4])
                employee_id_entry.insert(0, values[5])
                amount_entry.insert(0, values[6])
                estimate_entry.insert(0, values[7])
                balance_entry.insert(0, values[8])
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
            employee_name_entry.delete(0, END)
            employee_id_entry.delete(0, END)
            amount_entry.delete(0, END)
            estimate_entry.delete(0, END)
            balance_entry.delete(0, END)
            
            
            # mylb.delete(0,END)
            datetoday()
        
        
        def entering(self):
            # try:

            # mylb.delete(0, END)
            
            
            reciept_database.dbentry(dateentry.get(), customer_name_entry.get(), customer_id_entry.get(), employee_name_entry.get(), employee_id_entry.get(), amount_entry.get(), estimate_entry.get(),recieved_entry.get(), balance_entry.get(), combobox_2.get() )
            # mylb.insert(0, "New Data into the Database created")
            
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            employee_name_entry.delete(0, END)
            employee_id_entry.delete(0, END)
            amount_entry.delete(0, END)
            estimate_entry.delete(0, END)
            balance_entry.delete(0, END)
            recieved_entry.delete(0, END)
            # except:
            #     mylb.insert(0, "Boxes Cannot be Blank")
            datetoday()
        
        
        def deleting(self):
            
            selected = my_tree1.focus()
            values = my_tree1.item(selected, "values")
            reciept_database.dbdelete(values[0])
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            employee_name_entry.delete(0, END)
            employee_id_entry.delete(0, END)
            amount_entry.delete(0, END)
            estimate_entry.delete(0, END)
            balance_entry.delete(0, END)
            # mylb.delete(0, END)
            # mylb.insert(0, "One item is delted from database")
            datetoday()
        
        def updating(self):
            selected = my_tree1.focus()
            values = my_tree1.item(selected, "values")
        
            reciept_database.dbupdate(dateentry.get(), customer_name_entry.get(), customer_id_entry.get(), employee_name_entry.get(), employee_id_entry.get(), amount_entry.get(), estimate_entry.get(),recieved_entry.get(), balance_entry.get(), combobox_2.get(), values[0])
            
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            customer_name_entry.delete(0, END)
            customer_id_entry.delete(0, END)
            employee_name_entry.delete(0, END)
            employee_id_entry.delete(0, END)
            amount_entry.delete(0, END)
            estimate_entry.delete(0, END)
            balance_entry.delete(0, END)
            
            # mylb.delete(0, END)
            # mylb.insert(0, "One item is updated from database")
            datetoday()
        
        def fetching(self):
            data = reciept_database.dbfetch()
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
        
        
            
        
    record1 = Reciept_handling()
    # bind
    my_tree1.bind("<ButtonRelease-1>", record1.select_record)

    # buttons

    add_button = btn(b,
                                                 text="Add",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.entering)
    add_button.grid(row=8, column=2, padx=10)

    # del_button = btn(b,
    #                                              text="Remove",
    #                                              border_width=2,  # <- custom border_width
    #                                              fg_color=None,  # <- no fg_color
    #                                              command=record1.deleting)
    # del_button.grid(row=8, column=3, padx=10)

    
    def btndiable(combobox="Remove Disable"):
        
    
        if combobox == "Remove Disable":
            del_button = btn(b,
                                                    text="Remove",
                                                    border_width=2,  # <- custom border_width
                                                    fg_color=None,  # <- no fg_color
                                                    command=record1.deleting)
            del_button.grid(row=8, column=3, padx=10)
            del_button.configure(state="disabled", text="Disabled Remove Btn")
        elif combobox == "Remove Enable":
            del_button = btn(b,
                                                    text="Remove",
                                                    border_width=2,  # <- custom border_width
                                                    fg_color=None,  # <- no fg_color
                                                    command=record1.deleting)
            del_button.grid(row=8, column=3, padx=10)
    
    
    btndiable()
    def selection():
        combobox_1 = cb(b,
                                                        values=["Remove Disable", "Remove Enable"],
                                                        command = btndiable)
        combobox_1.grid(row=9, column=3, columnspan=1, pady=10, padx=20, sticky="we")
    
    
    
            
    selection()
    
    
    combobox_2 = cb(b,
                                                        values=["Construction", "Interior Designing"],)
    combobox_2.grid(row=9, column=4, columnspan=1, pady=10, padx=20, sticky="we")
    




    update_button = btn(b,
                                                 text="Update",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.updating)
    update_button.grid(row=8, column=4, padx=10)
    
    update_button.configure(state="disabled", text="Disabled Update Btn")

    # show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
    # show_button.grid(row=5, column=5, padx=10)

    record1.fetching()

    clear_button = btn(master=b,
                                                 text="Clear Boxes",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.clearentrybox)
    clear_button.grid(row=8, column=5, padx=10)


    def calculation():
            
            global total_recieved
            recieved = []
            
            data1 = reciept_database.dbfetch()
            
            for item in data1:
                if customer_id_entry.get() in item[3]:
                    recieved.append(item[6])
                else:
                    recieved.append(0)
            
            total_recieved = 0
            
            for item in recieved:
                total_recieved = total_recieved + item
        
        
    

    # balance_label = Label(data_frame, text="Balance", background="lightgrey")
    # balance_label.grid(row=4, column=0, padx=10, )
    # balance_entry = Entry(data_frame)
    # balance_entry.grid(row=1, column=3, padx=10, )
    # #####################################################################################################################################


    ########################################################################################################
    #######################################################################################################
    #########################################################################################################3

    # def updatelb(data):
    #     # lb15.delete(0, END)
    #     for item in data:
    #         lb15.insert(END, item)

    # def fillout(e):
    #     li14 = test3.dbfetch()
        

        
    #     customer_name_entry.delete(0, END)
    #     customer_id_entry.delete(0, END)
        
    
        
        
    #     # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
    #     for i in li14:
    #         if lb15.get(ANCHOR) in i:
    #             customer_name_entry.insert(0, i[2])
    #             customer_id_entry.insert(0, i[0])
    #             estimate_entry.insert(0, i[6])
    #             recieved_entry.insert(0, total_recieved)
        
        
    #     lb15.delete(0, END)

        
    # def check(e):
    #     li14 = test3.dbfetch()
    #     li15 = []

    #     for i in li14:
            
    #         li15.append(i[2])
            
            
    #     typed = customer_name_entry.get()
    #     if typed == '':
    #         data = li15
    #     else:
    #         data = []
    #         for item in li15:
    #             if typed.lower() in item.lower():
    #                 data.append(item)
    #     updatelb(data)
        
        

    

    


    # lb15 = Listbox(b)
    # lb15.grid(row=9, column=1, rowspan=3, padx=20, pady=5)


    # # updatelb(li15)



    # lb15.bind("<<ListboxSelect>>", fillout)

    # customer_name_entry.bind("<KeyRelease>", check)
    
    
    
    
    
    ##########################################################################
    
    def updatelb1(data):
        lb16.delete(0, END)
        for item in data:
            lb16.insert(END, item)

    def fillout1(e):
        li14 = empdatabase.dbfetchemp()        

        
        employee_name_entry.delete(0, END)
        employee_id_entry.delete(0, END)
       
            
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
        for i in li14:
            if lb16.get(ANCHOR) in i:
                try:
                    employee_name_entry.insert(0, i[2])
                    employee_id_entry.insert(0, i[0])
                   
                except:
                    pass
               
          
        
        lb16.delete(0, END)
        
    

            
    def check1(e):
        global lb16
        
        li14 = empdatabase.dbfetchemp()
        
        # lb15.destroy()
        lb16 = Listbox(b)
        lb16.grid(row=9, column=1, rowspan=4, padx=20, pady=5)
        
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
        updatelb1(data)
        lb16.bind("<<ListboxSelect>>", fillout1)
        
        
    employee_name_entry.bind("<KeyRelease>", check1)

        
    # ############################################################
    
    
    ##########################################################################
    
    def updatelb2(data):
        lb17.delete(0, END)
        for item in data:
            lb17.insert(0, item)

    def fillout2(e):
        li14 = test3.dbfetch()
        

        
        customer_name_entry.delete(0, END)
        customer_id_entry.delete(0, END)
       
            
    
        
        
        # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        # lb16.destroy()
        
        for i in li14:
            if lb17.get(ANCHOR) in i:
                try:
                    customer_name_entry.insert(0, i[2])
                    customer_id_entry.insert(0, i[0])
                    estimate_entry.insert(0, i[6])
                except:
                    pass
               
          
        
        lb17.delete(0, END)
        
    

            
    def check2(e):
  
        
        li14 = test3.dbfetch()
        
        # lb15.destroy()
        
        
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

        
    # ############################################################
    
    
    
    
    def balanceent(e):
        calculation()
        balance_entry.delete(0, END)
        
        recieved_entry.delete(0, END)
        
        current = amount_entry.get()
        if current and total_recieved != "":
            grandtotal = int(current) + int(total_recieved)
        
            recieved_entry.insert(0, grandtotal)
        
        
            est = int(estimate_entry.get())
            balance = est - grandtotal
        
            balance_entry.insert(0, balance)
        
    
    
    
    
    
    
    
    
    
    amount_entry.bind("<KeyRelease>", balanceent)
    
    
    
    # def updatelb2(data):
    #         lb17.delete(0, END)
    #         for item in data:
    #             lb17.insert(END, item)

    # def fillout2(e):
    #     li14 = test3.dbfetchsup()
        

        
    #     unit_entry.delete(0, END)
       
            
    
        
        
    #     # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
    #     for i in li14:
    #         if lb17.get(ANCHOR) in i:
    #             unit_entry.insert(0, i[2])
              
               
          
        
    #     lb17.delete(0, END)
        
    

            
    # def check2(e):
    #     global lb17
        
    #     li14 = test3.dbfetchsup()
        
    #     lb16.destroy()
    #     lb17 = Listbox(b)
    #     lb17.grid(row=9, column=1, rowspan=4, padx=20, pady=5)
        
    #     li16 = []

    #     for i in li14:
            
    #         li16.append(i[2])
            
            
    #     typed = unit_entry.get()
    #     if typed == '':
    #         data = li16
    #     else:
    #         data = []
    #         for item in li16:
    #             if typed.lower() in item.lower():
    #                 data.append(item)
    #     updatelb2(data)
    #     lb17.bind("<<ListboxSelect>>", fillout2)
    
    
    # ############################################################
    
    
    # def updatelb3(data):
    #         lb18.delete(0, END)
    #         for item in data:
    #             lb18.insert(END, item)

    # def fillout3(e):
    #     li14 = test3.dbfetchemp()
        

        
    #     inventory_entry.delete(0, END)
    #     inventory_id_entry.delete(0, END)
       
            
    
        
        
    #     # supplier_name_entry.insert(0, lb15.get(ANCHOR))
        
    #     for i in li14:
    #         if lb18.get(ANCHOR) in i:
    #             emp_entry.insert(0, i[2])
                
          
        
    #     lb16.delete(0, END)
        
    

            
    # def check3(e):
    #     global lb18
        
    #     li14 = test3.dbfetchemp()
        
    #     lb17.destroy()
    #     lb18 = Listbox(b)
    #     lb18.grid(row=9, column=1, rowspan=4, padx=20, pady=5)
        
    #     li16 = []

    #     for i in li14:
            
    #         li16.append(i[2])
            
            
    #     typed = emp_entry.get()
    #     if typed == '':
    #         data = li16
    #     else:
    #         data = []
    #         for item in li16:
    #             if typed.lower() in item.lower():
    #                 data.append(item)
    #     updatelb3(data)
    #     lb18.bind("<<ListboxSelect>>", fillout3)
    
        
        
    # ###############################################################


       


    #     # updatelb(li15)



    

    # inventory_entry.bind("<KeyRelease>", check1)
    
    # unit_entry.bind("<KeyRelease>", check2)
    
    # emp_entry.bind("<KeyRelease>", check3)
    
    
    
    
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