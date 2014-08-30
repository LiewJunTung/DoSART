__author__ = 'Liew Jun Tung'

from Tkinter import *
from ttk import *

import HTTPDoS
import time
import tkFont
import Check
from threading import Thread
import database
import webbrowser
import drawline


class App:
    def __init__(self, root):
        self.maxprogress = 0
        self.progressvalue = 0
        self.timeLimit = 0
        self.checkflag1 = 0
        self.checkflag2 = 0
        self.port = 0
        self.operatingSystem = "Others"
        self.currentInterval = 1
        self.atk_flag = True

        self.descFont = tkFont.Font(family='Helvetica',
                                    size=10)
        self.opFont = tkFont.Font(underline=1, size=10)

        self.frame = Frame(root)
        self.notebook = Notebook(self.frame)
        self.f1 = Frame(self.notebook, width=200, height=100)
        self.f2 = Frame(self.notebook, width=200, height=100)
        self.f3 = Frame(self.notebook, width=200, height=100)
        self.f4 = Frame(self.notebook, width=200, height=100)

        self.notebook.add(self.f1, text="1. Set Up")
        self.notebook.add(self.f2, text="2. Attack", state="normal")
        self.notebook.add(self.f3, text="3. Report", state="normal")
        self.notebook.add(self.f4, text="4. Log")

        self.setup_mod(self.f1)
        self.attacking_mod(self.f2)
        self.report_mod(self.f3)
        self.log_mod(self.f4)
        self.frame.grid(row=0, column=0, sticky=(N, S, E, W))
        self.notebook.grid(row=0, column=0, sticky=(N, S, E, W))

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=2)
        self.frame.rowconfigure(0, weight=2)



    def setup_mod(self, parent):

        self.setup_grid0 = Frame(parent)
        self.setup_grid1 = Frame(parent)

        master_desc = "Welcome to Denial of Service Attack and Reporting Tool(DoSaRT).\n1. This program is to help you " \
                      "understand the durability of your web server \n    against various HTTP Denial of Services." \
                      "\n2. Please remember that this tool have the potential to cause loss of data. " \
                      "\n3. Do ensure your test system is not currently under official usage."

        entry1_desc = "The IP address of \nthe test machine.\nMake sure the data \nof this web server" \
                      "\nis backup before \nproceeding."
        entry2_desc = "The Port of machine. \n Default is 80"

        check1_desc = "Test Slowloris DoS \nattack <SAFE>"
        check2_desc = "Test HULK DoS\nattack \n<EXTREMELY UNSAFE>\nMake sure your \nsystem is not " \
                      "doing \nimportant functions"
        checkfin_desc = "Confirm settings and ready to test the \ntarget system."

        self.setup_description = Label(self.setup_grid1, text="Description")
        self.setup_descText = Text(self.setup_grid0, font=self.descFont, height=5, width=65, bg="PeachPuff",
                                   borderwidth=3, relief=GROOVE)
        self.setup_descText.insert(INSERT, master_desc)
        self.setup_descText.config(state=DISABLED)

        #self.setup_descText.bind('<Button-1>', lambda event, desc=entry1_desc: self.test(event, desc))

        self.setup_help = Text(self.setup_grid1, height=15, width=20, state=DISABLED, bg="PeachPuff", borderwidth=3,
                               relief=GROOVE)

        self.setup_button1 = Button(self.setup_grid1, text="Next", state="disabled", command=self.prep_http_attack)
        # self.setup_button1['command'] = launch_http_attack
        self.setup_check10 = Checkbutton(self.setup_grid0, command=self.check_dos)
        self.setup_check11 = Checkbutton(self.setup_grid0)
        self.setup_check20 = Checkbutton(self.setup_grid0, command=self.check_dos)
        self.setup_check21 = Checkbutton(self.setup_grid0)
        self.setup_checkfin = Checkbutton(self.setup_grid0, text="ARE YOU READY", command=self.checkall)
        # self.setup_check1.invoke()

        self.setup_entry1 = Entry(self.setup_grid0)
        self.setup_entry2 = Entry(self.setup_grid0)
        self.setup_entry30 = Entry(self.setup_grid0, width=3)
        self.setup_entry31 = Entry(self.setup_grid0, width=3)
        self.setup_entry1.bind("<FocusOut>", self.check_website)

        self.setup_label1 = Label(self.setup_grid0, text="Target Server IP Address")
        self.setup_label1_ = Label(self.setup_grid0)
        self.setup_label2 = Label(self.setup_grid0, text="Port <optional>")
        self.setup_entry2.insert(0, "80")
        self.setup_label30 = Label(self.setup_grid0, text="Attacking Method", font=self.opFont)
        self.setup_label31 = Label(self.setup_grid0, text="Test", font=self.opFont)
        self.setup_label32 = Label(self.setup_grid0, text="Fix Applied", font=self.opFont)
        self.setup_label33 = Label(self.setup_grid0, text="Duration(sec)", font=self.opFont)
        self.setup_label4 = Label(self.setup_grid0, text="Slowloris")
        self.setup_label5 = Label(self.setup_grid0, text="HULK")

        self.setup_entry30.insert(0, "20")
        self.setup_entry31.insert(0, "20")

        #bind action
        self.setup_entry1.bind('<Enter>', lambda event, desc=entry1_desc: self.test(event, desc))
        self.setup_entry2.bind('<Enter>', lambda event, desc=entry2_desc: self.test(event, desc))
        self.setup_check10.bind('<Enter>', lambda event, desc=check1_desc: self.test(event, desc))
        self.setup_check20.bind('<Enter>', lambda event, desc=check2_desc: self.test(event, desc))
        self.setup_checkfin.bind('<Enter>', lambda event, desc=checkfin_desc: self.test(event, desc))

        #Frame Grid
        self.setup_grid0.grid(row=0, column=0)
        self.setup_grid1.grid(row=0, column=1)

        self.setup_descText.grid(row=0, columnspan=4)

        self.setup_label1.grid(row=1, columnspan=4)
        self.setup_label1_.grid(row=2, columnspan=4)
        self.setup_entry1.grid(row=3, columnspan=4)
        self.setup_label2.grid(row=4, columnspan=4)
        self.setup_entry2.grid(row=5, columnspan=4)
        self.setup_label30.grid(row=6, column=0)
        self.setup_label31.grid(row=6, column=1)
        self.setup_label32.grid(row=6, column=2)
        self.setup_label33.grid(row=6, column=3)

        self.setup_label4.grid(row=7, column=0)
        self.setup_check10.grid(row=7, column=1)
        self.setup_check11.grid(row=7, column=2)
        self.setup_entry30.grid(row=7, column=3)

        self.setup_label5.grid(row=8, column=0)
        self.setup_check20.grid(row=8, column=1)
        self.setup_check21.grid(row=8, column=2)
        self.setup_entry31.grid(row=8, column=3)

        self.setup_checkfin.grid(row=9, columnspan=4)


        #self.setup_entry3.grid(row=10)
        #self.setup_label4.grid(row=11)

        # self.setup_check1.grid(row=13)
        # self.setup_check2.grid(row=14)

        self.setup_description.grid(row=0)
        self.setup_help.grid(row=1, sticky=(N))
        self.setup_button1.grid(row=2)

        self.setup_label1_.grid_remove()
        # parent.columnconfigure(0, weight=1)
        # parent.rowconfigure(0, weight=1)

    def attacking_mod(self, parent):
        self.atk_grid0 = Frame(parent)
        self.atk_grid1 = Frame(parent)

        self.atk_label1 = Label(self.atk_grid0, text="IP Address: ")
        self.atk_label2 = Label(self.atk_grid0, text="Operating System: ")
        self.atk_label3 = Label(self.atk_grid0, text="Port: ")
        self.atk_label4 = Label(self.atk_grid0, text="Attacking Method: ")
        self.atk_label5 = Label(self.atk_grid0, text="Time Elapsing: ")
        self.atk_label6 = Label(self.atk_grid0, text="Status: ")
        self.atk_label7 = Label(self.atk_grid0, text="Progress")

        self.atk_label1_ = Label(self.atk_grid0)
        self.atk_label2_ = Label(self.atk_grid0)
        self.atk_label3_ = Label(self.atk_grid0)
        self.atk_label4_ = Label(self.atk_grid0)
        self.atk_label5_ = Label(self.atk_grid0)
        self.atk_label6_ = Label(self.atk_grid0)
        self.atk_progress = Progressbar(self.atk_grid0, mode="determinate", length=200)
        self.atk_button = Button(self.atk_grid0, text="Cancel", command=self.pop)

        self.atk_console = Text(self.atk_grid1, font=self.descFont, height=9, width=50, bg="PeachPuff",
                                borderwidth=3, relief=GROOVE)

        self.atk_draw = drawline.App(self.atk_grid1)
        # self.atk_status = Canvas(self.atk_grid1, width=270, height=160, bg='white')

        self.atk_grid0.grid(row=1)
        self.atk_label1.grid(row=0)
        self.atk_label2.grid(row=1)
        self.atk_label3.grid(row=2)
        self.atk_label4.grid(row=3)
        self.atk_label5.grid(row=4)
        self.atk_label6.grid(row=5)
        self.atk_label1_.grid(row=0, column=1)
        self.atk_label2_.grid(row=1, column=1)
        self.atk_label3_.grid(row=2, column=1)
        self.atk_label4_.grid(row=3, column=1)
        self.atk_label5_.grid(row=4, column=1)
        self.atk_label6_.grid(row=5, column=1)

        self.atk_label7.grid(row=6, columnspan=2)
        self.atk_progress.grid(row=7, columnspan=2)
        self.atk_grid1.grid(row=8, columnspan=2)
        self.atk_console.grid(row=0, column=1)
        self.atk_draw.grid(row=0, column=2)

    def report_mod(self, parent):
        self.setup_grid0 = Frame(parent)

        self.rpt_label1 = Label(parent, text="IP Address: ")
        self.rpt_label2 = Label(parent, text="Operating System: ")
        self.rpt_label3 = Label(parent, text="Port: ")
        self.rpt_label4 = Label(parent, text="Attacking Method: ")
        self.rpt_label5 = Label(parent, text="Time Elapsed: ")
        self.rpt_label6 = Label(parent, text="Status: ")
        self.rpt_label7 = Label(parent, text="Solution")

        self.rpt_label1_ = Label(parent)
        self.rpt_label2_ = Label(parent)
        self.rpt_label3_ = Label(parent)
        self.rpt_label4_ = Label(parent)
        self.rpt_label5_ = Label(parent)
        self.rpt_label6_ = Label(parent)
        self.rpt_label7_ = Label(parent)

        self.rpt_button = Button(parent, text="Cancel", command=self.pop)

        self.setup_grid0.grid(row=0, column=2, pady=20)
        self.rpt_label1.grid(row=1, column=2, sticky=(N, S, E, W), padx=200)
        self.rpt_label2.grid(row=2, column=2)
        self.rpt_label3.grid(row=3, column=2)
        self.rpt_label4.grid(row=4, column=2)
        self.rpt_label5.grid(row=5, column=2)
        self.rpt_label6.grid(row=6, column=2)
        self.rpt_label7.grid(row=7, column=2)

        self.rpt_label7_.bind('<Enter>', self.pop1)
        self.rpt_label7_.bind('<Leave>', self.pop2)
        self.rpt_label7_.bind('<Button-1>', self.openURL)

        self.rpt_label1_.grid(row=1, column=3)
        self.rpt_label2_.grid(row=2, column=3)
        self.rpt_label3_.grid(row=3, column=3)
        self.rpt_label4_.grid(row=4, column=3)
        self.rpt_label5_.grid(row=5, column=3)
        self.rpt_label6_.grid(row=6, column=3)
        self.rpt_label7_.grid(row=7, column=3)

        self.rpt_button.grid(row=8, column=4, padx=10, pady=10, sticky=(S, E))

    def log_mod(self, parent):
        self.log_button = Button(parent, text="Load", command=self.loadRecords)
        self.tree = Treeview(parent, columns=('IP', 'OS', 'Port', 'Atk', 'Duration', 'Status', 'Solution'))

        self.tree.column('#0', width=50)
        self.tree.column('#1', width=100)
        self.tree.column('#2', width=80)
        self.tree.column('#3', width=50)
        self.tree.column('#4', width=100)
        self.tree.column('#5', width=50)
        self.tree.column('#6', width=80)
        self.tree.column('#7', width=80)
        self.tree.heading('#0', text="No.")
        self.tree.heading('#1', text="IP")
        self.tree.heading('#2', text="OS")
        self.tree.heading('#3', text="Port")
        self.tree.heading('#4', text="Attack Method")
        self.tree.heading('#5', text="Duration")
        self.tree.heading('#6', text="Status")
        self.tree.heading('#7', text="Solution")

        self.tree.grid(row=1, column=1, columnspan=2)
        self.log_button.grid(row=2, column=2, sticky=(E, S))

        for records in database.getRecords():
            self.tree.insert('', 'end', text=records[0],
                             values=(records[1], records[2], records[3], records[4], records[5],
                                     records[6], records[7]))
            self.numbers = records[0]

    def loadRecords(self):
        record = self.tree.set(self.tree.get_children()[self.tree.index(self.tree.focus())])
        print record
        self.rpt_label1_['text'] = record['IP']
        self.rpt_label2_['text'] = record['OS']
        self.rpt_label3_['text'] = record['Port']
        self.rpt_label4_['text'] = record['Atk']
        self.rpt_label5_['text'] = record['Duration']
        self.rpt_label6_['text'] = record['Status']
        self.rpt_label7_['text'] = "CLICK HERE"
        self.operatingSystem = record['OS']
        self.notebook.tab(2, state='normal')
        self.notebook.select(2)

    def validIP(self, address):
        parts = address.split(".")
        if len(parts) != 4:
            return False
        for item in parts:
            if not 0 <= int(item) <= 255:
                return False
        return True


    def prep_atk(self):
        self.atk_flag = True
        if any('selected' in x for x in self.setup_check10.state()):
            self.prep_http_attack()
        if any('selected' in x for x in self.setup_check20.state()):
            self.prep_hulk_attack()

    def prep_http_attack(self):
        if self.validIP(self.setup_entry1.get()):

            if self.setup_entry2.get() == "":
                self.setup_entry2.insert(0, "80")
            if self.setup_entry30.get() == "":
                self.setup_entry30.insert(0, "20")
            self.progressvalue = 0
            self.atk_progress["value"] = 0
            self.duration = int(self.setup_entry30.get())
            self.atk_progress["maximum"] = self.duration
            self.maxprogress = self.duration
            self.timeLimit = self.maxprogress
            self.check_status(self.setup_entry1.get())
            self.set_config()
            t1 = Thread(target=self.launch_http_attack, args=(500,))
            t2 = Thread(target=self.launch_dos)
            t1.start()
            t2.start()

        else:
            print "Invalid IP address"


    def launch_http_attack(self, trd):
        self.maxprogress = self.duration
        for i in range(1, self.interval+1):
            HTTPDoS.setTarget(trd*i/self.interval, self.setup_entry1.get(), self.maxprogress, self.setup_entry2.get())
            self.atk_console.insert(INSERT, HTTPDoS.getstatus())
            self.atk_console.see(END)
            time.sleep(self.maxprogress)

    def prep_hulk_attack(self):
        pass

    def launch_hulk(self):
        pass

    def set_config(self):
        self.interval = 3



    def launch_dos(self):
        self.progressvalue += 1
        self.timeLimit -= 1
        self.atk_progress["value"] = self.progressvalue
        self.notebook.tab(1, state="normal")
        self.notebook.select(1)

        self.atk_label1_["text"] = self.setup_entry1.get()
        self.atk_label2_["text"] = self.operatingSystem
        self.atk_label3_["text"] = self.setup_entry2.get()
        self.atk_label4_["text"] = "HTTP DOS #%d" %self.currentInterval
        self.atk_label5_["text"] = self.timeLimit
        self.rpt_label1_["text"] = self.setup_entry1.get()
        self.rpt_label2_["text"] = self.operatingSystem
        self.rpt_label3_["text"] = self.setup_entry2.get()
        self.rpt_label4_["text"] = "something"
        self.rpt_label5_["text"] = str(self.timeLimit) + "seconds(s)"

        if self.progressvalue < self.maxprogress and self.currentInterval <= self.interval:
            self.notebook.tab(0, state="disabled")
            self.notebook.tab(2, state="disabled")
            self.notebook.tab(3, state="disabled")
            #self.check_status(self.setup_entry1.get())
            root.after(1000, self.launch_dos)

        elif self.progressvalue == self.maxprogress and self.currentInterval <= self.interval:
            self.progressvalue = 0
            self.timeLimit = self.maxprogress
            self.currentInterval += 1
            self.atk_draw.redraw()
            self.notebook.tab(0, state="disabled")
            self.notebook.tab(2, state="disabled")
            self.notebook.tab(3, state="disabled")
            #self.check_status(self.setup_entry1.get())
            root.after(1000, self.launch_dos)

        else:
            self.notebook.tab(2)
            self.notebook.tab(0, state="normal")
            self.notebook.tab(2, state="normal")
            self.notebook.tab(3, state="normal")
            self.notebook.tab(1, state="disabled")
            self.atk_flag = False
            self.progressvalue = 0
            self.report()
            self.notebook.select(2)

    def report(self):
        database.insertData(self.setup_entry1.get(), self.operatingSystem, self.setup_entry2.get(),
                            self.setup_choice1.get(),
                            self.setup_entry3.get(), self.status)
        self.tree.insert('', 'end', text=str(self.numbers + 1), values=(
        self.setup_entry1.get(), self.operatingSystem, self.setup_entry2.get(), self.setup_choice1.get(),
        self.setup_entry3.get(), self.status))
        self.rpt_label1_["text"] = self.setup_entry1.get()
        self.rpt_label2_["text"] = self.setup_entry2.get()
        self.rpt_label3_["text"] = self.setup_choice1.get()
        self.rpt_label4_["text"] = self.maxprogress
        print self.operatingSystem
        self.rpt_label7_["text"] = database.findSolution(self.operatingSystem)


    def check_status(self, iPaddress):
        if Check.main(iPaddress) != "OK":
            self.atk_label6_.config(foreground="RED")
            self.rpt_label6_.config(foreground="RED")
            self.status = "Website down"
            self.atk_label6_["text"] = self.status
            self.rpt_label6_["text"] = self.status
            self.atk_draw.tik("OFF")
        else:
            self.atk_label6_.config(foreground="GREEN")
            self.rpt_label6_.config(foreground="GREEN")
            self.status = "Website up"
            self.atk_label6_["text"] = self.status
            self.rpt_label6_["text"] = self.status
            self.atk_draw.tik("ON")
        self.atk_console.insert(END, self.status + '\n')
        self.atk_console.see(END)
        if self.atk_flag:
            self.atk_grid1.after(1000, self.check_status, iPaddress)

    def check_website(self, event):
        iPaddress = self.setup_entry1.get()
        if self.setup_entry1.get() != "":
            if self.validIP(iPaddress):
                if Check.main(iPaddress) == "OK":
                    self.setup_label1_.grid()
                    self.setup_label1_.config(background="DARK GREEN")
                    self.setup_label1_.config(foreground="WHITE")
                    self.setup_label1_.config(anchor=CENTER)
                    self.setup_label1_["text"] = "Website is valid"
                    self.checkflag1 = 1
                    self.operatingSystem = Check.checkOS(iPaddress)
                else:
                    self.setup_label1_.grid()
                    self.setup_label1_.config(background="RED")
                    self.setup_label1_.config(foreground="WHITE")
                    self.setup_label1_.config(anchor=CENTER)
                    self.setup_label1_["text"] = "Website is down or invalid"
                    #self.checkflag1 = 0
                    self.checkflag1 = 0
            else:
                self.setup_label1_.grid()
                self.setup_label1_.config(background="RED")
                self.setup_label1_.config(foreground="WHITE")
                self.setup_label1_.config(anchor=CENTER)
                self.setup_label1_["text"] = "Invalid IP"
                self.checkflag1 = 0
        else:
            self.setup_label1_.grid_remove()
            self.checkflag1 = 0
        self.checkall()

    def checkall(self):
        if any('selected' in x for x in self.setup_checkfin.state()):
            if self.checkflag1 == 1 and self.checkflag2 == 1:
                self.setup_button1.configure(state="enabled")
            else:
                self.setup_button1.configure(state="disabled")
        else:
            self.setup_button1.configure(state="disabled")

    def check_dos(self):
        if any('selected' in x for x in self.setup_check10.state()) or \
                any('selected' in x for x in self.setup_check20.state()):
            self.checkflag2 = 1
        else:
            self.checkflag2 = 0
        self.checkall()

    def pop(self):
        self.notebook.tab(0, state="normal")
        self.notebook.tab(2, state="normal")
        self.notebook.tab(1, state="disabled")
        self.progressvalue = self.maxprogress

    def pop1(self, event):
        self.rpt_label7_.config(foreground="BLUE")

    def pop2(self, event):
        self.rpt_label7_.config(foreground="BLACK")

    def openURL(self, event):
        new = 2
        webbrowser.open(database.findSolution(self.operatingSystem), new=new)

    def test(self, event, desc):
        self.setup_help.config(state=NORMAL)
        self.setup_help.delete('1.0', END)
        self.setup_help.insert('1.0', desc)
        self.setup_help.config(state=DISABLED)

root = Tk()
root.wm_title("Denial Of Service Attack and Reporting Tool")
app = App(root)
root.mainloop()