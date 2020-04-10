#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)
    # Insert Tickets
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Order tickets by hash source/destination
    curr_ticket = hash_table_retrieve(hashtable, "NONE")
    for i in range(0, len(tickets) - 1):
        route[i] = curr_ticket
        curr_ticket = hash_table_retrieve(hashtable, curr_ticket)

    # Print just because
    print(f"Route: {route}")
    return route
