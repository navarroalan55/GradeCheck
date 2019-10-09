import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter import ttk
import os
import requests
from io import BytesIO

global actual_grades
# makes it go headless
#options = Options()
#options.headless = True

# Headless
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome()


def fetch():
    driver.get('https://www.fridayparentportal.com/northbergen')

    # gets the elements from the web page to log in
    portalcode_box = driver.find_element_by_name('portalcode')
    username_box = driver.find_element_by_name('username')
    password_box = driver.find_element_by_name('password')

    # sends information to web page to log in.

    portalcode_box.send_keys(portalcode.get())
    username_box.send_keys(username.get())
    password_box.send_keys(password.get())

    # presses the log in button
    login_button = driver.find_element_by_css_selector('button.btn')
    login_button.click()

    try:
        # opens up to the gradebook
        gradebook = driver.find_element_by_link_text('Gradebook')
        gradebook.click()

        # saves student picture
        student_pic = driver.find_element_by_css_selector('img.img').get_attribute('src')
        print(student_pic)
        #s = urllib.request.urlretrieve(student_pic, "s.jpeg")

        #
        #response = requests.get(student_pic)
        #picR = response.content
        #image = tk.PhotoImage(data = picR)
        #label = tk.Label(image=image)
        #label.pack(page2)

        # finds the name of the courses/ teacher/ grade

        list_course = driver.find_elements_by_css_selector('td.finedetail')

        for n in list_course:
            grades_listed = [n.text]

            grades = ttk.Label(page2, text=n.text)
            grades.pack()

    except selenium.common.exceptions.NoSuchElementException:
        print("Mhmm did you type your login correctly? Try again.")

HEIGHT = 500
WIDTH = 600

# make window
root = tk.Tk()
root.title("Grade Finder")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# makes tabs
NB = ttk.Notebook(frame)
NB.place(relx=0, rely=0, relwidth=1, relheight=1)
page1 = ttk.Frame(NB)
page2 = ttk.Frame(NB)
NB.add(page1, text='Login')
NB.add(page2, text='Grades')



# page 1
# portalcode
portalcode = ttk.Entry(page1)
portalcode.pack()

# username
username = ttk.Entry(page1)
username.pack()

#password
password = ttk.Entry(page1, show="*")
password.pack()

NB.pack(expand=1, fill="both")

# page 2
refresh = ttk.Button(page2, text="REFRESH", command=fetch)

refresh.pack()



root.mainloop()




