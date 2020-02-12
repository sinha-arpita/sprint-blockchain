#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)#given already

    """
    YOUR CODE HERE
    """
    #print("here",weights, length, limit)
    #weights is an array of weights;get index of the pair.... that will be limit-weight we arev looping through, so if 16 is limit and first weight in array is 5 then 16-5=8 ,
    # e have to look for 8 if its there then index of 8
    for i in range(length):
        index= hash_table_retrieve(ht, (limit-weights[i]))
        print("i am index",index)
        if index != None:
            return((i,index))
        hash_table_insert(ht,weights[i],i)
        print("WEIGHT AND INDEX are respectively",weights[i],i)


    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
