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

while action !="e" and action !="d" and action !="q":
    print("Did not understand command, try again.")
    action = input("Enter e to encrypt, d to decrypt, or q to quit: ")
#-------------------------------------------------------------------------------
if action == "q":
    print("Goodbye!")
#-------------------------------------------------------------------------------

#trying to make key longer than message
"""
if k < m:
# newkey= k
# k= k + newkey
# example: message is 5 and key is 4
#find remainder of m/k. round up to next whole number, and multilpy k by that number. 

"""
#-------------------------------------------------------------------------------
if action == "e" or "d":
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

q = len("Message")
r = len("Key")
        
key = mkey*int((q/r))
remainders = q%r
        
if remainders != 0:
    remainder = range(remainders)
    for h in remainder:
        key.append(mkey[h])


elist = (list(zip(message,key)))
print(elist)


if action == "e":
    for c in elist:
        g = associations[c[0]+c[1]]
        print(g)
        
#working on this...
for n in elist:
    print(n,end="")
#-------------------------------------------------------------------------------

if action == "d":
    for c in elist:
        gg = associations[c[0]-c[1]]
        print(gg)
#-------------------------------------------------------------------------------

result = []

for n in result:
    print(n,end="")

