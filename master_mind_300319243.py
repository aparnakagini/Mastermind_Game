import random

user_guess = []

name = input('What is your name? ')

print('Welcome to Master Mind', name + '!')
colours = ['Red', 'Yellow', 'Blue', 'Green', 'Orange', 'Pink', 'Purple', 'Cyan', 'Silver', 'Teal']
print('The code maker is here. Available colours are')
print(', '.join(colours))

colours_chosen = random.sample(colours, 4)

print('You have 15 guesses, total of 5 penalties are allowed but avoid penalties.')
print('The code maker selected 4 colours.')
print('You can start guessing', name)
print()

num_guesses = 1

def point_system(colours_chosen):
    num_guesses = 0
    num_penalties = 0
    black = 0
    white = 0

    while num_guesses <= 15 and num_penalties < 5:
        black = 0
        white = 0
        num_guesses += 1 
        
        user_guess = input('Enter guess number ' + str(num_guesses) + ": ").split()  
        
        for i in range(len(user_guess)):
          user_guess[i] = user_guess[i].capitalize()
      
        if penalty_count(user_guess):   
            num_penalties += 1
            print('Total Penalties = ', num_penalties)
        else:
            for i in range(len(user_guess)):
                if user_guess[i] == colours_chosen[i]:    
                    black += 1
                elif user_guess[i] in colours_chosen:     
                    white += 1
            
            print('You got ', black, ' black, and ', white, ' whites for this guess.')

        #final output messages
        if num_penalties == 5:
            print(name + ', you lost the game by reaching the maximum number of allowed penalties.')
        if num_guesses > 15:
            print('Sorry', name, 'you ran out of guesses and lost the game with', num_penalties, 'penalties.')
        if black == 4:
            print('You got 4 blacks', name)
            print('You won with', num_guesses, 'guesses and', num_penalties, 'penalties. Congratulations.')
            break

    return black, white

def penalty_count(user_guess):
    penalty_check = False
    penalty_message = 'Sorry ' + name + ','

    #penalty check for number of colours entered by player
    if len(user_guess) != 4: 
        penalty_message += ' you need to enter atleast 4 colours for each guess.'
        penalty_check = True
    
    #penalty check for repeated colours
    if len(user_guess) != len(list(set(user_guess))):  
      if penalty_check == True: 
          penalty_message += ' Also,'
      penalty_message += ' repeated colors are not allowed in this game.'
      penalty_check = True
    
    #penalty check to see if colours entered belong in original list of colours
    for k in range(len(user_guess)):
        if user_guess[k] not in colours:   
            if penalty_check is True:
                penalty_message += ' Also,' 
            penalty_message += ' cannot recognize the colours you entered.'
            penalty_check = True
            break  

    penalty_message += ' One penalty is considered.'   
    if penalty_check is True:  
        print(penalty_message)
    return penalty_check

point_system(colours_chosen)
