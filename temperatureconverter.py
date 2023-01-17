from tkinter import *
import tkinter as tk
from tkinter.tix import*
from tkinter import ttk
from tkinter import tix
from tkinter import BOTH, END, LEFT
#assigning constants
FAHRENHEIT_RADIO =1
CELSIUS_RADIO=2
FORMULA_NINE=9
FORMULA_FIVE=5
FORMULA_THIRTY_TWO=32

#function to exit the program
def close(event=None):
    root1.quit()
#function to convert the temperature, 
def calculate():
  #if the fahrenheit radio button is checked, this will execute.
  if val_radio.get() == FAHRENHEIT_RADIO:
    #getting the users input
    get_cel = float(y.get())
    #performing calculation to convert fahrenheit to celsius 
    value=((get_cel*FORMULA_NINE)/(FORMULA_FIVE)+FORMULA_THIRTY_TWO)
    #concatenating the result
    res= str(get_cel)+ str(" degrees celsius converts to ")+ str(round(value,2))+ str(" degrees fahrenheit")
   #if the celsius radio button is checked, this will execute.
  elif val_radio.get() == CELSIUS_RADIO:
    #getting the users input
    get_far=float(y.get())
    #performing calculation to convert celcius to fahrenheit
    value=((float(get_far) - FORMULA_THIRTY_TWO) * FORMULA_FIVE / FORMULA_NINE)
     #concatenating the result
    res = str(get_far)+str(" degrees fahrenheit converts to ")+ str(round(value,2))+str( " degrees celsius")
 #storing the result
  my_text1.set(res)
  my_text2.set(res)
#function for validating user input
def validations(event=None):
  value1=y.get()
  try:
   float(value1)
  except:
    #storing error message
      res =("ERROR: Please enter a numeric temperature to convert.")
      my_text1.set(res)
      my_text2.set(res)
      return
    #calling the calculate function after validation
  calculate()
#function for clearing the form
def clear(event=None):
  #it clears the previous output from the screen
    my_text1.set("")
    my_text2.set("")
    #it clears the previous input from the text box
    y.delete(0,END)
    y.bind("<0>", clear)
    #this ensures to check the default radio button on celsius
    val_radio.set(CELSIUS_RADIO)
#assigning variables to objects
root1 = tix.Tk()
val_radio = tk.IntVar()
val_radio.set(CELSIUS_RADIO)
my_text1=tk.StringVar()
my_text2=tk.StringVar()
value1=tk.StringVar
tip=Balloon()
style = ttk.Style()
#giving title to our GUI
root1.title("Temperature Converter")
#size of the window
root1.geometry("900x500")
#background colour of 
root1.configure(bg='white')
#text label
tk.Label(root1, 
  text="Temperature Calculator", bg='white').grid(row = 0, column = 0)
#giving white background for output
style.configure("BW.TLabel", background="white")
#displaying the output
result=ttk.Label( textvariable=my_text1,style="BW.TLabel").grid(row=12,column=8)
result=ttk.Label( textvariable=my_text2,style="BW.TLabel").grid(row=12,column=8)
#creating radio buttons
r1 = tk.Radiobutton(text="Farenheit", bg='white',
      variable=val_radio, value=1).grid(row=3, column=0)
r2 = tk.Radiobutton(text="Celsius", bg='white',
      variable=val_radio, value=2).grid(row=3, column=1)
#text label
tk.Label(text=("Input"), bg='white').grid(row=1,column = 0)
#input text box
y=ttk.Entry(root1)
y.grid(row=1, column=1)
 #button to validate and convert the temperature
b = Button(root1,text="Convert",fg='white', bg='green' , command=validations)
b.grid(row=8, column=3)
#giving descriptive help text to the button
tip.bind_widget(b,balloonmsg="Calculate the output")
#reset button
Reset=tk.Button(text="Clear",fg='white', bg='orange' ,command=clear)
Reset.grid(row=8, column=4)
#giving descriptive help text to the button
tip.bind_widget(Reset,balloonmsg="Clear the screen")
#exiting button
c=tk.Button(text="Exit", fg='white', bg='red' , command=close)
c.grid(row=8, column=5)
#giving descriptive help text to the button
tip.bind_widget(c,balloonmsg="Close the program")
#creating keyboard shortcuts for the buttons
root1.bind_all("<Alt-x>", close)
root1.bind("<Alt-c>", clear)
root1.bind("<Return>",validations)
#telling python to run the tkinter event loop
root1.mainloop()
 