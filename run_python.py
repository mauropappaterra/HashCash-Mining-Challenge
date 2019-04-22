# HashCash Mining Challenge
# run_python.py
# Created by Mauro J. Pappaterra on 22 of April 2019.
import brute_force_sha256 as py

# Input
student_id = '45648766'
zeroes = 9

print("\nFinding a nonce for student id '" + student_id + "' resulting in a\
 sha256 hash that begins with at least " + str(zeroes) + " zeroes...\n")

while (True): # Infinite Loop
    my_solution = py.find_hash(student_id, zeroes)

    message = "\nSOLUTION FOUND!\nInput -> '"+ student_id +"' with at least " + str(zeroes) +" zeroes\nNonce -> " + my_solution[0] + "\nHash -> " + my_solution[1] + "\nNumber of Attempts Needed -> " + str(my_solution[2]) + "\nTime Needed -> " + str(my_solution[3])
    print(message)

    with open ("output/"+ str(zeroes) + "z_" + my_solution[0] + ".txt", 'w') as file: # Save solution to external file
        file.write (message)