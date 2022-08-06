
from tkinter import *
from tkinter import ttk
import datetime

import test3
import time

import tkinter.messagebox
import customtkinter








win = Tk()
win.geometry("1500x750")
win.title("Sabik- Construction company application")




date_and_time = datetime.date.today()
date1 = str(date_and_time)
notebook1 = ttk.Notebook(win)
notebook1.pack()

note_frame1 = Frame(notebook1)
note_frame = Frame(notebook1)
note_frame6 = Frame(notebook1)
note_frame2 = Frame(notebook1)
note_frame3 = Frame(notebook1)
note_frame4 = Frame(notebook1)



note_frame1.pack(fill="both", expand=1)
note_frame.pack(fill="both", expand=1)
note_frame6.pack(fill="both", expand=1)
note_frame2.pack(fill="both", expand=1)
note_frame3.pack(fill="both", expand=1)
note_frame4.pack(fill="both", expand=1)

notebook1.add(note_frame1, text="Customer and Employee Record Book")
notebook1.add(note_frame, text="Expenses Record Book")
notebook1.add(note_frame6, text="Supplier Record Book")
notebook1.add(note_frame2, text="Reciepts and Payments")
notebook1.add(note_frame3, text="General Reports")
notebook1.add(note_frame4, text="Customer Reports")


# create scroll bar






#######################################################################################################################

# mainlbl = Label(note_frame1, text="Record Book", font="bold", background="grey", foreground="white")
# mainlbl.pack(fill="x", anchor=W)

datalbl1 = Label(note_frame1, text="Customer Record", background="darkgrey", foreground="white")
datalbl1.pack(fill="x", pady=10)
data_frame = LabelFrame(note_frame1, text="Customer Record Book", background="lightgrey")
data_frame.pack(fill="x",)

datalbl2 = Label(note_frame1, text="Employee Record", background="darkgrey", foreground="white")
datalbl2.pack(fill="x", pady=10)
data_frame2 = LabelFrame(note_frame1, text="Employee Record Book", background="lightgrey")
data_frame2.pack(fill="x",)

datalbl3 = Label(note_frame, text="Expense Record", background="darkgrey", foreground="white")
datalbl3.pack(fill="x", pady=10)
data_frame3= LabelFrame(note_frame, text="Expense Record Book", background="lightgrey")
data_frame3.pack(fill="x",)

datalbl4 = Label(note_frame2, text="Reciept and Payment", background="darkgrey", foreground="white")
datalbl4.pack(fill="x", pady=10)
data_frame4= LabelFrame(note_frame2, text="Reciept and payment", background="lightgrey")
data_frame4.pack(fill="x",)

datalbl6 = Label(note_frame6, text="Supplier Record", background="darkgrey", foreground="white")
datalbl6.pack(fill="x", pady=10)
data_frame6= LabelFrame(note_frame6, text="Supplier Record Book", background="lightgrey")
data_frame6.pack(fill="x",)





# add some style
style = ttk.Style()


# pick a theme
style.theme_use('default')


# configure the treeview colors
style.configure("Treeview", background="#D3D3D3", foreground="darkgrey", rowheight=25, fieldbackground="#D3D3D3")

# change selected color
style.map("Treeview", background=[('selected', "#347083")])

# create a treeview


# x = data_frame

def customer1(x, b):

    tree_frame1 = Frame(x)
    tree_frame1.grid(padx=10, pady=10, row=0, column=6, rowspan=11)


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
    my_tree1.column("date_and_time", anchor=W, width=100)
    my_tree1.column("customer_name", anchor=W, width=100)
    my_tree1.column("address", anchor=CENTER, width=100 )
    my_tree1.column("phone", anchor=CENTER, width=70)
    my_tree1.column("pincode", anchor=CENTER, width=50)
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
    my_tree1.tag_configure('oddrow', background="lightgrey", foreground="darkgreen")
    my_tree1.tag_configure('evenrow', background="grey", foreground="darkblue")



    # add record entry boxes 





    date_label = customtkinter.CTkLabel(b,
                                              text="Date",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_label.grid(row=5, column=0)
    dateentry = customtkinter.CTkEntry(b,
                                             width=10,
                                             placeholder_text="Date")
    dateentry.grid(row=5, column=1, columnspan=1, pady=20, padx=20, sticky="we")

    # def set_time():
    #     dateentry.delete(0, END)
    #     dateentry.insert(0, date1)
    # timebtn = Button(x, text="Today", command=set_time, background="darkgrey", foreground="blue")
    # timebtn.grid(row=0, column=2)
    date_inst = customtkinter.CTkLabel(b,
                                              text="Date",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_inst.grid(row=6, column=0)



    date_entry = customtkinter.CTkEntry(b,
                                             width=10,
                                             placeholder_text="Date")
    date_entry.grid(row=6, column=1, columnspan=1, pady=20, padx=20, sticky="we")


    name_label = customtkinter.CTkLabel(b,
                                              text="Date",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    name_label.grid(row=7, column=0, padx=10, )
    name_entry = customtkinter.CTkEntry(b,
                                             width=10,
                                             placeholder_text="Date")
    name_entry.grid(row=7, column=1, columnspan=1, pady=20, padx=20, sticky="we")


    address_label = customtkinter.CTkLabel(b,
                                              text="Date",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    address_label.grid(row=8, column=0, padx=10, )
    address_entry = customtkinter.CTkEntry(b,
                                             width=10,
                                             placeholder_text="Date")
    address_entry.grid(row=8, column=1, columnspan=1, pady=20, padx=20, sticky="we")


    phone_label = customtkinter.CTkLabel(b,
                                              text="Date",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    phone_label.grid(row=9, column=0, padx=10, )
    phone_entry =customtkinter.CTkEntry(b,
                                             width=10,
                                             placeholder_text="Date")
    phone_entry.grid(row=9, column=1, columnspan=1, pady=20, padx=20, sticky="we")


    pincode_label = customtkinter.CTkLabel(b,
                                              text="Date",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    pincode_label.grid(row=10, column=0, padx=10, )
    pincode_entry = customtkinter.CTkEntry(b,
                                             width=10,
                                             placeholder_text="Date")
    pincode_entry.grid(row=10, column=1, columnspan=1, pady=20, padx=20, sticky="we")

    estimate_label = customtkinter.CTkLabel(b,
                                              text="Date",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    estimate_label.grid(row=11, column=0, padx=10, )
    estimate_entry = customtkinter.CTkEntry(b,
                                             width=10,
                                             placeholder_text="Date")
    estimate_entry.grid(row=11, column=1, columnspan=1, pady=20, padx=20, sticky="we")

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
            dateentry.insert(0, values[1])
            name_entry.insert(0, values[2])
            address_entry.insert(0, values[3])
            phone_entry.insert(0, values[4])
            pincode_entry.insert(0, values[5])
            estimate_entry.insert(0, values[6])
            
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
        
        def fetching(self):
            data = test3.dbfetch()
            # mylb.delete(0, END)
            # mylb.insert(0, "Fetched data from database to the table")
            
            count = 0
            
            
            for i in data:
                
                if count % 2 == 0:
                    my_tree1.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]), tags=("evenrow",))
                    
                else:
                    my_tree1.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], [5], i[6]), tags=("oddrow",))
                
                # increment counter
                count += 1
            
            
            
        
    record1 = Record_handling()
    # bind
    my_tree1.bind("<ButtonRelease-1>", record1.select_record)

    # buttons

    add_button = customtkinter.CTkButton(b,
                                                 text="CTkButton",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.entering)
    add_button.grid(row=3, column=5, padx=10)

    del_button = customtkinter.CTkButton(b,
                                                 text="CTkButton",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.deleting)
    del_button.grid(row=4, column=5, padx=10)

    update_button = customtkinter.CTkButton(b,
                                                 text="CTkButton",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.updating)
    update_button.grid(row=5, column=5, padx=10)

    # show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
    # show_button.grid(row=5, column=5, padx=10)

    record1.fetching()

    clear_button = customtkinter.CTkButton(master=b,
                                                 text="CTkButton",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record1.clearentrybox)
    clear_button.grid(row=6, column=5, padx=10)




    # balance_label = Label(data_frame, text="Balance", background="lightgrey")
    # balance_label.grid(row=4, column=0, padx=10, )
    # balance_entry = Entry(data_frame)
    # balance_entry.grid(row=1, column=3, padx=10, )
    # #####################################################################################################################################
# customer1(data_frame, data_frame)

tree_frame2 = Frame(data_frame2)
tree_frame2.grid(padx=10, pady=10, row=0, column=6, rowspan=11)


# create scroll bar
tree_scroll3 = Scrollbar(tree_frame2)
tree_scroll3.pack(side=RIGHT, fill=Y)


# create the treeview
my_tree2 = ttk.Treeview(tree_frame2, yscrollcommand=tree_scroll3.set, selectmode="extended")
my_tree2.pack()



# configure the scroll bar
tree_scroll3.config(command=my_tree2.yview)

# define our columns
my_tree2['columns'] = ("id","date_and_time", "employee_name", "address", "phone", "pincode")

# format our columns
my_tree2.column("#0", width=0, stretch=NO)
my_tree2.column("id", anchor=CENTER, width=50)
my_tree2.column("date_and_time", anchor=W, width=140)
my_tree2.column("employee_name", anchor=W, width=140)
my_tree2.column("address", anchor=CENTER, width=100 )
my_tree2.column("phone", anchor=CENTER, width=140)
my_tree2.column("pincode", anchor=CENTER, width=140)


# create Headings
my_tree2.heading("#0", text="", anchor=W)
my_tree2.heading("id", text="ID", anchor=CENTER)
my_tree2.heading("date_and_time", text="Date", anchor=W)
my_tree2.heading("employee_name", text="Employee Name", anchor=W)
my_tree2.heading("address", text="Address", anchor=CENTER)
my_tree2.heading("phone", text="Phone", anchor=CENTER)
my_tree2.heading("pincode", text="Pincode", anchor=CENTER)
# create striped row tags
my_tree2.tag_configure('oddrow', background="lightgrey", foreground="darkgreen")
my_tree2.tag_configure('evenrow', background="grey", foreground="darkblue")



# add record entry boxes 






dateentry1 = Entry(data_frame2)
dateentry1.grid(row=0, column=1, columnspan=2, sticky=W, padx=10)





# date_entry = Entry(data_frame)
# date_entry.grid(row=0, column=1, padx=10, )


name_label1 = Label(data_frame2, text="Employee Name", background="lightgrey")
name_label1.grid(row=1, column=0, padx=10, )
name_entry1 = Entry(data_frame2)
name_entry1.grid(row=1, column=1, padx=10, sticky=W)


address_label1 = Label(data_frame2, text="Employee Address", background="lightgrey")
address_label1.grid(row=2, column=0, padx=10, )
address_entry1 = Entry(data_frame2, width=62)
address_entry1.grid(row=2, column=1, padx=10, columnspan=3, sticky=W)


phone_label1 = Label(data_frame2, text="Phone", background="lightgrey")
phone_label1.grid(row=1, column=2, padx=10, )
phone_entry1 = Entry(data_frame2)
phone_entry1.grid(row=1, column=3, padx=10, )


pincode_label1 = Label(data_frame2, text="Pincode", background="lightgrey")
pincode_label1.grid(row=1, column=4, padx=10, )
pincode_entry1 = Entry(data_frame2)
pincode_entry1.grid(row=1, column=5, padx=10, )

info_label1 = Label(data_frame2, text="Information Box", background="lightgrey")
info_label1.grid(row=3, column=2)
mylb3 = Listbox(data_frame2, width=90, background="darkgrey", height=8)
mylb3.grid(row=4, column=0, columnspan=5, rowspan=4)

# functions

test3.dbconnectemp()

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
        dateentry1.insert(0, values[1])
        name_entry1.insert(0, values[2])
        address_entry1.insert(0, values[3])
        phone_entry1.insert(0, values[4])
        pincode_entry1.insert(0, values[5])
        
        #output listbox
        
        mylb3.delete(0, END)
        mylb3.insert(0, f"Employee Details {values}")
        # mylb.insert(1, values[2])
        # mylb.insert(2, values[3])
        

    def clearentrybox(self):
        # clear box
        
        dateentry1.delete(0, END)
        name_entry1.delete(0, END)
        address_entry1.delete(0, END)
        phone_entry1.delete(0, END)
        pincode_entry1.delete(0, END)
        
        mylb3.delete(0,END)
    
    
    def entering(self):
        # try:

        mylb3.delete(0, END)
        
        
        test3.dbentryemp(dateentry1.get(), name_entry1.get(), address_entry1.get(), phone_entry1.get(), pincode_entry1.get())
        mylb3.insert(0, "New Data into the Database created")
        
        my_tree2.delete(*my_tree2.get_children())
        
        record3.fetching()
        
        dateentry1.delete(0, END)
        name_entry1.delete(0, END)
        address_entry1.delete(0, END)
        phone_entry1.delete(0, END)
        pincode_entry1.delete(0, END)
        # except:
        #     mylb.insert(0, "Boxes Cannot be Blank")
    
    
    def deleting(self):
        
        selected = my_tree2.focus()
        values = my_tree2.item(selected, "values")
        test3.dbdeleteemp(values[0])
        my_tree2.delete(*my_tree2.get_children())
        
        record3.fetching()
        
        dateentry1.delete(0, END)
        name_entry1.delete(0, END)
        address_entry1.delete(0, END)
        phone_entry1.delete(0, END)
        pincode_entry1.delete(0, END)
        mylb3.delete(0, END)
        mylb3.insert(0, "One item is delted from database")
        
    
    def updating(self):
        selected = my_tree2.focus()
        values = my_tree2.item(selected, "values")
    
        test3.dbupdateemp(dateentry1.get(), name_entry1.get(), address_entry1.get(), phone_entry1.get(), pincode_entry1.get(), values[0])
        
        my_tree2.delete(*my_tree2.get_children())
        
        record3.fetching()
        
        dateentry1.delete(0, END)
        name_entry1.delete(0, END)
        address_entry1.delete(0, END)
        phone_entry1.delete(0, END)
        pincode_entry1.delete(0, END)
        mylb3.delete(0, END)
        mylb3.insert(0, "One item is updated from database")
    
    def fetching(self):
        data = test3.dbfetchemp()
        mylb3.delete(0, END)
        mylb3.insert(0, "Fetched data from database to the table")
        
        count = 0
        
        
        for i in data:
            
            if count % 2 == 0:
                my_tree2.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=("evenrow",))
                
            else:
                my_tree2.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], [5]), tags=("oddrow",))
            
            # increment counter
            count += 1
        
        
        
    
record3 = Employee_handling()
# bind
my_tree2.bind("<ButtonRelease-1>", record3.select_record)

# buttons

add_button1 = Button(data_frame2, text="Add", width=10, command=record3.entering)
add_button1.grid(row=3, column=5, padx=10)

del_button1 = Button(data_frame2, text="Remove", width=10, command=record3.deleting)
del_button1.grid(row=4, column=5, padx=10)

update_button1 = Button(data_frame2, text="Update", width=10, command=record3.updating)
update_button1.grid(row=5, column=5, padx=10)

# show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
# show_button.grid(row=5, column=5, padx=10)

record3.fetching()

clear_button1 = Button(data_frame2, text="Clear Boxes", width=10, command=record3.clearentrybox)
clear_button1.grid(row=6, column=5, padx=10)





######################################################################################################################################

#####################################################################################################################################


tree_frame3 = Frame(data_frame3)
tree_frame3.grid(padx=10, pady=10, row=0, column=6, rowspan=11)


# create scroll bar
tree_scroll4 = Scrollbar(tree_frame3)
tree_scroll4.pack(side=RIGHT, fill=Y)


# create the treeview
my_tree3 = ttk.Treeview(tree_frame3, yscrollcommand=tree_scroll4.set, selectmode="extended")
my_tree3.pack()



# configure the scroll bar
tree_scroll4.config(command=my_tree3.yview)

# define our columns
my_tree3['columns'] = ("id", "expense_name", "discription")

# format our columns
my_tree3.column("#0", width=0, stretch=NO)
my_tree3.column("id", anchor=CENTER, width=50)
my_tree3.column("expense_name", anchor=W, width=140)
my_tree3.column("discription", anchor=W, width=350)



# create Headings
my_tree3.heading("#0", text="", anchor=W)
my_tree3.heading("id", text="ID", anchor=CENTER)
my_tree3.heading("expense_name", text="Expense Name", anchor=W)
my_tree3.heading("discription", text="Discription", anchor=W)

# create striped row tags
my_tree3.tag_configure('oddrow', background="lightgrey", foreground="darkgreen")
my_tree3.tag_configure('evenrow', background="grey", foreground="darkblue")



# add record entry boxes 





# date_label2 = Label(data_frame3, text=f"Date and Time:", background="lightgrey")
# date_label2.grid(row=0, column=0)
# dateentry2 = Entry(data_frame3)
# dateentry2.grid(row=0, column=1, columnspan=2, sticky=W, padx=10)

# def set_time():
#     dateentry2.delete(0, END)
#     dateentry2.insert(0, date1)
# timebtn2 = Button(data_frame3, text="Today", command=set_time, background="darkgrey", foreground="blue")
# timebtn2.grid(row=0, column=2)
# date_inst = Label(data_frame3, text="Date format: Year - Month - Day", background="lightgrey")
# date_inst.grid(row=0, column=3)



# date_entry = Entry(data_frame)
# date_entry.grid(row=0, column=1, padx=10, )


name_label2 = Label(data_frame3, text="Expense Name", background="lightgrey")
name_label2.grid(row=1, column=0, padx=10, )
name_entry2 = Entry(data_frame3)
name_entry2.grid(row=1, column=1, padx=10, sticky=W)


address_label2 = Label(data_frame3, text="Discription", background="lightgrey")
address_label2.grid(row=2, column=0, padx=10, )
address_entry2 = Entry(data_frame3, width=62)
address_entry2.grid(row=2, column=1, padx=10, columnspan=3, sticky=W)



info_label2 = Label(data_frame3, text="Information Box", background="lightgrey")
info_label2.grid(row=3, column=2)
mylb4 = Listbox(data_frame3, width=90, background="darkgrey", height=8)
mylb4.grid(row=4, column=0, columnspan=5, rowspan=4)

# functions

test3.dbconnectexp()

class Expense_handling:
    def select_record(self, e):
        # clear box
    
        name_entry2.delete(0, END)
        address_entry2.delete(0, END)
    
        
        # Grab record number
        selected = my_tree3.focus()
        values = my_tree3.item(selected, "values")
        
        #output entrybox
        
        try:
    
            name_entry2.insert(0, values[1])
            address_entry2.insert(0, values[2])
        except:
            print("error detected")
        
        
        #output listbox
        
        mylb4.delete(0, END)
        mylb4.insert(0, f"Employee Details {values}")
        # mylb.insert(1, values[2])
        # mylb.insert(2, values[3])
        

    def clearentrybox(self):
        # clear box
        
        
        name_entry2.delete(0, END)
        address_entry2.delete(0, END)
    
        mylb4.delete(0,END)
    
    
    def entering(self):
        # try:

        mylb4.delete(0, END)
        
        
        test3.dbentryexp(name_entry2.get(), address_entry2.get())
        mylb4.insert(0, "New Data into the Database created")
        
        my_tree3.delete(*my_tree3.get_children())
        
        record4.fetching()
        
    
        name_entry2.delete(0, END)
        address_entry2.delete(0, END)
    
        # except:
        #     mylb.insert(0, "Boxes Cannot be Blank")
    
    
    def deleting(self):
        
        selected = my_tree3.focus()
        values = my_tree3.item(selected, "values")
        test3.dbdeleteexp(values[0])
        my_tree3.delete(*my_tree3.get_children())
        
        record4.fetching()
        

        name_entry2.delete(0, END)
        address_entry2.delete(0, END)
    
        mylb4.delete(0, END)
        mylb4.insert(0, "One item is delted from database")
        
    
    def updating(self):
        selected = my_tree3.focus()
        values = my_tree3.item(selected, "values")
        try:
    
            test3.dbupdatexp(name_entry2.get(), address_entry2.get(), values[0])
        except:
            print("Error detected")
        
        my_tree3.delete(*my_tree3.get_children())
        
        record4.fetching()
        
        
        name_entry2.delete(0, END)
        address_entry2.delete(0, END)
    
        mylb4.delete(0, END)
        mylb4.insert(0, "One item is updated from database")
    
    def fetching(self):
        data = test3.dbfetchexp()
        mylb4.delete(0, END)
        mylb4.insert(0, "Fetched data from database to the table")
        
        count = 0
        
        try:
            for i in data:
                
                if count % 2 == 0:
                    my_tree3.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2]), tags=("evenrow",))
                    
                else:
                    my_tree3.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2]), tags=("oddrow",))
                
                # increment counter
                count += 1
        except:
            print("error detected")
        
        
        
    
record4 = Expense_handling()
# bind
my_tree3.bind("<ButtonRelease-1>", record4.select_record)

# buttons

add_button2 = Button(data_frame3, text="Add", width=10, command=record4.entering)
add_button2.grid(row=3, column=5, padx=10)

del_button2 = Button(data_frame3, text="Remove", width=10, command=record4.deleting)
del_button2.grid(row=4, column=5, padx=10)

update_button2 = Button(data_frame3, text="Update", width=10, command=record4.updating)
update_button2.grid(row=5, column=5, padx=10)

# show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
# show_button.grid(row=5, column=5, padx=10)

record4.fetching()

clear_button2 = Button(data_frame3, text="Clear Boxes", width=10, command=record4.clearentrybox)
clear_button2.grid(row=6, column=5, padx=10)





######################################################################################################################################

# Reciept Handling

#####################################################################################################################################


tree_frame4 = Frame(data_frame4)
tree_frame4.grid(padx=10, pady=10, row=0, column=6, rowspan=11)


# create scroll bar
tree_scroll5 = Scrollbar(tree_frame4)
tree_scroll5.pack(side=RIGHT, fill=Y)


# create the treeview
my_tree4 = ttk.Treeview(tree_frame4, yscrollcommand=tree_scroll4.set, selectmode="extended")
my_tree4.pack()



# configure the scroll bar
tree_scroll5.config(command=my_tree4.yview)

# define our columns
my_tree4['columns'] = ("id","date", "customer_name", "discription", "customer_id", "employee_name", "discription1", "employee_id", "amount")

# format our columns
my_tree4.column("#0", width=0, stretch=NO)
my_tree4.column("id", anchor=CENTER, width=100)
my_tree4.column("date", anchor=W, width=100)
my_tree4.column("customer_name", anchor=W, width=100)
my_tree4.column("discription", anchor=W, width=100)
my_tree4.column("customer_id", anchor=W, width=50)
my_tree4.column("employee_name", anchor=W, width=100)
my_tree4.column("discription1", anchor=W, width=100)
my_tree4.column("employee_id", anchor=W, width=50)
my_tree4.column("amount", anchor=W, width=100)


# create Headings
my_tree4.heading("#0", text="", anchor=W)
my_tree4.heading("id", text="ID", anchor=CENTER)
my_tree4.heading("date", text="Date", anchor=W)
my_tree4.heading("customer_name", text="Customer Name", anchor=W)
my_tree4.heading("discription", text="Discription", anchor=W)
my_tree4.heading("customer_id", text="CID", anchor=W)
my_tree4.heading("employee_name", text="Employee Name", anchor=W)
my_tree4.heading("discription1", text="Discription", anchor=W)
my_tree4.heading("employee_id", text="EID", anchor=W)
my_tree4.heading("amount", text="Amount", anchor=W)


# create striped row tags
my_tree4.tag_configure('oddrow', background="lightgrey", foreground="darkgreen")
my_tree4.tag_configure('evenrow', background="grey", foreground="darkblue")



# add record entry boxes 





# date_label2 = Label(data_frame3, text=f"Date and Time:", background="lightgrey")
# date_label2.grid(row=0, column=0)
# dateentry2 = Entry(data_frame3)
# dateentry2.grid(row=0, column=1, columnspan=2, sticky=W, padx=10)

# def set_time():
#     dateentry2.delete(0, END)
#     dateentry2.insert(0, date1)
# timebtn2 = Button(data_frame3, text="Today", command=set_time, background="darkgrey", foreground="blue")
# timebtn2.grid(row=0, column=2)
# date_inst = Label(data_frame3, text="Date format: Year - Month - Day", background="lightgrey")
# date_inst.grid(row=0, column=3)

def updatelb(data):
    lb15.delete(0, END)
    for item in data:
        lb15.insert(END, item)

def fillout(e):
    li14 = test3.dbfetch()
    

    
    address_entry3.delete(0, END)
 
    myentry.delete(0, END)
    name_entry3.delete(0, END)
    foreignkey1.delete(0, END)
    
    myentry.insert(0, lb15.get(ANCHOR))
    name_entry3.insert(0, lb15.get(ANCHOR))
    for i in li14:
        if lb15.get(ANCHOR) in i:
            address_entry3.insert(0, i)
            foreignkey1.insert(0, i[0])

    
def check(e):
    li14 = test3.dbfetch()
    li15 = []

    for i in li14:
        print(i[2])
        li15.append(i[2])
        
        
    typed = myentry.get()
    if typed == '':
        data = li15
    else:
        data = []
        for item in li15:
            if typed.lower() in item.lower():
                data.append(item)
    updatelb(data)

lbl1 = Label(data_frame4, text="Select Customer", background="lightgrey")
lbl1.grid(row=14, column=0, pady=10, padx=10)

myentry = Entry(data_frame4)
myentry.grid(row=15, column=0, padx=10, pady=10)


lb15 = Listbox(data_frame4)
lb15.grid(row=14, column=1, rowspan=5, padx=10, pady=10)


# updatelb(li15)



lb15.bind("<<ListboxSelect>>", fillout)

myentry.bind("<KeyRelease>", check)


####################################################################
def updatelb1(data):
    lb16.delete(0, END)
    for item in data:
        lb16.insert(END, item)

def fillout1(e):
    li16 = test3.dbfetchemp()
    

    
    address_entrye3.delete(0, END)
 
    myentry1.delete(0, END)
    name_entrye3.delete(0, END)
    foreignkeye1.delete(0, END)
    
    myentry1.insert(0, lb16.get(ANCHOR))
    name_entrye3.insert(0, lb16.get(ANCHOR))
    for i in li16:
        if lb16.get(ANCHOR) in i:
            address_entrye3.insert(0, i)
            foreignkeye1.insert(0, i[0])

    
def check1(e):
    li16 = test3.dbfetchemp()
    li17 = []

    for i in li16:
        print(i[2])
        li17.append(i[2])
        
        
    typed = myentry1.get()
    if typed == '':
        data = li17
    else:
        data = []
        for item in li17:
            if typed.lower() in item.lower():
                data.append(item)
    updatelb1(data)

lbl2 = Label(data_frame4, text="Select Employee", background="lightgrey")
lbl2.grid(row=21, column=0, pady=10, padx=10)

myentry1 = Entry(data_frame4)
myentry1.grid(row=22, column=0, padx=10, pady=10)


lb16 = Listbox(data_frame4)
lb16.grid(row=20, column=1, rowspan=5, padx=10, pady=10)


# updatelb(li15)

lb16.bind("<<ListboxSelect>>", fillout1)

myentry1.bind("<KeyRelease>", check1)


##########################################################################




















# date_entry = Entry(data_frame)
# date_entry.grid(row=0, column=1, padx=10, )

dateentry3 = Entry(data_frame4)
dateentry3.grid(row=0, column=1, sticky=W, padx=10)

dateentry3.insert(0, date1)

name_label3 = Label(data_frame4, text="Customer Name", background="lightgrey")
name_label3.grid(row=1, column=0, padx=10, )
name_entry3 = Entry(data_frame4)
name_entry3.grid(row=1, column=1, padx=10, sticky=W)


address_label3 = Label(data_frame4, text="Discription", background="lightgrey")
address_label3.grid(row=2, column=0, padx=10, )
address_entry3 = Entry(data_frame4, width=62)
address_entry3.grid(row=2, column=1, padx=10, columnspan=3, sticky=W, pady=5)

foreignkey1 = Entry(data_frame4, width=2)
foreignkey1.grid(row=2, column=4, padx=5)

name_labele3 = Label(data_frame4, text="Employee Name", background="lightgrey")
name_labele3.grid(row=4, column=0, padx=10, )
name_entrye3 = Entry(data_frame4)
name_entrye3.grid(row=4, column=1, padx=10, sticky=W)


address_labele3 = Label(data_frame4, text="Discription", background="lightgrey")
address_labele3.grid(row=5, column=0, padx=10, )
address_entrye3 = Entry(data_frame4, width=62)
address_entrye3.grid(row=5, column=1, padx=10, columnspan=3, sticky=W)

foreignkeye1 = Entry(data_frame4, width=2)
foreignkeye1.grid(row=5, column=4, padx=5)

amtlbl = Label(data_frame4, text="Amount", background="lightgrey")
amtlbl.grid(row=7, column=0)
amt = Entry(data_frame4)
amt.grid(row=7, column=1, sticky=W, padx=10)


info_label3 = Label(data_frame4, text="Information Box", background="lightgrey")
info_label3.grid(row=8, column=2)
mylb5 = Listbox(data_frame4, width=90, background="darkgrey", height=8)
mylb5.grid(row=9, column=0, columnspan=5, rowspan=4)

# functions

test3.dbconnectreciept()

class Reciept_handling:
    def select_record(self, e):
        # clear box
        dateentry3.delete(0, END)
        name_entry3.delete(0, END)
        address_entry3.delete(0, END)
        foreignkey1.delete(0, END)
        name_entrye3.delete(0, END)
        address_entrye3.delete(0, END)
        foreignkeye1.delete(0, END)
        amt.delete(0, END)
    
        
        # Grab record number
        selected = my_tree4.focus()
        values = my_tree4.item(selected, "values")
        
        #output entrybox
        dateentry3.insert(0, values[1])
        name_entry3.insert(0, values[2])
        address_entry3.insert(0, values[3])
        foreignkey1.insert(0, values[4])
        name_entrye3.insert(0, values[5])
        address_entrye3.insert(0, values[6])
        foreignkeye1.insert(0, values[7])
        amt.insert(0, values[8])
        
        
        #output listbox
        
        mylb5.delete(0, END)
        mylb5.insert(0, f"Employee Details {values}")
        # mylb.insert(1, values[2])
        # mylb.insert(2, values[3])
        

    def clearentrybox(self):
        # clear box
        
        
        dateentry3.delete(0, END)
        name_entry3.delete(0, END)
        address_entry3.delete(0, END)
        foreignkey1.delete(0, END)
        name_entrye3.delete(0, END)
        address_entrye3.delete(0, END)
        foreignkeye1.delete(0, END)
        amt.delete(0, END)
    
        mylb5.delete(0,END)
    
    
    def entering(self):
        # try:

        mylb5.delete(0, END)
        
        
        test3.dbentryreciept(dateentry3.get(), name_entry3.get(), address_entry3.get(), foreignkey1.get(), name_entrye3.get(), address_entrye3.get(), foreignkeye1.get(), amt.get() )
        mylb5.insert(0, "New Data into the Database created")
        
        my_tree4.delete(*my_tree4.get_children())
        
        record5.fetching()
        
    
        dateentry3.delete(0, END)
        name_entry3.delete(0, END)
        address_entry3.delete(0, END)
        foreignkey1.delete(0, END)
        name_entrye3.delete(0, END)
        address_entrye3.delete(0, END)
        foreignkeye1.delete(0, END)
        amt.delete(0, END)
        # except:
        #     mylb.insert(0, "Boxes Cannot be Blank")
    
    
    def deleting(self):
        
        selected = my_tree4.focus()
        values = my_tree4.item(selected, "values")
        try:
            test3.dbdeletereciept(values[0])
        except:
            print("error detected")
        my_tree4.delete(*my_tree4.get_children())
        
        record4.fetching()
        

        dateentry3.delete(0, END)
        name_entry3.delete(0, END)
        address_entry3.delete(0, END)
        foreignkey1.delete(0, END)
        name_entrye3.delete(0, END)
        address_entrye3.delete(0, END)
        foreignkeye1.delete(0, END)
        amt.delete(0, END)
        mylb5.delete(0, END)
        mylb5.insert(0, "One item is delted from database")
        
    
    def updating(self):
        selected = my_tree4.focus()
        values = my_tree4.item(selected, "values")
    
        test3.dbupdatereciept(dateentry3.get(), name_entry3.get(), address_entry3.get(), foreignkey1.get(), name_entrye3.get(), address_entrye3.get(), foreignkeye1.get(), amt.get() ,values[0])
        
        my_tree4.delete(*my_tree4.get_children())
        
        record5.fetching()
        
        
        dateentry3.delete(0, END)
        name_entry3.delete(0, END)
        address_entry3.delete(0, END)
        foreignkey1.delete(0, END)
        name_entrye3.delete(0, END)
        address_entrye3.delete(0, END)
        foreignkeye1.delete(0, END)
        amt.delete(0, END)
    
        mylb5.delete(0, END)
        mylb5.insert(0, "One item is updated from database")
    
    def fetching(self):
        data = test3.dbfetchreciept()
        mylb5.delete(0, END)
        mylb5.insert(0, "Fetched data from database to the table")
        
        count = 0
        
        
        for i in data:
            
            if count % 2 == 0:
                my_tree4.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]), tags=("evenrow",))
                
            else:
                my_tree4.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]), tags=("oddrow",))
            
            # increment counter
            count += 1
        
        
        
    
record5 = Reciept_handling()
# bind
my_tree4.bind("<ButtonRelease-1>", record5.select_record)

# buttons

add_button3 = Button(data_frame4, text="Add", width=10, command=record5.entering)
add_button3.grid(row=3, column=5, padx=10)

del_button3 = Button(data_frame4, text="Remove", width=10, command=record5.deleting)
del_button3.grid(row=4, column=5, padx=10)

update_button3 = Button(data_frame4, text="Update", width=10, command=record5.updating)
update_button3.grid(row=5, column=5, padx=10)

# show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
# show_button.grid(row=5, column=5, padx=10)

record5.fetching()

clear_button3 = Button(data_frame4, text="Clear Boxes", width=10, command=record5.clearentrybox)
clear_button3.grid(row=6, column=5, padx=10)





######################################################################################################################################

######################################################################################################################################


################################### from here onwards
################################### ...........................................







tree_frame6 = Frame(data_frame6)
tree_frame6.grid(padx=10, pady=10, row=0, column=6, rowspan=11)


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
my_tree6.tag_configure('oddrow', background="lightgrey", foreground="darkgreen")
my_tree6.tag_configure('evenrow', background="grey", foreground="darkblue")



# add record entry boxes 





date_label6 = Label(data_frame6, text=f"Date and Time:", background="lightgrey")
date_label6.grid(row=0, column=0)
dateentry6 = Entry(data_frame6)
dateentry6.grid(row=0, column=1, columnspan=2, sticky=W, padx=10)

def set_time():
    dateentry6.delete(0, END)
    dateentry6.insert(0, date1)
timebtn6 = Button(data_frame6, text="Today", command=set_time, background="darkgrey", foreground="blue")
timebtn6.grid(row=0, column=2)
date_inst6 = Label(data_frame6, text="Date format: Year - Month - Day", background="lightgrey")
date_inst6.grid(row=0, column=3)



# date_entry = Entry(data_frame)
# date_entry.grid(row=0, column=1, padx=10, )


name_label6 = Label(data_frame6, text="Supplier Name", background="lightgrey")
name_label6.grid(row=1, column=0, padx=10, )
name_entry6 = Entry(data_frame6)
name_entry6.grid(row=1, column=1, padx=10, sticky=W)


address_label6 = Label(data_frame6, text="Supplier Address", background="lightgrey")
address_label6.grid(row=2, column=0, padx=10, )
address_entry6 = Entry(data_frame6, width=62)
address_entry6.grid(row=2, column=1, padx=10, columnspan=3, sticky=W)


phone_label6 = Label(data_frame6, text="Phone", background="lightgrey")
phone_label6.grid(row=1, column=2, padx=10, )
phone_entry6 = Entry(data_frame6)
phone_entry6.grid(row=1, column=3, padx=10, )


pincode_label6 = Label(data_frame6, text="Pincode", background="lightgrey")
pincode_label6.grid(row=1, column=4, padx=10, )
pincode_entry6 = Entry(data_frame6)
pincode_entry6.grid(row=1, column=5, padx=10, )

info_label6 = Label(data_frame6, text="Information Box", background="lightgrey")
info_label6.grid(row=3, column=2)
mylb6= Listbox(data_frame6, width=90, background="darkgrey", height=8)
mylb6.grid(row=4, column=0, columnspan=5, rowspan=4)

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
        
        mylb6.delete(0, END)
        mylb6.insert(0, f"Supplier Details {values}")
        # mylb.insert(1, values[2])
        # mylb.insert(2, values[3])
        

    def clearentrybox(self):
        # clear box
        
        dateentry6.delete(0, END)
        name_entry6.delete(0, END)
        address_entry6.delete(0, END)
        phone_entry6.delete(0, END)
        pincode_entry6.delete(0, END)
        
        mylb6.delete(0,END)
    
    
    def entering(self):
        # try:

        mylb6.delete(0, END)
        
        
        test3.dbentrysup(dateentry6.get(), name_entry6.get(), address_entry6.get(), phone_entry6.get(), pincode_entry6.get())
        mylb6.insert(0, "New Data into the Database created")
        
        my_tree6.delete(*my_tree6.get_children())
        
        record6.fetching()
        
        dateentry6.delete(0, END)
        name_entry6.delete(0, END)
        address_entry6.delete(0, END)
        phone_entry6.delete(0, END)
        pincode_entry6.delete(0, END)
        # except:
        #     mylb.insert(0, "Boxes Cannot be Blank")
    
    
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
        mylb6.delete(0, END)
        mylb6.insert(0, "One item is delted from database")
        
    
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
        mylb6.delete(0, END)
        mylb6.insert(0, "One item is updated from database")
    
    def fetching(self):
        data = test3.dbfetchsup()
        mylb6.delete(0, END)
        mylb6.insert(0, "Fetched data from database to the table")
        
        count = 0
        
        
        for i in data:
            
            if count % 2 == 0:
                my_tree6.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], i[5]), tags=("evenrow",))
                
            else:
                my_tree6.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4], [5]), tags=("oddrow",))
            
            # increment counter
            count += 1
        
        
        
    
record6 = supplier_handling()
# bind
my_tree6.bind("<ButtonRelease-1>", record6.select_record)

# buttons

add_button6 = Button(data_frame6, text="Add", width=10, command=record6.entering)
add_button6.grid(row=3, column=5, padx=10)

del_button6 = Button(data_frame6, text="Remove", width=10, command=record6.deleting)
del_button6.grid(row=4, column=5, padx=10)

update_button6 = Button(data_frame6, text="Update", width=10, command=record6.updating)
update_button6.grid(row=5, column=5, padx=10)

clear_button6 = Button(data_frame6, text="Clear Boxes", width=10, command=record6.clearentrybox)
clear_button6.grid(row=6, column=5, padx=10)

# show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
# show_button.grid(row=5, column=5, padx=10)

record6.fetching()






# balance_label = Label(data_frame, text="Balance", background="lightgrey")
# balance_label.grid(row=4, column=0, padx=10, )
# balance_entry = Entry(data_frame)
# balance_entry.grid(row=1, column=3, padx=10, )



########################################################################################################################################



########################################################################################################################################
#########################################################################################################################################



creportlbl = Label(note_frame4, text="Search customer report")
creportlbl.pack()

creportentry = Entry(note_frame4)
creportentry.pack()

def calc():
    a = test3.dbfetch()

    ares = 0
    name1 = ''
    for i in a:
        
        ares = i[6]
        name1 = i[2]
        print(i[6])

    b = test3.dbfetchreciept()
    bres = 0

    for i in b:
    
        bres = i[8]
        print(i[8])


    res1 = int(ares) -  int(bres)

    reportlabel = Label(note_frame4, text=f"Customer {name1} have paid {bres} towards his estimate {ares} and he have a balance of {res1}")
    reportlabel.pack()
    ########################################################################################################################################

b1 = Button(note_frame4, text="click", command=calc)
b1.pack()


win.mainloop()