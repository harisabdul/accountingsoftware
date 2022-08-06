
from tkinter import *
from tkinter import ttk
import datetime
import test3

import databaseinv


date_and_time = datetime.date.today()
date1 = str(date_and_time)


def inventory(x, lbl):
    global my_tree3
    
    label1 = lbl(x, text="Inventory Record Book")
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
    
    
    tree_frame3 = Frame(x)
    tree_frame3.grid(padx=10, pady=10, row=1, column=0, rowspan=11)


    # create scroll bar
    tree_scroll4 = Scrollbar(tree_frame3)
    tree_scroll4.pack(side=RIGHT, fill=Y)


    # create the treeview
    my_tree3 = ttk.Treeview(tree_frame3, yscrollcommand=tree_scroll4.set, selectmode="extended")
    my_tree3.pack()



    # configure the scroll bar
    tree_scroll4.config(command=my_tree3.yview)

    # define our columns
    my_tree3['columns'] = ("id", "inventory_name", "discription", "cost", "unit")

    # format our columns
    my_tree3.column("#0", width=0, stretch=NO)
    my_tree3.column("id", anchor=CENTER, width=50)
    my_tree3.column("inventory_name", anchor=W, width=140)
    my_tree3.column("discription", anchor=W, width=350)
    my_tree3.column("cost", anchor=CENTER, width=50)
    my_tree3.column("unit", anchor=CENTER, width=50)



    # create Headings
    my_tree3.heading("#0", text="", anchor=W)
    my_tree3.heading("id", text="ID", anchor=CENTER)
    my_tree3.heading("inventory_name", text="Inventory Name", anchor=W)
    my_tree3.heading("discription", text="Discription", anchor=W)
    my_tree3.heading("cost", text="Cost", anchor=CENTER)
    my_tree3.heading("unit", text="Unit", anchor=CENTER)

    # create striped row tags
    my_tree3.tag_configure('oddrow', background="white", foreground="darkgreen")
    my_tree3.tag_configure('evenrow', background="white", foreground="darkblue")




def inventory1(lbl, ent, btn, b, opt):
    
    
    
    date_label = lbl(b,
                                              text="Execute Above Mentioned Details Here ------------>",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
    date_label.grid(row=7, column=0,)
    
    

    name_entry2 = ent(b,
                                             width=10,
                                             placeholder_text="Name of Inventory")
    name_entry2.grid(row=3, column=0, columnspan=1, pady=0, padx=20, sticky="we")



    address_entry2 = ent(b,
                                             width=10,
                                             placeholder_text="Discription")
    address_entry2.grid(row=4, column=0, columnspan=4, pady=0, padx=20, sticky="we")


    cost_entry2 = ent(b,
                                             width=10,
                                             placeholder_text="Cost")
    cost_entry2.grid(row=3, column=1, columnspan=1, pady=0, padx=20, sticky="we")
    
    optionmenu_2 = opt(b,
                                                        values=["Unit", "Pcs", "Kg", "Ltr", "Pkt"])
    optionmenu_2.grid(row=3, column=2, pady=0, padx=20, sticky="w")



    # functions

    databaseinv.dbconnectinv()

    class Inventory_handling:
        def select_record(self, e):
            # clear box
        
            name_entry2.delete(0, END)
            address_entry2.delete(0, END)
            cost_entry2.delete(0, END)
        
            
            # Grab record number
            selected = my_tree3.focus()
            values = my_tree3.item(selected, "values")
            
            #output entrybox
            
            try:
        
                name_entry2.insert(0, values[1])
                address_entry2.insert(0, values[2])
                cost_entry2.insert(0, values[3])
            except:
                print("error detected")
            
            
            #output listbox
            
            
            # mylb.insert(1, values[2])
            # mylb.insert(2, values[3])
            

        def clearentrybox(self):
            # clear box
            
            
            name_entry2.delete(0, END)
            address_entry2.delete(0, END)
            cost_entry2.delete(0, END)
        
          
        
        
        def entering(self):
            # try:

            
            
            databaseinv.dbentryinv(name_entry2.get(), address_entry2.get(), cost_entry2.get(), optionmenu_2.get())
    
            my_tree3.delete(*my_tree3.get_children())
            
            record4.fetching()
            
        
            name_entry2.delete(0, END)
            address_entry2.delete(0, END)
            cost_entry2.delete(0, END)
        
            # except:
            #     mylb.insert(0, "Boxes Cannot be Blank")
        
        
        def deleting(self):
            
            selected = my_tree3.focus()
            values = my_tree3.item(selected, "values")
            databaseinv.dbdeleteinv(values[0])
            my_tree3.delete(*my_tree3.get_children())
            
            record4.fetching()
            

            name_entry2.delete(0, END)
            address_entry2.delete(0, END)
            cost_entry2.delete(0, END)
        
        
            
        
        def updating(self):
            selected = my_tree3.focus()
            values = my_tree3.item(selected, "values")
            try:
        
                databaseinv.dbupdatinv(name_entry2.get(), address_entry2.get(), cost_entry2.get(), optionmenu_2.get(), values[0])
            except:
                print("Error detected")
            
            my_tree3.delete(*my_tree3.get_children())
            
            record4.fetching()
            
            
            name_entry2.delete(0, END)
            address_entry2.delete(0, END)
            cost_entry2.delete(0, END)
        
      
        
        def fetching(self):
            data = databaseinv.dbfetchinv()
          
            count = 0
            
            try:
                for i in data:
                    
                    if count % 2 == 0:
                        my_tree3.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4]), tags=("evenrow",))
                        
                    else:
                        my_tree3.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3], i[4]), tags=("oddrow",))
                    
                    # increment counter
                    count += 1
            except:
                print("error detected")
            
            
            
        
    record4 = Inventory_handling()
    # bind
    my_tree3.bind("<ButtonRelease-1>", record4.select_record)

    # buttons

    add_button2 = btn(b,
                                                 text="Add",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record4.entering)
    add_button2.grid(row=7, column=2, padx=10)

    del_button2 = btn(b,
                                                 text="Remove",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record4.deleting)
    del_button2.grid(row=7, column=3, padx=10)

    update_button2 = btn(b,
                                                 text="Update",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record4.updating)
    update_button2.grid(row=7, column=4, padx=10)

    # show_button = Button(data_frame, text="Show", width=10, command=record1.fetching)
    # show_button.grid(row=5, column=5, padx=10)

    record4.fetching()

    clear_button2 = btn(b,
                                                 text="Clear Boxes",
                                                 border_width=2,  # <- custom border_width
                                                 fg_color=None,  # <- no fg_color
                                                 command=record4.clearentrybox)
    clear_button2.grid(row=7, column=5, padx=10)



    
