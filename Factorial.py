def fact(n):  
  
      if n == 0:  
  
          return 1  
  #because 0! and 1! equal to 1.
  
      if n == 1:  
  
          return 1  
  
      return n * fact(n-1)  
  
    
  
  print(fact(5))
