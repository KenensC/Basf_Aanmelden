########################## Import ########################

import datetime
import threading
import time
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import About
import sap

from cv2 import destroyAllWindows

########################## GUI maken ##########################

root = tk.Tk()
width_value = root.winfo_screenwidth()
width_geo = root.winfo_screenwidth
heigth_value = root.winfo_screenheight()
root.title(" Online Analyse Basf ")
# root.geometry("%dx%d+0+0" % (s_width_value, s_height_value))
# root.geometry("250x250+250+200")
root.resizable(False, False)

########################## Frames ##########################

topFrame = tk.Frame(root)
topFrame.pack()
middleFrame = tk.Frame(root)
middleFrame.pack()
bottomFrame = tk.Frame(root)
bottomFrame.pack(side=BOTTOM, fill=X)

########################## Var ###########################
PIAU, PIAN, PIAI = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()
fil_lijst = []
groep = ""

########################## Labels #########################

theLabel = tk.Label(topFrame, text=f" Aanwezigheid {groep}", font=('Ariel', 20, 'italic', 'underline'))
theLabel.grid(row=0, column=1, padx=(10, 25))
l1 = tk.Label(topFrame, text="Naam", font=('Ariel', 16, 'italic')).grid(row=2, column=0, padx=10)
l2 = tk.Label(topFrame, text="Status", font=('Ariel', 16, 'italic')).grid(row=2, column=1, padx=(25, 25))
l3 = tk.Label(topFrame, text="Glijtijd", font=('Ariel', 16, 'italic')).grid(row=2, column=2, padx=(25, 25))
l4 = tk.Label(topFrame, text="Set", font=('Ariel', 16, 'italic')).grid(row=2, column=4, padx=(25, 10))
labelStatus = tk.Label(root, font=("Ariel", 16, "italic"), bd=1, pady=30)
labelterugMelding = tk.Label(bottomFrame, font=("Ariel", 10, "italic"), relief=tk.SUNKEN, bd=1,
                             anchor="w", width=55)
labelDate = Label(bottomFrame, text="", font=("Times", 10))


############################ Classes ######################

class Persoon:
    def __init__(self, naam, voornaam, groep):
        self.naam = naam
        self.voornaam = voornaam
        self.volledigeNaam = self.voornaam + " " + self.naam
        self.groep = groep
        self.aangemeld = False
        self.bg = "red"


########################### Lists #########################

lijst = [
    Persoon('Ribbens', 'Stefan', 'PIA/U'),
    Persoon('Bollens', 'Mark', 'PIA/U'),
    Persoon('Konings', 'Patrick', 'PIA/U'),
    Persoon('Kenens', 'Christoph', 'PIA/U'),
    Persoon('De Schepper', 'Jonas', 'PIA/U'),
    Persoon('De Vynck', 'Yannick', 'PIA/U'),
    Persoon('De Rango', 'Marco', 'PIA/U'),
    Persoon('Lens', 'Jeff', 'PIA/U'),
    Persoon('Marijnissen', 'Matthijs', 'PIA/U'),
    Persoon('Vansant', 'Frank', 'PIA/U'),
    Persoon('Verlinden', 'Jens', 'PIA/N'),
    Persoon('De Bell', 'Gert', 'PIA/N'),
    Persoon('Van Bogaert', 'Ivo', 'PIA/N'),
]

########################### ProggressBar ###################

progBarVar = IntVar()
progBar = ttk.Progressbar(bottomFrame, orient=HORIZONTAL, length=110, variable=progBarVar)
progBar.config(mode="determinate", maximum=10, value=0)

aantalTechniekers = 0


########################## Functions #######################
def groepSelectie():
    global fil_lijst
    global groep
    if PIAU.get() == True and PIAN.get() == False and PIAI.get() == False:
        groep = "PIA/U"
        filter_lijst()
    elif PIAU.get() == False and PIAN.get() == True and PIAI.get() == False:
        groep = "PIA/N"
        filter_lijst()
    elif PIAU.get() == False and PIAN.get() == False and PIAI.get() == True:
        groep = "PIA/I"
        filter_lijst()
    elif PIAU.get() == False and PIAN.get() == False and PIAI.get() == False:
        groep = ""
        fil_lijst = []
        filter_lijst()


def updatetime():
    now = datetime.datetime.now()
    time_string = now.strftime("Datum: %d-%m-%Y  Tijd:  %H:%M:%S")
    print(time_string)
    labelDate["text"] = time_string


def filter_lijst():
    global fil_lijst
    for item in lijst:
        if item.groep == groep:
            fil_lijst.append(item)
            print(item.naam)
            knoppen()


# if groep == "":
#  fil_lijst.clear()
#  knoppen()
# print("lijst leeg")


def startclock():
    while True:
        updatetime()
        time.sleep(1)


def techniek():
    print("Hiermee open ik de databank")
    # open(Techniekers.py)
    pass


def functie_exit():
    mbox = messagebox.askquestion("Exit", "Bent u zeker om het program te verlaten?", icon="warning")
    if mbox == "yes":
        destroyAllWindows()
        root.destroy()
    else:
        pass


def on_progress_bar_updated(*args):
    # when the progress bar reaches 100, it wraps around to 0
    if progBarVar.get() == 0:
        progBar.stop()
        labelterugMelding["text"] = ""


progBarVar.trace('w', on_progress_bar_updated)


def setStatus(label2: tk.Label, terugMelding):
    print(str(terugMelding))
    label2["text"] = str(terugMelding)


def setStatusBalk(label: tk.Label, aantalTechniekers):
    if aantalTechniekers == 0:
        label["text"] = "Iedereen naar huis, geen techniekers aanwezig!"
    elif aantalTechniekers == 1:
        label["text"] = str(aantalTechniekers) + " Technieker Aanwezig "
    else:
        label["text"] = str(aantalTechniekers) + " Techniekers Aanwezig "


terugMelding = tk.Label


# def meldAan(b: tkMac.Button, item: Persoon, label: tk.Label):
def meldAan(b: Button, item: Persoon, label: tk.Label):
    global aantalTechniekers
    if not item.aangemeld:
        terugMelding = (" " + item.voornaam + " is aangemeld.")
        print(item.voornaam + " is aangemeld.")
        b["bg"] = "green"
        b["text"] = "Aangemeld"
        item.aangemeld = True
        aantalTechniekers = aantalTechniekers + 1
    else:
        terugMelding = (" " + item.voornaam + " is afgemeld.")
        print(item.voornaam + " is afgemeld.")
        b["bg"] = "red"
        b["text"] = "Afgemeld"
        item.aangemeld = False
        aantalTechniekers = aantalTechniekers - 1
    setStatusBalk(label, aantalTechniekers)
    setStatus(labelterugMelding, terugMelding)
    progBar.start()
    print(progBar["value"])


bkIndienst = FALSE


def busk():
    global bkIndienst
    global lblBuskot
    print("controle")
    print(bkIndienst)
    if not bkIndienst:
        buskot["text"] = "IN"
        lblBuskot["text"] = "Buskot in dienst! "
        buskot["bg"] = "green"
        bkIndienst = True
        print("in")

    else:
        buskot["text"] = "Uit"
        lblBuskot["text"] = "Buskot uit dienst!"
        buskot["bg"] = "red"
        bkIndienst = FALSE
        print("uit")


def clearFrame():
    # destroy all widgets from frame
    for widget in middleFrame.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    middleFrame.pack_forget()


def knoppen():
    i = 0
    if fil_lijst == []:
        print(len(fil_lijst))
        clearFrame()
    else:
        for item in fil_lijst:
            # Labels voor de drukknoppen maken
            label = tk.Label(middleFrame, text=item.volledigeNaam).grid(row=i, column=0, padx=16)
            # Drukknoppen maken (pad hier geef je de grote van de knop mee weer)
            b = Button(middleFrame, text="Afgemeld", fg="black", padx=8, pady=8, bg=item.bg, width=10,
                       highlightbackground="white")
            b["command"] = lambda b=b, item=item: meldAan(b, item, labelStatus)
            b.grid(row=i, column=1)
            # Invoervakken definieren
            stringVar = tk.StringVar()
            tk.Entry(middleFrame, textvariable=stringVar, font=('Ariel', 10)).grid(row=i, column=3, padx=10, pady=10)
            t = Button(middleFrame, text="Tijd", fg="black", padx=16, pady=16, width=1, height=1,
                       highlightbackground="white")
            # t["command"] = lambda t=t, item=item: meldAan(t, item, labelStatus)
            t.grid(row=i, column=4)
            i += 1
            print(i)

        buskot.grid(row=i, column=0)
        lblBuskot.grid(row=i, column=1)


########################## Menu ############################

menuBar = tk.Menu(root)
root.config(menu=menuBar)
file = tk.Menu(menuBar, tearoff=0)
techniekers = tk.Menu(menuBar, tearoff=0)
about = tk.Menu(menuBar, tearoff=0)
cluster = tk.Menu(menuBar, tearoff=0)
SAP = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=file)
menuBar.add_cascade(label="Techniekers", menu=techniekers)
menuBar.add_cascade(label="About", menu=about)
file.add_cascade(label="SAP", menu=SAP)
file.add_cascade(label="Cluster", menu=cluster)
cluster.add_checkbutton(label="PIA/U", variable=PIAU, command=groepSelectie)
cluster.add_checkbutton(label="PIA/N", variable=PIAN, command=groepSelectie)
cluster.add_checkbutton(label="PIA/I", variable=PIAI, command=groepSelectie)
SAP.add_command(label="Overzicht IW65", command=sap.main)
SAP.add_command(label="Vergunningen D700")
SAP.add_command(label="Overzicht Meldingen")
file.add_command(label="Exit", command=functie_exit)
techniekers.add_command(label="Techniekers")
about.add_command(label="About", command=About.main)

buskot = Button(middleFrame, text="Uit", font=("Ariel", 10, "italic"), pady=20, width=10, height=1,
                bg="red", highlightbackground="white", anchor="center", command=busk)

lblBuskot = tk.Label(middleFrame, text="Buskot uit dienst!", font=("Ariel", 20, "italic"), pady=10)

############################## Label packs #####################
labelStatus.pack(side=TOP, fill=X)
labelDate.pack(anchor="e")
progBar.pack(side=RIGHT)
labelterugMelding.pack(side=LEFT, fill=X)

t1 = threading.Thread(target=startclock)
t1.start()

root.mainloop()
