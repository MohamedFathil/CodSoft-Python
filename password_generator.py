import random
import string

def generate_password(length):
    char = string.ascii_letters + string.digits + string.punctuation
    
    if length < 1:
        raise ValueError("Password Length must be atleast 1 character..")
    
    password = ''.join(random.choice(char) for i in range(length))
    
    return password

def inp():
    try:
        length = int(input("Enter the length of the Password : "))
        password = generate_password(length)
        print(f"Generated Password : {password}")
    
    except ValueError as v:
        print(f"Invalid Input : {v}")    
        
if __name__ == "__main__":
    inp()