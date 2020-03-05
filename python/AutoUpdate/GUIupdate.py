import tkinter as t
import os
from tkinter import *
from tkinter import ttk
from time import sleep

from AutoUpdate import AutoUpdate

#imports Para a thread
from os import system
from time import sleep
from threading import Thread
from threading import Event
import sys
import time
import math

class ThreadAutoUpdate(Thread):

    def __init__ (self, objAutoUpdate):
        Thread.__init__(self)  
        self._stop = Event()        
        self.update = objAutoUpdate
        self.Quit = None
        self.AutoUpdateStart = False        
        print("THREAD T1 INICIADA")
        

    # function using _stop function 
    def stop(self): 
        self._stop.set() 
  
    def stopped(self): 
        return self._stop.isSet() 

    def run(self):   

        while True: 
            if self.stopped(): 
                return

            if not self.AutoUpdateStart:
                self.update.Mostrar_Versoes()                
                self.AutoUpdateStart = True
                self.stop()

                
class GUI:
    Font = [("Rockwell", "16"),
            ("Rockwell", "14")]
    l = []
    
    u = AutoUpdate()
    t1 = ThreadAutoUpdate(u)    
    t1.start()
    
    
    def __init__(self, master):        
        self.Size_File = 0
        self.vProgressBar = t.IntVar()  
        self.Valor = 0
        self.Desatualizado = False
        master["bg"] = "#ffd800"
        self.Frame = Frame(master)           
        self.Frame.pack(fill=X, expand=1)
        self.lb = Label(self.Frame, text="Verificando Update...", font=self.Font[0])
        self.lb.pack(side=TOP)
        #
        self.ProgressBar = ttk.Progressbar(self.Frame, variable = self.vProgressBar, maximum=100)        
        self.lb_info = Label(self.Frame, text="0%", font=self.Font[0])        
        self.scrollBar = Scrollbar(self.Frame, relief=FLAT, width=5) 
        self.text = Text(self.Frame, width=30, height=20, insertborderwidth=4, padx=2, pady=2, font=self.Font[1],
                            background="#c9af28", foreground="#fff" , yscrollcommand=self.scrollBar.set)
               
        self.l = [   self.Frame,
                        self.lb,
                     self.lb_info                     
                 ]
        self._ChangeBgColor(self.l)
        self._SizeFile()

    def _ChangeBgColor(self, l):
        for a in l:
            a["bg"] = "#ffd800"

    
    def _SizeFile(self):	
        
        try:
            v = (self.u.size_dl / self.u.block_size) // 1000
            self.Valor = int(((self.u.arq_dl / self.u.block_size)/v)*100)
        except ZeroDivisionError:
            self.Valor = 0
      
        self.vProgressBar.set( self.Valor )        
        self.ProgressBar.update()        
        self.lb_info['text'] = str( self.vProgressBar.get() )+" %"
        if not self.Desatualizado and v > 0:
            self._Visible()
            self.Desatualizado = True
        
        if self.u._quit != None:
            print("Download Complete")
            self._Exit()
            self.u._quit = None
        self.lb["text"] = self.u.Info
        tk.after(100, self._SizeFile)
        
    def _Visible(self):
        self.Frame.pack(fill=BOTH, expand=1)
        self.ProgressBar.pack(side=TOP)
        self.lb_info.pack(side=TOP)                
        self.text.insert(t.END, self.u.Mostrar_Mudancas())
        self.text.config(state=DISABLED)
        self.scrollBar.pack(side=RIGHT, fill=Y)
        self.text.pack(side=TOP, fill=BOTH, expand=1)
        self.scrollBar.config(command=self.text.yview)       

    def _Exit(self):
        tk.after(200, tk.quit)

tk = Tk()

w = tk.winfo_screenwidth()//2
h = tk.winfo_screenheight()//2
tk.wm_attributes("-topmost", 1)
tk.geometry("250x350+"+str(w)+"+"+str(h))
tk.iconbitmap('logo.ico')
tk.title("Update - v1")
#tk.overrideredirect(1)
GUI(tk)
tk.mainloop()
