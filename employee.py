
from tkinter import *
from tkinter import ttk
import datetime
import test3
import empdatabase

date_and_time = datetime.date.today()
date1 = str(date_and_time)



def employee(x, lbl):
    
    global my_tree2
     # add some style
     
    label1 = lbl(x, text="Employee Record Book")
    label1.grid(column=0, row=0)
     
    style = ttk.Style()


    # pick a theme
    style.theme_use('default')


    # configure the treeview colors
    style.configure("Treeview", background="black", foreground="white", rowheight=25, fieldbackground="grey")

    # change selected color
    style.map("Treeview", background=[('selected', "green")])

    # create a treeview
    tree_frame2 = Frame(x)
    tree_frame2.grid(padx=10, pady=10, row=1, column=0, rowspan=11)


    # create scroll bar
    tree_scroll3 = Scrollbar(tree_frame2)
    tree_scroll3.pack(side=RIGHT, fill=Y)


    # create the treeview
    my_tree2 = ttk.Treeview(tree_frame2, yscrollcommand=tree_scroll3.set, selectmode="extended")
    my_tree2.pack()



    # configure the scroll bar
    tree_scroll3.config(command=my_tree2.yview)

    # define our columns
    my_tree2['columns'] = ("id","date_and_time", "employee_name", "address", "phone", "pincode", "position")

    # format our columns
    my_tree2.column("#0", width=0, stretch=NO)
    my_tree2.column("id", anchor=CENTER, width=50)
    my_tree2.column("date_and_time", anchor=W, width=140)
    my_tree2.column("employee_name", anchor=W, width=140)
    my_tree2.column("address", anchor=CENTER, width=100 )
    my_tree2.column("phone", anchor=CENTER, width=140)
    my_tree2.column("pincode", anchor=CENTER, width=140)
    my_tree2.column("position", anchor=CENTER, width=140)

    # create Headings
    my_tree2.heading("#0", text="", anchor=W)
    my_tree2.heading("id", text="ID", anchor=CENTER)
    my_tree2.heading("date_and_time", text="Date", anchor=W)
    my_tree2.heading("employee_name", text="Employee Name", anchor=W)
    my_tree2.heading("address", text="Address", anchor=CENTER)
    my_tree2.heading("phone", text="Phone", anchor=CENTER)
    my_tree2.heading("pincode", text="Pincode", anchor=CENTER)
    my_tree2.heading("position", text="Position", anchor=CENTER)
    
    # create striped row tags
    my_tree2.tag_configure('oddrow', background="white", foreground="darkgreen")
    my_tree2.tag_configure('evenrow', background="white", foreground="darkblue")



    # add record entry boxes 

def employee1(lbl, ent, btn, b, cb):
    def datetoday():
        date2 = datetime.date.today()
        date3 = str(date2)
        dateentry1.insert(0, date3)

    dateentry1 = ent(b,
                                             width=10,
                                             placeholder_text="Date")
    dateentry1.grid(row=3, column=0, columnspan=1, pady=0, padx=20, sticky="we")
    
    
    datetoday()





    # date_entry = Entry(data_frame)
    # date_entry.grid(row=0, column=1, padx=10, )


    
    name_entry1 = ent(b,
                                             width=10,
                                             placeholder_text="Employee Name")
    name_entry1.grid(row=4, column=0, columnspan=1, pady=5, padx=20, sticky="we")



    address_entry1 = ent(b,
                                             width=10,
                                             placeholder_text="Address")
    address_entry1.grid(row=5, column=0, columnspan=4, pady=5, padx=20, sticky="we")

 
    phone_entry1 = ent(b,
                                             width=10,
                                             placeholder_text="Phone")
    phone_entry1.grid(row=4, column=1, columnspan=1, pady=5, padx=20, sticky="we")


    pincode_entry1 = ent(b,
                                             width=10,
                                             placeholder_text="Pincode")
    pincode_entry1.grid(row=4, column=2, columnspan=1, pady=5, padx=20, sticky="we")
    
    combobox_3 = cb(b,
                                                        values=["supervisor", "Manager", "accountant", "department manager", "janitor", "driver", "construction worker", "assistant construction worker"],
                                                        )
    combobox_3.grid(row=3, column=1, columnspan=1, pady=10, padx=20, sticky="we")


    # functions

    empdatabase.dbconnectemp()

    class Employee_handling:
        def select_record(self, e):
            # clear box
            dateentry1.delete(0, END)
            name_entry1.delete(0, END)
            address_entry1.delete(0, END)
            phone_entry1.delete(0, END)
            pincode_entry1.delete(0, END)
            
            # Grab record number
            selected = my_tree2.focus()
            values = my_tree2.item(selected, "values")
            
            #output entrybox
            
            try:
                dateentry1.insert(0, values[1])
                name_entry1.insert(0, values[2])
                address_entry1.insert(0, values[3])
                phone_entry1.insert(0, values[4])
                pincode_entry1.insert(0, values[5])
            except:
                pass 
            #output listbox
            
      
            # mylb.insert(1, values[2])
            # mylb.insert(2, values[3])
            

        def clearentrybox(self):
            # clear box
            
            dateentry1.delete(0, END)
            name_entry1.delete(0, END)
            address_entry1.delete(0, END)
            phone_entry1.delete(0, END)
            pincode_entry1.delete(0, END)
            
            datetoday()
        
        
        
        def entering(self):
            # try:

        
            
            
            empdatabase.dbentryemp(dateentry1.get(), name_entry1.get(), address_entry1.get(), phone_entry1.get(), pincode_entry1.get(), combobox_3.get())
        
            my_tree2.delete(*my_tree2.get_children())
            
            record3.fetching()
            
            dateentry1.delete(0, END)
            name_entry1.delete(0, END)
            address_entry1.delete(0, END)
            phone_entry1.delete(0, END)
            pincode_entry1.delete(0, END)
            # except:
            #     mylb.insert(0, "Boxes Cannot be Blank")
            
            
            datetoday()
        
        
        def deleting(self):
            
            selected = my_tree2.focus()
            values = my_tree2.item(selected, "values")
            empdatabase.dbdeleteemp(values[0])
            my_tree2.delete(*my_tree2.get_children())
            
            record3.fetching()
            
            dateentry1.delete(0, END)
            name_entry1.delete(0, END)
            address_entry1.delete(0, END)
            phone_entry1.delete(0, END)
            pincode_entry1.delete(0, END)
        
            datetoday()
        
        def updating(self):
            selected = my_tree2.focus()
            values = my_tree2.item(selected, "values")
        
            empdatabase.dbupdateemp(dateentry1.get(), name_entry1.get(), address_entry1.get(), phone_entry1.get(), pincode_entry1.get(), combobox_3.get(), values[0])
            
            my_tree2.delete(*my_tree2.get_children())
            
            record3.fetching()
            
            dateentry1.delete(0, END)
            name_entry1.delete(0, END)
            address_entry1.delete(0, END)
            phone_entry1.delete(0, END)
            pincode_entry1.delete(0, END)
            
            datetoday()
         
        
        def fetching(self):
            data = empdatabase.dbfetchemp()
           
            count = 0
            
            try:
                for i in data:
                    
                    if count % 2 == 0:
                     
                        my_tree2.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=("evenrow",))
                        
                    else:
                        my_tree2.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], [5], i[6]), tags=("oddrow",))
                    
                    # increment counter
                    count += 1
            except:
                pass
            
            
        
    record3 = Employee_handling()
    # bind
    my_tree2.bind("<ButtonRelease-1>", record3.select_record)

    # buttons

    add_button1 = btn(b,
                                                 text="Add",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record3.entering)
    add_button1.grid(row=7, column=2, padx=10)

    

    update_button1 = btn(b,
                                                 text="Update",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record3.updating)
    update_button1.grid(row=7, column=4, padx=10)
    
    
    
    def btndiable(combobox="Remove Disable"):
            
    
        if combobox == "Remove Disable":
            del_button1 = btn(b,
                                                 text="Remove",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record3.deleting)
            del_button1.grid(row=7, column=3, padx=10)
            del_button1.configure(state="disabled", text="Disabled Remove Btn")
        elif combobox == "Remove Enable":
            del_button1 = btn(b,
                                                 text="Remove",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record3.deleting)
            del_button1.grid(row=7, column=3, padx=10)
    
    btndiable()
    def selection():
        combobox_1 = cb(b,
                                                        values=["Remove Disable", "Remove Enable"],
                                                        command = btndiable)
        combobox_1.grid(row=8, column=3, columnspan=1, pady=10, padx=20, sticky="we")
    
    
    
            
    selection()

    # show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
    # show_button.grid(row=5, column=5, padx=10)

    record3.fetching()

    clear_button1 = btn(b,
                                                 text="Clear Boxes",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record3.clearentrybox)
    clear_button1.grid(row=7, column=5, padx=10)


    date_label = lbl(b,
                                              text="Execute Above Mentioned Details Here ------------>",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_label.grid(row=7, column=0,)
