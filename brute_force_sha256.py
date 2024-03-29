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
    no_zeroes = '0' * zeroes
    start_time = t.datetime.now()

    while (not flag):
        # Create nonce
        nonce = ''.join(r.choices(s.ascii_letters + s.digits, k=r.randint(1, 20)))
        # Hash it!
        hash = c.sha256((student_id + nonce).encode()).hexdigest()

        # For Testing purposes
        #if (attempts == 1000000):
        #    hash = '000000000000000000'

        # Check solution
        if (hash[:zeroes] == no_zeroes):
            flag = True
            solution = (nonce, hash, attempts, t.datetime.now() - start_time)
        else:
            attempts += 1

    return solution