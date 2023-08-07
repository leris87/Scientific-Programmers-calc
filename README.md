This is my first-year final project at University, a scientific calculator with some programming calculator features. 
You need both files in the same folder. 
Run the app from finalcount.py. calcs.py contain the father class Calcs that inherits the functions to our ScientificCalculator class, mainly for better visibility of the code.

When the app is in "dec" mode it is a proper scientific calc.
Calculations include +-*/, modulo, raise x to the power y(x**y), change sign(+/-), value of the fraction 1/x,  square root, Nth square root(nsqrt), factorial of a number, log for Natural numbers, for floats, for negative numbers(imaginary number as a result), pi and e numbers (π, e), and trigonometric calculation sin, cos, tan, asin, acos, atan, sinh, cosh in rad or degrees.

The rad/deg button changes the input of a number to radians or degrees.
if you want to input a number in radians and the screen shows "Deg", you press the button "rad/deg", the screen will turn to "Rad" and you input radians for trigonometric calculations. And the opposite.

With the use of "()" the app can calculate whole numerical expressions like 9*(5^3)+5-(6^2) etc.
"-/+" and "1/x" works also for a whole numerical expression and not just for a given number. 
When you change base mode, the app converts the number or a whole numeric expression on the screen to hexadecimal, octal ,or binary base mode.
When you add a number in the memory with "MS" the app save the number's base also, so if you want to make an addition of a number in the number already stored in the memory("M+"),
the app will convert the number to the base of the number already stored in the memory, and make the addition.

Changing base modes convert the number stored in memory to that base too.
The idea behind the main calculating sort of engine of the app is simple.
Lets say we have the expression -9*(5^3)+5-(6^2)
You press the buttons and create a string(numerical expression) that the app will separate into two components, a list of the numbers contained(-9,5,3,5,6,2), and the basic expression in the form of num*(num^num)+num-(num^num).
After that, we can convert the number to a different base, change the sign of the number, recreate the expression by replacing "num" in the expression with the new number, and use eval to get a result or just present the expression with converted numbers.

in "bin" mode you can calculate logic gate expressions like NOT1, 1NAND0, and whole logic gates expressions in the form of (((NOT1)OR(1NAND0))NOR(1AND(1OR1))).
A recursive function will enter first the inner () parentheses and start to calculate the result, the result will replace the inner parentheses expression, and the function will move to outer parentheses and do the same.
The function will be doing that until no logic gates expression exists in our expression.
In "bin" mode you can do more bitwise operations, shift left "<<" and shift right ">>".
