from tkinter import *
from tkinter import ttk
import datetime
import test3


date_and_time = datetime.date.today()
date1 = str(date_and_time)



def supplier(x, lbl):
    
    global my_tree6
    
    

    label1 = lbl(x, text="Supplier Record Book")
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
    
    
    



    tree_frame6 = Frame(x)
    tree_frame6.grid(padx=10, pady=10, row=1, column=0, rowspan=11)


    # create scroll bar
    tree_scroll6 = Scrollbar(tree_frame6)
    tree_scroll6.pack(side=RIGHT, fill=Y)


    # create the treeview
    my_tree6 = ttk.Treeview(tree_frame6, yscrollcommand=tree_scroll6.set, selectmode="extended")
    my_tree6.pack()



    # configure the scroll bar
    tree_scroll6.config(command=my_tree6.yview)

    # define our columns
    my_tree6['columns'] = ("id","date_and_time", "supplier_name", "address", "phone", "pincode")

    # format our columns
    my_tree6.column("#0", width=0, stretch=NO)
    my_tree6.column("id", anchor=CENTER, width=50)
    my_tree6.column("date_and_time", anchor=W, width=140)
    my_tree6.column("supplier_name", anchor=W, width=140)
    my_tree6.column("address", anchor=CENTER, width=100 )
    my_tree6.column("phone", anchor=CENTER, width=140)
    my_tree6.column("pincode", anchor=CENTER, width=140)


    # create Headings
    my_tree6.heading("#0", text="", anchor=W)
    my_tree6.heading("id", text="ID", anchor=CENTER)
    my_tree6.heading("date_and_time", text="Date", anchor=W)
    my_tree6.heading("supplier_name", text="Customer Name", anchor=W)
    my_tree6.heading("address", text="Address", anchor=CENTER)
    my_tree6.heading("phone", text="Phone", anchor=CENTER)
    my_tree6.heading("pincode", text="Pincode", anchor=CENTER)
    # create striped row tags
    my_tree6.tag_configure('oddrow', background="white", foreground="darkgreen")
    my_tree6.tag_configure('evenrow', background="white", foreground="darkblue")
    
    
    
def supplier1(lbl, ent, btn, b):
    def datetoday():
        date2 = datetime.date.today()
        date3 = str(date2)
        dateentry6.insert(0, date3)



    date_label = lbl(b,
                                              text="Execute Above Mentioned Details Here ------------>",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_label.grid(row=7, column=0,)


    dateentry6 = ent(b,
                                             width=10,
                                             placeholder_text="Date")
    dateentry6.grid(row=3, column=0, columnspan=1, pady=0, padx=20, sticky="we")
    
    datetoday()




    # date_entry = Entry(data_frame)
    # date_entry.grid(row=0, column=1, padx=10, )


  
    name_entry6 = ent(b,
                                             width=10,
                                             placeholder_text="Supplier Name")
    name_entry6.grid(row=4, column=0, columnspan=1, pady=0, padx=20, sticky="we")


   
    address_entry6 = ent(b,
                                             width=10,
                                             placeholder_text="Address")
    address_entry6.grid(row=5, column=0, columnspan=4, pady=0, padx=20, sticky="we")



    phone_entry6 = ent(b,
                                             width=10,
                                             placeholder_text="Phone")
    phone_entry6.grid(row=4, column=1, columnspan=1, pady=0, padx=20, sticky="we")

    pincode_entry6 = ent(b,
                                             width=10,
                                             placeholder_text="Pincode")
    pincode_entry6.grid(row=4, column=2, columnspan=1, pady=0, padx=20, sticky="we")



    # functions

    test3.dbconnectsup()

    class supplier_handling:
        def select_record(self, e):
            # clear box
            dateentry6.delete(0, END)
            name_entry6.delete(0, END)
            address_entry6.delete(0, END)
            phone_entry6.delete(0, END)
            pincode_entry6.delete(0, END)
            
            # Grab record number
            selected = my_tree6.focus()
            values = my_tree6.item(selected, "values")
            
            #output entrybox
            dateentry6.insert(0, values[1])
            name_entry6.insert(0, values[2])
            address_entry6.insert(0, values[3])
            phone_entry6.insert(0, values[4])
            pincode_entry6.insert(0, values[5])
            
            #output listbox
            
    
            # mylb.insert(1, values[2])
            # mylb.insert(2, values[3])
            

        def clearentrybox(self):
            # clear box
            
            dateentry6.delete(0, END)
            name_entry6.delete(0, END)
            address_entry6.delete(0, END)
            phone_entry6.delete(0, END)
            pincode_entry6.delete(0, END)
            
            datetoday()
  
        
        
        def entering(self):
            # try:

      
            
            test3.dbentrysup(dateentry6.get(), name_entry6.get(), address_entry6.get(), phone_entry6.get(), pincode_entry6.get())

            
            my_tree6.delete(*my_tree6.get_children())
            
            record6.fetching()
            
            dateentry6.delete(0, END)
            name_entry6.delete(0, END)
            address_entry6.delete(0, END)
            phone_entry6.delete(0, END)
            pincode_entry6.delete(0, END)
            # except:
            #     mylb.insert(0, "Boxes Cannot be Blank")
            
            datetoday()
        
        
        def deleting(self):
            
            selected = my_tree6.focus()
            values = my_tree6.item(selected, "values")
            test3.dbdeletesup(values[0])
            my_tree6.delete(*my_tree6.get_children())
            
            record6.fetching()
            
            dateentry6.delete(0, END)
            name_entry6.delete(0, END)
            address_entry6.delete(0, END)
            phone_entry6.delete(0, END)
            pincode_entry6.delete(0, END)
            
            datetoday()
        
        
        def updating(self):
            selected = my_tree6.focus()
            values = my_tree6.item(selected, "values")
        
            test3.dbupdatesup(dateentry6.get(), name_entry6.get(), address_entry6.get(), phone_entry6.get(), pincode_entry6.get(), values[0])
            
            my_tree6.delete(*my_tree6.get_children())
            
            record6.fetching()
            
            dateentry6.delete(0, END)
            name_entry6.delete(0, END)
            address_entry6.delete(0, END)
            phone_entry6.delete(0, END)
            pincode_entry6.delete(0, END)
            
            datetoday()
        
        
        def fetching(self):
            data = test3.dbfetchsup()
         
            
            count = 0
            
            
            for i in data:
                
                if count % 2 == 0:
                    my_tree6.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=("evenrow",))
                    
                else:
                    my_tree6.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=("oddrow",))
                
                # increment counter
                count += 1
            
            
            
        
    record6 = supplier_handling()
    # bind
    my_tree6.bind("<ButtonRelease-1>", record6.select_record)

    # buttons

    add_button6 = btn(b,
                                                 text="Add",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record6.entering)
    add_button6.grid(row=7, column=2, padx=10)

    del_button6 = btn(b,
                                                 text="Remove",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record6.deleting)
    del_button6.grid(row=7, column=3, padx=10)

    update_button6 = btn(b,
                                                 text="Update",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record6.updating)
    update_button6.grid(row=7, column=4, padx=10)

    clear_button6 = btn(b,
                                                 text="Clear Boxes",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record6.clearentrybox)
    clear_button6.grid(row=7, column=5, padx=10)

    # show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
    # show_button.grid(row=5, column=5, padx=10)

    record6.fetching()


    
    

