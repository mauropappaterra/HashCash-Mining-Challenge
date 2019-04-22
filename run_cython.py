# HashCash Mining Challenge
# run_cython.py
# Created by Mauro J. Pappaterra on 12 of April 2019.
import datetime as t
import pyximport
pyximport.install()
import cython_optimized as cy

# Input
student_id = '45648766'
zeroes = 9

print("\nFinding a nonce for student id '" + student_id + "' resulting in a\
 sha256 hash that begins with at least " + str(zeroes) + " zeroes...\n")

# Infinite Loop
while (True):
    start_time = t.datetime.now()
    my_solution = cy.find_hash(student_id, zeroes)
    total_time = t.datetime.now() - start_time

    message = "\nSOLUTION FOUND!\nInput -> '"+ student_id +"' with at least " + str(zeroes) +" zeroes\nNonce -> " + my_solution[0] + "\nHash -> " + my_solution[1] + "\nNumber of Attempts Needed -> " + str(my_solution[2]) + "\nTime Needed -> " + str(total_time)
    print(message)

    with open ("output/"+ str(zeroes) + "z_" + my_solution[0] + ".txt", 'w') as file: # Save solution to external file
        file.write (message)