# HashCash Mining Challenge
# brute_force_sha256.py
# Created by Mauro J. Pappaterra on 07 of April 2019.

import datetime as t
import hashlib as c
import random as r
import string as s

def find_hash (student_id):
    attemps = 0
    flag = False
    start_time = t.datetime.now()

    print ("Finding nonce for " + student_id + "...")

    while (not flag):
        # Create nonce
        nonce = ''.join(r.choices(s.ascii_letters + s.digits, k=r.randint(1, 20)))
        # Hash it!
        hash = c.sha256((student_id + nonce).encode()).hexdigest()

        # FOR TESTING PURPOSES
        #if (attemps == 200000):
        #    hash = '000000000'

        if (hash[:7] == '0000000'): #Check solution
            flag = True
            total_time = t.datetime.now()- start_time
            solution = (hash, nonce, attemps, total_time)
        else:
            attemps += 1

    return solution

my_solution = find_hash('45648766')
message = "SOLUTION FOUND!\nHash -> " + my_solution[0] + "\nNonce -> " + my_solution[1] + "\nNumber of Attemps Needed -> " + str(my_solution[2]) + "\nTime Needed -> " + str(my_solution[3])

with open (my_solution[1] + ".txt", 'w') as file: # Save solution to external file
    file.write (message)