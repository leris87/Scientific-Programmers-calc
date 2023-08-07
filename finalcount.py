import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import math
import cmath
import re
from decimal import Decimal
from calcs import Calcs
# ----------------------------------------


class ScientificCalculator(Calcs):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Calculator")

        self.result_var = tk.StringVar()
        self.mode_var = tk.StringVar(value="Rad")
        
        self.memory = None
        self.memorybase = None
        self.number_base = tk.StringVar(value="Dec")
        self.radians = tk.BooleanVar(value=True)
        
        print(self.number_base)
        self.create_widgets()

    def create_widgets(self):
        for button in self.master.grid_slaves():
            button.grid_forget()

        entry = tk.Entry(self.master, textvariable=self.result_var, justify='right', font=("Arial", 24), width=50)
        entry.grid(row=0, column=0, columnspan=5)
        mode_label = tk.Label(self.master, textvariable=self.mode_var, font=("Arial", 12))
        mode_label.grid(row=0, column=0, sticky="w")
        
        
        # ----------
        
        # ...

        
        
        
        buttons = []  
        # ------------
        print(self.number_base.get())
        if self.number_base.get()=="Dec":
            buttons = [
                ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
                ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),("AC", 2, 4),
                ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),("CE", 3, 4),
                ("0", 5, 1),
                ("/", 2, 3), ("*", 3, 3), ("-", 4, 3), ("+", 5, 3),
                ("rad/deg", 5, 0), (".", 5, 2),
                ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2),("=", 6, 3),("modulo",7,3),
                ("asin", 7, 0), ("acos", 7, 1), ("atan", 7, 2),("MS", 4, 4),
                ("sinh", 8, 0), ("cosh", 8, 1), ("sqrt", 8, 2),("X**Y", 9, 4),("MC", 5, 4),
                ("fact", 9, 0), ("log", 9, 1), ("1/x", 9, 2),("nsqrt", 9 , 3), ("MR", 6, 4),
                ("π", 10, 0), ("e", 10, 1),("+/-", 10, 2),("M+", 7, 4),("(", 8, 3), (")", 8, 4)
                
            ]
            base_button = tk.Button(self.master, textvariable=self.number_base, command=self.change_base, width=10)
            base_button.grid(row=1, column=1, sticky="w")        
        
            self.mode_var.set("Rad")
            
                
        elif self.number_base.get()=="Oct":
            buttons = [
                ("7", 2, 0), ("(", 2, 1), (")", 2, 2),
                ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),("AC", 2, 4),
                ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),("CE", 3, 4),
                ("0", 5, 1),
                ("/", 2, 3), ("*", 3, 3), ("-", 4, 3), ("+", 5, 3),("modulo",7,3),
                 (".", 5, 2),
                ("=", 6, 3),
                ("MS", 4, 4),
                ("MC", 5, 4),
                 ("1/x", 6, 2), ("MR", 6, 4),
                ("+/-", 6, 1),("M+", 7, 4)
            ]
            base_button = tk.Button(self.master, textvariable=self.number_base, command=self.change_base, width=10)
            base_button.grid(row=1, column=1, sticky="w")        
        
            self.mode_var.set("")
            
               
        elif self.number_base.get()=="Hex":
            buttons = [
               ("A",2,0),  ("CE", 3, 5),("AC", 2, 5),
                ("B",3,0),("(", 6, 1), (")", 6, 2),                ("/", 2, 4),
                ("C",4,0),("7", 2, 1), ("8", 2, 2), ("9", 2, 3), ("*", 3, 4),
                ("D", 5, 0),("4", 3, 1), ("5", 3, 2), ("6", 3, 3), ("-", 4, 4),
                ("E",6,0),("1", 4, 1), ("2", 4, 2), ("3", 4, 3), ("+", 5, 4),("modulo",5,3),
                ("F",7,0),("+/-", 7, 2),("0", 5, 1),(".", 5, 2),("=", 6, 4),
                
                 
                    
                ("MS", 4, 5),
                 ("1/x", 7, 1), ("MC", 5, 5),
                ("MR", 6, 5),("M+", 7, 5)
                
            ]
            base_button = tk.Button(self.master, textvariable=self.number_base, command=self.change_base, width=10)
            base_button.grid(row=1, column=1, sticky="w")        
        
            self.mode_var.set("")
            
        elif self.number_base.get()=="Bin":
            
            buttons = [
                ("<<", 2, 0), (">>", 2, 1), ("CE", 3, 4),("AC", 2, 4),
                ("(", 3, 0), (")", 3, 1),("/", 2, 3),
                 ("*", 3, 3),("AND", 2, 2),("OR", 3, 2),
                 ("-", 4, 3),("NOT", 4, 2),("NAND", 5, 2),("XNOR", 7, 1),
                ("1", 4, 1),("NOR", 6, 2),("XOR", 7, 2), ("+", 5, 3),
                ("+/-", 6, 0),("0", 4, 0),(".", 5, 1),("=", 6, 3),("modulo",7,3),
                ("1/x",5,0),
                 
                 ("MS",4,4),   
                ("MC", 5, 4),
                 ("MR", 6, 4),
                ("M+", 7, 4)
            ]
            base_button = tk.Button(self.master, textvariable=self.number_base, command=self.change_base, width=10)
            base_button.grid(row=1, column=1, sticky="w")        
            self.mode_var.set("")
        x=0.5
        for (text, row, col) in buttons:
            color1="white smoke"
            color2="black"
            
            if text in ("sin", "cos", "tan", "asin", "acos", "atan", "sinh", "cosh"):
                color1="grey"
                color2="white"
            elif text in ("/","*","-","+"):
                color1="honeydew"
                color2="black"   
            elif text in ("MC","M+","MR","MS"):
                color1="lightcyan3"
                color2="black" 
            elif text =="=":
                color1="orange2"
                color2="black"     
            button = tk.Button(self.master, text=text, command=lambda t=text: self.button_function(t), width=6, height=2,bg=color1, fg=color2,font=12)
            button.grid(row=row, column=col,sticky='w',padx=x)    
       
            

    def button_function(self, text):
       
        if text.isdigit() or text in "+-*/.":
            self.result_var.set(self.result_var.get() + text)
            print(text,"4")
            print(self.result_var.get())
            
        elif text == "rad/deg":
            self.radians.set(not self.radians.get())
            mode = "Rad" if self.radians.get() else "Deg"
            self.mode_var.set(mode)
        elif text in "ABCDEF":
            self.result_var.set(self.result_var.get() + text.lower())
        elif text == "(":
            
            self.result_var.set(self.result_var.get() + text)
        
        elif text == ")":
            
            self.result_var.set(self.result_var.get() + text)
        elif text == "modulo":
            text = "%"
            self.result_var.set(self.result_var.get() + text)
        elif text == "AND":
            
            
            self.result_var.set(self.result_var.get() + text)
        elif text == "OR":
            
            self.result_var.set(self.result_var.get() + text)
        elif text == "NOT":
            

                self.result_var.set(self.result_var.get() + text)
        elif text == "XOR":
            
            
            self.result_var.set(self.result_var.get() + text)    
        elif text == "XNOR":
            
            
            self.result_var.set(self.result_var.get() + text)
        elif text == "NAND":
            
            
            self.result_var.set(self.result_var.get() + text )
        elif text == "NOR":
            
            
            self.result_var.set(self.result_var.get() + text )
        elif text == "<<":
            try: 
                result = self.binaryshift(self.result_var.get(), text)
                self.result_var.set(result)                
            except Exception as e:
                        self.result_var.set("Error")
            
        elif text == ">>":
            try:
                result = self.binaryshift(self.result_var.get(), text)
                self.result_var.set(result)    
            except Exception as e:
                        self.result_var.set("Error")
            
        elif text == "AC":
            self.result_var.set("")
        elif text == "CE":
            self.result_var.set(self.result_var.get()[:-1])
        elif text == "=":
            if self.number_base.get()=="Dec":
                try:
                    
                    
                    rebuilt_expression = self.equals(self.result_var.get(), self.number_base.get())
                    if "^" in rebuilt_expression:
                        rebuilt_expression = rebuilt_expression.replace("^", "**")
                    result = eval(rebuilt_expression)
                    print(result)
                    
                    
                    if len(str(result)) > 20:
                        formatted_result = "{:.5e}".format(result)
                        self.result_var.set(formatted_result)
                        print(formatted_result)
                    else:
                        self.result_var.set(str(result))
                except Exception as e:
                    self.result_var.set("Error")
                
            elif self.number_base.get()=="Bin":
                try:
                    
                    if "AND" in self.result_var.get() or "NAND" in self.result_var.get() or "NOT" in self.result_var.get() or "XOR" in self.result_var.get() or "XNOR" in self.result_var.get() or "OR" in self.result_var.get():
                        print("222222")
                        lista = []
                    
                        
                        result = self.binarycalc((str("("+ self.result_var.get() +")")), lista)
                        print(result)
                        print(lista)
                        
                        if result[0]=="-":
                            result = "-" + str(result)[3:]
                        else:    
                            result = str(result)[2:]
                             
                            
                            

                        
                    
                    else:
                        print("peee")
                        rebuilt_expression = self.equals(self.result_var.get(), self.number_base.get())
                        
                        print(rebuilt_expression,"666")
                        
                        result = (str(self.dectoother((eval(rebuilt_expression)), self.number_base.get() )))
                        print(result)
                        if len(str(result)) > 20:
                            formatted_result = "{:.5e}".format(result)
                            result = formatted_result
                            print(formatted_result)
                       
                        print(rebuilt_expression)
                            
                        print(result)
                        
                       
                    self.result_var.set(result)
                except Exception as e:
                    self.result_var.set("Error")
                
            elif self.number_base.get()=="Hex":
                try:
                    
                    rebuilt_expression = self.equals(self.result_var.get(), self.number_base.get())
                    print(rebuilt_expression,"reb")
                    print("ok2")
                    result = (str(self.dectoother((eval(rebuilt_expression)), self.number_base.get() )))
                    print(result, "ok3")
                    
                    if len(str(result)) > 20:
                        formatted_result = "{:.5e}".format(result)
                        result = formatted_result
                        print(formatted_result)
                    
                    self.result_var.set(str(result))
                except Exception as e:
                    self.result_var.set("Error")
                
            elif self.number_base.get()=="Oct":
                try:
                    
                    rebuilt_expression = self.equals(self.result_var.get(), self.number_base.get())
                    result = (str(self.dectoother((eval(rebuilt_expression)), self.number_base.get() )))
                    if len(str(result)) > 20:
                        formatted_result = "{:.5e}".format(result)
                        result = formatted_result
                        print(formatted_result)
                    
                    self.result_var.set(str(result))
                except Exception as e:
                    self.result_var.set("Error")
                
        elif text in ("sin", "cos", "tan"):
            try:
                angle = float(self.result_var.get())
                if not self.radians.get():
                    angle = math.radians(angle)
                result = getattr(math, text)(angle)
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
                
        elif text in ("asin", "acos", "atan"):
            try:
                angle = float(self.result_var.get())
                if not self.radians.get():
                    angle = math.radians(angle)
                result = getattr(math, text)(angle)
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
                
        elif text in ("sinh", "cosh"):
            try:
                angle = float(self.result_var.get())
                if not self.radians.get():
                    angle = math.radians(angle)
                result = getattr(math, text)(angle)
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
                
        elif text =="sqrt":
            try:
                num = float(self.result_var.get())
                # if num<0:
                #     result = cmath.sqrt(num)
                # else:
                result = math.sqrt(num)    
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
                
        elif text =="1/x":
            if self.result_var.get() !="":
                
                
                if self.number_base.get()=="Dec":
                    try:
                        
                        
                        rebuilt_expression = self.equals(self.result_var.get(), self.number_base.get())
                        result = eval("1/("+ rebuilt_expression +")")
                        print(result)
                        
                        
                        if len(str(result)) > 20:
                            formatted_result = "{:.5e}".format(result)
                            self.result_var.set(formatted_result)
                            print(formatted_result)
                        else:
                            self.result_var.set(str(result))
                    except Exception as e:
                        self.result_var.set("Error")
                    
                elif self.number_base.get()=="Bin":
                    try:
                        
                        
                        
                            rebuilt_expression = self.equals(self.result_var.get(), self.number_base.get())
                            
                        
                            result = (str(self.dectoother((eval("1/("+ rebuilt_expression +")")), self.number_base.get() )))
                            print(result)
                            if len(str(result)) > 20:
                                formatted_result = "{:.5e}".format(result)
                                result = formatted_result
                                print(formatted_result)
                        
                            print(rebuilt_expression)
                                
                            print(result)
                            
                            self.result_var.set(str(result))
                    except Exception as e:
                        self.result_var.set("Error")
                    
                elif self.number_base.get()=="Hex":
                    try:
                        
                        rebuilt_expression = self.equals(self.result_var.get(), self.number_base.get())
                        print(rebuilt_expression,"reb")
                        print("ok2")
                        result = (str(self.dectoother((eval("1/("+ rebuilt_expression +")")), self.number_base.get() )))
                        print(result, "ok3")
                        
                        if len(str(result)) > 20:
                            formatted_result = "{:.5e}".format(result)
                            result = formatted_result
                            print(formatted_result)
                        
                        self.result_var.set(str(result))
                    except Exception as e:
                        self.result_var.set("Error")
                    
                elif self.number_base.get()=="Oct":
                    try:
                        
                        rebuilt_expression = self.equals(self.result_var.get(), self.number_base.get())
                        result = (str(self.dectoother((eval("1/("+ rebuilt_expression +")")), self.number_base.get() )))
                        if len(str(result)) > 20:
                            formatted_result = "{:.5e}".format(result)
                            result = formatted_result
                            print(formatted_result)
                        
                        self.result_var.set(str(result))
                    except Exception as e:
                        self.result_var.set("Error")
                    
                        
                
            else:
                messagebox.showerror("Error", "Enter a number before you press ""1/x")
        # ---------------------------------------------------
        elif text =="+/-":
            
            if self.result_var.get() !="":
                numbers = re.findall(r'[-+]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', self.result_var.get())
                print(numbers)
        
        
                modified_expression = re.sub(r'(?<![0-9a-fA-F])[-+]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', 'n', self.result_var.get())
                modified_expression = modified_expression.replace('-', '+')
                
                print(modified_expression)
                print(numbers)
                for num in numbers:
                    if num[0]=="-":
                        num = num[1:]
                    elif num[0]=="+":
                        num = num[1:]
                        num = "-" + num
                    else:
                        num = "-" + num
                    modified_expression = re.sub(r'n', num, modified_expression, count=1)
                pattern = r"\+-"
                has_plus_minus = re.search(pattern, modified_expression) is not None
                if has_plus_minus:
                    modified_expression = modified_expression.replace("+-", "-")
                self.result_var.set(str(modified_expression))
            else:
                messagebox.showerror("Error", "Enter a number before you press ""+/-")
        elif text == "nsqrt":
            try:
                num = float(self.result_var.get())
                try:
                    n = float(simpledialog.askinteger("Input", "Enter the Νth root v=", parent=self.master))
                
                    
                    result = num**(1/n)
                    if "j" in str(result):
                        result = "Error"  
                    self.result_var.set(str(result))
                except Exception as e:
                    self.result_var.set("Error")
                    
            except Exception as e:
                self.result_var.set("Error")
                
        elif text == "fact":
            try:
                n = int(self.result_var.get())
                result = math.factorial(n)
                if len(str(result)) > 20:
                    formatted_result = "{:.5e}".format(result)
                    self.result_var.set(formatted_result)
                else:
                    self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
                
        elif text == "rad/deg":
            self.radians.set(not self.radians.get())
            mode = "Rad" if self.radians.get() else "Deg"
            self.mode_var.set(mode)
        elif text == "MS":
            try:
                self.memory = self.result_var.get()
                self.memorybase = self.number_base.get()
                self.result_var.set("")
            except Exception as e:
                messagebox.showerror("Error", "Wrong input to the memory")
        elif text == "M+":
            print(self.memory,"mem")
            if self.memory is not None:
                if self.memorybase =="Dec" and self.number_base.get()=="Dec":
                    self.memory += float(self.result_var.get())
                elif self.memorybase =="Dec" and self.number_base.get()!="Dec":
                    self.memory += float(self.othertodec(self.result_var.get(), self.number_base.get()))
                elif self.memorybase !="Dec" and self.number_base.get()=="Dec":
                    self.memory = self.dectoother((float(self.othertodec(str(self.memory), self.memorybase)) + float(self.result_var.get())), self.memorybase)
                elif self.memorybase !="Dec" and self.number_base.get()!="Dec":
                    self.memory = self.dectoother((float(self.othertodec(str(self.memory), self.memorybase)) + float(self.othertodec(self.result_var.get(), self.number_base.get()))), self.memorybase)
                self.result_var.set("")
            else:
                messagebox.showerror("Error", "Memory is empty")
        elif text == "MR":
            if self.memory is not None:
                if self.memorybase =="Dec" and self.number_base.get()=="Dec":
                    self.result_var.set(str(self.memory))
                elif self.memorybase =="Dec" and self.number_base.get()!="Dec":
                    self.result_var.set((self.dectoother(str(self.memory), self.number_base.get())))
                elif self.memorybase !="Dec" and self.number_base.get()=="Dec":
                    self.result_var.set((self.othertodec(str(self.memory), self.memorybase)))
                elif self.memorybase !="Dec" and self.number_base.get()!="Dec":
                    self.result_var.set((self.dectoother((self.othertodec(str(self.memory), self.memorybase)), self.number_base.get())))
            else:
                messagebox.showerror("Error", "Memory is empty")
        elif text == "MC":
            if self.memory is not None:
                self.memory=None
                self.result_var.set("")
            else:
                messagebox.showerror("Error", "Memory is empty")
        elif text in ("π", "e"):
            
            if text=="π":
                text=str(getattr(math, "pi"))
            else:
                text=str(getattr(math, text))
            
            current_result = self.result_var.get()
            # if current_result.endswith("+") or current_result == "":
            self.result_var.set(current_result + text)
            # else:
            #     self.result_var.set(current_result + "+" + text)
        elif text == "X**Y":
            if self.result_var.get() !="":
                result = self.result_var.get() + "^"
                self.result_var.set(str(result))
            else:
                messagebox.showerror("Error", "Enter a number(base) before you press ""X**Y")
        elif text in ("log"):
            try:
                num = float(self.result_var.get())
                if num<0:
                    if str(num*-1).isdigit():
                        base = (int(-10))
                        result = math.log(abs(num)) / math.log(abs(base)) + 1j * math.pi / math.log(abs(base))
                    else:
                        base = simpledialog.askinteger("Enter", "Enter the base:", parent=self.master)
                        if base is not None:
                            
                            result = math.log(abs(num)) / math.log(abs(base)) + 1j * math.pi / math.log(abs(base))
                            self.result_var.set(str(result))
                        else:
                            
                            pass

                else:
                    if str(num).isdigit():
                        base = (int(10))
                        result = math.log(num, base)
                    else:
                        result = math.log(num)    
                    
                self.result_var.set(str(result))
            except Exception as e:
                self.result_var.set("Error")
    def change_base(self):
        current_base = self.number_base.get()
        new_base = ""
        if current_base == "Bin":
            new_base = "Dec"
            if self.result_var.get()!="":
                
                    
                    rebuilt_expression = self.convert_expression(self.result_var.get(), "Bin", "Dec")
                    self.result_var.set(rebuilt_expression)
        elif current_base == "Dec":
            new_base = "Hex"
            if self.result_var.get()!="":
                
                    
                    rebuilt_expression = self.convert_expression(self.result_var.get(), "Dec", "Hex")
                    self.result_var.set(rebuilt_expression)
                
        elif current_base == "Hex":
            new_base = "Oct"
            if self.result_var.get()!="":
                
                    rebuilt_expression = self.convert_expression(self.result_var.get(), "Hex", "Oct")
                    self.result_var.set(rebuilt_expression)
                

        elif current_base == "Oct":
            new_base = "Bin"
            if self.result_var.get()!="":    
                  
                    rebuilt_expression = self.convert_expression(self.result_var.get(), "Oct", "Bin")
                    self.result_var.set(rebuilt_expression)
                
        self.number_base.set(new_base)
        self.create_widgets()
if __name__ == "__main__":
    root = tk.Tk()
    calculator = ScientificCalculator(root)
    root.mainloop()