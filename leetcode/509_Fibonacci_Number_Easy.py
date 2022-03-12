class Solution:
    def fib(self, n: int) -> int:   
        # 0, 1, 1, 2, 3, 5, 8, 13 ...
        
        # method 1 recursion
        if n <= 1:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        
        # method 2 array to save all the fib(n) by Dynamic programming
        if n <= 1:
            return n
        
        fib_array = [0, 1]
        for i in range(2, n+1):
            fib_array.append(fib_array[i-1] + fib_array[i-2])
            
        return fib_array.pop()

        # method 3 mathmatical general formula
        phi = (1+5**0.5)/2
        inverse_phi = (1-5**0.5)/2
        result = (phi**n - inverse_phi**n)/(5**0.5)
        return int(result)
        
        # method 4 DP, less space complaxcity 
        if n <= 1:
            return n
        first_element, second_element = 0, 1
        for i in range(2, n+1):
            temp = first_element + second_element
            first_element, second_element = second_element, temp
        return second_element