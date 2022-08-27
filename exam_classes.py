from tkinter import *
import tkinter.messagebox
import mysql.connector
import tkinter as tk
from tkinter import ttk
import sqlite3
import simil_function


#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="Pallinotato1666!",database="exam2")
cursordb = connectiondb.cursor()



class login_class:
    
    def failed_destroy():
        failed_message.destroy()
        
    def logged_destroy():
        logged_message.destroy()
        root2.destroy()
    
    def failed():
        global failed_message
        failed_message = Toplevel(root2)
        failed_message.title("Invalid Message")
        failed_message.geometry("500x100")
        Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
        Label(failed_message, text="").pack()
        Button(failed_message,text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=login_class.failed_destroy).pack()
    
    
    
    def Exit():
        wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
        if wayOut > 0:
            root.destroy()
            return
    def logged():
        global logged_message
        logged_message = Toplevel(root2)
        logged_message.title("Welcome")
        logged_message.geometry("500x500")
        Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
        Label(logged_message, text="").pack()
        Button(logged_message, text="See and Change your data", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=change_data_class.change_data).pack()
        Label(logged_message, text="").pack()
        Button(logged_message, text="See people like you", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=simil_class.simil).pack()
        Label(logged_message, text="").pack()
        Button(logged_message, text="Logout", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=login_class.logged_destroy).pack()
    
    def login_verification():
        global user_verification 
        global pass_verification
        user_verification = username_verification.get()
        pass_verification = password_verification.get()
        sql = "select * from users where name = %s and password = %s"
        cursordb.execute(sql,[(user_verification),(pass_verification)])
        results = cursordb.fetchall()
        if results:
            for i in results:
                login_class.logged()
                break
            
        else:
            login_class.failed()
            
                
        
    
    
        
    
    def login():
        global root2
        root2 = Toplevel(root)
        root2.title("Account Login")
        root2.geometry("450x300")
        root2.config(bg="white")
        global username_verification
        global password_verification
        Label(root2, text='Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
        bg="blue",width=300).pack()
        username_verification = StringVar()
        password_verification = StringVar()
        Label(root2, text="").pack()
        Label(root2, text="name :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=username_verification).pack()
        Label(root2, text="").pack()
        Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=password_verification, show="*").pack()
        Label(root2, text="").pack()
        Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=login_class.login_verification).pack()
        Label(root2, text="")
     
 
    
 
    
 
    
 
    
 
    
 
    
 
    

class register_class:
    def registered_destroy():
        registered_message.destroy()
        root2.destroy()
        
    def registered_mysql():
        global registered_message
        registered_message = Toplevel(root2)
        registered_message.title("Registration")
        registered_message.geometry("500x100")
        Label(registered_message, text="You are registered ".format(username.get()), fg="blue", font="bold").pack()
        Label(registered_message, text="").pack()
        Label(registered_message, text="Now you will be able to see who is like you", fg="blue", font="bold").pack()
        Label(registered_message, text="").pack()
        Button(registered_message, text="", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=register_class.registered_destroy).pack()
    
    
    def register_mysql():
        user = username.get()
        passw = password.get()
        country_reg = country.get()
        nationality_reg = nationality.get()
        profession_reg = profession.get()
        favfood_reg = favfood.get()
        favdrink_reg = favdrink.get()
        hobbies_reg = hobbies.get()
        
        sql = "INSERT INTO `users` (`name`,`password`, `country`,`nationality`, `profession`,`favfood`, `favdrink`,`hobbies`) VALUES ( %s , %s , %s , %s , %s , %s , %s , %s )"
        cursordb.execute(sql,[(user),(passw),(country_reg),(nationality_reg),(profession_reg),(favfood_reg),(favdrink_reg),(hobbies_reg)])
        connectiondb.commit()
        register_class.registered_mysql()
    
    
    
    def register():
        global username
        global password
        global country
        global nationality
        global profession
        global favfood
        global favdrink
        global hobbies
        global root2
        
        root2 = Toplevel(root)
        root2.title("Account register")
        root2.geometry("450x700")
        root2.config(bg="white")
        
        
        
        Label(root2, text='Enter your details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
        bg="blue",width=300).pack()
        
        username = StringVar()
        password = StringVar()
        country = StringVar()
        nationality = StringVar()
        profession = StringVar()
        favfood = StringVar()
        favdrink = StringVar()
        hobbies = StringVar()
        
        Label(root2, text="").pack()
        
        Label(root2, text="name :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=username).pack()
        Label(root2, text="").pack()
        
        Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=password).pack()
        Label(root2, text="").pack()
        
        Label(root2, text="country :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=country).pack()
        Label(root2, text="").pack()
        
        Label(root2, text="nationality :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=nationality).pack()
        Label(root2, text="").pack()
        
        Label(root2, text="profession :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=profession,).pack()
        Label(root2, text="").pack()
        
        Label(root2, text="favorite food :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=favfood).pack()
        Label(root2, text="").pack()
        
        Label(root2, text="favorite drink :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=favdrink,).pack()
        Label(root2, text="").pack()
        
        Label(root2, text="hobby :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=hobbies).pack()
        Label(root2, text="").pack()
        Button(root2, text="register", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=register_class.register_mysql).pack()
        Label(root2, text="")
    




    
    
class features_class:
    
    def country():
        global resu_c
        sql="SELECT `country` from users WHERE `name`=%s and `password`=%s"
        cursordb.execute(sql,[(user_verification),(pass_verification)])
        resu=cursordb.fetchall()
        resu_c=(' '.join(map(str, resu)))
        return resu_c
    
    def nationality():
        global resu_n
        sql="SELECT `nationality` from users WHERE `name`=%s and `password`=%s"
        cursordb.execute(sql,[(user_verification),(pass_verification)])
        resu_1=cursordb.fetchall()
        resu_n=(' '.join(map(str, resu_1)))
        return resu_n
    
    def profession():
        global resu_p
        sql="SELECT `profession` from users WHERE `name`=%s and `password`=%s"
        cursordb.execute(sql,[(user_verification),(pass_verification)])
        resu_2=cursordb.fetchall()
        resu_p=(' '.join(map(str, resu_2)))
        return resu_p
    
    def favfood():
        global resu_ff
        sql="SELECT `favfood` from users WHERE `name`=%s and `password`=%s"
        cursordb.execute(sql,[(user_verification),(pass_verification)])
        resu_3=cursordb.fetchall()
        resu_ff=(' '.join(map(str, resu_3)))
        return resu_ff
    
    def favdrink():
        global resu_fd
        sql="SELECT `favdrink` from users WHERE `name`=%s and `password`=%s"
        cursordb.execute(sql,[(user_verification),(pass_verification)])
        resu_4=cursordb.fetchall()
        resu_fd=(' '.join(map(str, resu_4)))
        return resu_fd
    
    def hobbies():
        global resu_h
        sql="SELECT `hobbies` from users WHERE `name`=%s and `password`=%s"
        cursordb.execute(sql,[(user_verification),(pass_verification)])
        resu_5=cursordb.fetchall()
        resu_h=(' '.join(map(str, resu_5)))
        return resu_h
       


        

class change_data_class:
    def change_data_destroy():
        changed_message.destroy()
        
    def final_message():
        global changed_message
        changed_message = Toplevel(root2)
        changed_message.title("message")
        changed_message.geometry("500x100")
        Label(changed_message, text="your data have been modified correctly", fg="red", font="bold").pack()
        Label(changed_message, text="").pack()
        Button(changed_message,text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=change_data_class.change_data_destroy).pack()
    
        
    def change_data_finished():     
        password_change = password.get()
        user_change = username.get()
        country_change = country.get()
        nationality_change = nationality.get()
        profession_change = profession.get()
        favfood_change = favfood.get()
        favdrink_change = favdrink.get()
        hobbies_change = hobbies.get()
        real_name= user_verification
        real_pass=pass_verification
        
        if user_change:
            print(user_change)
            sql = "UPDATE users SET `name` = %s WHERE `name` = %s and `password` = %s"
            cursordb.execute(sql,[(user_change), (real_name), (real_pass)])
            real_name=user_change
            
        
        if  password_change:
            print(password_change)
            sql = "UPDATE users SET `password` = %s WHERE `name` = %s and `password` = %s"
            cursordb.execute(sql,[(password_change), (real_name), (real_pass)])    
            real_pass=password_change
            
            
        
        
        if country_change:
            print(country_change)
            sql = "UPDATE users SET `country` = %s WHERE `name` = %s and `password` = %s"
            cursordb.execute(sql,[(country_change), (real_name), (real_pass)])
            
            
            
        if nationality_change:
            print(nationality_change)
            sql = "UPDATE users SET `nationality` = %s WHERE `name` = %s and `password` = %s"
            cursordb.execute(sql,[(nationality_change), (real_name), (real_pass)])
            
            

        if profession_change:
            print(profession_change)
            sql = "UPDATE users SET `profession` = %s WHERE `name` = %s and `password` = %s"
            cursordb.execute(sql,[(profession_change), (real_name), (real_pass)])
            
            
            
        if favfood_change:
            print(favfood_change)
            sql = "UPDATE users SET `favfood` = %s WHERE `name` = %s  and `password` = %s"
            cursordb.execute(sql,[(favfood_change), (real_name), (real_pass)])
            


        if favdrink_change:
            print(favdrink_change)
            sql = "UPDATE users SET `favdrink` = %s WHERE `name` = %s  and `password` = %s"
            cursordb.execute(sql,[(favdrink_change), (real_name), (real_pass)])
            
            
            
        if hobbies_change:
            print(hobbies_change)
            sql = "UPDATE users SET `hobbies` = %s WHERE `name` = %s and `password` = %s"
            cursordb.execute(sql,[(hobbies_change), (real_name), (real_pass)])
        
        connectiondb.commit()
        change_data_class.final_message()
        
         
    def change_data():
        global username
        global password
        global country
        global nationality
        global profession
        global favfood
        global favdrink
        global hobbies
        global root2
        username = StringVar()
        password = StringVar()
        country = StringVar()
        nationality = StringVar()
        profession = StringVar()
        favfood = StringVar()
        favdrink = StringVar()
        hobbies = StringVar()
            
        root2 = Toplevel(root)
        root2.title("Account details")
        root2.geometry("450x700")
        root2.config(bg="white")
        Label(root2, text='Edit your details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
        bg="blue",width=300).pack()      
        
       
        
      
        Label(root2, text="").pack()
        
        Label(root2, text="name :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=username).pack()
        Label(root2, textvariable=username_verification).pack()
        
        Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=password).pack()
        Label(root2, textvariable=password_verification).pack()
        
        Label(root2, text="country :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=country).pack()
        Label(root2, text=features_class.country()).pack()
        
        Label(root2, text="nationality :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=nationality).pack()
        Label(root2, text=features_class.nationality()).pack()
        
        Label(root2, text="profession :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=profession).pack()
        Label(root2, text=features_class.profession()).pack()
        
        Label(root2, text="favorite food :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=favfood).pack()
        Label(root2, text=features_class.favfood()).pack()
        
        Label(root2, text="favorite drink :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=favdrink).pack()
        Label(root2, text=features_class.favdrink()).pack()
        
        Label(root2, text="Hobby :", fg="black", font=('arial', 12, 'bold')).pack()
        Entry(root2, textvariable=hobbies).pack()
        Label(root2, text=features_class.hobbies()).pack()
        
       
        
        Button(root2, text="finished", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=change_data_class.change_data_finished).pack()
        Label(root2, text="")      
        






class simil_class:
    global root2
    root2 = Toplevel(root)
    root2.title("Similarities")
    root2.geometry("450x1000")
    root2.config(bg="white")
    Label(root2, text='Here you will find people like you', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",width=300).pack()
    Label(root2, text="").pack()    
    Button(root2, text="same country", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=simil_function.same_country(features_class.country())).pack()
    Label(root2, text="")
    Label(root2, text="").pack()    
    Button(root2, text="same nationality", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=simil_function.same_nationality(features_class.nationality())).pack()
    Label(root2, text="")
    Label(root2, text="").pack()    
    Button(root2, text="same profession", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=simil_function.same_profession(features_class.profession())).pack()
    Label(root2, text="")
    Label(root2, text="").pack()    
    Button(root2, text="same favorite food", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=simil_function.same_favfood(features_class.favfood())).pack()
    Label(root2, text="")
    Label(root2, text="").pack()    
    Button(root2, text="same favorite drink", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=simil_function.same_favdrink(features_class.favdrink())).pack()
    Label(root2, text="")
    Label(root2, text="").pack()    
    Button(root2, text="same hobbies", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=simil_function.same_hobbies(features_class.hobbies())).pack()
    Label(root2, text="")
    
    
    
    
   
            
   
       
   

        

    
        
    

            


        






















def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Login System")
    root.geometry("500x500")
    Label(root,text='Welcome to Log In System', bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
    bg="blue",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Log In', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",command=login_class.login).pack()
    Label(root,text="").pack()
    Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",command=login_class.Exit).pack()
    Label(root,text="").pack()
    Button(root,text='Register', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
    bg="blue",command=register_class.register).pack()
    Label(root,text="").pack()
    



main_display()
root.mainloop()   

for x in cursordb  :
    print(x) 
