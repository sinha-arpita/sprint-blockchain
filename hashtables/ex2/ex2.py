#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):#given from line 9 to 17
    hashtable = HashTable(length)


    """
    YOUR CODE HERE
    
    
    """
    # each ticket has source and destination, we are inserting key as source and destination as value for each ticket in the hash
    for ticket in tickets:
        hash_table_insert(hashtable,ticket.source,ticket.destination)


        #in a simple hashtable h={}, h[ticket.source]=ticket.destination, making key  value pair
    route = []
    src="NONE"
    while hash_table_retrieve(hashtable,src) != "NONE":
        #in a simplehash it will be while hash[src]!="NONE"
        route.append(hash_table_retrieve(hashtable,src))#route.append(hash[src]
        src=hash_table_retrieve(hashtable,src)
        #in simple hash it will be src=hash[src]

    route.append("NONE")


    return route
