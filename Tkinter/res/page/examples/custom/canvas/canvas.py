#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.8.7a
# In conjunction with Tcl version 8.6
#    Jan 16, 2017 06:50:34 PM
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

import canvas_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Canvas_Example (root)
    canvas_support.init(root, top)
    root.mainloop()

w = None
def create_Canvas_Example(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Canvas_Example (w)
    canvas_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Canvas_Example():
    global w
    w.destroy()
    w = None


class Canvas_Example:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#f5deb3'  # X11 color: 'wheat'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2'

        top.geometry("600x450+650+150")
        top.title("Canvas Example")
        top.configure(background="#f5deb3")
        top.configure(highlightbackground="#f5deb3")
        top.configure(highlightcolor="black")



        self.Custom1 = canvas_support.Custom(top)
        self.Custom1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)






if __name__ == '__main__':
    vp_start_gui()


