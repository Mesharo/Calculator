import tkinter as tk
from tkinter import font
import math


class Window:
    def __init__(self, root : tk.Tk):

        root.title("Calculator by Mesharo")
        root.geometry('400x400')

        self.numberLeft = ""
        self.operator = ""
        self.numberRight = ""

        self.numbers, self.mathSymbols, self.controlFunctions = self.defineElements()
        self.displayElements()

        self.rowConfiguration()
        self.columnConfiguration()

        self.setNumbers()
        self.setMathSymbols()
        self.setFunctions()


    def defineElements(self):
        self.display = tk.Label(root, text="", bg="#FFFFFF", anchor="e", font=("Arial", 20))

        self.buttonEraseNumber  = tk.Button(root, text='←', bg="gray", width=2)  
        self.buttonEraseLast    = tk.Button(root, text='CE', bg="gray", width=2)    
        self.buttonEraseAll     = tk.Button(root, text='C', bg="gray", width=2) 
        self.buttonEquals       = tk.Button(root, text='=', bg="gray", width=2)

        self.buttonFloat        = tk.Button(root, text='.', bg="gray", width=2) 
        self.button0            = tk.Button(root, text='0', bg="azure3", width=2) 
        self.button1            = tk.Button(root, text='1', bg="azure3", width=2) 
        self.button2            = tk.Button(root, text='2', bg="azure3", width=2) 
        self.button3            = tk.Button(root, text='3', bg="azure3", width=2) 
        self.button4            = tk.Button(root, text='4', bg="azure3", width=2) 
        self.button5            = tk.Button(root, text='5', bg="azure3", width=2) 
        self.button6            = tk.Button(root, text='6', bg="azure3", width=2) 
        self.button7            = tk.Button(root, text='7', bg="azure3", width=2) 
        self.button8            = tk.Button(root, text='8', bg="azure3", width=2) 
        self.button9            = tk.Button(root, text='9', bg="azure3", width=2) 

        self.buttonDivide       = tk.Button(root, text='/', bg="gray", width=2) 
        self.buttonModulo       = tk.Button(root, text='%', bg="gray", width=2) 
        self.buttonMultiply     = tk.Button(root, text='*', bg="gray", width=2) 
        self.buttonPower        = tk.Button(root, text='^', bg="gray", width=2) 
        self.buttonSubtract     = tk.Button(root, text='-', bg="gray", width=2) 
        self.buttonAdd          = tk.Button(root, text='+', bg="gray", width=2) 
        self.buttonPlusMinus    = tk.Button(root, text='±', bg="gray", width=2)    
        self.buttonSquareRoot   = tk.Button(root, text='√', bg="gray", width=2)   

        return  [self.buttonFloat, self.button0, self.button1, self.button2, self.button3, self.button4, self.button5, self.button6, self.button7, self.button8, self.button9], [self.buttonDivide, self.buttonModulo, self.buttonMultiply, self.buttonPower, self.buttonSubtract, self.buttonAdd, self.buttonPlusMinus, self.buttonSquareRoot], [self.buttonEraseNumber, self.buttonEraseLast, self.buttonEraseAll, self.buttonEquals]


    def displayElements(self):
        self.display.grid(row=0, column=0, columnspan=5, sticky="nswe", padx=2, pady=2)

        self.buttonEraseNumber.grid(row=1, column=0, sticky="nswe", padx=2, pady=2)  
        self.buttonEraseLast.grid(row=1, column=1, sticky="nswe", padx=2, pady=2)            
        self.buttonEraseAll.grid(row=1, column=2, sticky="nswe", padx=2, pady=2)      
        self.buttonPlusMinus.grid(row=1, column=3, sticky="nswe", padx=2, pady=2)        
        self.buttonSquareRoot.grid(row=1, column=4, sticky="nswe", padx=2, pady=2)         
        
        self.button7.grid(row=2, column=0, sticky="nswe", padx=2, pady=2)               
        self.button8.grid(row=2, column=1, sticky="nswe", padx=2, pady=2)               
        self.button9.grid(row=2, column=2, sticky="nswe", padx=2, pady=2)               
        self.buttonDivide.grid(row=2, column=3, sticky="nswe", padx=2, pady=2)          
        self.buttonPower.grid(row=2, column=4, sticky="nswe", padx=2, pady=2)          

        self.button4.grid(row=3, column=0, sticky="nswe", padx=2, pady=2)               
        self.button5.grid(row=3, column=1, sticky="nswe", padx=2, pady=2)               
        self.button6.grid(row=3, column=2, sticky="nswe", padx=2, pady=2)               
        self.buttonMultiply.grid(row=3, column=3, sticky="nswe", padx=2, pady=2)    
        self.buttonModulo.grid(row=3, column=4, sticky="nswe", padx=2, pady=2)      
     
        self.button1.grid(row=4, column=0, sticky="nswe", padx=2, pady=2)               
        self.button2.grid(row=4, column=1, sticky="nswe", padx=2, pady=2)               
        self.button3.grid(row=4, column=2, sticky="nswe", padx=2, pady=2)               
        self.buttonSubtract.grid(row=4, column=3, sticky="nswe", padx=2, pady=2)   
        self.buttonEquals.grid(row=4, column=4, sticky="nswe", rowspan=2, padx=2, pady=2)      

        self.button0.grid(row=5, column=0, sticky="nswe", columnspan=2, padx=2, pady=2)             
        self.buttonFloat.grid(row=5, column=2, sticky="nswe", padx=2, pady=2)          
        self.buttonAdd.grid(row=5, column=3, sticky="nswe", padx=2, pady=2)    


    def setNumbers(self):
        def myLambda(x):
            if (isinstance(x, tk.Button)):
                return lambda _ : self.numberPressed(x.cget("text"))
            raise ValueError
        
        for x in self.numbers:
            x.bind("<Button-1>", myLambda(x))


    def setMathSymbols(self):
        def myLambda(x):
            if (isinstance(x, tk.Button)):
                return lambda _ : self.mathSymbolPressed(x.cget("text"))
            raise ValueError
        
        for x in self.mathSymbols:
            x.bind("<Button-1>", myLambda(x))


    def setFunctions(self):
        def myLambda(x):
            if (isinstance(x, tk.Button)):
                return lambda _ : self.functionPressed(x.cget("text"))
            raise ValueError
        
        for x in self.controlFunctions:
            x.bind("<Button-1>", myLambda(x))

            
    def rowConfiguration(self):
        for current in range(6):
            root.rowconfigure(current, weight=1)

    
    def columnConfiguration(self):
        for current in range(5):
            root.columnconfigure(current, weight=1)


    def numberPressed(self, number):
        if (self.operator == ""):
            if ((number != ".") or ((number not in self.numberLeft) and (self.numberLeft != ""))):
                self.numberLeft += number
        else:
            if ((number != ".") or ((number not in self.numberRight) and (self.numberRight != ""))):
                self.numberRight += number

        self.display.config(text=(self.numberLeft + self.operator + self.numberRight))

    
    def negation(self):
        if (self.operator == ""):
            if (self.numberLeft == ""):
                return
            if (self.numberLeft[0] == "-"):
                self.numberLeft = self.numberLeft[1::]
            else:
                self.numberLeft = "-" + self.numberLeft
        else:
            if (self.numberRight == ""):
                return
            if (self.numberRight[0] == "-"):
                self.numberRight = self.numberRight[1::]
            else:
                self.numberRight = "-" + self.numberRight   


    def mathSymbolPressed(self, mathSymbol):
        basic = ["+", "-", "*", "/", "^", "%"]

        if ((mathSymbol in basic[0:2]) and (self.operator == "")):
            self.operator = mathSymbol
        elif ((mathSymbol in basic) and (self.operator == "")):
            if (self.numberLeft != ""):
                self.operator = mathSymbol
        else:
            if (mathSymbol == "±"):
                self.negation()
            
            if (mathSymbol == "√"):
                if ((self.operator == "") and (self.numberLeft == "")):
                    self.operator = "√"


        self.display.config(text=(self.numberLeft + self.operator + self.numberRight))


    def eraseNumber(self):
        if (self.operator == ""):
            self.numberLeft = ""
        else:
            if (self.numberRight == ""):
                self.operator = ""
            else:
                self.numberRight = ""


    def eraseLast(self):
        if (self.operator == ""):
            if (self.numberLeft != ""):
                self.numberLeft = self.numberLeft[:len(self.numberLeft) - 1]
        else:
            if (self.numberRight != ""):
                self.numberRight = self.numberRight[:len(self.numberRight) - 1]
            else:
                self.operator = ""    


    def compute(self):
        result = self.numberLeft + self.operator + self.numberRight
        if (self.operator == "√"):
            result = "math.sqrt(" + self.numberRight + ")"
        if (self.operator == "^"):
            result = self.numberLeft + "**" + self.numberRight

        self.display.config(text=(eval(result)))
        self.operator = self.numberLeft = self.numberRight = ""        


    def functionPressed(self, function):
        if (function == "←"):
            self.eraseNumber()
        
        if (function == "CE"):
            self.eraseLast()
        
        if (function == "C"):
            self.operator = self.numberLeft = self.numberRight = ""

        if (function == "="):
            self.compute()
            return

        self.display.config(text=(self.numberLeft + self.operator + self.numberRight))


if __name__ == "__main__":
    root = tk.Tk()
    window = Window(root)
    root.mainloop()