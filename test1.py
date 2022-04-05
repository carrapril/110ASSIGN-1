



from re import I


def younger_person():
    ages = [72,42,32,50,56,14,78,30,51,89,12,38,67,10]
    
    solution = ages[0]
    
    for age in ages:
        if age < solution: 
            solution = age
            
    print(solution)
    
    
def statistics():
    data = [12,-1,123,345,412,4.55,123,23.4,123,4587,-129,94,956,14565,32, 0.001, 123]
    
    list = 0
    total = 0
    negative = 0
    
    for num in data:
        list += 1
        total += num
        
        if num < 0:
            negative = negative + num
           
        
    
    print(f"1 solution is: {list}")
    print(f"2 solution is: {total}")
    print(f"1 solution is: {len(data)}")
    print(f"negative : {negative}")
    
def print_some_nums():  
    for i in range(1,11):
        print(i*10)  
    

        
        




print("Test test test")
younger_person()
statistics()
print_some_nums()