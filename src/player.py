# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    # constructor
    def __init__(self, name, location, items = []):
        self.name = name
        self.location = location
        self.items = items
    # default representation
    def __repr__(self):
        return(f'Player is currently at the following location: {self.location}')
    