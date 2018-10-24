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
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

action = input("Enter e to encrypt, d to decrypt, or q to quit: ")


while action !="q":
    
    if action == "e" or action =="d":
        m = input("Message: ")
        k = input("Key: ")
        message = []
        for l in m:
            c = associations.find(l)
            message.append(c)
        mkey = []
        for l in k:
            f = associations.find(l)
            mkey.append(f)
            
        L1 = len(message)
        L2 = len(mkey)
        rkey = mkey*int((L1/L2))
        remainders = L1%L2 
        if remainders !=0:
            remainder = range(remainders)
            for k in remainder:
                rkey.append(mkey[k])
        result = []
        elist = (list(zip(message,rkey)))
        if action == "e":
            for c in elist:
                g = associations[c[0]+c[1]]
                print(g,end="")
        if action == "d":
            for c in elist:
                gg = associations[c[0]-c[1]]
                print(gg,end="")
        for l in result:
            print(l,end="")
        print('')
    if action !="e" and action !="d" and action !="q":
        print("Did not understand command, try again.")
    action = input("Enter e to encrypt, d to decrypt, or q to quit: ")
        
if action == "q":
    print("Goodbye!")
    
    
    
    