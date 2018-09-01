class Player:
    def __init__(self, name, bids):
        self.name = name
        # bids is an array. First elem == first pref.
        # each elem is a tuple (faction, bid)
        self.bids = bids
        self.faction = ""
        self.bid_paid = 0
        self.extra_bid_paid = 0
        # {faction -> extra bid}
        self.extra_bid = {}

    def print_player(self):
        print(self.name + "'s bid is as follow:")
        for i in range(0, len(self.bids)):
            print ("Pref %d - Faction: %s, Bid: %d" %
                   (i + 1, self.bids[i][0], self.bids[i][1]))

    def assign_preference(self, preference):
        self.faction = self.bids[preference - 1][0]
        if self.faction in self.extra_bid:
            self.extra_bid_paid = self.extra_bid[self.faction]
        self.bid_paid = self.bids[preference - 1][1]

    def remove_faction(self, faction):
        new_bids = []
        for bid in self.bids:
            if bid[0] != faction:
                new_bids.append(bid)
        self.bids = new_bids

    def is_assigned(self):
        return self.faction != ""

    def tie_preference(self, preference, player_b):
        if self.is_assigned() or player_b.is_assigned():
            return False
        return (self.bids[preference - 1][0] == player_b.bids[preference - 1][0] and
                self.bids[preference - 1][1] == player_b.bids[preference - 1][1])

    def win_preference(self, preference, players):
        if self.is_assigned():
            return False
        faction = self.bids[preference - 1][0]

        for playerB in players:
            if not self.win_faction_against(playerB, faction):
                return False
        return True

    # return True if this player win the faction against playerB
    def win_faction_against(self, player_b, faction):
        if player_b.name == self.name:
            return True
        if self.is_assigned():
            return False
        if player_b.is_assigned():
            return True
        A_bid, A_pref = self.get_bid_and_pref_by_faction(faction)
        B_bid, B_pref = player_b.get_bid_and_pref_by_faction(faction)

        # larger bid wins / or even bid and larger pref
        if (A_bid > B_bid) or (A_bid >= B_bid and A_pref < B_pref):
            return True
        # print ("{} lost {} against {} {}-{} / {}-{}".format(self.name, faction, player_b.name, A_bid, A_pref, B_bid, B_pref))
        return False

    def get_bid_and_pref_by_faction(self, faction):
        pref = 1
        for bid in self.bids:
            if bid[0] == faction:
                return bid[1], pref
            pref += 1
        return None
