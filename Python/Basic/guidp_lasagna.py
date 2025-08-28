"""
Make functions to make a lasagna from a cookbook
Functions:
1. Bake time remaining
2. Preparation time
3. elapsed_time_in_minutes

"""

EXPECTED_BAKE_TIME = 40
print(EXPECTED_BAKE_TIME)
print('\n')

def bake_time_remaining(actual_bake_time):

    """
    Calculate the bake time remaining

    parameter actual_bake_time = int - a number that represent how long the lasagna was in the oven 
    return = int - bake time remaining

    This function take the actual_bake_time and use the constant to calculate this
    
    """

    time_remaining = EXPECTED_BAKE_TIME - actual_bake_time
    return time_remaining

print('Time remaining: ', bake_time_remaining(30))
print('-'*30)


def preparation_time_in_minutes(number_of_layers):

    """ 
    Calculate the preparation time
    
    parameter parameter number_of_layers = int - the number of layers in the lasagna
    return = int - time of the preparation
    
    This function returns takes one integer as a parameter 
    to calculate the preparation time of the lasagna based on the number of layers
    and each layer take 2 minutes to be prepared 
    
    """

    preparation_time = number_of_layers * 2
    return preparation_time

print('Preparation time in minutes: ', preparation_time_in_minutes(2))
print('-'*30)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """
    Calculate the elapsed cooking time

    parameter number_of_layers = int - the number of layers in the lasagna
    parameter elapsed_bake_time = int - elapsed cooking time
    return = int - total time elapsed (in minutes) preparing and cooking

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.

    """

    cooking_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return cooking_time
    # elapsed_bake_time = the number of minutes the lasagna has spent baking in the oven already
    # number_of_layers = the number of layers added to the lasagna

print('Time cooking: ', elapsed_time_in_minutes(3, 26))
print('-'*30)
