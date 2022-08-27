from tkinter import *
import tkinter.messagebox

records = {}
fr = open('S&S-data.txt', 'r')
for line in fr:
    for i in range(len(line)):
        if line[i] == ':':
            key = line[0:i]
            break
    records[key] = eval(line[i + 1:])


def behind_the_scene_create_account():
    global records
    x = enter_name_entry.get()
    y = password_entry.get()
    if len(y) == 4:
        f = open('S&S-data.txt', 'a+')
        z = x[0::2] + x[:0:-1]
        if z in records.keys():
            answer_1 = tkinter.messagebox.askretrycancel("ERROR", "Enter different username")
            if answer_1 == True:
                create_account()
            else:
                main_window()
        else:
            fp = open(z + '.txt', 'a+')
            records[z] = [x[0::2] + x[:0:-1], x, 0, y]
            f.write("%s:%s" % (z, records[z]))
            fp.write("%s:%s" % (z, records[z]))
            f.write("\n")
            fp.write('\n')
            f.close()
            fp.close()
            answer = tkinter.messagebox.askyesno("INFO", "Account created succesfully Continue?")
            if answer == True or answer == False:
                main_window()
    else:
        tkinter.messagebox.showerror("ERROR", "Enter 4 digit password")


def logout():
    login()


def back():
    main_window()


def online():
    def amount_transferred():
        m = online_entry.get()
        sender_file = open(z + '.txt', 'r')
        all_lines = sender_file.readlines()
        last_line = all_lines[-1]
        temp_data = {}
        temp_data[z] = eval(last_line[len(z) + 1:])
        sender_file.close()
        if temp_data[z][2] >= int(online_entry_2.get()) and m in records.keys():
            recv_file = open(m + '.txt', 'r')
            allLines = recv_file.readlines()
            lastLine = allLines[-1]
            temp = {}
            temp[m] = eval(lastLine[len(m) + 1:])
            recv_file.close()
            recv_file = open(m + '.txt', 'a+')
            temp[m][2] = temp[m][2] + int(online_entry_2.get())
            recv_file.write("%s:%s" % (m, temp[m]))
            recv_file.write('\n')
            recv_file.close()
            updating = open(z + '.txt', 'a+')
            temp_data[z][2] = temp_data[z][2] - int(online_entry_2.get())
            updating.write("%s:%s" % (z, temp_data[z]))
            updating.write('\n')
            updating.close()
            portal()
        else:
            tkinter.messagebox.showerror("ERROR", " Invalid accountname")

    online_frame = Frame(display_frame, width=900, height=400)
    online_frame.place(x=0, y=0)
    online_frame.tkraise()
    online_label = Label(online_frame, text="Enter the account name of reciever")
    online_label.place(x=400, y=100)
    online_entry = Entry(online_frame)
    ddd = Label(online_frame, text='AMOUNT')
    ddd.place(x=400, y=250)
    online_entry.place(x=400, y=200)
    online_entry_2 = Entry(online_frame)
    online_entry_2.place(x=400, y=300)
    online_button = Button(online_frame, text='TRANSFER', command=amount_transferred)
    online_button.place(x=400, y=350)


def withdraw():
    def amount_withdrawn():
        fr = open(z + '.txt', 'r')
        all_lines = fr.readlines()
        last_line = all_lines[-1]
        temp_data = {}
        temp_data[z] = eval(last_line[len(z) + 1:])
        fr.close()
        if temp_data[z][2] >= int(withdraw_entry.get()):
            temp_data[z][2] = temp_data[z][2] - int(withdraw_entry.get())
            file_update = open(z + '.txt', 'a+')
            file_update.write("%s:%s" % (z, temp_data[z]))
            file_update.write('\n')
            file_update.close()
            portal()
        else:
            answer_1 = tkinter.messagebox.askretrycancel("ERROR", "YOU DO NO HAVE SUFFICIENT BALANCE")
            if answer_1 == True:
                withdraw()
            else:
                portal()

    withdraw_frame = Frame(display_frame, width=900, height=400)
    withdraw_frame.place(x=0, y=0)
    withdraw_frame.tkraise()
    withdraw_label = Label(withdraw_frame, text="Enter the amount you want to withdraw")
    withdraw_label.place(x=400, y=100)
    withdraw_entry = Entry(withdraw_frame)
    withdraw_entry.place(x=400, y=200)
    withdraw_button = Button(withdraw_frame, text='WITHDRAW', command=amount_withdrawn)
    withdraw_button.place(x=400, y=300)


def deposit():
    def amount_deposited():
        fr = open(z + '.txt', 'r')
        all_lines = fr.readlines()
        last_line = all_lines[-1]
        temp_data = {}
        temp_data[z] = eval(last_line[len(z) + 1:])
        fr.close()
        temp_data[z][2] = temp_data[z][2] + int(deposit_entry.get())
        file_update = open(z + '.txt', 'a+')
        file_update.write("%s:%s" % (z, temp_data[z]))
        file_update.write('\n')
        file_update.close()
        portal()

    deposit_frame = Frame(display_frame, width=900, height=400)
    deposit_frame.place(x=0, y=0)
    deposit_frame.tkraise()
    deposit_label = Label(deposit_frame, text="Enter the amount u want to deposit")
    deposit_label.place(x=400, y=100)
    deposit_entry = Entry(deposit_frame)
    deposit_entry.place(x=400, y=200)
    deposit_button = Button(deposit_frame, text='Deposit', command=amount_deposited)
    deposit_button.place(x=400, y=300)


def view_account():
    view_account_frame = Frame(display_frame, width=900, height=400)
    view_account_frame.place(x=0, y=0)
    view_account_frame.tkraise()
    fr = open(z + '.txt', 'r')
    all_lines = fr.readlines()
    last_line = all_lines[-1]
    temp_data = {}
    temp_data[z] = eval(last_line[len(z) + 1:])
    fr.close()
    account_name = Label(view_account_frame, text='ACCOUNT NAME: ' + records[z][1])
    account_name.place(x=400, y=100)
    account_code = Label(view_account_frame, text='CODE NAME: ' + records[z][0])
    account_code.place(x=400, y=200)
    account_amount = Label(view_account_frame, text='CURRENT AMOUNT: ' + str(temp_data[z][2]))
    account_amount.place(x=400, y=300)


display_frame = None


def portal():
    dasboard_frame = Frame(login_frame, width=900, height=100, bg='black')
    dasboard_frame.place(x=0, y=0)
    dasboard_frame.tkraise()
    dasboard_button_1 = Button(dasboard_frame, text='VIEW ACCOUNT', command=view_account)
    dasboard_button_1.place(x=100, y=50)
    dasboard_button_2 = Button(dasboard_frame, text='DEPOSIT', command=deposit)
    dasboard_button_2.place(x=300, y=50)
    dasboard_button_3 = Button(dasboard_frame, text='WITHDRAW', command=withdraw)
    dasboard_button_3.place(x=500, y=50)
    dasboard_button_5 = Button(dasboard_frame, text='Online', command=online)
    dasboard_button_5.place(x=700, y=50)
    dasboard_button_4 = Button(dasboard_frame, text='LOGOUT', command=logout)
    dasboard_button_4.place(x=850, y=50)
    global display_frame
    display_frame = Frame(login_frame, width=900, height=400, bg='white')
    display_frame.place(x=0, y=100)
    display_frame.tkraise()

    portal_logo = Label(display_frame, image=img1, bg='white')
    portal_logo.place(x=150, y=0)


x = ''
z = ''


def behind_the_scene_login():
    global x
    global z
    x = enter_username_entry.get()
    z = x[0::2] + x[:0:-1]
    if z in records.keys():
        if login_password_entry.get() == records[z][3]:
            '''fr = open(z + '.txt', 'r')
            last_line = fr.readlines()
            fr.close()'''
            portal()
        else:
            a = tkinter.messagebox.askretrycancel("ERROR", "Invalid username or Password")
            if a == True:
                login()
            else:
                main_window()
    else:
        b = tkinter.messagebox.askretrycancel("ERROR", "Invalid username or Password")
        if b == True:
            login()
        else:
            main_window()


enter_username_entry = None
login_password_entry = None
login_frame = None


def login():
    global login_frame
    login_frame = Frame(login_create_frame, width=900, height=500)
    login_frame.place(x=0, y=0)
    login_frame.tkraise()
    enter_username_label = Label(login_frame, text="Enter User Name: ")
    enter_username_label.place(x=300, y=100)
    global enter_username_entry
    enter_username_entry = Entry(login_frame)
    enter_username_entry.place(x=400, y=100)
    login_password_label = Label(login_frame, text="Enter Password: ")
    login_password_label.place(x=300, y=200)
    global login_password_entry
    login_password_entry = Entry(login_frame, show='*')
    login_password_entry.place(x=400, y=200)
    login_button = Button(login_frame, text='LOGIN', command=behind_the_scene_login)
    login_button.place(x=300, y=300)
    back_button = Button(login_frame, text='BACK', command=back)
    back_button.place(x=500, y=300)


enter_name_entry = None
password_entry = None


def create_account():
    create_account_frame = Frame(login_create_frame, width=900, height=500)
    create_account_frame.place(x=0, y=0)
    create_account_frame.tkraise()
    enter_name_label = Label(create_account_frame, text="Enter Name: ")
    enter_name_label.place(x=300, y=100)
    global enter_name_entry
    enter_name_entry = Entry(create_account_frame)
    enter_name_entry.place(x=400, y=100)
    password_label = Label(create_account_frame, text="Enter Password: ")
    password_label.place(x=300, y=200)
    global password_entry
    password_entry = Entry(create_account_frame)
    password_entry.place(x=400, y=200)
    create_account_button = Button(create_account_frame, text='CREATE ACCOUNT', command=behind_the_scene_create_account)
    create_account_button.place(x=300, y=300)
    back_button = Button(create_account_frame, text='BACK', command=back)
    back_button.place(x=500, y=300)


login_create_frame = None


def main_window():
    global login_create_frame
    login_create_frame = Frame(root, width=900, height=500)
    login_create_frame.place(x=0, y=0)
    main_logo=Label(login_create_frame,image=img2)
    main_logo.place(x=50,y=0)
    login_button = Button(login_create_frame, text='LOGIN', command=login)
    login_button.place(x=300, y=400)
    create_button = Button(login_create_frame, text='CREATE ACCOUNT', command=create_account)
    create_button.place(x=550, y=400)


root = Tk()
root.geometry("900x500")
root.title("Banking System")
img1=PhotoImage(file='plogo.png')
img2=PhotoImage(file='main-logo.png')
main_window()
root.mainloop()
