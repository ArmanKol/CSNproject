import tkinter


def verander_led_groen():
    global groene_led
    groene_led["background"] = "green"


def verander_led_geel():
    global gele_led
    gele_led["background"] = "yellow"


def verander_led_rood():
    global rode_led
    rode_led["background"] = "red"


def toonhoofdmenu():
    hoofdmenuframe.pack()


root = tkinter.Tk()
root.title("Alarm systeem")
root.configure(background="white")

hoofdmenuframe = tkinter.Frame(root)
hoofdmenuframe.configure(background="white")
hoofdmenuframe.pack()

aanuitlabel = tkinter.Label(master=hoofdmenuframe, text="Alarm", background="white")
aanuitlabel.grid(row=0, column=0)

aanknop = tkinter.Button(master=hoofdmenuframe, text="AAN")
aanknop.grid(row=1, column=0)

uitknop = tkinter.Button(master=hoofdmenuframe, text="UIT")
uitknop.grid(row=1, column=1)

rode_led = tkinter.Label(master=hoofdmenuframe, background="red4", height=1, width=2)
rode_led.grid(row=2, column=0)

gele_led = tkinter.Label(master=hoofdmenuframe, background="yellow4", height=1, width=2)
gele_led.grid(row=2, column=1)

groene_led = tkinter.Label(master=hoofdmenuframe, background="green4", height=1, width=2)
groene_led.grid(row=2, column=2)

toonhoofdmenu()
root.mainloop()
