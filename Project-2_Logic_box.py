print("Welcome to the Pattern Generator and Number Analyzer!\n")

while True:
    print("Select an option:\n")
    print("1. Genrate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            rows = int(input("\nEnter the number of rows for the pattern : "))
            for i in range(1,rows+1):
                for j in range(1,i+1):
                    print("*", end = " ")
                print() 
            print()
        case 2:
            start = int(input("\nEnter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            sum = 0
            for i in range(start, end+1):
                if i%2 == 0:
                    print("Number",i,"is Even")
                else:
                    print("Number",i,"is Odd")
                sum += i
            print("Sum of all numbers from",start,"to",end,"is:",sum,"\n")
        case 3:
            print("\nExiting the program. Goodbye!")
            break
        case _:
            print("invalid choice!")
        