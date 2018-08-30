class Player:
    def __init__(self, name, bids):
        self.name = name
        # bids is an array. First elem == first pref.
        # each elem is a tuple (faction, bid)
        self.bids = bids
        self.faction = ""

    def print_player(self):
        print(self.name + "'s bid is as follow:")
        for i in range(0, len(self.bids)):
            print ("Pref %d - Faction: %s, Bid: %d" %
                   (i + 1, self.bids[i][0], self.bids[i][1]))

    def is_assigned(self):
        return self.faction != ""
