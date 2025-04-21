# Employing tkinter star import to access several methods.
# Importing colorchooser to access color customization in panels.
# Importing 'os' as an abstraction with the Operating System.
# Importing showinfo to access messagebox options.
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter.messagebox import showinfo
import sqlite3
import os

def register(): # Function that handles user registration when prompted.
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("User Registration")
    register_screen.geometry("300x270")
    register_screen.configure(background="light blue")
    register_screen.iconbitmap('GUI Icon.ico')
    register_screen.resizable(False, False)
    register_screen.attributes("-topmost", True)
    register_screen.grab_set()
    register_screen.focus_set()

    # Variables declared as 'global' to be defined on other usage.
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="", bg="light blue").pack()
    Label(register_screen, text="Enter details below:", bg="light blue", font=("Century gothic bold", 12)).pack()
    Label(register_screen, text="", bg="light blue").pack()
    username_lable = Label(register_screen, text="Username", bg="light blue", font=("Century gothic", 11))
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password", bg="light blue", font=("Century gothic", 11))
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="", bg="light blue").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="white", font=("Century gothic bold", 10), command = register_user).pack()
    # Passing of command with a lambda to avoid defining another function.
    register_screen.bind('<Return>', lambda event=None: register_user())
    
def login(): # Function that handles user log-ins.
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.configure(background="light blue")
    Label(login_screen, text="", bg="light blue").pack()
    Label(login_screen, text="Enter details below:", bg="light blue", font=("Century gothic bold", 12)).pack()
    Label(login_screen, text="", bg="light blue").pack()
    login_screen.iconbitmap('GUI Icon.ico')
    login_screen.resizable(False, False)
    # Prioritizes focus on this window when many is called.
    login_screen.grab_set()
    login_screen.focus_set()    

    # Variables declared as 'global' to be defined on other usage.
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username", bg="light blue", font=("Century gothic", 11)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", bg="light blue").pack()
    Label(login_screen, text="Password", bg="light blue", font=("Century gothic", 11)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="", bg="light blue").pack()
    Button(login_screen, text="Login", width=10, height=1, bg="white", font=("Century gothic bold", 10), command = login_verify).pack()
    # Passing of command with a lambda to avoid defining another function.
    login_screen.bind('<Return>', lambda event=None: login_verify())
    
def register_user(): # Tallies recorded user data on a textfile.
    username_info = username.get()
    password_info = password.get()

    # Generates and writes on the textfile with the username and password input. File is named after the username.
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    # Deletes entry input when data from user registration has been recorded.
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    Label(register_screen, text="", bg="light blue").pack()
    Label(register_screen, text="Registration Success!", fg="black", font=("Century gothic", 12)).pack()   
 
def login_verify(): # Verifies username/password combination and allows the next window to pass if proven correct.
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    # Inspects all files in the specified diretory (in this case, the same location as the .py file)
    list_of_files = os.listdir()
    if username1 in list_of_files: # Opens the textfiles in the directory and looks for a matching username/password combination, prompting windows depending on the conditions set by the following if-else statement.
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()
 
    else:
        user_not_found()
        
def login_sucess(): # The main menu window of FinMan that has all the features.
    login_screen.destroy()
    main_screen.destroy()
    class FinMan(ttk.Frame): # class that inherits the ttk Frame method.
        def __init__(self, master, name, number, balance, debt, incomeflow, interest): # Initializes all values.
            super().__init__(master)
            self.master = master
            self.master.title("FinMan™")
            self.master.configure(background="light blue")
            self.window_width = 400
            self.window_height = 260
            self.screen_width = self.master.winfo_screenwidth()
            self.screen_height = self.master.winfo_screenheight()
            self.center_x = int(self.screen_width/2 - self.window_width/2)
            self.center_y = int(self.screen_height/2 - self.window_height/2)
            self.master.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')
            self.master.attributes('-alpha', 1)
            self.master.iconbitmap('GUI Icon.ico')
            self.master.resizable(False, False)
            self.master.focus_force() # Focus is strictly forced in this window after successful log-in.
            
            Label(self.master, text="FinMan™", bg="sky blue", width="300", height="1", font=("Century gothic", 18)).pack()
            Label(self.master, text="Manage your money, manage your dreams.", bg="sky blue", width="300", height="1", font=("Century gothic bold", 11), pady=10).pack()
            Label(self.master, text="", bg="light blue", height="1").pack()
            FinManButton = Button(self.master, text="Manage Financial Info", height="1", width="30", bg="white", font=("Century gothic bold", 10), command=self.finmancrud).pack()
            Label(self.master, text="", bg="light blue", height="1").pack()
            RECButton = Button(self.master, text="Real Estate Calculations", height="1", width="30", bg="white", font=("Century gothic bold", 10), command=self.showformulas).pack()
            Label(self.master, text="", bg="light blue", height="1").pack()
            CalculatorButton = Button(self.master, text="Calculator", height="1", width="30", bg="white", font=("Century gothic bold", 10), command=self.showcalculator).pack()
        # Create Treeview Method
        def finmancrud(self): 
            global finmanroot
            finmanroot = Toplevel(self.master)
            finmanroot.title("Financial Information Management")
            finmanroot.geometry("1000x550")
            finmanroot.iconbitmap('GUI Icon.ico')
            finmanroot.grab_set()
            finmanroot.focus_set()
            finmanroot.configure(background="light blue")
            #Clear Tree View
            def query_database():
                for record in my_tree.get_children():
                    my_tree.delete(record)
                # Create or Connect to a database
                conn = sqlite3.connect('FinMan.db')
                # Create cursor instance
                c = conn.cursor()  
                # Get database records
                c.execute("SELECT rowid, * FROM accounts")
                records = c.fetchall()
                # Declare a variable to 0
                global count
                count = 0
                # Create loop that changes the database colors according to row
                for record in records:
                	if count % 2 == 0:
                		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
                	else:
                		my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
                    # Increment counter
                	count += 1
                # Commit the changes
                conn.commit()
                # Always close the connection
                conn.close()

            def search_records():
                lookup_record = search_entry.get()
                # Close search box
                search.destroy()
                # Clear Tree View
                for record in my_tree.get_children():
                    my_tree.delete(record)
                # Create or Connect to a database  
                conn = sqlite3.connect('FinMan.db')
                # Create cursor instance
                c = conn.cursor()  
                # Get database records where Profile Number is to be searched
                c.execute("SELECT rowid, * FROM accounts WHERE prof_num = ?", (lookup_record,))
                records = c.fetchall()
                # Show data to the screen
                global count
                count = 0

                for record in records:
                    if count % 2 == 0:
                    	my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('evenrow',))
                    else:
                    	my_tree.insert(parent='', index='end', iid=count, text='', values=(record[1], record[2], record[0], record[4], record[5], record[6], record[7]), tags=('oddrow',))
                    # Increment counter
                    count += 1
                # Commit the changes
                conn.commit()
                # Always close the connection
                conn.close()

            def lookup_records():
                global search, search_entry
                search = Toplevel(finmanroot)
                search.title("Lookup Records")
                search.geometry("400x200")
                
                # Create label frame
                search_frame = LabelFrame(search, bg="sky blue", text= "Profile Number")
                search_frame.pack(padx=10, pady=10)
                
                # Add entry box
                search_entry = Entry(search_frame, font=("Helvetica", 18))
                search_entry.pack(pady=20, padx=20)
                
                # Add button
                search_button = Button(search, text="Search Records", command=search_records)
                search_button.pack(padx=20, pady=20)
                
            def primary_color():
                # Color selector
            	primary_color = colorchooser.askcolor()[1]
                
                # Update Treeview color
            	if primary_color:
                    # Create Striped Row Tags
            		my_tree.tag_configure('evenrow', background=primary_color)


            def secondary_color():
                # Color selector
            	secondary_color = colorchooser.askcolor()[1]
            	
                # Update Treeview color
            	if secondary_color:
                    # Create Striped Row Tags
            		my_tree.tag_configure('oddrow', background=secondary_color)
            		

            def highlight_color():
                # Color selector
            	highlight_color = colorchooser.askcolor()[1]
                # Update Treeview Color
            	# Change Selected Color
            	if highlight_color:
            		style.map('Treeview',
            			background=[('selected', highlight_color)])
            
            # Add Menu
            my_menu = Menu(finmanroot)
            finmanroot.config(menu=my_menu)
            
            # Configure Menu
            option_menu = Menu(my_menu, tearoff=1)
            my_menu.add_cascade(label="Options", menu=option_menu)
            
            # Create drop down for Menu
            option_menu.add_command(label="Primary Color", command=primary_color)
            option_menu.add_command(label="Secondary Color", command=secondary_color)
            option_menu.add_command(label="Highlight Color", command=highlight_color)
            option_menu.add_separator()
            option_menu.add_command(label="Exit", command=finmanroot.quit)

            # Search Menu
            search_menu = Menu(my_menu, tearoff=0)
            my_menu.add_cascade(label="Search", menu=search_menu)
            search_menu.add_command(label="Search", command=lookup_records)
            search_menu.add_separator()
            search_menu.add_command(label="Reset", command=query_database)
            
            # Create or Connect to a database
            conn = sqlite3.connect('FinMan.db')
            # Create cursor instance
            c = conn.cursor()
            # Create Table
            c.execute("""CREATE TABLE if not exists accounts ( 
                    prof_name text,
                    prof_num integer,
                    id integer,
                    balance float,
                    debt float,
                    cashflow float,
                    interest float)
                      """)
            # Commit the changes
            conn.commit()
            # Always close the connection
            conn.close()
            # Add Some Style
            style = ttk.Style()
            # Choose Style Theme
            style.theme_use('default')
            
            #Configure Treeview colors
            style.configure("Treeview",
            	background="#D3D3D3",
            	foreground="black",
            	rowheight=25,
            	fieldbackground="#D3D3D3")
            
            # Change selected color
            style.map('Treeview',
            	background=[('selected', "#347083")])

            # Create frame for Treeview
            tree_frame = Frame(finmanroot)
            tree_frame.pack(pady=10)
            
            # Create scrollbar for Treeview
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)
            
            # Create the Treeview
            my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
            my_tree.pack()
            
            # Configure the Treeview scrollbar
            tree_scroll.config(command=my_tree.yview)
            # Define columns of the Treeview
            my_tree['columns'] = ("Profile Name", "Profile Number", "ID", "Balance", "Debt", "Cash Flow", "Interest")
            
            # Format columns in the Treeview
            my_tree.column("#0", width=0, stretch=NO)
            my_tree.column("Profile Name", anchor=W, width=140)
            my_tree.column("Profile Number", anchor=W, width=140)
            my_tree.column("ID", anchor=CENTER, width=100)
            my_tree.column("Balance", anchor=CENTER, width=140)
            my_tree.column("Debt", anchor=CENTER, width=140)
            my_tree.column("Cash Flow", anchor=CENTER, width=140)
            my_tree.column("Interest", anchor=CENTER, width=140)
            
            # Create Treeview Headings
            my_tree.heading("#0", text="", anchor=W)
            my_tree.heading("Profile Name", text="Profile Name", anchor=W)
            my_tree.heading("Profile Number", text="Profile Number", anchor=W)
            my_tree.heading("ID", text="ID", anchor=CENTER)
            my_tree.heading("Balance", text="Balance", anchor=CENTER)
            my_tree.heading("Debt", text="Debt", anchor=CENTER)
            my_tree.heading("Cash Flow", text="Cash Flow", anchor=CENTER)
            my_tree.heading("Interest", text="Interest", anchor=CENTER)
            
            # Create Treeview Striped Row Tags
            my_tree.tag_configure('oddrow', background="white")
            my_tree.tag_configure('evenrow', background="lightblue")
            
            # Add Record Entry Boxes
            data_frame = LabelFrame(finmanroot, bg="sky blue", text="Record")
            data_frame.pack(fill="x", expand="yes", padx=20)

            pname_label = Label(data_frame, text="Profile Name", fg="white", bg="#B22222")
            pname_label.grid(row=0, column=0, padx=10, pady=10)
            pname_entry = Entry(data_frame)
            pname_entry.grid(row=0, column=1, padx=10, pady=10)

            pnum_label = Label(data_frame, text="Profile Number", fg="white", bg="#B22222")
            pnum_label.grid(row=0, column=2, padx=10, pady=10)
            pnum_entry = Entry(data_frame)
            pnum_entry.grid(row=0, column=3, padx=10, pady=10)

            id_label = Label(data_frame, text="ID", fg="white", bg="#B22222")
            id_label.grid(row=0, column=4, padx=10, pady=10)
            id_entry = Entry(data_frame)
            id_entry.grid(row=0, column=5, padx=10, pady=10)

            bal_label = Label(data_frame, text="Balance", fg="white", bg="#B22222")
            bal_label.grid(row=1, column=0, padx=10, pady=10)
            bal_entry = Entry(data_frame)
            bal_entry.grid(row=1, column=1, padx=10, pady=10)

            deb_label = Label(data_frame, text="Debt", fg="white", bg="#B22222")
            deb_label.grid(row=1, column=2, padx=10, pady=10)
            deb_entry = Entry(data_frame)
            deb_entry.grid(row=1, column=3, padx=10, pady=10)

            cflow_label = Label(data_frame, text="Cash Flow", fg="white", bg="#B22222")
            cflow_label.grid(row=1, column=4, padx=10, pady=10)
            cflow_entry = Entry(data_frame)
            cflow_entry.grid(row=1, column=5, padx=10, pady=10)

            intrst_label = Label(data_frame, text="Interest", fg="white", bg="#B22222")
            intrst_label.grid(row=1, column=6, padx=10, pady=10)
            intrst_entry = Entry(data_frame)
            intrst_entry.grid(row=1, column=7, padx=10, pady=10)

            # Move Row Up
            def up():
                rows = my_tree.selection()
                for row in rows:
                    my_tree.move(row, my_tree.parent(row), my_tree.index(row)-1)
            
            # Move row down
            def down():
                rows = my_tree.selection()
                for row in reversed(rows):
                    my_tree.move(row, my_tree.parent(row), my_tree.index(row)+1)
                  
            # Remove one record
            def remove_one():
                # Remove selection in Treeview
                x = my_tree.selection()[0]
                my_tree.delete(x)
                # Create or Connect to a database
                conn = sqlite3.connect('FinMan.db')
                # Create cursor instance
                c = conn.cursor()  
                # Delete From Database
                c.execute("DELETE from accounts WHERE oid=" + id_entry.get())
                # Commit the changes
                conn.commit()
                # Always close the connection
                conn.close()
                clear_entries()
                
                messagebox.showinfo("Deleted!", "Your Record Has Been Deleted!")
             
            # Remove many records
            def remove_many():
                # Create messagebox asking if you must continue removing many records
            	response = messagebox.askyesno("Notice", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")
                
                # Add logic for messagebox
            	if response == 1:
                    # Declare variable for selection
            		x = my_tree.selection()
                    # Create List of ID's
            		ids_to_delete = []
            		
                    # Add selections to ids_to_delete list
            		for record in x:
            			ids_to_delete.append(my_tree.item(record, 'values')[2])
                    # Delete From Treeview
            		for record in x:
            			my_tree.delete(record)
                    # Create or Connect to a database   
            		conn = sqlite3.connect('FinMan.db')
                    # Create cursor instance
            		c = conn.cursor()
                    # Delete data from the database
            		c.executemany("DELETE FROM accounts WHERE oid = ?", [(a,) for a in ids_to_delete])
                    # Reset List
            		ids_to_delete = []
                    # Commit the changes
            		conn.commit()
                    # Always close the connection
            		conn.close()
                    # Clear entry boxes
            		clear_entries() 
                     
            def remove_all():
                # Create messagebox asking if you must continue removing all records
                response = messagebox.askyesno("Notice", "This will delete all your data in the table\n Are you sure?")
                #Add logic for message box
                if response == 1:
                    # Clear Treeview
                    for record in my_tree.get_children():
                        my_tree.delete(record)
                    # Create or Connect to a database
                    conn = sqlite3.connect('FinMan.db')
                    # Create cursor instance
                    c = conn.cursor()  
                    c.execute("DROP TABLE accounts")
                    # Commit the changes
                    conn.commit()
                    # Always close the connection
                    conn.close()
                    
                    clear_entries() 
                    # Create table again because the table is also deleted when removing all records
                    create_table_again()          
            # Clear Entry Boxes       
            def clear_entries():
                pname_entry.delete(0, END)
                pnum_entry.delete(0, END)
                id_entry.delete(0, END)
                bal_entry.delete(0, END)
                deb_entry.delete(0, END)
                cflow_entry.delete(0, END)
                intrst_entry.delete(0, END)
            
            # Select Record
            def select_record(e):
                # Clear Entry Boxes 
                pname_entry.delete(0, END)
                pnum_entry.delete(0, END)
                id_entry.delete(0, END)
                bal_entry.delete(0, END)
                deb_entry.delete(0, END)
                cflow_entry.delete(0, END)
                intrst_entry.delete(0, END)
                
                # Grab Record Number
                selected = my_tree.focus()
                # Grab Record Values
                values = my_tree.item(selected, 'values')
                
                # Output to entry boxes
                pname_entry.insert(0, values[0])
                pnum_entry.insert(0, values[1])
                id_entry.insert(0, values[2])
                bal_entry.insert(0, values[3])
                deb_entry.insert(0, values[4])
                cflow_entry.insert(0, values[5])
                intrst_entry.insert(0, values[6])
            
            # Update record
            def update_record():
                # Grab record number
                selected = my_tree.focus()
                # Update record
                my_tree.item(selected, text="", values=(pname_entry.get(), pnum_entry.get(), id_entry.get(), bal_entry.get(), deb_entry.get(), cflow_entry.get(), intrst_entry.get(), ))
                # Create or Connect to a database
                conn = sqlite3.connect('FinMan.db')
                # Create cursor instance
                c = conn.cursor()  
                # Update database
                c.execute("""UPDATE accounts SET
                    prof_name = :first,
                    prof_num = :last,
                    balance = :balance,
                    debt = :debt,
                    cashflow = :cashflow,
                    interest = :interest
                    
                    WHERE oid = :oid""",
                    {
                        'first': pname_entry.get(),
                        'last': pnum_entry.get(),
                        'balance': bal_entry.get(),
                        'debt': deb_entry.get(),
                        'cashflow': cflow_entry.get(),
                        'interest': intrst_entry.get(),
                        'oid': id_entry.get(),
                        }
                          
                    )
                # Commit the changes
                conn.commit()
                # Always close the connection
                conn.close()
                
                pname_entry.delete(0, END)
                pnum_entry.delete(0, END)
                id_entry.delete(0, END)
                bal_entry.delete(0, END)
                deb_entry.delete(0, END)
                cflow_entry.delete(0, END)
                intrst_entry.delete(0, END)
            
            # Add new record 
            def add_record():
                # Create or Connect to a database
                conn = sqlite3.connect('FinMan.db')
                # Create cursor instance
                c = conn.cursor()  
                # Add new record to database
                c.execute("INSERT INTO accounts VALUES (:first, :last, :id, :balance, :debt, :cashflow, :interest)",
                {
                'first': pname_entry.get(),
                'last': pnum_entry.get(),
                'id': id_entry.get(),
                'balance': bal_entry.get(),
                'debt': deb_entry.get(),
                'cashflow': cflow_entry.get(),
                'interest': intrst_entry.get(),
                
                })
                # Commit the changes
                conn.commit()
                # Always close the connection
                conn.close()
                
                # Clear entry boxes
                pname_entry.delete(0, END)
                pnum_entry.delete(0, END)
                id_entry.delete(0, END)
                bal_entry.delete(0, END)
                deb_entry.delete(0, END)
                cflow_entry.delete(0, END)
                intrst_entry.delete(0, END)
                
                my_tree.delete(*my_tree.get_children())
                
                # Show database with newly added record
                query_database()
                 
                # Create method for creating a new table
            def create_table_again(): 
                # Create or Connect to a database
                conn = sqlite3.connect('FinMan.db')
                # Create cursor instance
                c = conn.cursor()
                c.execute("""CREATE TABLE if not exists accounts ( 
                        prof_name text,
                        prof_num integer,
                        id integer,
                        balance float,
                        debt float,
                        cashflow float,
                        interest float)
                          """)
                # Commit the changes          
                conn.commit()
                # Always close the connection
                conn.close()
            
            # Add the Buttons
            button_frame = LabelFrame(finmanroot, bg="sky blue", text="Commands")
            button_frame.pack(fill="x", expand="yes", padx=20)

            update_button = Button(button_frame, text="Update Record", fg="white", bg="#B22222", command=update_record)
            update_button.grid(row=0, column=0, padx=10, pady=10)

            add_button = Button(button_frame, text="Add Record", fg="white", bg="#B22222", command=add_record)
            add_button.grid(row=0, column=1, padx=10, pady=10)

            remove_all_button = Button(button_frame, text="Remove All Records", fg="white", bg="#B22222", command=remove_all)
            remove_all_button.grid(row=0, column=2, padx=10, pady=10)

            remove_one_button = Button(button_frame, text="Remove One Selected", fg="white", bg="#B22222", command=remove_one)
            remove_one_button.grid(row=0, column=3, padx=10, pady=10)

            remove_many_button = Button(button_frame, text="Remove Many Selected", fg="white", bg="#B22222", command=remove_many)
            remove_many_button.grid(row=0, column=4, padx=10, pady=10)

            move_up_button = Button(button_frame, text="Move Up", fg="white", bg="#B22222", command=up)
            move_up_button.grid(row=0, column=5, padx=10, pady=10)

            move_down_button = Button(button_frame, text="Move Down", fg="white", bg="#B22222", command=down)
            move_down_button.grid(row=0, column=6, padx=10, pady=10)

            select_record_button = Button(button_frame, text="Clear Entry Boxes", fg="white", bg="#B22222", command=clear_entries)
            select_record_button.grid(row=0, column=7, padx=10, pady=10)
            
            # Bind Treeview for selecting data in the records
            my_tree.bind("<ButtonRelease-1>", select_record)
            
            #Run to pull data from database on start
            query_database()

            finmanroot.mainloop()
        
        def showformulas(self): # Function that includes all the Real-Estate formulas and their execution when called.
            global realestateroot
            realestateroot = Toplevel(self.master)
            realestateroot.title("Real Estate Calculations")
            realestateroot.configure(background="light blue")
            realestateroot.geometry("540x310")
            realestateroot.iconbitmap("GUI Icon.ico")
            realestateroot.resizable(True, True)
            realestateroot.grab_set()
            realestateroot.focus_set()  

            # Variables declared as 'global' to be defined on other usage. These variables are used in formulaic calculations.
            global blank_label
            global v1 
            global v2
            global v3
            
            def formulaexecution(): # A sub-function of the showformulas(self) that executes the formulas through elif statements dictated by var.get() value.
                if var.get() == "Break-Even Ratio":
                  
                    dsc = Entry(realestateroot, width=40, borderwidth=5)
                    dsc.grid(row=6, column=1)
                    oe = Entry(realestateroot, width=40, borderwidth=5)
                    oe.grid(row=7, column=1)
                    goi = Entry(realestateroot, width=40, borderwidth=5)
                    goi.grid(row=8, column=1)
                    
                    dbc_label = Label(realestateroot, text="Debt Servicing Costs", bg="light blue", font=("Century gothic bold", 10), padx=17)
                    dbc_label.grid(row=6, column=0)
                    oe_label = Label(realestateroot, text="Operating Expenses",  bg="light blue", font=("Century gothic bold", 10), padx=17)
                    oe_label.grid(row=7, column=0)
                    goi_label = Label(realestateroot, text="Gross Operating Income",  bg="light blue", font=("Century gothic bold", 10), padx=10)
                    goi_label.grid(row=8, column=0)
                    
                    def breakevenratio(): # Contains the formula and the output bay for this real-estate calculation.
                        global v1
                        global v2
                        global v3
                        v1=int(dsc.get())
                        v2=int(oe.get())
                        v3=int(goi.get())
                        sum = ((v1 + v2)/v3)
                        ber_label = Label(realestateroot, text="Calculated Break Even Ratio is " + str(sum), font=("Century gothic bold", 8))
                        ber_label.grid(row=9, column=1)
               
                    button = Button(realestateroot, text="Calculate", bg="#B22222", fg="white", font=("Century gothic bold", 9), command=breakevenratio).grid(row=9,column=0)   
                   
                elif var.get() == "Operating Cash Flow":
                    noi = Entry(realestateroot, width=40, borderwidth=5)
                    noi.grid(row=6, column=1)
                    ce = Entry(realestateroot, width=40, borderwidth=5)
                    ce.grid(row=7, column=1)
                    
                    noi_label = Label(realestateroot, text="Net Operating Income", bg="light blue", font=("Century gothic bold", 10), padx=10)
                    noi_label.grid(row=6, column=0)
                    ce_label = Label(realestateroot, text="Capital Expenditures", bg="light blue", font=("Century gothic bold", 10), padx=10)
                    ce_label.grid(row=7, column=0)
                    blank_entry = Label(realestateroot, text="", bg="light blue", padx=125, pady=5)
                    blank_entry.grid(row=8, column=1)
                    blank_label = Label(realestateroot, text="", bg="light blue", padx=80)
                    blank_label.grid(row=8, column=0)
                    
                    def operatingcashflow(): # Contains the formula and the output bay for this real-estate calculation.
                        global v1
                        global v2
                        v1=int(noi.get())
                        v2=int(ce.get())
                        sum = (v1-v2)
                        ber_label = Label(realestateroot, text="Calculated Operating Cash Flow is " + str(sum), font=("Century gothic bold", 8))
                        ber_label.grid(row=9, column=1)
                   
                    button = Button(realestateroot, text="Calculate", bg="#B22222", fg="white", font=("Century gothic bold", 9), command=operatingcashflow).grid(row=9,column=0)
                
                elif var.get() == "Return on Investment":
                    ar = Entry(realestateroot, width=40, borderwidth=5)
                    ar.grid(row=6, column=1)
                    coi = Entry(realestateroot, width=40, borderwidth=5)
                    coi.grid(row=7, column=1)
                    
                    ar_label = Label(realestateroot, text="Annual Returns", width=15, bg="light blue", font=("Century gothic bold", 10), padx=25)
                    ar_label.grid(row=6, column=0)
                    coi_label = Label(realestateroot, text="Cost of Investment", bg="light blue", font=("Century gothic bold", 10), padx=15)
                    coi_label.grid(row=7, column=0)
                    blank_entry = Label(realestateroot, text="", bg="light blue", padx=100)
                    blank_entry.grid(row=8, column=1)
                    blank_label = Label(realestateroot, text="", bg="light blue", padx=80)
                    blank_label.grid(row=8, column=0)
                    
                    def returnoninvestment(): # Contains the formula and the output bay for this real-estate calculation.
                        global v1
                        global v2
                        v1=int(ar.get())
                        v2=int(coi.get())
                        sum = (v1/v2)
                        ber_label = Label(realestateroot, text="Calculated Return on Investment is " + str(sum), font=("Century gothic bold", 8))
                        ber_label.grid(row=9, column=1)
                   
                    button = Button(realestateroot, text="Calculate", bg="#B22222", fg="white", font=("Century gothic bold", 9), command=returnoninvestment).grid(row=9,column=0)
                
                elif var.get() == "Price to Rent Ratio":
                    ppp = Entry(realestateroot, width=40, borderwidth=5)
                    ppp.grid(row=6, column=1)
                    arr = Entry(realestateroot, width=40, borderwidth=5)
                    arr.grid(row=7, column=1)
                    
                    ppp_label = Label(realestateroot, text="Purchase Price of Property", bg="light blue", font=("Century gothic bold", 10), padx=10)
                    ppp_label.grid(row=6, column=0)
                    arr_label = Label(realestateroot, text="Annual Rental Revenue", bg="light blue", font=("Century gothic bold", 10), padx=10)
                    arr_label.grid(row=7, column=0)
                    blank_entry = Label(realestateroot, text="", bg="light blue", padx=125, pady=5)
                    blank_entry.grid(row=8, column=1)
                    blank_label = Label(realestateroot, text="", bg="light blue", padx=80)
                    blank_label.grid(row=8, column=0)
                    
                    def pricetorentratio(): # Contains the formula and the output bay for this real-estate calculation.
                        global v1
                        global v2
                        v1=int(ppp.get())
                        v2=int(arr.get())
                        sum = (v1/v2)
                        ber_label = Label(realestateroot, text="Calculated Price to Rent Ratio is " + str(sum))
                        ber_label.grid(row=9, column=1)
                   
                    button = Button(realestateroot, text="Calculate", bg="#B22222", fg="white", font=("Century gothic bold", 9), command=pricetorentratio).grid(row=9,column=0)
                
                elif var.get() == "Capitalization Rate":
                    noi = Entry(realestateroot, width=40, borderwidth=5)
                    noi.grid(row=6, column=1)
                    mvp = Entry(realestateroot, width=40, borderwidth=5)
                    mvp.grid(row=7, column=1)
                    
                    noi_label = Label(realestateroot, text="Net Operating Income", bg="light blue", font=("Century gothic bold", 10), padx=30)
                    noi_label.grid(row=6, column=0)
                    mvp_label = Label(realestateroot, text="Market Value of Property", bg="light blue", font=("Century gothic bold", 10), padx=30)
                    mvp_label.grid(row=7, column=0)
                    blank_entry = Label(realestateroot, text="", bg="light blue", padx=125, pady=5)
                    blank_entry.grid(row=8, column=1)
                    blank_label = Label(realestateroot, text="", bg="light blue", padx=80)
                    blank_label.grid(row=8, column=0)
                    
                    def capitalizationrate(): # Contains the formula and the output bay for this real-estate calculation.
                        global v1
                        global v2
                        v1=int(noi.get())
                        v2=int(mvp.get())
                        sum = (v1/v2)
                        ber_label = Label(realestateroot, text="Calculated Capitalization Rate is " + str(sum))
                        ber_label.grid(row=9, column=1)
                   
                    button = Button(realestateroot, text="Calculate", bg="#B22222", fg="white", font=("Century gothic bold", 9), command=capitalizationrate).grid(row=9,column=0)

            # Contains the dropdown items through a tuple.
            options = [
                "Break-Even Ratio",
                "Operating Cash Flow",
                "Return on Investment",
                "Price to Rent Ratio",
                "Capitalization Rate"
            ]
    
            var = StringVar()
            var.set(options[0]) # Calls Element 0 (Break-even Ratio) and sets it as the default value.
            
            Label(realestateroot, text="Real Estate Calculations", height="2", bg="light blue", font=("Century gothic bold", 14)).grid(row=0, column=1)
            Label(realestateroot, text="*Calculate various finances by the dropdown below", bg="light blue", font=("Century gothic bold", 8)).grid(row=1, column=1)
            
            drop = OptionMenu(realestateroot, var, *options)
            drop.configure(font=("Century gothic bold", 10), bg="sky blue", fg="black")
            drop.grid(pady=20, row=3,column=1)
            
            executebutton = Button(realestateroot, text="Execute Formula", bg="#B22222", fg="white", font=("Century gothic bold", 10), command=formulaexecution)
            executebutton.grid(row=4, column=1)
            buttonspace = Label(realestateroot, text="", bg="light blue")
            buttonspace.grid(row=5, column=1)
            
        def showcalculator(self): # Function that displays the working calculator when called by button press.
            calculatorscreen = Toplevel(self.master)
            calculatorscreen.title("Calculator")
            calculatorscreen.configure(background="light blue")
            calculatorscreen.iconbitmap('GUI Icon.ico')
            calculatorscreen.geometry("255x180")
            calculatorscreen.resizable(False, False)
            calculatorscreen.grab_set() # Sets focus priority to this tab.
            calculatorscreen.focus_set()
           
            def press(num): # Function for number pressing that sets the equation, defining the expression that will be evaluated later.
                global expression
                expression = expression + str(num)
                equation.set(expression)
             
            def equalpress(): # Evaluates the totality of the defined expression, which is defined by the set equation. Uses try-except handling to display an error if the calculation is not possible.
                try:
                    global expression             
                    total = str(eval(expression))             
                    equation.set(total)             
                    expression = ""   
                    
                except:             
                    equation.set(" Cannot be computed. ")
                    expression = ""  
                    
            def clear(): # Resets the expression to an empty string, nullifying the calculator space.
                global expression
                expression = ""
                equation.set("")
                
            global expression # Globally-defined variable used in different scenarios in this method.
            expression = ""
            
            equation = StringVar()
            expression_field = Entry(calculatorscreen, textvariable=equation)
            expression_field.grid(columnspan=4, ipadx=60)

            # Lambda is repeatedly use to prevent spamming of user-defined functions per button, optimizing the code.
            button1 = Button(calculatorscreen, text=' 1 ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press(1), width=6)
            button1.grid(row=4, column=0)
            button2 = Button(calculatorscreen, text=' 2 ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press(2), width=6)
            button2.grid(row=4, column=1)
            button3 = Button(calculatorscreen, text=' 3 ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press(3), width=6)
            button3.grid(row=4, column=2)
            button4 = Button(calculatorscreen, text=' 4 ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press(4), width=6)
            button4.grid(row=3, column=0)
            button5 = Button(calculatorscreen, text=' 5 ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press(5), width=6)
            button5.grid(row=3, column=1)
            button6 = Button(calculatorscreen, text=' 6 ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press(6), width=6)
            button6.grid(row=3, column=2)
            button7 = Button(calculatorscreen, text=' 7 ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press(7), width=6)
            button7.grid(row=2, column=0)
            button8 = Button(calculatorscreen, text=' 8 ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press(8), width=6)
            button8.grid(row=2, column=1)
            button9 = Button(calculatorscreen, text=' 9 ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press(9), width=6)
            button9.grid(row=2, column=2)
            button0 = Button(calculatorscreen, text=' 0 ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press(0), width=6)
            button0.grid(row=5, column=0)
            
            plus = Button(calculatorscreen, text=' + ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press("+"), width=6)
            plus.grid(row=2, column=3)
            minus = Button(calculatorscreen, text=' — ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press("-"), width=6)
            minus.grid(row=3, column=3)
            multiply = Button(calculatorscreen, text=' x ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press("*"), width=6)
            multiply.grid(row=4, column=3)         
            divide = Button(calculatorscreen, text=' ÷ ', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press("/"), width=6)
            divide.grid(row=5, column=3)         
            equal = Button(calculatorscreen, text=' = ', fg='white', bg='#B22222', font=("Century gothic bold", 11), cursor = "hand1", command=equalpress, width=6)
            equal.grid(row=5, column=2)
            clear = Button(calculatorscreen, text='Clear', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=clear, width=6)
            clear.grid(row=5, column=1)
            Decimal= Button(calculatorscreen, text='.', fg='white', bg='#7592cb', font=("Century gothic bold", 11), cursor = "hand1", command=lambda: press('.'), width=6)
            Decimal.grid(row=6, column=0)
                
            calculatorscreen.mainloop() # Loops the functions of the calculator until the window is closed.
            
    if __name__ == "__main__": # Driver function for this class.
        root = tk.Tk()
        app = FinMan(root, name="", number="", balance ="", debt="", incomeflow="", interest="")
        root.mainloop()
 
def password_not_recognised(): # Function called when input password does not match any opened textfiles in the directory.
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Warning!")
    password_not_recog_screen.geometry("225x75")
    password_not_recog_screen.resizable(False, False)
    password_not_recog_screen.iconbitmap("GUI Icon.ico")
    Label(password_not_recog_screen, text="Unmatching Password.").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found(): # Function called when input username is not present in any of the stored textfiles in the directory.
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Unregistered")
    user_not_found_screen.geometry("250x75")
    user_not_found_screen.resizable(False, False)
    user_not_found_screen.iconbitmap("GUI Icon.ico")
    Label(user_not_found_screen, text="User not yet registered.").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
def delete_login_success(): # Destroys the prompt screen after successful operation.
    login_success_screen.destroy()
 
def delete_password_not_recognised(): # Destroys the prompt screen after successful operation.
    password_not_recog_screen.destroy()
 
def delete_user_not_found_screen(): # Destroys the prompt screen after successful operation.
    user_not_found_screen.destroy()
  
def main_account_screen(): # Opening window of FinMan presenting two commands: Login and Register.
    global main_screen # Heavily used global variable for Toplevel windowing.
    main_screen = Tk() # Root window.
    main_screen.geometry("350x215")
    main_screen.resizable(False, False)
    main_screen.iconbitmap('GUI Icon.ico')
    main_screen.focus_force()
   
    main_screen.configure(background='light blue')
    main_screen.title("FinMan™")
    Label(text="FinMan™", bg="sky blue", width="300", font=("Century gothic", 18)).pack()
    Label(text="Manage your money, manage your dreams.", bg="sky blue", width="300", height="1", font=("Century gothic bold", 11), pady=10).pack()
    Label(text="", bg="light blue").pack()
    login_button = Button(text="Login", height="1", width="30", bg="white", font=("Century gothic bold", 10), command=login)
    login_button.pack()
    Label(text="", bg="light blue").pack()
    register_button = Button(text="Register", height="1", width="30", bg="white", font=("Century gothic bold", 10), command=register)
    register_button.pack()  

    # Allow keybind of more than one button on a single window.
    def on_enter_pressed(event):
        focused_widget = main_screen.focus_get()
        if focused_widget == login_button:
            login()
        elif focused_widget == register_button:
            register()  
    main_screen.bind('<Return>', on_enter_pressed)
   
    main_screen.mainloop() # Repeats the process of this window until destroyed after successful operation of log-in.
   
main_account_screen() # Calls an instance of main_account_screen, the startup window, when the code is run.