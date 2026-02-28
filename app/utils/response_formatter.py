# यह फाइल सुनिश्चित करती है कि शिव एआई बिना हकलाए बोले
import re

def clean_for_speech(text):
    # नंबरों को शब्दों में बदलने का शब्दकोश
    num_map = {
        '0': 'शून्य', '1': 'एक', '2': 'दो', '3': 'तीन', '4': 'चार',
        '5': 'पांच', '6': 'छह', '7': 'सात', '8': 'आठ', '9': 'नौ'
    }
    
    # अंकों को ढूंढना और बदलना
    for digit, word in num_map.items():
        text = text.replace(digit, word)
    
    # डॉट को कोमा में बदलना ताकि एआई रुके
    text = text.replace(".", ",")
    return text
  
