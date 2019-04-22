# HashCash Mining Challenge
# cython_optimized.pyx
# Created by Mauro J. Pappaterra on 12 of April 2019.
import hashlib as c
import random as r
import string as s

def find_hash (student_id, zeroes):
    cdef int attempts = 0
    cdef int flag = 1
    cdef str nonce
    cdef str hash
    cdef str no_zeroes = '0' * zeroes

    while (flag):
        # Create nonce
        nonce = ''.join(r.choices(s.ascii_letters + s.digits, k=r.randint(1, 20)))
        # Hash it!
        hash = c.sha256((student_id + nonce).encode()).hexdigest()

        # For Testing purposes
        #if (attempts == 1000000):
        #    hash = '0000000000000000'

        # Check solution
        if (hash[:zeroes] == no_zeroes):
            flag = 0
            solution = (nonce, hash, attempts)
        else:
            attempts += 1

    return solution