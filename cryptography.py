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



m = input("Enter e to encrypt, d to decrypt, or q to quit: ")

while m !="e" and m !="d" and m !="q":
    print("Did not understand command, try again.")
    m = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    
if m == "q":
    print("Goodbye!")
    
elif m == "e":
    f = input ("Message: ")
    s = input ("Key: ")
    
    message= []

    for l in f:
        n = associations.find(l)
    message.append(n)


elif m == "d":
    f = input ("Message: ")
    s = input ("Key: ")
    
    message= []
    
    
"""
associations.find(m)

associations[index]

        message= []
        for n in b:
         d = associations.find(n)
         message.append(d)
    
        key1 = []
        for n in c:
            e = associations.find(n)
            key1.append(e)
        
"""

