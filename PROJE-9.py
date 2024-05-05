#PROJECT - 9
import customtkinter
import tkinter as tk
import sqlite3
import bcrypt
from tkinter import *
from tkinter import messagebox

#////////////////////////////////////////////////////////////////////////////////////////////#

r10 = customtkinter.CTk()
r10.title(" ")

r9 = customtkinter.CTk()
r9.title(" ")

r8 = customtkinter.CTk()
r8.title(" ")

r7 = customtkinter.CTk()
r7.title(" ")

r6 = customtkinter.CTk()
r6.title(" ")

r5 = customtkinter.CTk()
r5.title(" ")

r4 = customtkinter.CTk()
r4.title(" ")

r3 = customtkinter.CTk()
r3.title("RECIPE APP")

r2 = customtkinter.CTk()
r2.title("LOGIN")

r1 = customtkinter.CTk()
r1.title("REGISTER")

#////////////////////////////////////////////////////////////////////////////////////////////#

conn = sqlite3.connect("data9.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT NOT NULL,
        password TEXT NOT NULL)''')

#////////////////////////////////////////////////////////////////////////////////////////////#

def login():

    r1.destroy()
    frame2 = customtkinter.CTkFrame(master=r2,
                                    width=350,
                                    height=350)
    frame2.pack(padx=20,pady=20)

    global username_entry_login
    global password_entry_login

    username_entry_login = customtkinter.CTkEntry(master=frame2,
                                                placeholder_text="Username",
                                                width=150,
                                                height=40)
    username_entry_login.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

    password_entry_login = customtkinter.CTkEntry(master=frame2,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
    password_entry_login.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

    verification_button = customtkinter.CTkButton(master=frame2,
                                          text="Verify and Continue!",
                                          command=loginaccount)
    verification_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
    r2.mainloop()

#////////////////////////////////////////////////////////////////////////////////////////////#

def signup():
    username = username_entry_register.get()
    password = password_entry_register.get()
    if ((username != "") and (password != "")):
        cursor.execute("SELECT username FROM users WHERE username=?", [username])
        if(cursor.fetchone() is not None):
            messagebox.showerror("Error","Username already exists!")
        else:
            encodedpassword = password.encode("utf-8")
            hashedpassword = bcrypt.hashpw(encodedpassword, bcrypt.gensalt())
            print(hashedpassword)
            cursor.execute("INSERT into users VALUES(?, ?)", [username, hashedpassword])
            conn.commit()
            messagebox.showinfo("Sucsess!","Account has been created")
            register_to_login_page_button = customtkinter.CTkButton(master=r1,
                                                                    text="Go to Login Page",
                                                                    command=login,)
            register_to_login_page_button.place(relx=0.5, rely=0.6, anchor = tk.CENTER)
    else:
        messagebox.showerror("Error","Enter all data.")

#////////////////////////////////////////////////////////////////////////////////////////////#

def register_to_login_page():
    
    r1.destroy()
    frame2 = customtkinter.CTkFrame(master=r2,
                                    width=350,
                                    height=350)
    frame2.pack(padx=20,pady=20)

    global username_entry_login
    global password_entry_login

    username_entry_login = customtkinter.CTkEntry(master=frame2,
                                                placeholder_text="Username",
                                                width=150,
                                                height=40)
    username_entry_login.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

    password_entry_login = customtkinter.CTkEntry(master=frame2,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
    password_entry_login.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

    verification_button = customtkinter.CTkButton(master=frame2,
                                          text="Verify and Continue!",
                                          command=loginaccount)
    verification_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
    r2.mainloop()

#////////////////////////////////////////////////////////////////////////////////////////////#

def loginaccount():
    username = username_entry_login.get()
    password = password_entry_login.get()
    if ((username != "") and (password != "")):
        cursor.execute("SELECT password FROM users WHERE username=?", [username])
        result = cursor.fetchone()
        if result:
            if bcrypt.checkpw(password.encode("utf-8"), result[0]):
                messagebox.showinfo("Success", f"Logged in successfully, Welcome {username}")
                r2.destroy()

 #////////////////////////////////////////////////////////////////////////////////////////////#
               
               
                def validate_entries():
                    # Hem "From Where" hem de "To Where" alanları doldurulmuş mu kontrol ediliyor
                    if from_where_entry.get() == "" and to_where_entry.get() == "":
                        messagebox.showerror("Error", "Please fill in both 'From Where' and 'To Where' fields.")
                        return False
                    # Sadece "From Where" alanı boşsa
                    elif from_where_entry.get() == "":
                        messagebox.showerror("Error", "Please fill in the 'From Where' field.")
                        return False
                    # Sadece "To Where" alanı boşsa
                    elif to_where_entry.get() == "":
                        messagebox.showerror("Error", "Please fill in the 'To Where' field.")
                        return False
                    else:
                        messagebox.showinfo("Success", "Entries validated successfully!")
                        return True

                # Main function to handle button click
                def on_save_and_show_otels_click():
                    if validate_entries():

                        r3.destroy()  

                        #////////////////////////////////////////////////////////////////////////////////////////////#

                        def otel1_button_function():
                            r4.destroy()

                            def calculate_button_otel_1_function():
                                
                                days_to_stay = calculate_entry_otel_1.get()

                                if not days_to_stay:
                                    messagebox.showerror("Hata", "Lütfen gün sayısını girin.")
                                    return

                                # Rota bilgisini giriş alanlarından alıyoruz.
                                

                                r5.destroy()
                                
                                to = "to"
                                otel_name = "Otel 1"
                                otel_price_per_day = 400
                                
                                
                                total_price = int(days_to_stay) * otel_price_per_day

                                main_frame = customtkinter.CTkFrame(master=r8,
                                                                    width=300,
                                                                    height=200)
                                main_frame.pack(padx=20, pady=20)

                                otel_name_label = customtkinter.CTkLabel(master=main_frame,
                                                                        text=f"Otel Name: {otel_name}")
                                otel_name_label.place(relx=0.1, rely=0.15)

                                how_many_days_label = customtkinter.CTkLabel(master=main_frame,
                                                                            text=f"Days to Stay: {days_to_stay}")
                                how_many_days_label.place(relx=0.1, rely=0.35)

                                otel_price_label = customtkinter.CTkLabel(master=main_frame,
                                                                        text=f"The Price: ${total_price}")
                                otel_price_label.place(relx=0.1, rely=0.55)


                                r8.mainloop()



                            main_frame = customtkinter.CTkFrame(master=r5,
                                            width= 400,
                                            height= 100)
                            main_frame.pack(padx=20,pady=20)

                            calculate_label_otel_1 = customtkinter.CTkLabel(master=main_frame,
                                                                                text="How many days do you wanna stay:")  # Ana çerçevenin arka plan rengi
                            calculate_label_otel_1.place(relx=0.05,rely=0.1)

                            calculate_entry_otel_1 = customtkinter.CTkEntry(master=main_frame)
                            calculate_entry_otel_1.place(relx=0.6,rely=0.1)

                            calculate_button_otel_1 = customtkinter.CTkButton(master=main_frame,
                                                                                text="Reservation and See the Informations!",
                                                                                width=350,
                                                                                command=calculate_button_otel_1_function)
                            calculate_button_otel_1.place(relx=0.05,rely=0.5)

                            r5.mainloop()

                        def otel2_button_function():
                            r4.destroy()

                            def calculate_button_otel_2_function():
                                
                                days_to_stay = calculate_entry_otel_2.get()

                                if not days_to_stay:
                                    messagebox.showerror("Hata", "Lütfen gün sayısını girin.")
                                    return
                                
                                r5.destroy()

                                otel_name = "Otel 2"
                                otel_price_per_day = 100

                                
                                total_price = int(days_to_stay) * otel_price_per_day

                                main_frame = customtkinter.CTkFrame(master=r9,
                                                                    width=300,
                                                                    height=200)
                                main_frame.pack(padx=20, pady=20)

                                otel_name_label = customtkinter.CTkLabel(master=main_frame,
                                                                        text=f"Otel Name: {otel_name}")
                                otel_name_label.place(relx=0.1, rely=0.15)

                                how_many_days_label = customtkinter.CTkLabel(master=main_frame,
                                                                            text=f"Days to Stay: {days_to_stay}")
                                how_many_days_label.place(relx=0.1, rely=0.4)

                                otel_price_label = customtkinter.CTkLabel(master=main_frame,
                                                                        text=f"The Price: ${total_price}")
                                otel_price_label.place(relx=0.1, rely=0.65)

                                

                                r9.mainloop()

                            main_frame = customtkinter.CTkFrame(master=r6,
                                        width= 400,
                                        height= 100)
                            main_frame.pack(padx=20,pady=20)

                            calculate_label_otel_2 = customtkinter.CTkLabel(master=main_frame,
                                                                            text="How many days do you wanna stay:")  # Ana çerçevenin arka plan rengi
                            calculate_label_otel_2.place(relx=0.05,rely=0.1)

                            calculate_entry_otel_2 = customtkinter.CTkEntry(master=main_frame)
                            calculate_entry_otel_2.place(relx=0.6,rely=0.1)

                            calculate_button_otel_2 = customtkinter.CTkButton(master=main_frame,
                                                                            text="Reservation and See the Informations!",
                                                                            width=350,
                                                                            command=calculate_button_otel_2_function)
                            calculate_button_otel_2.place(relx=0.05,rely=0.5)

                            r6.mainloop()

                        def otel3_button_function():
                            r4.destroy()

                            def calculate_button_otel_3_function():
                                
                                days_to_stay = calculate_entry_otel_3.get()

                                if not days_to_stay:
                                    messagebox.showerror("Hata", "Lütfen gün sayısını girin.")
                                    return

                                r5.destroy()

                                otel_name = "Otel 3"
                                otel_price_per_day = 200

                                

                                total_price = int(days_to_stay) * otel_price_per_day

                                main_frame = customtkinter.CTkFrame(master=r10,
                                                                    width=300,
                                                                    height=200)
                                main_frame.pack(padx=20, pady=20)

                                otel_name_label = customtkinter.CTkLabel(master=main_frame,
                                                                        text=f"Otel Name: {otel_name}")
                                otel_name_label.place(relx=0.1, rely=0.15)

                                how_many_days_label = customtkinter.CTkLabel(master=main_frame,
                                                                            text=f"Days to Stay: {days_to_stay}")
                                how_many_days_label.place(relx=0.1, rely=0.4)

                                otel_price_label = customtkinter.CTkLabel(master=main_frame,
                                                                        text=f"The Price: ${total_price}")
                                otel_price_label.place(relx=0.1, rely=0.65)

                                

                                r10.mainloop()

                            main_frame = customtkinter.CTkFrame(master=r7,
                                        width= 400,
                                        height= 100)
                            main_frame.pack(padx=20,pady=20)

                            calculate_label_otel_3 = customtkinter.CTkLabel(master=main_frame,
                                                                            text="How many days do you wanna stay:")  # Ana çerçevenin arka plan rengi
                            calculate_label_otel_3.place(relx=0.05,rely=0.1)

                            calculate_entry_otel_3 = customtkinter.CTkEntry(master=main_frame)
                            calculate_entry_otel_3.place(relx=0.6,rely=0.1)

                            calculate_button_otel_3 = customtkinter.CTkButton(master=main_frame,
                                                                            text="Reservation and See the Informations!",
                                                                            width=350,
                                                                            command=calculate_button_otel_3_function)
                            calculate_button_otel_3.place(relx=0.05,rely=0.5)

                            r7.mainloop()

                        #////////////////////////////////////////////////////////////////////////////////////////////#

                        main_frame = customtkinter.CTkFrame(master=r4,
                                        width= 520,
                                        height= 200)
                        main_frame.pack(padx=20,pady=20)

                        otel_frame_left = customtkinter.CTkFrame(master=main_frame,
                                                                width=172,
                                                                height=200)
                        otel_frame_left.pack(padx=20, pady=20, side="left")

                        otel_frame_middle = customtkinter.CTkFrame(master=main_frame,
                                                                width=172,
                                                                height=200)
                        otel_frame_middle.pack(padx=20, pady=20, side="left")

                        otel_frame_right = customtkinter.CTkFrame(master=main_frame,
                                                                width=172,
                                                                height=200)
                        otel_frame_right.pack(padx=20, pady=20, side="right")

                        otel_option1_label = customtkinter.CTkLabel(master=otel_frame_left,
                                                                    text="OTEL-1")
                        otel_option1_label.place(relx=0.37,rely=0.02)

                        otel_option2_label = customtkinter.CTkLabel(master=otel_frame_middle,
                                                                    text="OTEL-2")
                        otel_option2_label.place(relx=0.37,rely=0.02)
                            
                        otel_option3_label = customtkinter.CTkLabel(master=otel_frame_right,
                                                                    text="OTEL-3")
                        otel_option3_label.place(relx=0.37,rely=0.02)

                        otel_mile1_label = customtkinter.CTkLabel(master=otel_frame_left,
                                                                    text="10 Miles from the city center")
                        otel_mile1_label.place(relx=0.035,rely=0.2)

                        otel_mile2_label = customtkinter.CTkLabel(master=otel_frame_middle,
                                                                    text="20 Miles from the city center")
                        otel_mile2_label.place(relx=0.035,rely=0.2)
                            
                        otel_mile3_label = customtkinter.CTkLabel(master=otel_frame_right,
                                                                    text="15 Miles from the city center")
                        otel_mile3_label.place(relx=0.035,rely=0.2)

                        otel_prices1_label = customtkinter.CTkLabel(master=otel_frame_left,
                                                                    text="400$ Per-Day")
                        otel_prices1_label.place(relx=0.265,rely=0.4)

                        otel_prices2_label = customtkinter.CTkLabel(master=otel_frame_middle,
                                                                    text="100$ Per-Day")
                        otel_prices2_label.place(relx=0.265,rely=0.4)
                            
                        otel_prices3_label = customtkinter.CTkLabel(master=otel_frame_right,
                                                                    text="200$ Per-Day")
                        otel_prices3_label.place(relx=0.256,rely=0.4)

                        otel1_button = customtkinter.CTkButton(master=otel_frame_left,
                                                            text="Go for OTEL-1",
                                                            width=100,
                                                            command=otel1_button_function)
                        otel1_button.place(relx=0.23,rely=0.7)

                        otel2_button = customtkinter.CTkButton(master=otel_frame_middle,
                                                            text="Go for OTEL-2",
                                                            width=100,
                                                            command=otel2_button_function)
                        otel2_button.place(relx=0.23,rely=0.7)

                        otel3_button = customtkinter.CTkButton(master=otel_frame_right,
                                                            text="Go for OTEL-3",
                                                            width=100,
                                                            command=otel3_button_function)
                        otel3_button.place(relx=0.23,rely=0.7)
                            
                        r4.mainloop()                  

                main_frame = customtkinter.CTkFrame(master=r3,
                                                    width= 520,
                                                    height= 200)
                main_frame.pack(padx=20,pady=20)

                route_label = customtkinter.CTkLabel(master=main_frame,
                                                                text="Enter Your Route:")
                route_label.place(relx=0.05,rely=0.2)

                from_where_label = customtkinter.CTkLabel(master=main_frame,
                                                                text="From Where")
                from_where_label.place(relx=0.45,rely=0.05)

                to_where_label = customtkinter.CTkLabel(master=main_frame,
                                                                text="To Where")
                to_where_label.place(relx=0.78,rely=0.05)
                
                global to_where_entry
                global from_where_entry

                from_where_entry = customtkinter.CTkEntry(master=r3)
                from_where_entry.place(relx=0.4,rely=0.24)

                to_where_entry = customtkinter.CTkEntry(master=r3)
                to_where_entry.place(relx=0.7, rely=0.24)

                global from_where  
                global to_where

                from_where = from_where_entry.get()
                to_where = to_where_entry.get()

                save_and_show_otels_button = customtkinter.CTkButton(master=r3,
                                                                    text="Save and Show Otels",
                                                                    width= 200,
                                                                    command=on_save_and_show_otels_click)
                save_and_show_otels_button.place(relx=0.5,rely=0.5) 

 #////////////////////////////////////////////////////////////////////////////////////////////#
                
                r3.mainloop()

 #////////////////////////////////////////////////////////////////////////////////////////////#

            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            messagebox.showerror("Error", "Invalid Username")
    else:
        messagebox.showerror("Error", "Enter all data")

#////////////////////////////////////////////////////////////////////////////////////////////#

frame1 = customtkinter.CTkFrame(master=r1,
                                width=350,
                                height=350)
frame1.pack(padx=20,pady=20)

username_entry_register = customtkinter.CTkEntry(master=frame1,
                                     placeholder_text="Username",
                                     width=150,
                                     height=40)
username_entry_register.place(relx=0.5, rely=0.2, anchor = tk.CENTER)

password_entry_register = customtkinter.CTkEntry(master=frame1,
                                     placeholder_text="Password",
                                     width=150,
                                     height=40,
                                     show = "*")
password_entry_register.place(relx=0.5, rely=0.35, anchor = tk.CENTER)

register_button = customtkinter.CTkButton(master=frame1,
                                          text="Create Your account!",
                                          command=signup)
register_button.place(relx=0.5, rely=0.5, anchor = tk.CENTER)

register_to_login_label = customtkinter.CTkLabel(master=frame1, 
                                                 text="Already have an account?")
register_to_login_label.place(relx=0.5, rely=0.7, anchor = tk.CENTER)

register_to_login_button = customtkinter.CTkButton(master=frame1,
                                          text="Login!",
                                          command=register_to_login_page)
register_to_login_button.place(relx=0.5, rely=0.8, anchor = tk.CENTER)

#////////////////////////////////////////////////////////////////////////////////////////////#

r1.mainloop()    