import re
from decimal import Decimal
import math
class Calcs:
    def binaryshift(self, string, text):
        while string[0] =="(":
            string = string.replace("(","")

        if "<<" in text:
            
            number = string.replace("<<", "")
            while number[0]=="0":
                number = number[1:]
            mainnum = int(number, 2) 
            print(number)
            result = bin(mainnum << 1)
            print(result)
        elif ">>" in text:
            number = string.replace(">>", "")
            while number[0]=="0":
                number = number[1:]
            mainnum = int(number, 2) 
            print(number, "shin")
            result = bin(mainnum >> 1)
            print(result)
        if result[0]=="-":
                            result = "-" + str(result)[3:]
        else:    
                            result = str(result)[2:]
        return result
    def binarycalc(self, string, replacements):
       
        match = re.search(r'\(([^()]+)\)', string)
        
        if match:
            
            inner_expression = match.group(1)
            print(inner_expression,"m2")
            modified_expression = string.replace('(' + inner_expression + ')', 'n')
            print(modified_expression)
            if "NAND" in inner_expression:
                            print("11111")
                            numbers = re.split(r'[NAND]', inner_expression)
                            inner_expression =  inner_expression.replace("NAND", "&")
                            new_expression = re.sub(r'[-+]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', 'n', inner_expression)
                            
                            numbers = [num for num in numbers if num and not num.isspace()] #ΑΦΑΙΡΕΙ ΤΑ ΚΕΝΑ ΠΟΥ ΕΧΕΙ ΒΑΛΕΙ ΠΙΘΑΝΟΝ ΤΟ re.split ΣΤΗ ΛΙΣΤΑ NUMBERS
                            print(numbers)
                            
                            for num in numbers:
                                # num = str(bin(int(num, 2)))
                                new_expression = re.sub(r'n', num, new_expression, count=1)
                            print(new_expression,"33")
                            new_expression = "~("+ new_expression +")&0b1"
                            print(new_expression,"33")
                            result = (str(bin(eval(new_expression))))
                            
                            
                            modified_expression = modified_expression.replace('n', str(result))
                            
                            print(result, "con")
            elif "XOR" in inner_expression:
                            
                            numbers = re.split(r'[XOR]', inner_expression)
                            inner_expression =  inner_expression.replace("XOR", "^")
                            new_expression = re.sub(r'[-+]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', 'n', inner_expression)
                            
                            print(new_expression)
                            numbers = [num for num in numbers if num and not num.isspace()]
                            print(numbers)
                            
                            for num in numbers:
                                
                                new_expression = re.sub(r'n', num, new_expression, count=1)
                            print(new_expression)
                            new_expression = new_expression +"&0b1"
                            result = (str(bin(eval(new_expression))))
                            modified_expression = modified_expression.replace('n', str(result))
                            print(result, "con")
            elif "XNOR" in inner_expression:
                            
                            numbers = re.split(r'[XNOR]', inner_expression)
                            inner_expression =  inner_expression.replace("XNOR", "^")
                            new_expression = re.sub(r'[-+]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', 'n', inner_expression)
                            
                            numbers = [num for num in numbers if num and not num.isspace()]
                            print(numbers)
                            
                            for num in numbers:
                                
                                new_expression = re.sub(r'n', num, new_expression, count=1)
                            print(new_expression,"33")
                            new_expression = "~("+ new_expression +")&0b1"
                            print(modified_expression,"33")
                            result = (str(bin(eval(new_expression))))
                            modified_expression = modified_expression.replace('n', str(result))
                            print(result, "con")
            elif "NOR" in inner_expression:
                            
                            numbers = re.split(r'[NOR]', inner_expression)
                            inner_expression =  inner_expression.replace("NOR", "|")
                            new_expression = re.sub(r'[-+]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', 'n', inner_expression)
                            
                            numbers = [num for num in numbers if num and not num.isspace()]
                            print(numbers)
                            
                            print(new_expression, "first")
                            for num in numbers:
                                
                                new_expression = re.sub(r'n', num, new_expression, count=1)
                            print(new_expression,"33")
                            new_expression = "~("+ new_expression +")&0b1"
                            print(new_expression,"33")
                            result = (str(bin(eval(new_expression))))
                            modified_expression = modified_expression.replace('n', str(result))
                            print(result, "con")
                            print(modified_expression)
            elif "AND" in inner_expression:
                            print("!!!!!")
                            numbers = re.split(r'[AND]', inner_expression)
                            print(inner_expression,"pes")
                            inner_expression =  inner_expression.replace("AND", "&")
                            new_expression = re.sub(r'[-+]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', 'n', inner_expression)
                            
                            numbers = [num for num in numbers if num and not num.isspace()]
                            print(numbers)
                            
                            print(new_expression, "first")
                            for num in numbers:
                                
                                new_expression = re.sub(r'n', num, new_expression, count=1)
                            print(new_expression,"33")
                            
                            print(new_expression,"33")
                            result = (str(bin(eval(new_expression))))
                            print(result,"666")
                            
                            modified_expression = modified_expression.replace('n', str(result))
            elif "OR" in inner_expression:
                            
                            numbers = re.split(r'[OR]', inner_expression)
                            inner_expression =  inner_expression.replace("OR", "|")
                            new_expression = re.sub(r'[-+]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', 'n', inner_expression)
                            
                            numbers = [num for num in numbers if num and not num.isspace()]
                            print(numbers)
                            
                            print(new_expression, "first")
                            for num in numbers:
                                
                                new_expression = re.sub(r'n', num, new_expression, count=1)
                            print(new_expression,"33")
                            
                            print(new_expression,"33")
                            result = (str(bin(eval(new_expression))))
                            
                            modified_expression = modified_expression.replace('n', result)
                            print(result, "con")
                            print(modified_expression)
                        
                            result = (str(bin(eval(inner_expression))))
                            
                            print(result,"666")
                            print(result,"666")
                            
                            modified_expression = modified_expression.replace('n', str(result))
            elif "NOT" in inner_expression:
                            
                            numbers = re.split(r'[NOT]', inner_expression)
                            inner_expression =  inner_expression.replace("NOT", "~")
                            new_expression = re.sub(r'[-+]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', 'n', inner_expression)
                            
                            numbers = [num for num in numbers if num and not num.isspace()]
                            print(numbers)
                            new_expression = "~(n)&0b1"
                            print(new_expression, "first")
                            for num in numbers:
                                
                                new_expression = re.sub(r'n', num, new_expression, count=1)
                            print(new_expression,"33")
                            
                            print(new_expression,"33")
                            result = (str(bin(eval(new_expression))))
                            
                            modified_expression = modified_expression.replace('n', result)
                            print(result, "con")
                            print(modified_expression)
                        
                            
                            print(result,"666")
                            
                            modified_expression = modified_expression.replace('n', str(result))
            else:
                print(string,"00")
                while "(" in string[0]:
                    print(string,"1")
                    string = string.replace("(", "")
                while ")" in string[-1]:
                    string = string.replace(")", "")
                    print(string,"2")
                return string
            replacements.append(result)
            
            
            
            return self.binarycalc(modified_expression, replacements)
        else:
            
            
            return string
    def dectoother(self, num, base):
        try:
            if base == "Hex":
                basenum = int(16)
            elif base == "Oct":
                basenum = int(8)
            elif base == "Bin":
                basenum = int(2)
            print(num, "num")
            #  βγάζει το ακέραιο μέρος
            # Split το string στο κόμα
            if "." in str(num):
                integer_part, decimal_part = str(num).split('.')
                print(integer_part,"int")
                print(decimal_part,"dec")
                        # αφαιρεί τα μηδενικά στο ακέραιο μέρος αν βρίσκονται πριν τον αριθμό
                integer_part = str(int(integer_part))
                # if int(integer_part) != 0:
                #     integer_part = integer_part.lstrip('0')
                
                        # αφαιρεί τα μηδενικά στο δεκαδικό μέρος που βρίσκονται μετά τον αριθμό
                print(integer_part,"ppp")
                decimal_part = decimal_part.rstrip('0')
            else:
                integer_part = str(int(num))
                decimal_part = str(0)
            
            print(integer_part,"int")
            print(decimal_part,"dec")
                
            # if integer_part != "0":
            #     integer_part = integer_part.lstrip('0')

                
            # decimal_part = decimal_part.rstrip('0')
            print(decimal_part, "deccc")
            if integer_part == "0" and decimal_part =="0":
                print("swse")
                new_num = "0"
                
                return new_num
            else:
                minus = False
                # αν υπάρχει το - ή το + πριν το ακέραιο μέρος (αρνητικός αριθμός) το αφαιρεί για να κάνει τις πράξεις μόνο με αριθμό
                
                if integer_part[0]=="-":
                    integer_part= (abs(int(integer_part)))
                    # αν ο αριθμός είναι αρνητικός ενεργοποιεί το minus για να προσθέσει στο τέλος το "-"
                    minus = True
                elif integer_part[0]=="+":
                        integer_part=integer_part[1:]
                integer_part = int(integer_part)
                # αν στο δεκαδικό μέρος τα πρώτα πέντε ψηφία είναι 0 στρογγυλοποιεί το δεκαδικό μέρος σε 0
                if decimal_part[:5] == "00000":
                    decimal_part = int(0)    
                else:
                    decimal_part = Decimal("0." + decimal_part)
                
                
                print(integer_part,"int")
                print(decimal_part,"dec")
                
                print(integer_part,"int")
                print(decimal_part,"dec")
                new_integer = ""
                while integer_part > 0:
                    remainder = integer_part % basenum
                    if base == "Hex":    
                        # αφαιρεί το πρόθεμα των οκταδικών δυαδικών και δεκαεξαδικών αριθμών
                        # το μείον "-" έχει φύγει επίσης για να μην χρειαστεί να γίνει κάτι πιο πολύπλοκο από το να αφαιρέσει τα δυο πρώτα [:2]
                        digit = str(hex(int(remainder)))[2:]  
                    elif base =="Oct":
                        digit = str(oct(int(remainder)))[2:]  
                    elif base == "Bin":
                        digit = str(bin(int(remainder)))[2:]  
                    new_integer = str(digit + new_integer)
                    
                    integer_part = integer_part // basenum
                print(new_integer,"inthex")
                new_decimal = ""
                precision = 8 # αριθμός ψηφίων μετά το κόμα
                if decimal_part > 0:
                    for _ in range(precision):
                        decimal_part *= basenum
                        print(decimal_part,"συν")
                        if base == "Hex":    
                            d_digit = str(hex(int(decimal_part)))[2:]  
                        elif base =="Oct":
                            d_digit = str(oct(int(decimal_part)))[2:]  
                        elif base == "Bin":
                            d_digit = str(bin(int(decimal_part)))[2:]  
                        print(d_digit)
                        print(new_decimal)
                        new_decimal += d_digit
                        print(new_decimal, "meta")
                        decimal_part %= 1
                        print(decimal_part,"ρεμαιν")
                print(new_decimal,"dechex")
                if new_integer == "": 
                    new_num = str(integer_part) + '.' + new_decimal  # συνθεση του ακέραιου και δεκαδικού μέρους, αν δεν υπάρχει ακεραιο μέρος
                    new_num = new_num.rstrip('0')  
                else:
                    new_num = new_integer + '.' + new_decimal  # συνθεση του ακέραιου και δεκαδικού μέρους
                    new_num = new_num.rstrip('0')  
                
                if new_decimal == "":            # αν δεν υπάρχει δεκαδικό μέρος 
                    new_num = new_integer
                if minus:          # αν είναι αρνητικός προσθέτει το "-" 
                    new_num = "-" + new_num
                print(new_integer,"inthex")
                print(new_num, "pt")
            
                print(new_num,"gates")
                return new_num.lower() # επιστρέφει σε περιπτωση δεκαεξαδικού τους αριθμούς abcdef σε lower επειδή η  εφαρμογή σε lower τα εισάγει
        except Exception as e:
            return "Error"
    def othertodec(self, num, base):
            try:
                if base == "Hex":
                    basenum = int(16)
                elif base == "Oct":
                    basenum = int(8)
                elif base == "Bin":
                    basenum = int(2)
                
                if "." in str(num):
                        integer, decimal = num.split('.')

                    
                        if integer != "0":
                            integer = integer.lstrip('0')

                        
                        decimal = decimal.rstrip('0')
                else:
                        integer = str(num)
                        decimal = "0"

                print("Integer part:6666", integer)
                print("Decimal part:", decimal)
                if integer == "0" and decimal =="0":
                    print("edw")
                    sum = int(0)
                    return sum
                else:
                    print("mpika")
                    minus=False
                    if integer[0]=="-":
                        integer=integer[1:]
                        minus = True
                    elif integer[0]=="+":
                        integer=integer[1:]
                    j=int(0)
                    sum=int(0)
                    print("Integer part:", integer)
                    print("Decimal part:", decimal)
                    if integer!="0":
                        for i in range(len(integer)-1,-1,-1):
                            if integer[i] in "abcdef":
                                print("pin")
                                sum += (int(integer[i], 16))*(16**j)
                                print(sum)
                                print("pin2")
                                j+=1
                            else:
                                print("pin3")
                                sum += int(integer[i], basenum)*(basenum**j)
                                print(sum)
                                print("pin4")
                                j+=1 
                    print(sum,"edw")
                    j=int(-1)
                    # sum2 = 0
                    for i in range(len(decimal)):
                        if decimal[i] in "abcdef":
                            sum += (int(decimal[i], 16))*(16**j)
                            j-=1
                        else:
                            # print(sum2,"panw")
                            sum += int(decimal[i], basenum)*(basenum**j)
                            j-=1
                            print(sum, "katw") 
                    print(sum,"pio edw")
                    # if "9999999" in str(sum2):
                    #     sum2 = round(float(sum2), 1)
                    # sum = sum + sum2
                    
                    if minus:
                        sum = -1*sum
                    return sum
            except Exception as e:
                return "Error"
    def equals(self, expression, current_base):
        
        numbers = re.findall(r'[-+]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', expression)

        
        modified_expression = re.sub(r'(?<![0-9a-fA-F])[-]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', 'n', expression)
        modified_expression = modified_expression.replace('-', '+')
        if ")n" in modified_expression:
            modified_expression = modified_expression.replace(")n", ")+n")
        if "n(" in modified_expression:
            modified_expression = modified_expression.replace("n(", "n+(")
        print(modified_expression,"1")
        print(numbers)

        if current_base == "Hex":
                for num in numbers:
                    print("ok1")
                    if '.' in num:
                        print("ok2")
                        hex_num = str(self.othertodec((num), current_base))
                        print("ok3")
                        
                        print(modified_expression)
                    else:
                        hex_num = str(int(num, 16))
                        
                        print("ok")
                    
                
                        print(modified_expression)
                    modified_expression = re.sub(r'n', hex_num, modified_expression, count=1)
                    print("ok6")
        elif current_base == "Oct":
            for num in numbers:
                    if '.' in num:
                        print("ok2")
                        oct_num = str(self.othertodec((num), current_base))
                        print("ok3")
                        
                        print(modified_expression)
                    else:
                        oct_num = str((int(num, 8)))
                    modified_expression = re.sub(r'n', oct_num, modified_expression, count=1)
        elif current_base == "Bin":
            for num in numbers:
                    if '.' in num:
                        print("ok2")
                        bin_num = str(self.othertodec((num), current_base))
                        print("ok3")
                        
                        print(modified_expression)    
                    else:
                        bin_num = str((int(num, 2)))
                    modified_expression = re.sub(r'n', bin_num, modified_expression, count=1)
        elif current_base == "Dec":
            for num in numbers:
                    dec_num = str(float(num))
                    modified_expression = re.sub(r'n', dec_num, modified_expression, count=1)
        print(modified_expression,"2")
        pattern = r"\+-"
        has_plus_minus = re.search(pattern, modified_expression) is not None
        if has_plus_minus:
            modified_expression = modified_expression.replace("+-", "-")
        return modified_expression

    def convert_expression(self,expression, current_base, next_base):
        
        
        
        
        numbers = re.findall(r'[-+]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', expression)

        
        modified_expression = re.sub(r'(?<![0-9a-fA-F])[-]?(?:0[xX])?[0-9a-fA-F]+(?:\.[0-9a-fA-F]+)?', 'n', expression)
        modified_expression = modified_expression.replace('-', '+')
        if ")n" in modified_expression:
            modified_expression = modified_expression.replace(")n", ")+n")
        if "n(" in modified_expression:
            modified_expression = modified_expression.replace("n(", "n+(")
        

        print(numbers)
        print(modified_expression)
        if current_base == "Dec" and next_base == "Hex":
                for num in numbers:
                    
                    hex_num = str(self.dectoother((num), "Hex"))
                    print(hex_num,"777")
                    modified_expression = re.sub(r'n', hex_num, modified_expression, count=1)
        elif current_base == "Hex" and next_base == "Oct":
            for num in numbers:
                    
                    oct_num = str(self.dectoother((self.othertodec(num, "Hex")), "Oct"))
                    print(oct_num,"er")
                    modified_expression = re.sub(r'n', oct_num, modified_expression, count=1)
        elif current_base == "Oct" and next_base == "Bin":
            for num in numbers:
                    
                    bin_num = str(self.dectoother((self.othertodec(num, "Oct")), "Bin"))
                    modified_expression = re.sub(r'n', bin_num, modified_expression, count=1)
        elif current_base == "Bin" and next_base == "Dec":
            for num in numbers:
                    dec_num = str(self.othertodec(num, "Bin"))
                    modified_expression = re.sub(r'n', dec_num, modified_expression, count=1)
            print(modified_expression,"ei")
        print(numbers,"ela")
        print(modified_expression,"ela")
        pattern = r"\+-"
        has_plus_minus = re.search(pattern, modified_expression) is not None
        if has_plus_minus:
            modified_expression = modified_expression.replace("+-", "-")
        return modified_expression

    # ---------------------------------------