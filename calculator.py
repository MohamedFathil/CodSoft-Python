
def add(n1,n2):
    if n2 == 0:
        print("Cannot divide by 0")
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

def Calculator():
    while True:
        print("Select the Operations : ")
        print("""            
            1. Addition
            2. Subtraction
            3. Multiply
            4. Divide
            5. Exit""")
        
        ch = input("Enter the Choice : ")
        
        if ch == '5':
            print("Exiting the calculator. Bye...")
            break
        
        if ch in ['1','2','3','4']:
            try:
                n1 = float(input("Enter the First Number  : "))
                n2 = float(input("Enter the Second Number : "))
                
                
                if ch == '1':
                    print(n1," + ",n2," = ", add(n1,n2))
                elif ch == '2':
                    print(n1," - ",n2," = ", sub(n1,n2))
                elif ch == '3':
                    print(n1," * ",n2," = ", mul(n1,n2))
                elif ch == '4':
                    print(n1," / ",n2," = ", div(n1,n2))
            
            except ValueError:
                print("Invalid Input. Please enter numberic values...")
                continue
        
        else:
            print("Invalid Choice! Please select a valid option.")

if __name__ == "__main__":
    Calculator()