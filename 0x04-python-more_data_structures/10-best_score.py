#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        if a_dictionary == {}:
            return None
        else:
            h_key = None
            for k in a_dictionary:
                if h_key == None:
                    h_key = k
                else:
                    if a_dictionary[k] > a_dictionary[h_key]:
                        h_key = k
            return h_key
