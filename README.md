This is my first-year final project at University, a scientific calculator with some programming calculator features. 
When the app is in "dec" mode it is a proper scientific calc. With the use of "()" the app can calculate whole numerical
expressions like 9*(5^3)+5-(6^2) etc. "-/+" and "1/x" works also for a whole numerical expression and not just for a given number. 
When you change base mode, the app convert the number or a whole numeric expression in the screen to hexadecimal, octal or binary mode.
When you add a number in the memory with "MS" the app save the number's base also, so if you want to make an addition of a number in the number already stored in the memory("M+"),
the app will convert the number to the base of the number already stored in the memory, an make the addition.
Changing base modes convert the number stored in memory to that bases too.
The idea behind the main calculating sort of engine of the app is simple.
Lets say we have the expression -9*(5^3)+5-(6^2)
You press the buttons and create a string(numerical expression) that the app will separate to two components, a list of the numbers contained(-9,5,3,5,6,2), and the basic expession in the form of num*(num^num)+num-(num^num).
After that we can convert the number to a different base, or change the sing of the number, recreate the expression by replacing "num" in the expression with the new number, and use eval to get a result or just present the expression with converted numbers.

in "bin" mode you can calculate logic gate expressions like NOT1 , 1NAND0 and whole logic gates expressions in the form of (((NOT1)OR(1NAND0))NOR(1AND(1OR1))).
A recursive function will enter first the inner () parentheses and start calculate the result, the result will replace the inner paretheses expression, and the function will move to an outer parentheses and do the same.
The function will be doing that until no logic gates expression exists in our expression.
In "bin" mode you can do more bitwise operations, shift left "<<" and shift right ">>".
