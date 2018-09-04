import csv

from consts import preferenceOrderBidFile
from player import Player


def load_bid_data(bidFile):
    players = []
    with open(bidFile, 'rt') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        # header = True
        for row in reader:
            # if header:
            #     header = False
            #     continue
            players.append(parse_one_player(row))
    return players


def parse_one_player(row):
    bids = [None] * 7
    for i in range(1, 8):
        faction = preferenceOrderBidFile[i - 1]
        pref = int(row[i])
        bid = int(row[i + 7])
        bids[pref - 1] = (faction, bid)
    p = Player(row[0], bids)
    return p


def print_players(players):
    to_print = []

    # print assigned player
    for player in players:
        if player.is_assigned():
            to_print.append("{} is assigned with {}, bid {}, extra bid {}"
                            .format(player.name, player.faction.upper(), player.bid_paid, player.extra_bid_paid))

    # print name
    names = "|{:^15}|".format("pref/name")
    for player in players:
        if not player.is_assigned():
            names += "{:^15}|".format(player.name)
    to_print.append(names)

    # print bid
    for pref in range(0, len(players[0].bids)):
        bidOfPref = "|{:^15}|".format(pref+1)
        for player in players:
            if not player.is_assigned():
                bidOfPref += "{:^10}-{:^4}|".format(player.bids[pref][0], player.bids[pref][1])
        to_print.append(bidOfPref)

    return "\n".join(to_print)
