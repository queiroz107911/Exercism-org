"""
Make some functions for implementing the rules of the classic arcade game Pac-Man
Functions:
1. Pacman eat or not a ghost or not
2. Pacman scores or not
3. Pacman loses or not
4. Pacman wins or not

The main content is function and bool type

"""


# Verify is Pacman can eat or not a ghost
def eat_ghost(power_pellet_active, touching_ghost):
    if power_pellet_active is True:
        print('You are empowered')
        if touching_ghost is False:
            return False                
       
        return True                 
        
    else:
        print('You are not empowered')
        if touching_ghost is False:
            return False                

        return False           
        
print('I can eat a ghost?', eat_ghost(True, False))
print('\n')
print('I can eat a ghost?', eat_ghost(True, True))
print('\n')
print('I can eat a ghost?', eat_ghost(False, False))
print('\n')
print('I can eat a ghost?', eat_ghost(False, True))
print('-'*30)


# Verify if Pacman have Scored
def score(touching_power_pellet, touching_dot):
    
    match (touching_power_pellet, touching_dot):
        case (True, True):
            return True
        case (True, False):
            return True
        case (False, True):
            return True
        case (False, False):
            return False
    
    # or in a simple way

    # if touching_power_pellet or touching_dot is True:
    #     return True
    # else: 
    #     return False

print('Pacman scores?', score(True, True))
print('\n')
print('Pacman scores?', score(True, False))
print('\n')
print('Pacman scores?', score(False, True))
print('\n')
print('Pacman scores?', score(False, False))
print('-'*30)


# Verify if Pacman loses
def lose(power_pellet_active, touching_ghost):
    
    if power_pellet_active is False and touching_ghost is True:
        return True
    
    return False
    
print('Pacman loses?', lose(True, True))
print('\n')
print('Pacman loses?', lose(True, False))
print('\n')
print('Pacman loses?', lose(False, True))
print('\n')
print('Pacman loses?', lose(False, False))
print('-'*30)


# Verify if Pacman wins
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):

    # this part first because even if Pacman eats all dots, if he touches a ghost he loses
    if touching_ghost is True and not power_pellet_active:
        return False
    
    if has_eaten_all_dots is True:
        return True
    
    return False
    
    # without else to be more clean
    
print('Pacman wins?', win(True, True, False))
print('\n')
print('Pacman wins?', win(True, False, True))
print('\n')
print('Pacman wins?', win(False, True, True))
print('\n')
print('Pacman wins?', win(False, True, False))
print('\n')
print('Pacman wins?', win(False, False, False))
print('\n')
print('Pacman wins?', win(True, True, True))


    
