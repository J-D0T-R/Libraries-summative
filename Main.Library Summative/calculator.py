###   Libraries Summative: Main  ###
###   James Rutley   ###
###   Start date: 11/01/2021   ###
###   End date: 11/02/2021   ###

# Imports
import time
from modules import answers
from modules import operations

# Functions
def calc():
    while True:
        if answers.last_ans != "a":
            use_last = input("Would you like to use your previous solution?(y/n) ")
            if "y" in str(use_last):
                num = answers.last_ans
                
            else:
                try:
                    num = int(input("Enter a number: "))
                  
                except ValueError:
                    print("Value Error: Expected a Number.")
                    calc()
        else:
            try:
                num = int(input("Enter a number: "))
                  
            except ValueError:
                print("Value Error: Expected a Number.")
                calc()
        
        time.sleep(0.2)
        print("Add, Subtract, Multiply, Divide,")
        print("Exponent, Root")
        time.sleep(0.2)
        choice = input("Choose an operation: ").lower()
        
        if "add" in str(choice) or "plus" in str(choice):
            time.sleep(0.2)
            if answers.last_ans != "a":
                use_last = input("Would you like to use your previous solution?(y/n) ")
            
                if "y" in str(use_last):
                    time.sleep(0.2)
                    solution = operations.add(num,answers.last_ans)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
            
                else:
                    try:
                        second_num = int(input(f"{num} + "))
                        time.sleep(0.2)
                        solution = operations.add(num,second_num)
                        answers.past_ans.append(solution)
                        answers.last_ans = solution
                    
                    except ValueError:
                        time.sleep(0.2)
                        print("Value Error: Expected a Number.")
                        pass
                
            else:
                try:
                    second_num = int(input(f"{num} + "))
                    time.sleep(0.2)
                    solution = operations.add(num,second_num)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
                    
                except ValueError:
                    time.sleep(0.2)
                    print("Value Error: Expected a Number.")
                    pass
                    
        elif "subtract" in str(choice) or "minus" in str(choice):
            time.sleep(0.2)
            if answers.last_ans != "a":
                use_last = input("Would you like to use your previous solution?(y/n) ")
                
                if "y" in str(use_last):
                    time.sleep(0.2)
                    solution = operations.subtract(num,answers.last_ans)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
                
                else:
                    try:
                        second_num = int(input(f"{num} - "))
                        time.sleep(0.2)
                        solution = operations.subtract(num,second_num)
                        answers.past_ans.append(solution)
                        answers.last_ans = solution
                    
                    except ValueError:
                        time.sleep(0.2)
                        print("Value Error: Expected a Number.")
                        pass
            else:
                try:
                    second_num = int(input(f"{num} - "))
                    time.sleep(0.2)
                    solution = operations.subtract(num,second_num)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
                    
                except ValueError:
                    time.sleep(0.2)
                    print("Value Error: Expected a Number.")
                    pass
                
        elif "multiply" in str(choice) or "times" in str(choice):
            time.sleep(0.2)
            
            if answers.last_ans != "a":
                use_last = input("Would you like to use your previous solution?(y/n) ")
                
                if "y" in str(use_last):
                    time.sleep(0.2)
                    solution = operations.multiply(num,answers.last_ans)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
                
                else:
                    try:
                        second_num = int(input(f"{num} * "))
                        time.sleep(0.2)
                        solution = operations.multiply(num,second_num)
                        answers.past_ans.append(solution)
                        answers.last_ans = solution
                    
                    except ValueError:
                        time.sleep(0.2)
                        print("Value Error: Expected a Number.")
                        pass
            else:
                try:
                    second_num = int(input(f"{num} * "))
                    time.sleep(0.2)
                    solution = operations.multiply(num,second_num)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
                    
                except ValueError:
                    time.sleep(0.2)
                    print("Value Error: Expected a Number.")
                    pass
            
        elif "divide" in str(choice):
            time.sleep(0.2)
            if answers.last_ans != "a":
                use_last = input("Would you like to use your previous solution?(y/n) ")
                
                if "y" in str(use_last):
                    time.sleep(0.2)
                    solution = operations.divide(num,second_num)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
                
                else:
                    try:
                        second_num = int(input(f"{num} / "))
                        time.sleep(0.2)
                        solution = operations.divide(num,second_num)
                        answers.past_ans.append(solution)
                        answers.last_ans = solution
                    
                    except ValueError:
                        time.sleep(0.2)
                        print("Value Error: Expected a Number.")
                        pass
            else:
                try:
                    second_num = int(input(f"{num} / "))
                    time.sleep(0.2)
                    solution = operations.divide(num,second_num)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
                    
                except ValueError:
                    time.sleep(0.2)
                    print("Value Error: Expected a Number.")
                    pass
                
        elif "exponent" in str(choice) or "power" in str(choice):
            time.sleep(0.2)
            if answers.last_ans != "a":
                use_last = input("Would you like to use your previous solution?(y/n) ")
            
                if "y" in str(use_last):
                    time.sleep(0.2)
                    solution = operations.power(num,answers.last_ans)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
            
                else:
                    try:
                        second_num = int(input(f"{num} ^ "))
                        time.sleep(0.2)
                        solution = operations.power(num,second_num)
                        answers.past_ans.append(solution)
                        answers.last_ans = solution
                    
                    except ValueError:
                        time.sleep(0.2)
                        print("Value Error: Expected a Number.")
                        pass
                
            else:
                try:
                    second_num = int(input(f"{num} ^ "))
                    time.sleep(0.2)
                    solution = operations.power(num,second_num)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
                    
                except ValueError:
                    time.sleep(0.2)
                    print("Value Error: Expected a Number.")
                    pass
                
        elif "root" in str(choice):
            time.sleep(0.2)
            if answers.last_ans != "a":
                use_last = input("Would you like to use your previous solution?(y/n) ")
            
                if "y" in str(use_last):
                    time.sleep(0.2)
                    solution = operations.root(answers.last_ans,num)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
            
                else:
                    try:
                        second_num = int(input(f"{num}th root of "))
                        time.sleep(0.2)
                        solution = operations.root(second_num,num)
                        answers.past_ans.append(solution)
                        answers.last_ans = solution
                    
                    except ValueError:
                        time.sleep(0.2)
                        print("Value Error: Expected a Number.")
                        pass
                
            else:
                try:
                    second_num = int(input(f"{num}th root of "))
                    time.sleep(0.2)
                    solution = operations.root(second_num,num)
                    answers.past_ans.append(solution)
                    answers.last_ans = solution
                    
                except ValueError:
                    time.sleep(0.2)
                    print("Value Error: Expected a Number.")
                    pass
                
        else:
            print("That's not something I can do.")
            pass
        
        go_again = input("Would you like to do another calculation? (y/n) ").lower()
        
        if "y" in str(go_again):
            view_ans = input("Would you like to view past solutions?(y/n) ").lower()
            
            if "y" in str(view_ans):
                print(answers.past_ans)
                pass
        
            else:
                pass
            
            continue
        
        else:
            view_ans = input("Would you like to view past solutions?(y/n) ").lower()
            
            if "y" in str(view_ans):
                print(answers.past_ans)
                pass
        
            else:
                pass
            
            break
calc()

file_name = "maincalculator.py"