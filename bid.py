def find_assignable_players(players, current_preference_level):
    # format [ (player) ]
    assignable_players = []
    msg = ""
    for player in players:
        if player.win_preference(current_preference_level, players):
            msg += "{} wins {}, preference={}, bid ={}\n" \
                .format(player.name,
                        player.bids[current_preference_level - 1][0].upper(),
                        current_preference_level,
                        player.bids[current_preference_level - 1][1])
            assignable_players.append(player)

    if len(assignable_players) == 0:
        msg = "No assignable faction at preference {}\n".format(current_preference_level)
    return assignable_players, msg


def find_tie_players(players, current_preference_level):
    # format [ [player, player, ...], []  ]
    tie_players = []
    msg = ""
    for i in range(0, len(players) - 1):
        if not players[i].win_or_tie_preference(current_preference_level, players):
            continue
        tie_group = [players[i]]
        for j in range(i + 1, len(players)):
            if players[i].tie_preference(current_preference_level, players[j]):
                tie_group.append(players[j])
        if len(tie_group) > 1:
            msg += "players {} tie on {}, preference={}, bid ={}\n" \
                .format(",".join([p.name for p in tie_group]),
                        tie_group[0].bids[current_preference_level - 1][0].upper(),
                        current_preference_level,
                        tie_group[0].bids[current_preference_level - 1][1])
            tie_players.append(tie_group)

    if len(tie_players) == 0:
        msg = "No tie faction at preference {}\n".format(current_preference_level)
    return tie_players, msg


# return (position of winner in tie group, extra bid paid)
def rebid(tie_group, current_preference_level):
    msg = "Rebidding on {}, pref_level: {}, cur_bid: {}, players: {}" \
        .format(tie_group[0].bids[current_preference_level-1][0].upper(),
                current_preference_level,
                tie_group[0].bids[current_preference_level-1][1],
                ",".join(p.name for p in tie_group))

    print (msg)
    bid_msg = "Enter winner index, "
    for i in range(0, len(tie_group)):
        bid_msg += "{} ({}), ".format(tie_group[i].name, i)
    winner_index = int(raw_input(bid_msg))
    winner_bid = input("Enter top-up bid ")
    return winner_index, winner_bid, msg
