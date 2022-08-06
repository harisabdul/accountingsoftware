

from tkinter import *
from tkinter import ttk
import datetime
import test3


date_and_time = datetime.date.today()
date1 = str(date_and_time)




def customer(x, lbl):
    
    
    global my_tree1
    
    label1 = lbl(x, text="Customer Record Book")
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
    my_tree1['columns'] = ("id","date_and_time", "customer_name", "address", "phone", "pincode", "estimate")

    # format our columns
    my_tree1.column("#0", width=0, stretch=NO)
    my_tree1.column("id", anchor=CENTER, width=50)
    my_tree1.column("date_and_time", anchor=W, width=150)
    my_tree1.column("customer_name", anchor=W, width=160)
    my_tree1.column("address", anchor=CENTER, width=150 )
    my_tree1.column("phone", anchor=CENTER, width=170)
    my_tree1.column("pincode", anchor=CENTER, width=150)
    my_tree1.column("estimate", anchor=CENTER, width=140)


    # create Headings
    my_tree1.heading("#0", text="", anchor=W)
    my_tree1.heading("id", text="ID", anchor=CENTER)
    my_tree1.heading("date_and_time", text="Date", anchor=W)
    my_tree1.heading("customer_name", text="Customer Name", anchor=W)
    my_tree1.heading("address", text="Address", anchor=CENTER)
    my_tree1.heading("phone", text="Phone", anchor=CENTER)
    my_tree1.heading("pincode", text="Pincode", anchor=CENTER)
    my_tree1.heading("estimate", text="Estimate", anchor=CENTER)
    # create striped row tags

    # create striped row tags
    my_tree1.tag_configure('oddrow', background="white", foreground="darkgreen")
    my_tree1.tag_configure('evenrow', background="white", foreground="darkblue")




def customer1(lbl, ent, btn, b, cb):
    def datetoday():
        date2 = datetime.date.today()
        date3 = str(date2)
        dateentry.insert(0, date3)
    
    




    date_label = lbl(b,
                                              text="Execute Above Mentioned Details Here ------------>",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_label.grid(row=7, column=0,)
    dateentry = ent(b,
                                             width=10,
                                             placeholder_text="Date")
    dateentry.grid(row=4, column=0, columnspan=1, pady=0, padx=20, sticky="we")
    
    
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
    name_entry = ent(b,
                                             width=10,
                                             placeholder_text="Customer Name")
    name_entry.grid(row=5, column=0, columnspan=1, pady=5, padx=20, sticky="we")


    # address_label = lbl(b,
    #                                           text="Address",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # address_label.grid(row=6, column=0, padx=10, )
    address_entry = ent(b,
                                             width=10,
                                             placeholder_text="Address")
    address_entry.grid(row=6, column=0, columnspan=4, pady=5, padx=20, sticky="we")


    # phone_label = lbl(b,
    #                                           text="Phone",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # phone_label.grid(row=4, column=2, padx=10, )
    phone_entry =ent(b,
                                             width=10,
                                             placeholder_text="Phone")
    phone_entry.grid(row=4, column=1, columnspan=1, pady=5, padx=20, sticky="we")


    # pincode_label = lbl(b,
    #                                           text="Pincode",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # pincode_label.grid(row=4, column=4, padx=10, )
    pincode_entry = ent(b,
                                             width=10,
                                             placeholder_text="Pincode")
    pincode_entry.grid(row=4, column=2, columnspan=1, pady=5, padx=20, sticky="we")

    # estimate_label = lbl(b,
    #                                           text="Estimate Amount",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # estimate_label.grid(row=5, column=2, padx=10, )
    estimate_entry = ent(b,
                                             width=10,
                                             placeholder_text="Estimate Amount")
    estimate_entry.grid(row=5, column=1, columnspan=1, pady=5, padx=20, sticky="we")

    # info_label = customtkinter.CTkLabel(b,
    #                                           text="Date",
    #                                           text_font=("Roboto Medium", -16))  # font name and size in px
    # info_label.grid(row=4, column=2)
    # # mylb = Listbox(x, width=90, background="darkgrey", height=8)
    # # mylb.grid(row=5, column=0, columnspan=5, rowspan=4)

    # functions

    test3.dbconnect()

    class Record_handling:
        def select_record(self, e):
            # clear box
            dateentry.delete(0, END)
            name_entry.delete(0, END)
            address_entry.delete(0, END)
            phone_entry.delete(0, END)
            pincode_entry.delete(0, END)
            estimate_entry.delete(0, END)
            
            # Grab record number
            selected = my_tree1.focus()
            values = my_tree1.item(selected, "values")
            
            #output entrybox
            try:
                dateentry.insert(0, values[1])
                name_entry.insert(0, values[2])
                address_entry.insert(0, values[3])
                phone_entry.insert(0, values[4])
                pincode_entry.insert(0, values[5])
                estimate_entry.insert(0, values[6])
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
            name_entry.delete(0, END)
            address_entry.delete(0, END)
            phone_entry.delete(0, END)
            pincode_entry.delete(0, END)
            estimate_entry.delete(0, END)
            
            # mylb.delete(0,END)
            datetoday()
        
        
        def entering(self):
            # try:

            # mylb.delete(0, END)
            
            
            test3.dbentry(dateentry.get(), name_entry.get(), address_entry.get(), phone_entry.get(), pincode_entry.get(), estimate_entry.get())
            # mylb.insert(0, "New Data into the Database created")
            
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            name_entry.delete(0, END)
            address_entry.delete(0, END)
            phone_entry.delete(0, END)
            pincode_entry.delete(0, END)
            estimate_entry.delete(0, END)
            # except:
            #     mylb.insert(0, "Boxes Cannot be Blank")
            datetoday()
        
        
        def deleting(self):
            
            selected = my_tree1.focus()
            values = my_tree1.item(selected, "values")
            test3.dbdelete(values[0])
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            name_entry.delete(0, END)
            address_entry.delete(0, END)
            phone_entry.delete(0, END)
            pincode_entry.delete(0, END)
            estimate_entry.delete(0, END)
            # mylb.delete(0, END)
            # mylb.insert(0, "One item is delted from database")
            datetoday()
        
        def updating(self):
            selected = my_tree1.focus()
            values = my_tree1.item(selected, "values")
        
            test3.dbupdate(dateentry.get(), name_entry.get(), address_entry.get(), phone_entry.get(), pincode_entry.get(), estimate_entry.get(), values[0])
            
            my_tree1.delete(*my_tree1.get_children())
            
            record1.fetching()
            
            dateentry.delete(0, END)
            name_entry.delete(0, END)
            address_entry.delete(0, END)
            phone_entry.delete(0, END)
            pincode_entry.delete(0, END)
            estimate_entry.delete(0, END)
            # mylb.delete(0, END)
            # mylb.insert(0, "One item is updated from database")
            datetoday()
        
        def fetching(self):
            data = test3.dbfetch()
            # mylb.delete(0, END)
            # mylb.insert(0, "Fetched data from database to the table")
            
            count = 0
            
            
            for i in data:
                
                if count % 2 == 0:
                    my_tree1.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=("evenrow",))
                    
                else:
                    my_tree1.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=("oddrow",))
                
                # increment counter
                count += 1
            
            
            
        
    record1 = Record_handling()
    # bind
    my_tree1.bind("<ButtonRelease-1>", record1.select_record)

    # buttons

    add_button = btn(b,
                                                 text="Add",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.entering)
    add_button.grid(row=7, column=2, padx=10)

    
    
    
    #self.button_3.configure(state="disabled", text="Disabled CTkButton")
    
    def btndiable(combobox="Remove Disable"):
        
    
        if combobox == "Remove Disable":
            del_button = btn(b,
                                                    text="Remove",
                                                    border_width=2,  # <- custom border_width
                                                    fg_color=None,  # <- no fg_color
                                                    command=record1.deleting)
            del_button.grid(row=7, column=3, padx=10)
            del_button.configure(state="disabled", text="Disabled Remove Btn")
        elif combobox == "Remove Enable":
            del_button = btn(b,
                                                    text="Remove",
                                                    border_width=2,  # <- custom border_width
                                                    fg_color=None,  # <- no fg_color
                                                    command=record1.deleting)
            del_button.grid(row=7, column=3, padx=10)
    
    
    btndiable()
    def selection():
        combobox_1 = cb(b,
                                                        values=["Remove Disable", "Remove Enable"],
                                                        command = btndiable)
        combobox_1.grid(row=8, column=3, columnspan=1, pady=10, padx=20, sticky="we")
    
    
    
            
    selection()
    
        
    
    
    
    # self.switch_1 = customtkinter.CTkSwitch(master=self.frame_right,
        #                                         text="CTkSwitch")
    # self.switch_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

    update_button = btn(b,
                                                 text="Update",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.updating)
    update_button.grid(row=7, column=4, padx=10)

    # show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
    # show_button.grid(row=5, column=5, padx=10)

    record1.fetching()

    clear_button = btn(master=b,
                                                 text="Clear Boxes",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.clearentrybox)
    clear_button.grid(row=7, column=5, padx=10)




    # balance_label = Label(data_frame, text="Balance", background="lightgrey")
    # balance_label.grid(row=4, column=0, padx=10, )
    # balance_entry = Entry(data_frame)
    # balance_entry.grid(row=1, column=3, padx=10, )
    # #####################################################################################################################################
