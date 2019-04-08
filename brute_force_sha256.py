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
        # Check solution
        if (hash[:11] == '00000000000'):
            flag = True
            solution = (nonce, hash, attemps, t.datetime.now() - start_time)
        else:
            attemps += 1

    return solution

my_solution = find_hash('45648766')
message = "SOLUTION FOUND!\nNonce -> " + my_solution[0] + "\nHash -> " + my_solution[1] + "\nNumber of Attemps Needed -> " + str(my_solution[2]) + "\nTime Needed -> " + str(my_solution[3])

with open (my_solution[1] + ".txt", 'w') as file: # Save solution to external file
    file.write (message)