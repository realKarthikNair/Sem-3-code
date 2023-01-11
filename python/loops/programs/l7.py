# 7. Write a Python program to print alphabet pattern 'A'.
# Expected Output:

#   ***                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  *****                                                                 
#  *   *                                                                  
#  *   *                                                                  
#  *   *

for i in range(7):
    if (i==0 or i==3):
        if (i==0):
            print(" "+"*"*3)
        elif (i==3):
            print("*"*5)
    else:
        print("*"+(" "*3)+"*")
        