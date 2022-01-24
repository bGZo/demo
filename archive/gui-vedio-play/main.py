import re # judge the url whether a legal or not
import tkinter as tk # make software
from urllib import parse # url alaylase lib
import tkinter.messagebox as msgbox
import webbrowser # control browser

class App:
    # rewrite construction function
    def __init__(self, width=500, height=200):
        # softeare name, size and property must write here
        self.w = width
        self.h = height
        self.title = 'demo video helper'
        self.root = tk.Tk(className=self.title)
        self.url = tk.StringVar()
        self.v = tk.IntVar()
        self.v.set(1)

        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        group = tk.Label(frame_1, text='play way', padx=10, pady=10)
        tb=tk.Radiobutton(frame_1, text='only one way', variable=self.v, value=1, width=10, height=3)

        label = tk.Label(frame_2, text='input address:')
        entry=tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        play=tk.Button(frame_2, text='play', fg='Purple', width=2, height=1, command=self.video_play)

        # display
        frame_1.pack()
        frame_2.pack()

        group.grid(row=0, column=0)
        tb.grid(row=0, column=0)

        label.grid(row=0, column=0)
        entry.grid(row=0,column=1)
        play.grid(row=0, column=2, ipadx=10, ipady=10)

    def video_play(self):
        port='http://www.wmxz.wang/video.php?url='
        if re.match(r'https?:/{2}\w.+$', self.url.get()):
            ip = self.url.get()
            ip = parse.quote_plus(ip)
            webbrowser.open(port + ip)
        else:
            msgbox.showerror(title='error', message='video address error')
        

    def loop(self):
        self.root.mainloop()


if __name__=='__main__':
    app=App()
    app.loop()
