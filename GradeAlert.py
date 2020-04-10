from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import selenium
import time

options = Options()
options.headless = True

driver = webdriver.Chrome('/home/alan/Documents/Python/GradeCheck/chromedriver', options = options)
#add info to second tab, update clear button

class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.geometry("450x365")
        self.resizable(False, False)
        self.title("Grade Finder")
        self.notebook = ttk.Notebook()
        self.notebook.pack(fill="both", expand=1)
        self.add_tabs()


    def add_tabs(self):
        tab = Log(self.notebook)
        tab2 = Grade(self.notebook)
        self.notebook.add(tab, text="Log in")
        self.notebook.add(tab2, text="Grades")


class Log(Frame):
    def __init__(self, name, *args, **kwargs):
        def login():
            driver.get('https://www.fridayparentportal.com/northbergen')
            time.sleep(5)
            portalcode_box = driver.find_element_by_name('portalcode')
            username_box = driver.find_element_by_name('username')
            password_box = driver.find_element_by_name('password')

            portalcode_box.send_keys(t_code.get())
            username_box.send_keys(t_user.get())
            password_box.send_keys(t_pass.get())

            login_button = driver.find_element_by_css_selector('button.btn')
            login_button.click()

            try:
                gradebook = driver.find_element_by_link_text('Gradebook')
                gradebook.click()

                student_pic = driver.find_element_by_css_selector('img.img').get_attribute('src')
                print(student_pic)

                list_course = driver.find_elements_by_css_selector('td.finedetail')
                lists = [n.text for n in list_course]
                new_list = [n for n in lists if n != ""]
                s_class = [n.split("\n")[0] for n in new_list[::3]]
                s_grades = [n.split("/")[0] for n in new_list[1::3]]
                s_teacher = new_list[2::3]
                print(s_class,s_grades, s_teacher)
                Grade.__init__(self).tree.insert()



            except selenium.common.exceptions.NoSuchElementException:
                messagebox.showinfo("Error", "Mhmm did you type your login correctly? Try again.")



        def clear():
            t_code.delete(0, 'end')
            t_user.delete(0, 'end')
            t_pass.delete(0, 'end')

        Frame.__init__(self, *args, **kwargs)
        self.name = name
        self.f_log = Frame(self)
        f_code = Frame(self.f_log)
        l_code = Label(f_code, text=" Portal Code: ")
        t_code = Entry(f_code)
        t_code.focus_set()

        f_user = Frame(self.f_log, bg="#2863A4")
        l_user = Label(f_user, text="Username:    ")
        t_user = Entry(f_user)

        f_pass = Frame(self.f_log)
        l_pass = Label(f_pass, text="Password:      ")
        t_pass = Entry(f_pass, show="*")

        f_b = Frame(self.f_log)
        b_log = Button(f_b, text="LOG IN", command= login)
        b_c_log = Button(f_b, text="CLEAR ", command= clear)

        self.f_log.pack(fill="both", expand=1, padx=50, pady=100)

        f_code.pack(fill="both", expand=1, pady=5)
        l_code.pack(fill="y", side="left")
        t_code.pack(fill="both", side="left", expand=1)

        f_user.pack(fill="both", expand=1)
        l_user.pack(fill="y", side="left")
        t_user.pack(fill="both", side="left", expand=1)

        f_pass.pack(fill="both", expand=1)
        l_pass.pack(fill="y", side="left")
        t_pass.pack(fill="both", side="left", expand=1, pady=5)

        f_b.pack()
        b_log.pack(side="left")
        b_c_log.pack(side="left",padx =5)


class Grade(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.f_grade = Frame(self)
        f_user = Frame(self.f_grade)

        self.f_grades = Frame(self.f_grade)
        self.tree = ttk.Treeview(self.f_grades)
        self.tree["columns"] = ("one", "two")
        self.tree.column('#0', width=150)
        self.tree.column("one", width=100)
        self.tree.column("two", width=30)
        self.tree.heading("#0", text="Class")
        self.tree.heading("one", text="Teacher")
        self.tree.heading("two", text="Grade")
        self.tree.pack(fill="both", expand=1)

        self.f_grade.pack(fill="both", expand=1)
        f_user.place(height=100, width=450)

        self.f_grades.place(y=100, height=350, width=450)


my_app = App()
my_app.mainloop()