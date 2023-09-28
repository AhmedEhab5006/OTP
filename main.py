#importing libraries
from tkinter import *
import customtkinter
from customtkinter import *
import random
from tkinter import messagebox as msg
import smtplib , ssl



#creating confirm function which stores the OTP that user entered
def confirm () :
    global generated_OTP
    OTP = otp_entry.get()
    if generated_OTP == "" :
        msg.showerror(title = "OTP verification" , message = "You must generate an OTP first")
    if OTP == "" :
        error_label = customtkinter.CTkLabel(root , text = "You must enter an OTP" , text_color = "red" , bg_color = "#08c4b3")
        error_label.place(x = 140 , y = 220)
    else :
        ok_label = customtkinter.CTkLabel(root , text = "You must enter an OTP" , text_color = "#08c4b3" , bg_color = "#08c4b3")
        ok_label.place(x = 140 , y = 220 )


    #making sure that OTP which user entered is equal to generated OTP
    if int(OTP) == int(generated_OTP) :
        blank_label = customtkinter.CTkLabel(root, text_color="#08c4b3", bg_color="#08c4b3",text="OTP is sent to your Email", font=customtkinter.CTkFont(size=15))
        blank_label.place(x=300, y=389)
        msg.showinfo(title = "OTP verification" , message = "Your Email is verified successfully")
    else:
        msg.showerror(title = "OTP verification" , message = "Invalid OTP")



#creating clearing functions which clears inputs
def clear_all () :
    global Email , OTP , email_entry , otp_entry
    Email = ""
    OTP = ""
    email_entry = customtkinter.CTkEntry(root, bg_color="#08c4b3", width=260, height=10)
    email_entry.place(x=190, y=90)
    otp_entry = customtkinter.CTkEntry(root, bg_color="#08c4b3", width=260, height=10)
    otp_entry.place(x=190, y=190)
def clear_email () :
    global Email , email_entry
    Email = ""
    email_entry = customtkinter.CTkEntry(root, bg_color="#08c4b3", width=260, height=10)
    email_entry.place(x=190, y=90)
def clear_otp () :
    global OTP , otp_entry
    OTP = ""
    otp_entry = customtkinter.CTkEntry(root, bg_color="#08c4b3", width=260, height=10)
    otp_entry.place(x=190, y=190)




#creating function which generates an OTP and takes Email input from user
def Verify () :
    global Email , generated_OTP
    try:
        global Email
        Email = email_entry.get()
        if Email == "":
            error_label = customtkinter.CTkLabel(root, text="You must enter an Email", text_color="red",bg_color="#08c4b3")
            error_label.place(x=188, y=120)
            blank_label = customtkinter.CTkLabel(root, text="Email must be : example@gmail.com", text_color="#08c4b3",bg_color="#08c4b3")
            blank_label.place(x=87, y=140)

        elif "@gmail.com" not in Email:
            blank_label = customtkinter.CTkLabel(root, text="You must enter an Email", text_color="#08c4b3",bg_color="#08c4b3")
            blank_label.place(x=188, y=120)
            error_label = customtkinter.CTkLabel(root, text="Invalid Email", text_color="red", bg_color="#08c4b3")
            error_label.place(x=188, y=120)
            error_label = customtkinter.CTkLabel(root, text="Email must be : example@gmail.com", text_color="red",bg_color="#08c4b3")
            error_label.place(x=87, y=140)
        else:
            ok_label = customtkinter.CTkLabel(root, text="You must enter an Email", text_color="#08c4b3",bg_color="#08c4b3")
            ok_label.place(x=188, y=120)
            error_label = customtkinter.CTkLabel(root, text="Email must be : example@gmail.com", text_color="#08c4b3",bg_color="#08c4b3")
            error_label.place(x=87, y=140)
        generated_OTP = random.randint(100000 , 999999)
        sender_email = 'otp15102004@gmail.com'
        password = 'yhmt eewd jdsb syno'
        receiver_email = [Email , "otp15102004@gmail.com"]
        send_email = f'''OTP verification
        To: {','.join(receiver_email)}
        Your OTP is {generated_OTP}'''
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com" , 465 , context = context ) as server :
            server.login(sender_email , password )
            server.sendmail(sender_email , receiver_email , send_email)
        done_label = customtkinter.CTkLabel(root , text_color = "green" , bg_color = "#08c4b3" , text = "OTP is sent to your Email" )
        done_label.place(x = 170 , y = 120 )
        if Email == "" or "@gmail.com" not in Email:
            done_label.destroy()

    except:
        msg.showerror(title = "OTP verification" , message = "An error occurred" )



#creating app's window
root = CTk ()
Email = ""
OTP = ""
generated_OTP = ""
customtkinter.deactivate_automatic_dpi_awareness()
customtkinter.set_appearance_mode("Light")
root.title("OTP verification")
root.iconbitmap("Elements\\Images\\email.ico")
bg_img = PhotoImage(file = "Elements\\Images\\back.png")
bg_label = Label(root , image = bg_img)
bg_label.pack()
title_label = Label(root , text = "Simple OTP verification app" , fg = "white" , bg = "#08c4b3" , font = "Bold 17")
title_label.place(x =247 , y = 15)
email_label = customtkinter.CTkLabel (root , text = "Enter your Email" , bg_color = "#08c4b3" , text_color = "white" ,font = customtkinter.CTkFont(size = 15))
email_label.place(x = 60 , y = 88)
email_entry = customtkinter.CTkEntry(root , bg_color = "#08c4b3" , width = 260 , height = 10 )
email_entry.place(x = 190 , y = 90 )
confirm_button = customtkinter.CTkButton(root , text = "Verify" , fg_color = "green" , bg_color = "#08c4b3" , width = 100 , command = Verify)
confirm_button.place(x = 500 , y = 85)
clear_button1 = customtkinter.CTkButton(root , text = "Clear" , fg_color = "red" , bg_color = "#08c4b3" , width = 100 , command = clear_email)
clear_button1.place(x = 650 , y = 85)
clear_button2 = customtkinter.CTkButton(root , text = "Clear" , fg_color = "red" , bg_color = "#08c4b3" , width = 100 , command = clear_otp )
clear_button2.place(x = 650 , y = 185)
otp_label = customtkinter.CTkLabel(root ,text = "Enter the OTP" , text_color = "white" , bg_color = "#08c4b3" , font = customtkinter.CTkFont(size = 15) )
otp_label.place(x = 60 , y = 190)
otp_entry = customtkinter.CTkEntry(root , bg_color = "#08c4b3" , width = 260 , height = 10 )
otp_entry.place(x = 190 , y = 190)
confirm_button2 = customtkinter.CTkButton(root , text = "Confirm" , fg_color = "green" , bg_color = "#08c4b3" , width = 100 , command = confirm)
confirm_button2.place(x = 500 , y = 185)
clear_btn = customtkinter.CTkButton(root , text = "Clear all fields" , bg_color = "#08c4b3" , fg_color = "red" , command = clear_all)
clear_btn.place(x = 312 , y = 360)
root.geometry("780x440")
root.resizable(False , False)
root.mainloop()
