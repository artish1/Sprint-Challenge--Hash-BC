#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Insert weights into hash table
    # the weight amount is the key, the index is the value for later referencing
    for i in range(0, len(weights)):
        hash_table_insert(ht, weights[i], i)

    for index in range(0, len(weights)):
        # Find the difference
        difference = limit - weights[index]

        # Is there the same difference in our table?
        difference_tabled = hash_table_retrieve(ht, difference)
        if difference_tabled is not None:
            # find the bigger index
            if difference_tabled > index:
                return (difference_tabled, index)
            else:
                return (index, difference_tabled)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
