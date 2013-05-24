import MapReduce
import json
import sys

# Map function
# mr - MapReduce object
# data - json object formatted as a string
mr = MapReduce.MapReduce()
def mapper(data):

    person = data[0]
    friend = data[1]
    mr.emit_intermediate(person, friend)
    mr.emit_intermediate(friend, person)


# Reduce function
# mr - MapReduce object
# key - key generated from map phse, associated to list_of_values
# list_of_values - values generated from map phase, associated to key
def reducer(person, friends):

    # output item (only for reducer)
    for f in friends:
        if friends.count(f) == 1:
            mr.emit((person, f))

def main():
    # Assumes first argument is a file of json objects formatted as strings, 
    #one per line.
    mr.execute(open(sys.argv[1]), mapper, reducer)

if __name__ == '__main__':
    main()
