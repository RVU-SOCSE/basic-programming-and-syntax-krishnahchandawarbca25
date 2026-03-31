choice = input("Select conversion: \n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\nEnter 1 or 2: ")
temp = float(input("Enter temperature value: "))

match choice:
    
    case "1":
        
        result = (temp - 32) * 5/9
        print(f"{temp}°F is {result:.2f}°C")
    case "2":
        
        result = (temp * 9/5) + 32
        print(f"{temp}°C is {result:.2f}°F")
    case _:
        
        print("Invalid choice! Please select 1 or 2.")

                 
