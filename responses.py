import random

R_EATING = "I don't like eating because I'm a bot!"

def unknown():
    response = ['Could you please re-phrase that?',
                '...',
                'Sorry, I didn\'t get that right.',
                'Couldn\'t understand, sorry!'][random.randrange(4)]
    return response 