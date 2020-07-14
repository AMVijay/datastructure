# Fibonacci Search
Fibonacci Search algorithm uses fibonacci series numbers to determine the index of the element in traversel of the linear data structure until found the matched element.

## Algorithm Steps 
1. Find the length of the linear data structure.
2. Find the smallest fibonacci number which is greater than or equal to the length determined in step 1.
3. Declare the fibonacci number determined in step 2 as fibonacciM and find the next 2 smallest fibonacci number and define it as fibonacciM1, fibonnacciM2.
4. Initialize variable called offset as -1. 
5. Determine index value using formulae minimum value of offset + fibonacciM2 and length -1 of linear data structure.
6. Check whether value at the index matches the search element. 
7. If yes, return the index value. 
8. If no, then check whether value at the index is less than search element value. 
    8.1. If yes, then shift the fibonicci numbers one left from higher value, that reinitializes the variable as below 
          8.1.1 fibonacciM = fibonacciM1 
          8.1.2 fibonacciM1 = fibonacciM - fibonacciM1
          8.1.3 fibonacciM2 = fibonacciM - fibonacciM1
          8.1.4 offset = index
    8.2. If no, then check whether value at the index is greater than the search element value. 
    8.3. If yes, then shift the fibonacci numbers two left from higher value, that  reinitializes the variable as below
          8.3.1.  fibonacciM = fibonacciM2
          8.3.2.  fibonacciM1 = fibonacciM - fibonacciM1
          8.3.3   fibonacciM2 = fibonacciM - fibonacciM2
9. Repeat the step 5 to 8 until.           
