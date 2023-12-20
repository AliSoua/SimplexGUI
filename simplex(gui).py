import tkinter
import customtkinter    
from CTkMessagebox import CTkMessagebox
from Sub_Functions import *
from PIL import Image, ImageTk
import qrcode
import hashlib
from data import *
import pyotp
import qrcode
from maximisationfirst import *
from minimisationfirst import *


customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry("600x440")
app.title("Project Python")
my_image = ImageTk.PhotoImage(Image.open('bgp2.jpg'))
button = customtkinter.CTkLabel(app, image=my_image ,)
button.pack()
global max_entries 
max_entries = []  


def maxaxsupb() :
    pass


def maxaxinfb():
    global max_entries  
    maxframe.place_forget()
    maxframea.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    c = int(max_text.get()) 
    v = int(max_text1.get())  

    for i in range(v + 1): 
        for j in range(c + 1):  
            if i == v or j == c:  
                entry = customtkinter.CTkEntry(master=maxframea, width=40, placeholder_text=f"X{i * (c + 1) + j}")
                entry.grid(row=i, column=j, padx=5, pady=5) 
                max_entries.append(entry)
            else:
                entry = customtkinter.CTkEntry(master=maxframea, width=40, placeholder_text=f"X{i * c + j}")
                entry.grid(row=i, column=j, padx=5, pady=5)  
                max_entries.append(entry)
    pressmaxframea = customtkinter.CTkButton(master=maxframea, text="Perform Simplex", corner_radius=8, command=pressmaxframea1)
    pressmaxframea.grid(row=v+1, columnspan=c + 1, padx=5, pady=40)  

def pressmaxframea1():
    global max_entries
    rows = int(max_text.get())
    cols = int(max_text1.get())
    matrix = []
    index = 0
    for i in range(cols + 1):
        row_entries = []
        for j in range(rows + 1):
            value = max_entries[index].get() 
            row_entries.append(value)
            index += 1
        matrix.append(row_entries)
    for row in matrix:
        print(row)
    tab = []
    tab = maximisationfirst(matrix,int(max_text.get()),int(max_text1.get()))
    maxframea.place_forget()
    maxframearesult.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    l = 0
    for i in tab :
        log_label = customtkinter.CTkLabel(master=maxframearesult , text=i , font=('century gothic', 18))
        log_label.place(x=30 , y=50 + l)
        l+=40
################################################################################
def minaxinfb():
    global max_entries  
    minframe.place_forget()
    minframea.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    c = int(min_text.get()) 
    v = int(min_text1.get())  

    for i in range(v + 1): 
        for j in range(c + 1):  
            if i == v or j == c:  
                entry = customtkinter.CTkEntry(master=minframea, width=40, placeholder_text=f"X{i * (c + 1) + j}")
                entry.grid(row=i, column=j, padx=5, pady=5) 
                max_entries.append(entry)
            else:
                entry = customtkinter.CTkEntry(master=minframea, width=40, placeholder_text=f"X{i * c + j}")
                entry.grid(row=i, column=j, padx=5, pady=5)  
                max_entries.append(entry)
    pressminframea = customtkinter.CTkButton(master=minframea, text="Perform Simplex", corner_radius=8, command=pressminframea1)
    pressminframea.grid(row=v+1, columnspan=c + 1, padx=5, pady=40)  

def pressminframea1():
    global max_entries
    rows = int(min_text.get())
    cols = int(min_text1.get())
    matrix = []
    index = 0
    for i in range(cols + 1):
        row_entries = []
        for j in range(rows + 1):
            value = max_entries[index].get() 
            row_entries.append(value)
            index += 1
        matrix.append(row_entries)
    for row in matrix:
        print(row)
    tab = []
    tab = minimisationfirst(matrix,int(min_text.get()),int(min_text1.get()))
    minframea.place_forget()
    minframearesult.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    l = 0
    for i in tab :
        log_label = customtkinter.CTkLabel(master=minframearesult , text=i , font=('century gothic', 18))
        log_label.place(x=30 , y=50 + l)
        l+=40

################################################################################
################################################################################
def minaxsupb():
    global max_entries  
    minframe.place_forget()
    minframeb.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    c = int(max_text.get()) 
    v = int(max_text1.get())  

    for i in range(v + 1): 
        for j in range(c + 1):  
            if i == v or j == c:  
                entry = customtkinter.CTkEntry(master=minframeb, width=40, placeholder_text=f"X{i * (c + 1) + j}")
                entry.grid(row=i, column=j, padx=5, pady=5) 
                max_entries.append(entry)
            else:
                entry = customtkinter.CTkEntry(master=minframeb, width=40, placeholder_text=f"X{i * c + j}")
                entry.grid(row=i, column=j, padx=5, pady=5)  
                max_entries.append(entry)
    pressminframeb = customtkinter.CTkButton(master=minframeb, text="Perform Simplex", corner_radius=8, command=pressminframea1)
    pressminframeb.grid(row=v+1, columnspan=c + 1, padx=5, pady=40)  

def pressminframeb1():
    global max_entries
    rows = int(max_text.get())
    cols = int(max_text1.get())
    matrix = []
    index = 0
    for i in range(cols + 1):
        row_entries = []
        for j in range(rows + 1):
            value = max_entries[index].get() 
            row_entries.append(value)
            index += 1
        matrix.append(row_entries)
    for row in matrix:
        print(row)
    tab = []
    tab = minimisationfirst(matrix,int(max_text.get()),int(max_text1.get()))
    minframeb.place_forget()
    minframebresult.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    l = 0
    for i in tab :
        log_label = customtkinter.CTkLabel(master=maxframearesult , text=i , font=('century gothic', 18))
        log_label.place(x=30 , y=50 + l)
        l+=40
################################################################################        




def registerrandompass () :
    if wel_email.get()=="" or wel_pwd.get()!="" or wel_pwd2.get()!="" :
        CTkMessagebox(title="Error", message="To register using this feature you need just to fill email and leave the other textboxes empty")
    else:
        if check_email_existence(wel_email.get()) == False :
                if isValid(wel_email.get()) :
                    password = genererpass()
                    passqr = customtkinter.CTkLabel(qrframe , text="This is your pass : " + password , font=('century gothic', 16))
                    passqr.place(x=55 , y=20)

                    password = hashlib.sha256(wel_pwd.get().encode()).hexdigest()
                    add_user(wel_email.get(),password)
                    CTkMessagebox(title="Info", message="valid registration " ) 
                    registerframe.place_forget() 
                    key = "alisouasecretkey"
                    uri = pyotp.totp.TOTP(key).provisioning_uri(name="alisoua", issuer_name="crypt app")
                    totp = pyotp.TOTP(key)
                    qrcode.make(uri).save("qr.png")
                    my_imageqr = ImageTk.PhotoImage(Image.open('qr.png').resize((230,230)))
                    btnbackqr = customtkinter.CTkLabel(qrframe, image=my_imageqr , text="" ,)
                    btnbackqr.place(x=70 , y=140)
                    qrframe.place(relx=0.5 , rely=0.5 ,anchor =tkinter.CENTER )
                else :
                    CTkMessagebox(title="Info", message="Enter a valid email " )
        else :
            CTkMessagebox(title="Info", message="This email is already used in our database")


def log() :
    password = hashlib.sha256(log_pwd.get().encode()).hexdigest()
    if check_credentials(log_email.get(),password) :
            
            CTkMessagebox(title="Info", message="Access granted ") 
            login.place_forget()
            key = "alisouasecretkey"
            uri = pyotp.totp.TOTP(key).provisioning_uri(name="alisoua", issuer_name="crypt app")
            totp = pyotp.TOTP(key)
            qrcode.make(uri).save("qr.png")
            my_imageqr = ImageTk.PhotoImage(Image.open('qr.png').resize((220,220)))
            btnbackqr = customtkinter.CTkLabel(qrframe, image=my_imageqr , text="" ,)
            btnbackqr.place(x=65 , y=140)
            qrframe.place(relx=0.5 , rely=0.5 ,anchor =tkinter.CENTER )
    else : 
        CTkMessagebox(title="Info", message="Compte invalid !!")

def register2 () :
    if wel_email.get()=="" or wel_pwd.get()=="" or wel_pwd2.get()=="" :
        CTkMessagebox(title="Error", message="To register you need to fill the form")
    else:
        if check_email_existence (wel_email.get()) == False :
            if wel_pwd2.get() == wel_pwd.get() :    
                if isValid(wel_email.get()) and isValidpass(wel_pwd.get()):

                    password = hashlib.sha256(wel_pwd.get().encode()).hexdigest()
                    add_user(wel_email.get(),password)

                    CTkMessagebox(title="Info", message="valid registration") 
                    registerframe.place_forget()
                    key = "alisouasecretkey"
                    uri = pyotp.totp.TOTP(key).provisioning_uri(name="alisoua", issuer_name="crypt app")
                    totp = pyotp.TOTP(key)
                    qrcode.make(uri).save("qr.png")
                    my_imageqr = ImageTk.PhotoImage(Image.open('qr.png').resize((200,200)))
                    btnbackqr = customtkinter.CTkLabel(qrframe, image=my_imageqr , text="" ,)
                    btnbackqr.place(x=55 , y=100)
                    qrframe.place(relx=0.5 , rely=0.5 ,anchor =tkinter.CENTER )
                else :
                    CTkMessagebox(title="Info", message="Check the validity of both of your email and pass")
            else :
                CTkMessagebox(title="Info", message="Your password must match your confirmation")
        else :
            CTkMessagebox(title="Info", message="This email is already used in our database")

def gotoregister() :
    welcome.place_forget()
    registerframe.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def gotologin() :
    welcome.place_forget()
    login.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)  
def qrframetohome() :
    key = "alisouasecretkey"
    totp = pyotp.TOTP(key)
    if (totp.verify(qrframe_answer.get())) :
        qrframe.place_forget()
        home.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
    else :
        CTkMessagebox(title="Info", message="False Code .. Enter again !!")
def backwelcome() :
    login.place_forget()
    welcome.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)
def backwelcome2() :
    registerframe.place_forget()
    welcome.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER)   

def backwelcome3() :
    maxframe.place_forget()
    home.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER) 
def backwelcome4() :
    minframe.place_forget()
    home.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER) 



def btnfhere() :
    login.place_forget()
    registerframe.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER) 
def hometomin() :
    home.place_forget()
    minframe.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER) 
def hometomax() :
    home.place_forget()
    maxframe.place(relx=0.5 , rely=0.5 , anchor=tkinter.CENTER) 


### First Frame to show up(welcome) ##
welcome = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
log_label = customtkinter.CTkLabel(master=welcome , text="Welcome" , font=('century gothic', 36))
log_label.place(x=50 , y=50)
btnlogin = customtkinter.CTkButton(welcome , text="Login" , command=gotologin)
btnlogin.place(x=75 , y=200)
btnregister = customtkinter.CTkButton(welcome , text="Register" , command=gotoregister)
btnregister.place(x=75 , y=150)
welcome.place(relx=0.5,rely=0.5 , anchor=tkinter.CENTER)

######Login page###########
login = customtkinter.CTkFrame(master=button , width=280 ,height=330 , corner_radius=16 ,)
log_label = customtkinter.CTkLabel(master=login , text="Log into your account" , font=('century gothic', 20))
log_label.place(x=30 , y=50)
log_email = customtkinter.CTkEntry(master=login , width=220 , placeholder_text="Email")
log_email.place(x=30 , y=105)
log_pwd = customtkinter.CTkEntry(master=login , width=220 , placeholder_text="Password" ,show="*")
log_pwd.place(x=30 , y= 150)
log_label = customtkinter.CTkLabel(master=login , text="Forget Password" , font=('century gothic', 12))
log_label.place(x=150 , y=180)
btn_login = customtkinter.CTkButton(master=login , width=220 , text="Login" , corner_radius=8 , command=log)
btn_login.place(x=30 , y=210)
log_label = customtkinter.CTkLabel(master=login , text="Create Account Here" , font=('century gothic', 12))
log_label.place(x=70 , y=240)


#######register page#############
registerframe = customtkinter.CTkFrame(master=button , width=280 ,height=330 , corner_radius=16 ,)
wel_label = customtkinter.CTkLabel(master=registerframe , text="Register an account" , font=('century gothic', 20))
wel_label.place(x=40 , y=50)
wel_email = customtkinter.CTkEntry(master=registerframe , width=220 , placeholder_text="Email")
wel_email.place(x=30 , y=105)
wel_pwd = customtkinter.CTkEntry(master=registerframe, width=220 , placeholder_text="Password" ,show="*")
wel_pwd.place(x=30 , y= 150)
wel_pwd2 = customtkinter.CTkEntry(master=registerframe , width=220 , placeholder_text="Confirm Password",show="*")
wel_pwd2.place(x=30 , y= 195)
btn_login = customtkinter.CTkButton(master=registerframe , width=220 , text="Register" , corner_radius=8 ,command=register2)
btn_login.place(x=30 , y=240)
btn_login2 = customtkinter.CTkButton(master=registerframe , width=220 , text="Register (Using Pass Generator)" , corner_radius=8 ,command=registerrandompass)
btn_login2.place(x=30 , y=285)


######qr page###########
qrframe = customtkinter.CTkFrame(master=button , width=330 ,height=380 , corner_radius=16 ,)
qrframe_label = customtkinter.CTkLabel(master=qrframe , text="Scan this to get Access" , font=('century gothic', 20))
qrframe_label.place(x=50 , y=65)
qrframe_answer = customtkinter.CTkEntry(master=qrframe , width=220 , placeholder_text="Enter Qr Code",)
qrframe_answer.place(x=55 , y= 100)
btn_qrframe = customtkinter.CTkButton(master=qrframe , width=220 , text="Go to Home" , corner_radius=8 , command=qrframetohome)
btn_qrframe.place(x=60 , y=340)

###home
home = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
btnfunctcesar2 = customtkinter.CTkButton(master=home,  text="   Minimisation  ",  width=130 ,height=40 ,hover_color="#4158D0", command=hometomin)
btnfunctcesar2.place(x=70, y=30,)
btnfunctdataset3 = customtkinter.CTkButton(master=home,text="  Maximisation  ",  width=100 ,height=40 ,hover_color="#4158D0",command=hometomax)
btnfunctdataset3.place(x=70, y=90,)

#maxframe
maxframe = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
max_text = customtkinter.CTkEntry(master=maxframe, width=220 , placeholder_text=" Variables " )
max_text.place(x=30 , y= 50)
max_text1 = customtkinter.CTkEntry(master=maxframe, width=220 , placeholder_text=" Contraintes " )
max_text1.place(x=30 , y= 100)
max_c = customtkinter.CTkButton(master=maxframe, text="  AX >= B  ",  width=120 ,height=40 ,hover_color="#4158D0",command=maxaxsupb)
max_c.place(x=70, y=150,)
max_d = customtkinter.CTkButton(master=maxframe, text="  AX <= B  ",  width=120 ,height=40 ,hover_color="#4158D0",command=maxaxinfb)
max_d.place(x=70, y=200,)

#max>=frame
maxframea = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
#max>=frameresult
maxframearesult = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)

#max<=frame
maxframeb = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
#max<=frameresult
maxframebresult = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)


#minframe
minframe = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
min_text = customtkinter.CTkEntry(master=minframe, width=220 , placeholder_text=" Variables " )
min_text.place(x=30 , y= 50)
min_text1 = customtkinter.CTkEntry(master=minframe, width=220 , placeholder_text=" Contraintes " )
min_text1.place(x=30 , y= 50)
min_c = customtkinter.CTkButton(master=minframe, text="  AX >= B  ",  width=120 ,height=40 ,hover_color="#4158D0",command=minaxsupb)
min_c.place(x=70, y=150,)
min_d = customtkinter.CTkButton(master=minframe, text="  AX <= B  ",  width=120 ,height=40 ,hover_color="#4158D0",command=minaxinfb)
min_d.place(x=70, y=200,)

#min>=frame
minframea = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
#min>=frameresult
minframearesult = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)

#min<=frame
minframeb = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)
#min<=frameresult
minframebresult = customtkinter.CTkFrame(master=button , width=280 ,height=330, corner_radius=16 ,)



































my_image1 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback1 = customtkinter.CTkButton(login, image=my_image1 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=backwelcome)
btnback1.place(x=10 , y=10)
my_image2 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback2 = customtkinter.CTkButton(registerframe, image=my_image2 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=backwelcome2)
btnback2.place(x=10 , y=10)
my_image3 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback3 = customtkinter.CTkButton(maxframe, image=my_image3 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=backwelcome3)
btnback3.place(x=10 , y=10)
my_image4 = ImageTk.PhotoImage(Image.open('backbtn2.png').resize((30,30)))
btnback4 = customtkinter.CTkButton(minframe, image=my_image4 , text="" ,width=40, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=backwelcome4)
btnback4.place(x=10 , y=10)

btnhere = customtkinter.CTkButton(login , text="Here" , text_color="blue" , font=('century gothic', 13) , width=10, fg_color="#2B2B2B" ,bg_color="#2B2B2B" ,hover_color="#2B2B2B" ,command=btnfhere)
btnhere.place(x=166 , y=240)

app.mainloop()
