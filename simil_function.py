from tkinter import ttk
from tkinter import *
import tkinter.messagebox
import mysql.connector
import tkinter as tk
import sqlite3

import mysql.connector
#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="Pallinotato1666!",database="exam2")
cursordb = connectiondb.cursor()

def same_country(a):
    def View():

        

        cursordb.execute("SELECT * FROM users WHERE `country`= %s",a)

        rows = cursordb.fetchall()    

        for row in rows:

            print(row) 

            tree.insert("", tk.END, values=row)        

        connectiondb.close()


    root = tk.Tk()

    tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')

    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="name")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="country")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="nationality")

    tree.pack()

    button1 = tk.Button(text="Display data", command=View)

    button1.pack(pady=10)

    root.mainloop()

def same_nationality(a):
    def View():

        

        cursordb.execute("SELECT * FROM users WHERE `nationality`= %s",a)

        rows = cursordb.fetchall()    

        for row in rows:

            print(row) 

            tree.insert("", tk.END, values=row)        

        connectiondb.close()


    root = tk.Tk()

    tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')

    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="name")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="country")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="nationality")

    tree.pack()

    button1 = tk.Button(text="Display data", command=View)

    button1.pack(pady=10)

    root.mainloop()

def same_profession(a):
    def View():

        

        cursordb.execute("SELECT * FROM users WHERE `profession`= %s",a)

        rows = cursordb.fetchall()    

        for row in rows:

            print(row) 

            tree.insert("", tk.END, values=row)        

        connectiondb.close()


    root = tk.Tk()

    tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')

    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="name")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="country")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="nationality")

    tree.pack()

    button1 = tk.Button(text="Display data", command=View)

    button1.pack(pady=10)

    root.mainloop()

def same_favfood(a):
    def View():

        

        cursordb.execute("SELECT * FROM users WHERE `favfood`= %s",a)

        rows = cursordb.fetchall()    

        for row in rows:

            print(row) 

            tree.insert("", tk.END, values=row)        

        connectiondb.close()


    root = tk.Tk()

    tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')

    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="name")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="country")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="nationality")

    tree.pack()

    button1 = tk.Button(text="Display data", command=View)

    button1.pack(pady=10)

    root.mainloop()


def same_favdrink(a):
    def View():

        

        cursordb.execute("SELECT * FROM users WHERE `favdrink`= %s",a)

        rows = cursordb.fetchall()    

        for row in rows:

            print(row) 

            tree.insert("", tk.END, values=row)        

        connectiondb.close()


    root = tk.Tk()

    tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')

    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="name")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="country")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="nationality")

    tree.pack()

    button1 = tk.Button(text="Display data", command=View)

    button1.pack(pady=10)

    root.mainloop()
    
def same_hobbies(a):
    def View():

        

        cursordb.execute("SELECT * FROM users WHERE `hobbies`= %s",a)

        rows = cursordb.fetchall()    

        for row in rows:

            print(row) 

            tree.insert("", tk.END, values=row)        

        connectiondb.close()


    root = tk.Tk()

    tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')

    tree.column("#1", anchor=tk.CENTER)

    tree.heading("#1", text="name")

    tree.column("#2", anchor=tk.CENTER)

    tree.heading("#2", text="country")

    tree.column("#3", anchor=tk.CENTER)

    tree.heading("#3", text="nationality")

    tree.pack()

    button1 = tk.Button(text="Display data", command=View)

    button1.pack(pady=10)

    root.mainloop()