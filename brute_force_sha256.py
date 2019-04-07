# HashCash Mining Challenge
# brute_force_sha256.py
# Created by Mauro J. Pappaterra on 07 of April 2019.
from datetime import datetime as t
import hashlib as c
import random as r
import string as s

def find_hash (student_id):
    attemps = 0
    flag = False
    start_time = t.now()

    while (not flag):

        # Create nonce
        nonce = ''.join(r.choices(s.ascii_letters + s.digits, k=r.randint(1, 20)))
        #print(nonce)

        # Hash it!
        hash = c.sha256((student_id + nonce).encode()).hexdigest()
        #print(hash)
        #print(hash[:7])

        # FOR TESTING PURPOSES
        #if (attemps == 1500):
            #hash = '000000000000000000000'

        #Check if solution is right
        print("Compare " + hash[:7] + " with '0000000'")
        if (hash[:7] == '0000000'):
            flag = True
            total_time = start_time - t.now()

            print ("\nSolution Found!\nHash -> " + hash + "\nNonce -> " + nonce + "\nNumber of Attemps Needed -> " + str(attemps) + "\nTime Needed -> " + str(total_time))
        else:
            attemps += 1

    return "nothing"


print(find_hash('45648766'))
