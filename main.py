from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
from db import Database
from tkinter.messagebox import showerror, showinfo
class App(Tk):
    def __init__(self):
        super().__init__()

        self.db = Database("Employees.db")

        #connect to database
        self.db.connect()

        #variables
        self.id = StringVar()
        self.name = StringVar()
        self.job = StringVar()
        self.gender = StringVar()
        self.age = StringVar()
        self.email = StringVar()
        self.mobile = StringVar()
        self.address = None
        self.treeview = None

        #window configs
        self.title("Employees Management System")
        self.bg : str = "#2c3e50"
        self.font = {
            'family': "Arial Rounded MT Bold",
            'size': 13,
            'normal': 'normal',
            'bold': 'bold'
        }
        #center window
        self.width : int = 1310
        self.height : int = 515

        self.x_position : float = (self.winfo_screenwidth() - self.width) / 2
        self.y_position : float = (self.winfo_screenheight() - self.height) / 2

        self.geometry(f"{self.width}x{self.height}+{int(self.x_position)}+{int(self.y_position)}")
        self.resizable(False, False)
        self.config(bg=self.bg)
        self.iconbitmap('./favicon.ico')

        self.create_left_frame_widget()
        self.create_right_frame_widget()

        self.grid_layout()

        self.display_employees()

        self.mainloop()


    def grid_layout(self):
        self.grid_columnconfigure(0, weight=1, uniform='column')
        self.grid_columnconfigure(1, weight=3, uniform='column')
        self.grid_rowconfigure(0, weight=1, uniform='row')

    def create_left_frame_widget(self):
        frame = Frame(self, bg=self.bg)
        frame.grid(row=0, column=0, sticky='wesn', padx=5, pady=5)

        frame.grid_rowconfigure((0,1,2,3,4,5,6,7,8), weight=1, uniform='row')
        frame.grid_rowconfigure(9, weight=3, uniform='row')
        frame.columnconfigure(0, weight=1, uniform='column')
        frame.columnconfigure(1, weight=3, uniform='column')

        #navbar (title, btn hide, btn show)
        navbar = Frame(frame, bg=self.bg)
        navbar.grid(column=0, row=0, columnspan=3, sticky='wesn')

        navbar.grid_columnconfigure(0, weight=2, uniform="column")
        navbar.grid_columnconfigure(1, weight=1, uniform="column")
        navbar.grid_rowconfigure(0, weight=1, uniform="row")

        lbl_title = Label(navbar, text='Employee Company', bg=self.bg, font=(self.font['family'], 13, self.font.get("bold")), fg='white', anchor='w')
        lbl_title.grid(column=0, row=0, sticky='we', padx=5)

        btn_hide = Button(navbar, text='Exit', cursor='hand2', font=(self.font.get("family"), 10, self.font.get("normal")), command=lambda: exit())
        btn_hide.grid(column=1, row=0, sticky='we', padx=5)

        #name
        lbl_name = Label(frame, text='Name:', bg=self.bg, font=(self.font['family'], self.font['size'], self.font.get('normal')), fg='white')
        lbl_name.grid(column=0, row=1, sticky='w', padx=5)

        ent_name = Entry(frame, font=(self.font['family'], self.font['size'], self.font.get('normal')), textvariable=self.name)
        ent_name.grid(column=1, row=1, sticky='we', padx=5)

        #job
        lbl_job = Label(frame, text='Job:', bg=self.bg, font=(self.font['family'], self.font['size'], self.font.get('normal')), fg='white')
        lbl_job.grid(column=0, row=2, sticky='w', padx=5)

        ent_job = Entry(frame, font=(self.font['family'], self.font['size'], self.font.get('normal')), textvariable=self.job)
        ent_job.grid(column=1, row=2, sticky='we', padx=5)

        #gender
        lbl_gender = Label(frame, text='Gender:', bg=self.bg, font=(self.font['family'], self.font['size'], self.font.get('normal')), fg='white')
        lbl_gender.grid(column=0, row=3, sticky='w', padx=5)

        ent_gender = ttk.Combobox(frame, font=(self.font['family'], self.font['size'], self.font.get('normal')), values=('Male', 'Female'), state='readonly', textvariable=self.gender)
        ent_gender.grid(column=1, row=3, sticky='we', padx=5)

        #Age
        lbl_age = Label(frame, text='Age:', bg=self.bg, font=(self.font['family'], self.font['size'], self.font.get('normal')), fg='white')
        lbl_age.grid(column=0, row=4, sticky='w', padx=5)

        ent_age = Entry(frame, font=(self.font['family'], self.font['size'], self.font.get('normal')), textvariable=self.age)
        ent_age.grid(column=1, row=4, sticky='we', padx=5)

        #Email
        lbl_email = Label(frame, text='Email:', bg=self.bg, font=(self.font['family'], self.font['size'], self.font.get('normal')), fg='white')
        lbl_email.grid(column=0, row=5, sticky='w', padx=5)

        ent_email = Entry(frame, font=(self.font['family'], self.font['size'], self.font.get('normal')), textvariable=self.email)
        ent_email.grid(column=1, row=5, sticky='we', padx=5)

        #Mobile
        lbl_mobile = Label(frame, text='Mobile:', bg=self.bg, font=(self.font['family'], self.font['size'], self.font.get('normal')), fg='white')
        lbl_mobile.grid(column=0, row=6, sticky='w', padx=5)

        ent_mobile = Entry(frame, font=(self.font['family'], self.font['size'], self.font.get('normal')), textvariable=self.mobile)
        ent_mobile.grid(column=1, row=6, sticky='we', padx=5)

        # Address
        lbl_address = Label(frame, text='Address:', bg=self.bg, font=(self.font['family'], self.font['size'], self.font.get('normal')), fg='white')
        lbl_address.grid(column=0, row=7,columnspan=2, sticky='w', padx=5)

        frame_address = Frame(frame)
        frame_address.grid(column=0,columnspan=2, row=8, sticky='wesn', padx=5)

        self.address = ScrolledText(frame_address, font=(self.font['family'], self.font['size'], self.font.get('normal')), bg='white')
        self.address.place(x=0, y=0, relheight=1, relwidth=1)

        # #buttons
        buttons_frame = Frame(frame, bg=self.bg, highlightthickness=2, highlightbackground='white')
        buttons_frame.grid(column=0, columnspan=2, row=9, sticky='wesn', padx=5, pady=10)


        btn_add = Button(buttons_frame, text='Add Details', font=(self.font['family'], self.font['size'], self.font.get('normal')), bg='green', fg='white', cursor='hand2', command=self.add_employee)
        btn_add.grid(row=0, column=0, padx=5, pady=5, sticky='wens')

        btn_delete =  Button(buttons_frame, text='Delete Details', font=(self.font['family'], self.font['size'], self.font.get('normal')), bg='crimson', fg='white', cursor='hand2', command=self.delete_emloyee)
        btn_delete.grid(row=0, column=1, padx=5, pady=5, sticky='wens')

        btn_update =  Button(buttons_frame, text='Update Details', font=(self.font['family'], self.font['size'], self.font.get('normal')), bg='blue', fg='white', cursor='hand2', command=self.update_employee)
        btn_update.grid(row=1, column=0, padx=5, pady=5, sticky='wens')

        btn_clear = Button(buttons_frame, text='Clear Details', font=(self.font['family'], self.font['size'], self.font.get('normal')), bg='orange', fg='white', cursor='hand2', command=self.clear_fields)
        btn_clear.grid(row=1, column=1, padx=5, pady=5, sticky='wens')
        

        buttons_frame.grid_columnconfigure((0,1), weight=1, uniform='column')
        buttons_frame.grid_rowconfigure((0,1), weight=1, uniform='row')

    def create_right_frame_widget(self):
        tree_frame = Frame(self)
        tree_frame.grid(column=1, row=0, sticky='wesn', padx=5, pady=5)

        style = ttk.Style()
        style.configure('mystyle.Treeview', rowheight=25, font=(self.font['family'], 12, self.font.get('normal')))
        style.configure("mystyle.Treeview.Heading", font=(self.font['family'], 12, self.font.get('normal')))

        self.treeview = ttk.Treeview(tree_frame, columns=(0,1,2,3,4,5,6,7), show='headings', style='mystyle.Treeview')

        self.treeview.column(0, width=100, anchor='center')
        self.treeview.column(1, width=100, anchor='center')
        self.treeview.column(2, width=100, anchor='center')
        self.treeview.column(3, width=100, anchor='center')
        self.treeview.column(4, width=100, anchor='center')
        self.treeview.column(5, width=100, anchor='center')
        self.treeview.column(6, width=100, anchor='center')
        self.treeview.column(7, width=100, anchor='center')

        self.treeview.heading(0, text='Id')
        self.treeview.heading(1, text='Name')
        self.treeview.heading(2, text='Age')
        self.treeview.heading(3, text='Job')
        self.treeview.heading(4, text='Email')
        self.treeview.heading(5, text='Gender')
        self.treeview.heading(6, text='Mobile')
        self.treeview.heading(7, text='Address')

        self.treeview.pack(fill='both', expand=True)

        self.treeview.bind("<<TreeviewSelect>>", self.employee_selected)

    def add_employee(self):
        name = self.name.get()
        age = self.age.get()
        job = self.job.get()
        email = self.email.get()
        gender = self.gender.get()
        mobile = self.mobile.get()
        address = self.address.get('1.0', END)
        
        if name.strip() == '' or  age.strip() == '' or  job.strip() == '' or  email.strip() == '' or gender.strip() == '' or  mobile.strip() == '' or  address.strip() == '':
            showerror('Error', 'All fields are required.')
            return
        
        self.db.create(name, age, job, email, gender, mobile, address)
        showinfo("Success", "Employee has been added successfully")
        self.clear_fields()
        self.display_employees()

    def update_employee(self):
        id = self.id.get()
        name = self.name.get()
        age = self.age.get()
        job = self.job.get()
        email = self.email.get()
        gender = self.gender.get()
        mobile = self.mobile.get()
        address = self.address.get('1.0', END)

        if not id: return

        self.db.update(id, name, age, job, email, gender, mobile, address)
        showinfo("Success", "Employee has been updated informations")
        self.clear_fields()
        self.display_employees()

    def clear_fields(self):
        self.name.set('')
        self.age.set('')
        self.job.set('')
        self.email.set('')
        self.gender.set('')
        self.mobile.set('')
        self.address.delete('1.0', END)
    
    def employee_selected(self, event):
        for selected_item in self.treeview.selection():
            id, name, age, job, email, gender, phone, address = self.treeview.item(selected_item)['values']
            self.id.set(id)
            self.name.set(name)
            self.age.set(age)
            self.job.set(job)
            self.email.set(email)
            self.gender.set(gender)
            self.mobile.set(phone)
            self.address.delete('1.0', END)
            self.address.insert(END, address)

    def display_employees(self):

        for item in self.treeview.get_children():
            self.treeview.delete(item)

        employees = self.db.fetch()
        
        for employee in employees:
            self.treeview.insert("", END, values=employee)

    def delete_emloyee(self):
        if self.id.get():
            self.db.remove(self.id.get())
            showinfo("Success", "Employee has been deleted successfully")
            self.clear_fields()
            self.display_employees()

if __name__ == "__main__":
    app = App()
