import re
import responses

def message_probability(user_message, recognized_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    #Calculates the percentage of recognized words in a user message
    percentage = float(message_certainty) / float(len(recognized_words))

    #Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #Response --------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'wazzup', 'sup', 'heyo'], single_response=True)
    response('I\'m doing fine!', ['how', 'are', 'you'], required_words=['how'])
    response('Thank you!', ['you', 'are', 'doing', 'great'], required_words=['doing', 'great'])
    response(responses.R_EATING, ['do', 'you', 'like', 'eating'], required_words=['eating', 'like'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)
    return responses.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#Test response system
while True:
    print('Bot: ' + get_response(input('You: ')))
