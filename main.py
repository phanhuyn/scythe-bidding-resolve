#!python3
from bid import find_assignable_players, find_tie_players
from utils import load_bid_data, print_players

bidFile = "data/bid.csv"

players = load_bid_data(bidFile)
exported_report = ["Start bidding"]
cur_bids = print_players(players)
exported_report.append(cur_bids)
print(cur_bids)


while len(players[0].bids) > 0:
    current_preference_level = 1

    # 1.1. assignable players (no showdown)
    assignable_players, msg = find_assignable_players(players, current_preference_level)
    exported_report.append(msg)
    print(msg)

    if len(assignable_players) == 0:
        # 1.2. get tie player
        tie_players, msg = find_tie_players(players, current_preference_level)
        exported_report.append(msg)
        print(msg)

        if len(tie_players) > 0:
            print("unhandled tie")
            exit(1)
        else:
            current_preference_level += 1
            continue

    else:
        # assign faction to winners and remove assigned factions
        for winner in assignable_players:
            assigned_faction = winner.bids[current_preference_level - 1][0]
            winner.assign_preference(current_preference_level)
            for player in players:
                player.remove_faction(assigned_faction)

    cur_bids = print_players(players)
    print(cur_bids)
    exported_report.append(cur_bids)
