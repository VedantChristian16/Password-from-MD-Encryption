'''
Created by Vedant Christian
Created on 06 / 10 / 2019

You will need to download the file, "rockyou.txt", from the internet as it is a very large file and would not be uploaded onto the repository.
'''

from urllib.request import urlopen, hashlib
import time

MD5Hash = input("Please input the hash to crack.\n>")
HashedMD = hashlib.md5(bytes(MD5Hash, 'utf-8')).hexdigest()

LIST_OF_COMMON_PASSWORDS = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
    hashedGuess = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()

    if hashedGuess == HashedMD:
        print("The password is ", str(guess))
        time.sleep(5)

    elif hashedGuess != HashedMD:
        print("Password guess ",str(guess)," does not match, trying next...")

print("Password not in database, we'll get them next time.")
time.sleep(5)
inp1 = input("Do you want to continue searching in a different database? (y/n)")
print("Locating Database...")
time.sleep(5)
print("Found Database...")
time.sleep(2)
print("Searching Database...")
time.sleep(1)

if inp1 == "y":
    with open("rockyou.txt", "r") as a:
        for line in a:
            line = line.rstrip("\n")
            b = hashlib.md5((line).encode('utf-8'))
            print("\n")
            print(b.hexdigest())
            
            if (b.hexdigest()) == MD5Hash:
                print("\nThe password is", line)
                break

            if (b.hexdigest()) != MD5Hash:
                print("Password guess ", str(b), " does not match, trying next...")
