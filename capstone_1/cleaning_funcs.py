def tup_list_maker(tup_list):
    """
    Takes a list of tuples with index 0 being the text_id and index 1 being a 
    list of sentences and broadcasts the text_id to each sentence
    """
    final_list = []
    for item in tup_list:
        index = item[0]
        sentences = item[1]
        for sentence in sentences:
            pair = (index, sentence)
            final_list.append(pair)
    return final_list


def is_summary(number):
    """
    Takes a number as input
    Identifies a sentence as part of the summery or not
    """
    if number != 0:
        return 'yes'
    else:
        return 'no'


def is_sentence(sentence):
    """
    Evaluates if the input is a sentence (more than one word) 
    """
    return len(sentence.split(' ')) > 1


def clean_n_char(sentence):
    """
    Deletes the '\n' character at the begining of some sentences
    """
    word_list = sentence.split(' ')
    first_word = word_list[0]
    if first_word[:1] == '\n':
        return sentence[1:]
    else:
        return sentence
