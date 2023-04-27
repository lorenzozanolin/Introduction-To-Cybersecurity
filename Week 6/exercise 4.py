import random
import string


def match(guess):
    elapsed_time = 0
    match_value = True
    elapsed_time = elapsed_time + 1
    if len(secret) != len(guess):
        match_value = False
        elapsed_time = elapsed_time + 5
    if match_value:
        for i in range(len(secret)):
            elapsed_time = elapsed_time + 10
            if secret[i] != guess[i]:
                match_value = False
                return match_value, elapsed_time
        elapsed_time = elapsed_time + 10
    return match_value, elapsed_time

def guess_length () :
    duration = [] # array to hold the different amounts of time used to check guesses for the secret string
    
    for i in range ( max_len + 1):
        #generate a string of len i
        rvalue = ''.join(random.choice(string.ascii_lowercase)for j in range (i) )

        # take times
        duration.append(match(rvalue)[1])

    return duration.index(max(duration))

def recover_string ( length ) :
    likely_guess = ""
    for l in range (1 , length +1) :
        duration = [] # array to hold the different amounts of time used to check guesses for the secret string
        for i in range(26):
            rvalue = (likely_guess + string.ascii_lowercase[i]).ljust(length," ")
            duration.append(match(rvalue)[1])
            if i>0 and (duration[i] < duration[i-1]):
                break
        likely_guess += string.ascii_lowercase[len(duration)-2]    
        

    return likely_guess

max_len = 10  # Max length of password
pwd_len = random.randrange(3, max_len + 1)
secret = ''.join(random.choice(string.ascii_lowercase) for i in range(pwd_len))

#print(guess_length(),pwd_len) FOR DEBUGGING

#print(f"Secret is {secret}, guessed is {guess}, match function says {iscorrect}, and took {time} time.")
print(recover_string(guess_length()),secret)

#complexity: O(26*|input|)