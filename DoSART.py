__author__ = 'Liew Jun Tung'

from Tkinter import *
from ttk import *

from PIL import ImageTk, Image
import base64
import HTTPDoS
import time
import socket
import Check
from threading import Thread
import database
import webbrowser


class App:

    def __init__ (self, root):
        self.frame = Frame(root)

        self.notebook = Notebook(self.frame)
        self.f1 = Frame(self.notebook, width=200, height=100)
        self.f2 = Frame(self.notebook, width=200, height=100)
        self.f3 = Frame(self.notebook, width=200, height=100)
        self.f4 = Frame(self.notebook, width=200, height=100)

        self.notebook.add(self.f1, text="1. Set Up")
        self.notebook.add(self.f2, text="2. Attack", state="disabled")
        self.notebook.add(self.f3, text="3. Report", state="disabled")
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

        self.maxprogress = 0
        self.progressvalue = 0
        self.checkflag1 = 0
        self.checkflag2 = 0
        self.port = 0
        self.operatingSystem = "Others"

    def setup_mod(self, parent):

        self.empty = Frame(parent)
        self.setup_button1 = Button(parent, text="Next", state="disabled")
        self.setup_button1['command'] = self.launch_http_attack
        self.setup_check1 = Checkbutton(parent, text="Reporting", command=self.checkAll)
        self.setup_check2 = Checkbutton(parent, text="Fix Applied?", command=self.checkAll)
        #self.setup_check1.invoke()

        self.setup_choice1 = Combobox(parent)
        self.setup_choice1['values'] = ['HTTP']
        self.setup_choice1.current(0)
        self.setup_choice1.config(state='readonly')
        self.setup_choice1.bind("<<ComboboxSelected>>", self.bindPort)
        self.setup_entry1 = Entry(parent)
        self.setup_entry2 = Entry(parent)
        self.setup_entry3 = Entry(parent)
        self.setup_entry1.bind("<FocusOut>", self.checkWebsite)

        self.setup_label1 = Label(parent, text="IP Address: ")
        self.setup_label1_ = Label(parent)
        self.setup_label2 = Label(parent, text="Port <optional>")
        self.setup_entry2.insert(0, "80")
        self.setup_label3 = Label(parent, text="Attacking Method ")
        self.setup_label4 = Label(parent, text="Duration: <optional>")
        self.setup_entry3.insert(0, "20")


        self.empty.grid(row=0, column=2, pady=20)
        self.setup_label1.grid(row=1, column=2, sticky=(N, S, E, W), padx=200)
        self.setup_label1_.grid(row=2, column=2, sticky=(N, S, E, W), columnspan=2)
        self.setup_entry1.grid(row=3, column=2)
        self.setup_label2.grid(row=4, column=2, sticky=(N, S, E, W), padx=200)
        self.setup_entry2.grid(row=5, column=2)
        self.setup_label3.grid(row=8, column=2, sticky=(N, S, E, W), padx=200)
        self.setup_choice1.grid(row=9, column=2)
        self.setup_check1.grid(row=10, column=2)
        self.setup_check2.grid(row=11, column=2)
        self.setup_label4.grid(row=6, column=2)
        self.setup_entry3.grid(row=7, column=2)
        self.setup_button1.grid(row=12, column=3)
        self.setup_label1_.grid_remove()
        # parent.columnconfigure(0, weight=1)
        # parent.rowconfigure(0, weight=1)

    def attacking_mod(self, parent):
        self.empty = Frame(parent)

        self.atk_label1 = Label(parent, text="IP Address: ")
        self.atk_label2 = Label(parent, text="Server: ")
        self.atk_label3 = Label(parent, text="Port: ")
        self.atk_label4 = Label(parent, text="Attacking Method: ")
        self.atk_label5 = Label(parent, text="Time Elapsing: ")
        self.atk_label6 = Label(parent, text="Status: ")

        self.atk_label1_ = Label(parent)
        self.atk_label2_ = Label(parent)
        self.atk_label3_ = Label(parent)
        self.atk_label4_ = Label(parent)
        self.atk_label5_ = Label(parent)
        self.atk_label6_ = Label(parent)
        self.atk_progress = Progressbar(parent, mode="determinate")
        self.atk_button = Button(parent, text="Cancel", command=self.pop)

        self.empty.grid(row=0, column=2, pady=20)
        self.atk_label1.grid(row=1, column=2, sticky=(N, S, E, W), padx=200)
        self.atk_label2.grid(row=2, column=2)
        self.atk_label3.grid(row=3, column=2)
        self.atk_label4.grid(row=4, column=2)
        self.atk_label5.grid(row=5, column=2)
        self.atk_label1_.grid(row=1, column=3)
        self.atk_label2_.grid(row=2, column=3)
        self.atk_label3_.grid(row=3, column=3)
        self.atk_label4_.grid(row=4, column=3)
        self.atk_label5_.grid(row=5, column=3)
        self.atk_label6_.grid(row=6, column=3)

        self.atk_progress.grid(row=7, column=1, columnspan=3)
        self.atk_button.grid(row=8, column=4, padx=10, pady=10, sticky=(S,E))

    def report_mod(self, parent):
        self.empty = Frame(parent)

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

        self.empty.grid(row=0, column=2, pady=20)
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


        self.rpt_button.grid(row=8, column=4, padx=10, pady=10, sticky=(S,E))

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
            self.tree.insert('', 'end', text=records[0], values=(records[1], records[2], records[3], records[4], records[5],
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


    def bindPort(self, event):
        if self.setup_entry2.get() == "":
            if self.setup_choice1.get() == "HTTP":
                self.setup_entry2.insert(0, "80")
        else:
            print "nothing here"

    def validIP(self, address):
        parts = address.split(".")
        if len(parts) != 4:
            return False
        for item in parts:
            if not 0 <= int(item) <= 255:
                return False
        return True

    def launch_http_attack(self):
        if self.setup_entry1.get() != "" and self.setup_entry2.get() != "":
            if self.validIP(self.setup_entry1.get()):
                if self.setup_entry3.get() == "":
                    self.setup_entry3.insert(0, "80")
                if self.setup_entry2.get() == "":
                    self.setup_entry2.insert(0, "20")
                self.progressvalue = 0
                self.atk_progress["value"] = 0
                self.duration = int(self.setup_entry3.get())
                self.atk_progress["maximum"] = self.duration
                self.maxprogress = self.duration
                self.timelimit = self.maxprogress
                self.checkStatus(self.setup_entry1.get())
                t1 = Thread(target=self.HTTP)
                t2 = Thread(target=self.launch_attack)
                t1.start()
                #self.launch_attack()
                t2.start()
            else:
                print "Invalid IP address"
        else:
            print "ERROR"

    def HTTP(self):
        self.maxprogress=self.duration
        HTTPDoS.setTarget(self.setup_entry1.get(), self.maxprogress, self.setup_entry2.get())

    def launch_attack(self):
        self.progressvalue += 1
        self.timelimit -= 1
        self.atk_progress["value"] = self.progressvalue
        self.notebook.tab(1, state="normal")
        self.notebook.select(1)
        self.atk_label1_["text"] = self.setup_entry1.get()
        self.atk_label2_["text"] = self.operatingSystem
        self.atk_label3_["text"] = self.setup_entry2.get()
        self.atk_label4_["text"] = self.setup_choice1.get()
        self.atk_label5_["text"] = self.timelimit
        self.rpt_label1_["text"] = self.setup_entry1.get()
        self.rpt_label2_["text"] = self.operatingSystem
        self.rpt_label3_["text"] = self.setup_entry2.get()
        self.rpt_label4_["text"] = self.setup_choice1.get()
        self.rpt_label5_["text"] = str(self.timelimit) + "seconds(s)"

        if self.progressvalue < self.maxprogress:
            self.notebook.tab(0, state="disabled")
            self.notebook.tab(2, state="disabled")
            self.notebook.tab(3, state="disabled")

            root.after(1000, self.launch_attack)
            if self.progressvalue == 5 or self.progressvalue == 10 or self.progressvalue == 18:
                self.checkStatus(self.setup_entry1.get())
        else:
            self.notebook.tab(2)
            self.notebook.tab(0, state="normal")
            self.notebook.tab(2, state="normal")
            self.notebook.tab(3, state="normal")
            self.notebook.tab(1, state="disabled")
            self.progressvalue = 0
            self.report()
            self.notebook.select(2)

    def report(self):
        database.insertData(self.setup_entry1.get(), self.operatingSystem, self.setup_entry2.get(), self.setup_choice1.get(),
                            self.setup_entry3.get(), self.status)
        self.tree.insert('', 'end', text=str(self.numbers+1), values=(self.setup_entry1.get(), self.operatingSystem, self.setup_entry2.get(), self.setup_choice1.get(),
                            self.setup_entry3.get(), self.status))
        self.rpt_label1_["text"] = self.setup_entry1.get()
        self.rpt_label2_["text"] = self.setup_entry2.get()
        self.rpt_label3_["text"] = self.setup_choice1.get()
        self.rpt_label4_["text"] = self.maxprogress


    def checkStatus(self, iPaddress):
        if Check.main(iPaddress) != "OK":
            self.atk_label6_.config(foreground="GREEN")
            self.rpt_label6_.config(foreground="GREEN")
            self.atk_label6_["text"] = "Website down - Attack Successful"
            self.rpt_label6_["text"] = "Website down - Attack Successful"
            self.status = "Success"
        else:
            self.atk_label6_.config(foreground="RED")
            self.rpt_label6_.config(foreground="RED")
            self.atk_label6_["text"] = "Website up - Attack Unsuccessful"
            self.rpt_label6_["text"] = "Website up - Attack Unsuccessful"
            self.status = "Failed"

    def checkWebsite(self, event):
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

    def checkAll(self):

        if any('selected' in x for x in self.setup_check1.state()):
            if self.checkflag1 == 1:
                self.setup_button1.configure(state="enabled")
            else:
                self.setup_button1.configure(state="disabled")
        else:
            self.setup_button1.configure(state="disabled")

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
        new=2
        webbrowser.open(database.findSolution(self.operatingSystem), new=new)

root = Tk()
app = App(root)
root.mainloop()