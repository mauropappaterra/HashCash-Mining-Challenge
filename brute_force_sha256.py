# HashCash Mining Challenge
# brute_force_sha256.py
# Created by Mauro J. Pappaterra on 07 of April 2019.
import datetime as t
import hashlib as c
import random as r
import string as s

def find_hash (student_id, zeroes):
    attempts = 0
    flag = False
    start_time = t.datetime.now()

    print ("Finding a nonce for student id '" + student_id + "' resulting in a sha256 hash that begins with at least " + str(zeroes) + " zeroes...")

    while (not flag):
        # Create nonce
        nonce = ''.join(r.choices(s.ascii_letters + s.digits, k=r.randint(1, 20)))
        # Hash it!
        hash = c.sha256((student_id + nonce).encode()).hexdigest()
        # Check solution
        if (hash[:zeroes] == '0' * zeroes):
            flag = True
            solution = (nonce, hash, attempts, t.datetime.now() - start_time)
        else:
            attempts += 1

    return solution

while (True):
    my_solution = find_hash('45648766', 9)
    message = "SOLUTION FOUND!\nNonce -> " + my_solution[0] + "\nHash -> " + my_solution[1] + "\nNumber of Attemps Needed -> " + str(my_solution[2]) + "\nTime Needed -> " + str(my_solution[3])
    print(message)
    with open (my_solution[1] + ".txt", 'w') as file: # Save solution to external file
        file.write (message)