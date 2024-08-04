from tkinter import mainloop, ttk
import tkinter
import time
import pyautogui
import sv_ttk as sv
from PIL import ImageTk, Image
import win32mica
from win32mica import MicaTheme
from concurrent.futures import ThreadPoolExecutor, Future
import threading

executor = ThreadPoolExecutor()
future: Future | None = None
cancel = threading.Event()


def help():
    root2 = tkinter.Toplevel(root)
    root2.resizable(False, False)
    root2.title('Help')
    root2.geometry('300x305')
    root2.focus_set()
    ttk.Label(root2,
              text='1. How do I use this?',
              font=('Segoe UI Variable Display Semibold', 15),
              background="#000000").place(x=2, y=2)

    t1 = """Click on 'Yes' to unleash the bee movie 
script on unsuspecting victims 
after 5 seconds, and 'Noo' to exit."""
    ttk.Label(root2,
              text=t1,
              font=('Segoe UI Variable Display', 10),
              background="#000000").place(x=2, y=40)

    ttk.Label(root2,
              text='2. Who made this? Why?',
              font=('Segoe UI Variable Display Semibold', 15),
              background="#000000").place(x=2, y=135)

    t2 = """This was made for the sole purpose
of annoying others, and to ruin their day.
Thank you for asking."""
    ttk.Label(root2,
              text=t2,
              font=('Segoe UI Variable Display', 10),
              background="#000000").place(x=2, y=175)

    ttk.Label(root2,
              text='This abomination is made by SlavBoii420',
              background="#000000").place(x=25, y=275)

    root2.configure(bg='#000000')
    root2.wm_attributes("-transparent", "#000000")
    root2.update()

    HWND = root2.frame()
    win32mica.ApplyMica(HWND, Theme=MicaTheme.DARK)


def yesInput():

    def payloadFunc():
        if cancel.is_set():
            cancel.clear()

        payload = open('Beemovie.txt')
        time.sleep(5)

        for word in payload:
            if cancel.is_set():
                break
            pyautogui.typewrite(word)
            pyautogui.press("enter")

    def printDone(_: Future):
        print("Done")

    global future
    if future:
        future.cancel()
    future = executor.submit(payloadFunc)
    future.add_done_callback(printDone)


def noInput():
    global future
    if future:
        cancel.set()
        future.cancel()
    root.destroy()


root = tkinter.Tk()
root.title('Bee Movie Spewer v1.0')
root.resizable(False, False)
root.geometry('380x200')

photo = ImageTk.PhotoImage(Image.open('smol bee.png'))
root.iconphoto(True, photo)

mainText = """Do you really want to spew 
the Bee Movie Script after
the next five seconds?"""
ttk.Label(root,
          text=mainText,
          font=('Segoe UI Variable Display Semibold', 17),
          background="#000000").place(x=10, y=5)

yes = ttk.Button(root, text='YES', command=yesInput)
yes.place(x=100, y=140, height=45, width=70)

no = ttk.Button(root, text='NOO', style='Accent.TButton', command=noInput)
no.place(x=200, y=140, height=45, width=70)

help = ttk.Button(root, text='', command=help)
help.place(x=334, y=160)

root.configure(bg='#000000')
root.wm_attributes("-transparent", "#000000")
root.update()
HWND = root.frame()
win32mica.ApplyMica(HWND, Theme=MicaTheme.DARK)

sv.use_dark_theme()
mainloop()
