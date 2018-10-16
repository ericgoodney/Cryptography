"""
cryptography.py
Author: Eric Goodney
Credit: Peers, Teacher, Internet:

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md

Enter e to encrypt, d to decrypt, or q to quit: z
Did not understand command, try again.
Enter e to encrypt, d to decrypt, or q to quit: e
Message: Two plus two = Five
Key: Lorem ipsum
+KF;B(CH=NIZ}m;R\Dt
Enter e to encrypt, d to decrypt, or q to quit: d
Message: +KF;B(CH=NIZ}m;R\Dt
Key: Lorem ipsum
Two plus two = Five
Enter e to encrypt, d to decrypt, or q to quit: q
Goodbye!

"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"



action = input("Enter e to encrypt, d to decrypt, or q to quit: ")

while action !="e" and m !="d" and m !="q":
    print("Did not understand command, try again.")
    action = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    
if action == "q":
    print("Goodbye!")
    
elif action == "e":
    m = input("Message: ")
    k = input("Key: ")
    
    message = []

    for l in m:
        c = associations.find(l)
        message.append(c)

#searches through message
    
    mkey= []
    for l in k:
        f = associations.find(l)
        mkey.append(f)
    
#serches through key

print(message)       
print(mkey)
print(message+mkey)

#print a list of list of zip of 

    

    
  
    
