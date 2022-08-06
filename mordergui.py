import tkinter
import tkinter.messagebox
import customtkinter
import customer
import employee
import expense
import supplier
import inventory

import wrok_catogory
import inventory_purchase_sheet
import labour_purchase
import construction_cost
import labor_allocation
import interior_designing_material
import interior_designing_labor
import reciept
import payment
import customerreport
import supplierreport
import expense_allocation
import supplier_settlement
import supplierreport
import income_statement

import cashflow

import balance_sheet

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    WIDTH = 1500
    HEIGHT = 750

    def __init__(self):
        super().__init__()

        self.title("Capital Costruction and Interior desighning")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        # self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        # #self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        # self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        # self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing
        
        
        

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
       
        
        
        
        
        
    def record_book(self):
        
        
        
        
        
        self.frame_left_recordbook = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left_recordbook.grid(row=0, column=0, sticky="nswe")
        
        
        selecting(self.frame_left_recordbook)
    
    
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left_recordbook,
                                            text="Record Books",
                                            text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=2, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left_recordbook,
                                                text="Customer Record",
                                                command=self.button_event1)
        self.button_1.grid(row=3, column=0, pady=10, padx=20)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left_recordbook,
                                                text="Employee Record",
                                                command=self.button_event2)
        self.button_2.grid(row=4, column=0, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_left_recordbook,
                                                text="Expense Record",
                                                command=self.expensebtn)
        self.button_3.grid(row=5, column=0, pady=10, padx=20)
        
        self.button_4 = customtkinter.CTkButton(master=self.frame_left_recordbook,
                                                text="Inventory Record",
                                                command=self.inventory)
        self.button_4.grid(row=6, column=0, pady=10, padx=20)
        
        self.button_5 = customtkinter.CTkButton(master=self.frame_left_recordbook,
                                                text="Supplier Record",
                                                command=self.supplierbtn)
        self.button_5.grid(row=7, column=0, pady=10, padx=20)
        
        
        self.button_6 = customtkinter.CTkButton(master=self.frame_left_recordbook,
                                                text="Work Catogory Record",
                                                command=self.workbtn)
        self.button_6.grid(row=8, column=0, pady=10, padx=20)
            
        
        
        
        
        
    def day_book(self):
        
        self.frame_left_daybook = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left_daybook.grid(row=0, column=0, sticky="nswe")
        
        selecting(self.frame_left_daybook)
    
        self.label_2 = customtkinter.CTkLabel(master=self.frame_left_daybook,
                                            text="Day Book",
                                            text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_2.grid(row=2, column=0, pady=10, padx=10)
        
        self.button_7 = customtkinter.CTkButton(master=self.frame_left_daybook,
                                                text="Inventory Purchase",
                                                command=self.inv_purchase_btn)
        self.button_7.grid(row=3, column=0, pady=10, padx=20)
        
        
        self.button_8 = customtkinter.CTkButton(master=self.frame_left_daybook,
                                                text="Labor Purchase",
                                                command=self.labor_purchase_btn)
        self.button_8.grid(row=4, column=0, pady=10, padx=20)
        
        self.button_150 = customtkinter.CTkButton(master=self.frame_left_daybook,
                                                text="Supplier settlement",
                                                command=self.supplier_settlement_btn)
        self.button_150.grid(row=5, column=0, pady=10, padx=20)
    
        
        
        
        
        
    def cost_allocation(self):
        
        self.frame_left_cost = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left_cost.grid(row=0, column=0, sticky="nswe")
        
        selecting(self.frame_left_cost)
        
        self.label_3 = customtkinter.CTkLabel(master=self.frame_left_cost,
                                            text="Cost Allocation",
                                            text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_3.grid(row=2, column=0, pady=10, padx=10)
        
        
        self.button_9 = customtkinter.CTkButton(master=self.frame_left_cost,
                                                text="Material Allocation",
                                                command=self.constructionmaterial_btn)
        self.button_9.grid(row=3, column=0, pady=10, padx=20)
        
        self.button_13 = customtkinter.CTkButton(master=self.frame_left_cost,
                                                text="Labor Allocation",
                                                command=self.constructionlabor_btn)
        self.button_13.grid(row=4, column=0, pady=10, padx=20)
        
        self.button_10 = customtkinter.CTkButton(master=self.frame_left_cost,
                                                text="Expenses Allocation",
                                                command=self.expense_allocation_btn)
        self.button_10.grid(row=5, column=0, pady=10, padx=20)
        
      
    
    
    
        
        
        
    def cash_book(self):
        
        self.frame_left_cash = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left_cash.grid(row=0, column=0, sticky="nswe")
        
        selecting(self.frame_left_cash)
    
        self.label_4 = customtkinter.CTkLabel(master=self.frame_left_cash,
                                            text="Cash Book",
                                            text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_4.grid(row=2, column=0, pady=10, padx=10)
        
        
        self.button_11 = customtkinter.CTkButton(master=self.frame_left_cash,
                                                text="Reciept",
                                                command=self.reciept_btn)
        self.button_11.grid(row=3, column=0, pady=10, padx=20)
        
        self.button_12 = customtkinter.CTkButton(master=self.frame_left_cash,
                                                text="Payment",
                                                command=self.payment_btn)
        self.button_12.grid(row=4, column=0, pady=10, padx=20)
        
        
   
    
        
        # self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="")
        # self.label_mode.grid(row=15, column=0, pady=100, padx=20, sticky="w")

        

        # self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        # self.label_mode.grid(row=14, column=0, pady=0, padx=20, sticky="w")

        # self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
        #                                                 values=["Theme","Light", "Dark", "System"],
        #                                                 command=self.change_appearance_mode)
        # self.optionmenu_1.grid(row=15, column=0, pady=0, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        
    def report(self):
        
        self.frame_left_report = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left_report.grid(row=0, column=0, sticky="nswe")
        
        selecting(self.frame_left_report)
    
        self.label_40 = customtkinter.CTkLabel(master=self.frame_left_report,
                                            text="Report",
                                            text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_40.grid(row=2, column=0, pady=10, padx=10)
        
        self.button_41 = customtkinter.CTkButton(master=self.frame_left_report,
                                                text="Customer Report",
                                                command=self.customer_report_btn)
        self.button_41.grid(row=3, column=0, pady=10, padx=20)
        
        
        self.button_42 = customtkinter.CTkButton(master=self.frame_left_report,
                                                text="Supplier Report",
                                                command=self.supplier_report_btn)
        self.button_42.grid(row=4, column=0, pady=10, padx=20)
        
        self.button_43 = customtkinter.CTkButton(master=self.frame_left_report,
                                                text="Income Statement",
                                                command=self.income_statement_btn)
        self.button_43.grid(row=5, column=0, pady=10, padx=20)
        
        self.button_44 = customtkinter.CTkButton(master=self.frame_left_report,
                                                text="Position Statement",
                                                command=self.balance_sheeet_btn)
        self.button_44.grid(row=6, column=0, pady=10, padx=20)
        
        self.button_45 = customtkinter.CTkButton(master=self.frame_left_report,
                                                text="Cash Flow Statement",
                                                command=self.cashreport)
        self.button_45.grid(row=7, column=0, pady=10, padx=20)
        
        
        
        # self.button_60 = customtkinter.CTkButton(master=self.frame_left_report,
        #                                         text="Cash Flow Statement",
        #                                         command=self.supplier_report_btn)
        # self.button_60.grid(row=5, column=0, pady=10, padx=20)
    
        

        # self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
        #                                            text="CTkLabel: Lorem ipsum dolor sit,\n" +
        #                                                 "amet consetetur sadipscing elitr,\n" +
        #                                                 "sed diam nonumy eirmod tempor" ,
        #                                            height=100,
        #                                            fg_color=("white", "gray38"),  # <- custom tuple-color
        #                                            justify=tkinter.LEFT)
        # self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)

        # self.progressbar = customtkinter.CTkProgressBar(master=self.frame_info)
        # self.progressbar.grid(row=1, column=0, sticky="ew", padx=15, pady=15)

        # # ============ frame_right ============

        # self.radio_var = tkinter.IntVar(value=0)

        # self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
        #                                                 text="CTkRadioButton Group:")
        # self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=20, padx=10, sticky="")

        # self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        # self.radio_button_3 = customtkinter.CTkRadioButton(master=self.frame_right,
        #                                                    variable=self.radio_var,
        #                                                    value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # self.slider_1 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         from_=0,
        #                                         to=1,
        #                                         number_of_steps=3,
        #                                         command=self.progressbar.set)
        # self.slider_1.grid(row=4, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        # self.slider_2 = customtkinter.CTkSlider(master=self.frame_right,
        #                                         command=self.progressbar.set)
        # self.slider_2.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="we")

        # self.switch_1 = customtkinter.CTkSwitch(master=self.frame_right,
        #                                         text="CTkSwitch")
        # self.switch_1.grid(row=4, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.switch_2 = customtkinter.CTkSwitch(master=self.frame_right,
        #                                         text="CTkSwitch")
        # self.switch_2.grid(row=5, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.combobox_1 = customtkinter.CTkComboBox(master=self.frame_right,
        #                                             values=["Value 1", "Value 2"])
        # self.combobox_1.grid(row=6, column=2, columnspan=1, pady=10, padx=20, sticky="we")

        # self.check_box_1 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_1.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        # self.check_box_2 = customtkinter.CTkCheckBox(master=self.frame_right,
        #                                              text="CTkCheckBox")
        # self.check_box_2.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        
        # # set default values
        # self.optionmenu_1.set("Dark")
        # # self.button_3.configure(state="disabled", text="Disabled CTkButton")
        # self.combobox_1.set("CTkCombobox")
        # self.radio_button_1.select()
        # self.slider_1.set(0.2)
        # self.slider_2.set(0.7)
        # self.progressbar.set(0.5)
        # self.switch_2.select()
        # self.radio_button_3.configure(state=tkinter.DISABLED)
        # self.check_box_1.configure(state=tkinter.DISABLED, text="CheckBox disabled")
        # self.check_box_2.select()
    def sample(self):
        
        
        self.frame_right_customer = customtkinter.CTkFrame(master=self)
        self.frame_right_customer.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_customer.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_customer.rowconfigure(7, weight=10)
        self.frame_right_customer.columnconfigure((0, 1), weight=1)
        self.frame_right_customer.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_customer)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        customer.customer(self.frame_info, customtkinter.CTkLabel)
        customer.customer1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_customer, customtkinter.CTkComboBox)
        # customer1(, )
        
        self.record_book()
        
        
        # importing.customer(self.frame_info)
        
        
        # self.label_2 = customtkinter.CTkLabel(master=self.frame_right,
        #                                       text="Date",
        #                                       text_font=("Roboto Medium", -16))  # font name and size in px
        # self.label_2.grid(row=5, column=0, pady=10, padx=2)
        
        # self.entry_1 = customtkinter.CTkEntry(master=self.frame_right,
        #                                      width=10,
        #                                      placeholder_text="Date")
        # self.entry_1.grid(row=5, column=1, columnspan=1, pady=20, padx=20, sticky="we")

        # self.button_5 = customtkinter.CTkButton(master=self.frame_right,
        #                                          text="CTkButton",
        #                                          border_width=2,  # <- custom border_width
        #                                          fg_color=None,  # <- no fg_color
        #                                          command=self.button_event)
        # self.button_5.grid(row=5, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        
        
        
        
        
    def button_event(self):
        print("Button pressed")
    
    def button_event1(self):
        app.sample()
        
        
    def button_event2(self):
        self.frame_right_employee = customtkinter.CTkFrame(master=self)
        self.frame_right_employee.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_employee.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_employee.rowconfigure(7, weight=10)
        self.frame_right_employee.columnconfigure((0, 1), weight=1)
        self.frame_right_employee.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_employee)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        
        employee.employee(self.frame_info, customtkinter.CTkLabel)
        employee.employee1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_employee, customtkinter.CTkComboBox)
        # self.frame_right_customer.destroy()
        # self.frame_info_welcome.destroy()
        # self.frame_right_welcome.destroy()
        self.record_book()
        
    
    def expensebtn(self):
        self.frame_right_expense = customtkinter.CTkFrame(master=self)
        self.frame_right_expense.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_expense.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_expense.rowconfigure(7, weight=10)
        self.frame_right_expense.columnconfigure((0, 1), weight=1)
        self.frame_right_expense.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_expense)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        expense.expense(self.frame_info, customtkinter.CTkLabel)
        expense.expense1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_expense)
        
        self.record_book()
    
    
    def supplierbtn(self):
        self.frame_right_supplier = customtkinter.CTkFrame(master=self)
        self.frame_right_supplier.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_supplier.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_supplier.rowconfigure(7, weight=10)
        self.frame_right_supplier.columnconfigure((0, 1), weight=1)
        self.frame_right_supplier.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_supplier)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        supplier.supplier(self.frame_info, customtkinter.CTkLabel)
        supplier.supplier1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_supplier)
        
        self.record_book()
    
    
    def supplier_settlement_btn(self):
        self.frame_right_supplier_settlement = customtkinter.CTkFrame(master=self)
        self.frame_right_supplier_settlement.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_supplier_settlement.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_supplier_settlement.rowconfigure(7, weight=10)
        self.frame_right_supplier_settlement.columnconfigure((0, 1), weight=1)
        self.frame_right_supplier_settlement.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_supplier_settlement)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        
        
        supplier_settlement.sup(self.frame_info, customtkinter.CTkLabel)
        supplier_settlement.sup1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_supplier_settlement, customtkinter.CTkComboBox)
        
        self.day_book()
    
    def inventory(self):
        self.frame_right_inventory = customtkinter.CTkFrame(master=self)
        self.frame_right_inventory.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_inventory.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_inventory.rowconfigure(7, weight=10)
        self.frame_right_inventory.columnconfigure((0, 1), weight=1)
        self.frame_right_inventory.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_inventory)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        

        
        inventory.inventory(self.frame_info, customtkinter.CTkLabel,)
        inventory.inventory1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_inventory,customtkinter.CTkOptionMenu)
    
        self.record_book()
         
         
         
    def workbtn(self):
        self.frame_right_work = customtkinter.CTkFrame(master=self)
        self.frame_right_work.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_work.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_work.rowconfigure(7, weight=10)
        self.frame_right_work.columnconfigure((0, 1), weight=1)
        self.frame_right_work.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_work)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        wrok_catogory.work(self.frame_info, customtkinter.CTkLabel)
        wrok_catogory.work1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_work)
        
        self.record_book()
    
    
    def inv_purchase_btn(self):
        self.frame_right_inv_purchase = customtkinter.CTkFrame(master=self)
        self.frame_right_inv_purchase.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_inv_purchase.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_inv_purchase.rowconfigure(7, weight=10)
        self.frame_right_inv_purchase.columnconfigure((0, 1), weight=1)
        self.frame_right_inv_purchase.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_inv_purchase)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        
        inventory_purchase_sheet.inventory_purchase(self.frame_info, customtkinter.CTkLabel)
        inventory_purchase_sheet.inventory_purchase1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_inv_purchase, self.frame_info)
        
        self.day_book()
    
    def labor_purchase_btn(self):
        self.frame_right_inv_labor1 = customtkinter.CTkFrame(master=self)
        self.frame_right_inv_labor1.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_inv_labor1.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_inv_labor1.rowconfigure(7, weight=10)
        self.frame_right_inv_labor1.columnconfigure((0, 1), weight=1)
        self.frame_right_inv_labor1.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_inv_labor1)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        labour_purchase.labor(self.frame_info, customtkinter.CTkLabel)
        labour_purchase.labor1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_inv_labor1)
        
        self.day_book()
        
        
    
    def constructionmaterial_btn(self):

        
        
        self.frame_right_construction1 = customtkinter.CTkFrame(master=self)
        self.frame_right_construction1.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_construction1.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_construction1.rowconfigure(7, weight=10)
        self.frame_right_construction1.columnconfigure((0, 1), weight=1)
        self.frame_right_construction1.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_construction1)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        construction_cost.construction(self.frame_info, customtkinter.CTkLabel)
        construction_cost.construction1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_construction1)
    
        self.cost_allocation()
    
    try:
        def constructionlabor_btn(self):
        
        
            self.frame_right_construction2 = customtkinter.CTkFrame(master=self)
            self.frame_right_construction2.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

            self.frame_right_construction2.rowconfigure((0, 1, 2, 3), weight=1)
            self.frame_right_construction2.rowconfigure(7, weight=10)
            self.frame_right_construction2.columnconfigure((0, 1), weight=1)
            self.frame_right_construction2.columnconfigure(2, weight=0)

            self.frame_info = customtkinter.CTkFrame(master=self.frame_right_construction2)
            self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
            
            self.frame_info.rowconfigure(0, weight=1)
            self.frame_info.columnconfigure(0, weight=1)
            labor_allocation.construction_labor(self.frame_info, customtkinter.CTkLabel)
            labor_allocation.construction_labor1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_construction2)
        
        
            self.cost_allocation()
    except:
        pass   
    
    
    def expense_allocation_btn(self):
            try:
                 
                self.frame_right_construction3 = customtkinter.CTkFrame(master=self)
                self.frame_right_construction3.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

                self.frame_right_construction3.rowconfigure((0, 1, 2, 3), weight=1)
                self.frame_right_construction3.rowconfigure(7, weight=10)
                self.frame_right_construction3.columnconfigure((0, 1), weight=1)
                self.frame_right_construction3.columnconfigure(2, weight=0)

                self.frame_info = customtkinter.CTkFrame(master=self.frame_right_construction3)
                self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
                
                self.frame_info.rowconfigure(0, weight=1)
                self.frame_info.columnconfigure(0, weight=1)
                expense_allocation.construction(self.frame_info, customtkinter.CTkLabel)
                expense_allocation.construction1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_construction3)
            
            
                self.cost_allocation()
            except:
                pass
            
    def interior_designingmaterial_btn(self):
        pass
        
        # self.frame_right_construction3 = customtkinter.CTkFrame(master=self)
        # self.frame_right_construction3.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # self.frame_right_construction3.rowconfigure((0, 1, 2, 3), weight=1)
        # self.frame_right_construction3.rowconfigure(7, weight=10)
        # self.frame_right_construction3.columnconfigure((0, 1), weight=1)
        # self.frame_right_construction3.columnconfigure(2, weight=0)

        # self.frame_info = customtkinter.CTkFrame(master=self.frame_right_construction3)
        # self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        # self.frame_info.rowconfigure(0, weight=1)
        # self.frame_info.columnconfigure(0, weight=1)
        
        # interior_designing_material.interior_material(self.frame_info, customtkinter.CTkLabel)
        # interior_designing_material.interior_material1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_construction3)

        # self.cost_allocation()
    
    def interior_designinglabor_btn(self):
        
        pass
        # self.frame_right_construction4 = customtkinter.CTkFrame(master=self)
        # self.frame_right_construction4.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # self.frame_right_construction4.rowconfigure((0, 1, 2, 3), weight=1)
        # self.frame_right_construction4.rowconfigure(7, weight=10)
        # self.frame_right_construction4.columnconfigure((0, 1), weight=1)
        # self.frame_right_construction4.columnconfigure(2, weight=0)

        # self.frame_info = customtkinter.CTkFrame(master=self.frame_right_construction4)
        # self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        # self.frame_info.rowconfigure(0, weight=1)
        # self.frame_info.columnconfigure(0, weight=1)
        
        
        # interior_designing_labor.int_labor(self.frame_info, customtkinter.CTkLabel)
        # interior_designing_labor.int_labor1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_construction4)
        # self.cost_allocation()
    
    def reciept_btn(self):
        self.frame_right_construction5 = customtkinter.CTkFrame(master=self)
        self.frame_right_construction5.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_construction5.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_construction5.rowconfigure(7, weight=10)
        self.frame_right_construction5.columnconfigure((0, 1), weight=1)
        self.frame_right_construction5.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_construction5)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        reciept.recieptfn(self.frame_info, customtkinter.CTkLabel)
        reciept.recieptfn1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_construction5, customtkinter.CTkComboBox)
        self.cash_book()
    
    def payment_btn(self):
        self.frame_right_construction6 = customtkinter.CTkFrame(master=self)
        self.frame_right_construction6.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_construction6.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_construction6.rowconfigure(7, weight=10)
        self.frame_right_construction6.columnconfigure((0, 1), weight=1)
        self.frame_right_construction6.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_construction6)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        
        
        
        payment.paymentfn(self.frame_info, customtkinter.CTkLabel)
        payment.paymentfn1(customtkinter.CTkLabel, customtkinter.CTkEntry, customtkinter.CTkButton, self.frame_right_construction6, self.frame_info, customtkinter.CTkComboBox)
        self.cash_book()
    
    def pos_btn(self):
        
        pass
        # self.frame_right_construction7 = customtkinter.CTkFrame(master=self)
        # self.frame_right_construction7.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # self.frame_right_construction7.rowconfigure((0, 1, 2, 3), weight=1)
        # self.frame_right_construction7.rowconfigure(7, weight=10)
        # self.frame_right_construction7.columnconfigure((0, 1), weight=1)
        # self.frame_right_construction7.columnconfigure(2, weight=0)
    
    
    def customer_report_btn(self):
        self.frame_right_customer_report = customtkinter.CTkFrame(master=self)
        self.frame_right_customer_report.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_customer_report.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_customer_report.rowconfigure(7, weight=10)
        self.frame_right_customer_report.columnconfigure((0, 1), weight=1)
        self.frame_right_customer_report.columnconfigure(2, weight=0)
        
        
        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_customer_report)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        customerreport.searchentry(customtkinter.CTkEntry, self.frame_right_customer_report, customtkinter.CTkButton, self.frame_info, customtkinter.CTkLabel)
        
        self.report()
       
        
    def supplier_report_btn(self):
        
        self.frame_right_supplier_report = customtkinter.CTkFrame(master=self)
        self.frame_right_supplier_report.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_supplier_report.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_supplier_report.rowconfigure(7, weight=10)
        self.frame_right_supplier_report.columnconfigure((0, 1), weight=1)
        self.frame_right_supplier_report.columnconfigure(2, weight=0)
        
        
        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_supplier_report)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        supplierreport.searchentry(customtkinter.CTkEntry, self.frame_right_supplier_report, customtkinter.CTkButton, self.frame_info, customtkinter.CTkLabel)
        
        
        
        self.report()
        
    
    def income_statement_btn(self):
        
        self.frame_right_supplier_income_statement = customtkinter.CTkFrame(master=self)
        self.frame_right_supplier_income_statement.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_supplier_income_statement.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_supplier_income_statement.rowconfigure(7, weight=10)
        self.frame_right_supplier_income_statement.columnconfigure((0, 1), weight=1)
        self.frame_right_supplier_income_statement.columnconfigure(2, weight=0)
        
        
        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_supplier_income_statement)
        self.frame_info.grid(row=0, column=0, columnspan=1, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        income_statement.searchentry(customtkinter.CTkEntry, self.frame_right_supplier_income_statement, customtkinter.CTkButton, self.frame_info, customtkinter.CTkLabel)
        
        
        
        self.report()
        
        
    
    def cashreport(self):
        self.frame_right_cash_flow = customtkinter.CTkFrame(master=self)
        self.frame_right_cash_flow.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_cash_flow.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_cash_flow.rowconfigure(7, weight=10)
        self.frame_right_cash_flow.columnconfigure((0, 1), weight=1)
        self.frame_right_cash_flow.columnconfigure(2, weight=0)
        
        
        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_cash_flow)
        self.frame_info.grid(row=0, column=0, columnspan=6, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        cashflow.searchentry(customtkinter.CTkEntry, self.frame_right_cash_flow, customtkinter.CTkButton, self.frame_info, customtkinter.CTkLabel)
        
        
        
        self.report()
        
    def balance_sheeet_btn(self):
            
        self.frame_right_balance_sheet = customtkinter.CTkFrame(master=self)
        self.frame_right_balance_sheet.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_balance_sheet.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_balance_sheet.rowconfigure(7, weight=10)
        self.frame_right_balance_sheet.columnconfigure((0, 1), weight=1)
        self.frame_right_balance_sheet.columnconfigure(2, weight=0)
        
        
        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_balance_sheet)
        self.frame_info.grid(row=0, column=0, columnspan=1, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        balance_sheet.searchentry(customtkinter.CTkEntry, self.frame_right_balance_sheet, customtkinter.CTkButton, self.frame_info, customtkinter.CTkLabel)
        
        
        
        self.report()       
        
        
    
    

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()
        
    
    def welcome(self):
        
        self.frame_right_welcome = customtkinter.CTkFrame(master=self)
        self.frame_right_welcome.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right_welcome.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right_welcome.rowconfigure(7, weight=10)
        self.frame_right_welcome.columnconfigure((0, 1), weight=1)
        self.frame_right_welcome.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right_welcome)
        self.frame_info.grid(row=0, column=0, columnspan=7, rowspan=3, pady=20, padx=20, sticky="nsew")
        
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)
        
        mainlbl = customtkinter.CTkLabel(self.frame_info, text="Welcome to Capital Construction and Interior Designing")
        mainlbl.grid(column = 0, row = 4)
        
        self.label_mode = customtkinter.CTkLabel(master=self.frame_info, text="Appearance Mode:")
        self.label_mode.grid(row=2, column=0, pady=0, padx=0)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_info,
                                                        values=["Theme","Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=3, column=0, pady=20, padx=20)
        
        
        
        
        self.label_mode1 = customtkinter.CTkLabel(master=self.frame_right_welcome, text="Record Book:")
        self.label_mode1.grid(row=3, column=0, pady=0, padx=0)
        
        self.button_1 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Customer Record",
                                                command=self.button_event1)
        self.button_1.grid(row=3, column=1, pady=10, padx=20)
        
        self.button_2 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Employee Record",
                                                command=self.button_event2)
        self.button_2.grid(row=3, column=2, pady=10, padx=20)

        self.button_3 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Expense Record",
                                                command=self.expensebtn)
        self.button_3.grid(row=3, column=3, pady=10, padx=20)
        
        self.button_4 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Inventory Record",
                                                command=self.inventory)
        self.button_4.grid(row=3, column=4, pady=10, padx=20)
        
        self.button_5 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Supplier Record",
                                                command=self.supplierbtn)
        self.button_5.grid(row=3, column=5, pady=10, padx=20)
        
        
        self.button_6 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Work Catogory Record",
                                                command=self.workbtn)
        self.button_6.grid(row=3, column=6, pady=10, padx=20)

        
        
        
        
        self.label_mode1 = customtkinter.CTkLabel(master=self.frame_right_welcome, text="Day Book:")
        self.label_mode1.grid(row=4, column=0, pady=0, padx=0)
        
        
        self.button_7 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Inventory Purchase",
                                                command=self.inv_purchase_btn)
        self.button_7.grid(row=4, column=1, pady=10, padx=20)
        
        
        self.button_8 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Labor Purchase",
                                                command=self.labor_purchase_btn)
        self.button_8.grid(row=4, column=2, pady=10, padx=20)
        
        
        
        self.label_mode1 = customtkinter.CTkLabel(master=self.frame_right_welcome, text="Cost Allocation:")
        self.label_mode1.grid(row=5, column=0, pady=0, padx=0)
        
        
        
        self.button_9 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Mterial Allocation",
                                                command=self.constructionmaterial_btn)
        self.button_9.grid(row=5, column=1, pady=10, padx=20)
        
        self.button_10 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Expenses Allocation",
                                                command=self.expense_allocation_btn)
        self.button_10.grid(row=5, column=3, pady=10, padx=20)
        
        
        
        self.button_13 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Labor Allocation",
                                                command=self.constructionlabor_btn)
        self.button_13.grid(row=5, column=2, pady=10, padx=20)
        

    
    
        
        
        
        self.label_mode1 = customtkinter.CTkLabel(master=self.frame_right_welcome, text="Cash Book:")
        self.label_mode1.grid(row=6, column=0, pady=0, padx=0)
        
        self.button_11 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Reciept",
                                                command=self.reciept_btn)
        self.button_11.grid(row=6, column=1, pady=10, padx=20)
        
        self.button_12 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Payment",
                                                command=self.payment_btn)
        self.button_12.grid(row=6, column=2, pady=10, padx=20)
        
        
        
        
        
        
        self.label_40 = customtkinter.CTkLabel(master=self.frame_right_welcome,
                                            text="Report",
                                            text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_40.grid(row=7, column=0, pady=10, padx=10)
        
        self.button_41 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Customer Report",
                                                command=self.customer_report_btn)
        self.button_41.grid(row=7, column=1, pady=10, padx=20)
        
        
        self.button_42 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Supplier Report",
                                                command=self.supplier_report_btn)
        self.button_42.grid(row=7, column=2, pady=10, padx=20)
        
        # self.button_60 = customtkinter.CTkButton(master=self.frame_right_welcome,
        #                                         text="Cash Flow Statement",
        #                                         command=self.supplier_report_btn)
        # self.button_60.grid(row=7, column=3, pady=10, padx=20)
              
        self.button_43 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Income Statement",
                                                command=self.income_statement_btn)
        self.button_43.grid(row=7, column=3, pady=10, padx=20)
        
        self.button_44 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Position Statement",
                                                command=self.balance_sheeet_btn)
        self.button_44.grid(row=7, column=4, pady=10, padx=20)
        
        self.button_45 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Cash Flow Statement",
                                                command=self.cashreport)
        self.button_45.grid(row=7, column=5, pady=10, padx=20)
        
        
        self.button_150 = customtkinter.CTkButton(master=self.frame_right_welcome,
                                                text="Supplier settlement",
                                                command=self.supplier_settlement_btn)
        self.button_150.grid(row=4, column=3, pady=10, padx=20)
    
        
        
    
    




if __name__ == "__main__":
    app = App()
    app.welcome()
    
    
    
    def select1(res):
        
        # res1 = optionmenu_3.get()
        # print(res)
        
        if res == "Record Book":
            
            # app.frame_left_cash.destroy()
            # app.frame_left_cost.destroy()
            # app.frame_left_daybook.destroy()
            app.record_book()
            
            
            
            
        if res == "Day Book":
            # app.frame_left_cost.destroy()
            # app.frame_left_cash.destroy()
            # app.frame_left_recordbook.destroy()
            app.day_book()
           
        
        if res == "Cost Allocation":
            # app.frame_left_daybook.destroy()
            # app.frame_left_cash.destroy()
            # app.frame_left_recordbook.destroy()
            app.cost_allocation()
           
        if res == "Cash Book":
            # app.frame_left_cost.destroy()
            # app.frame_left_cost.destroy()
            # app.frame_left_recordbook.destroy()
            app.cash_book()
        
        if res == "Home":
            app.welcome()
            
        if res == "Report":
            app.report()
    
      
    def selecting(x=app.frame_left):
        
        optionmenu_3 = customtkinter.CTkOptionMenu(x,
                                                            values=["Home", "Cash Book","Record Book", "Day Book", "Cost Allocation", "Report"],
                                                            command= select1)
        optionmenu_3.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        
        
        
    
    selecting()
            
    
    
    
    
    # def select2(res):
            
    #         # res1 = optionmenu_3.get()
    #         # print(res)
            
    #         if res == "Material Allocation":
    #             app.constructionmaterial_btn()
                
                
                
                
    #         if res == "Labor Allocation":
    #             pass
              
            
    #         if res == "Overhead Allocation":
    #             pass
            
    

    # def selecting1(x=app.frame_right_construction1):
        
    #     optionmenu_4 = customtkinter.CTkOptionMenu(x,
    #                                                         values=["Material Allocation", "Labor Allocation", "Overhead Allocation"],
    #                                                         command= select2)
    #     optionmenu_4.grid(row=3, column=3, pady=10, padx=20, sticky="w")
            
    
    # selecting1()
                
 
    
            
    app.mainloop()
    
