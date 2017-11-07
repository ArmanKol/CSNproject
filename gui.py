import tkinter

def verander_led_groen():
    global groene_led
    global rode_led
    global gele_led
    global counter

    if counter == 0:
        groene_led["background"] ="green2"
        rode_led["background"] ="red4"
        gele_led["background"] ="yellow4"
        counter += 1


def verander_led_geel():
    global gele_led
    global rode_led
    global groene_led
    global counter

    gele_led["background"] = "yellow"
    rode_led["background"] = "red4"
    groene_led["background"] = "green4"

    counter +=1
    root.after(2000, verander_led_rood)


def verander_led_rood():
    global rode_led
    global groene_led
    global gele_led
    global counter

    if counter == 1:
        rode_led["background"] ="red"
        groene_led["background"] ="green4"
        gele_led["background"] ="yellow4"
        counter -= 1


def toonhoofdmenu():
    hoofdmenuframe.pack()


root = tkinter.Tk()
root.title("Alarm systeem")
root.configure(background="white")

counter =0

hoofdmenuframe = tkinter.Frame(root)
hoofdmenuframe.configure(background="white")
hoofdmenuframe.pack()

aanuitlabel = tkinter.Label(master=hoofdmenuframe, text="Alarm", background="white")
aanuitlabel.grid(row=0, column=0)

aanknop = tkinter.Button(master=hoofdmenuframe, text="AAN", command=verander_led_groen)
aanknop.grid(row=1, column=0)

uitknop = tkinter.Button(master=hoofdmenuframe, text="UIT", command=verander_led_rood)
uitknop.grid(row=1, column=1, padx=10)

stopknop = tkinter.Button(master=hoofdmenuframe, text="STOP")
stopknop.grid(row=1, column=2, padx=10)

alarmknop = tkinter.Button(master=hoofdmenuframe, text="ALARM TESTEN", command=verander_led_geel)
alarmknop.grid(row=1, column=3)

rode_led = tkinter.Label(master=hoofdmenuframe, background="red4", width=2)
rode_led.grid(row=2, column=0)

gele_led = tkinter.Label(master=hoofdmenuframe, background="yellow4", width=2)
gele_led.grid(row=2, column=1)

groene_led = tkinter.Label(master=hoofdmenuframe, background="green4", width=2)
groene_led.grid(row=2, column=2, padx=8, pady=10)

toonhoofdmenu()
root.mainloop()
