#!python3

from utils import load_bid_data, print_players

bidFile = "data/bid.csv"

players = load_bid_data(bidFile)
print(print_players(players))
