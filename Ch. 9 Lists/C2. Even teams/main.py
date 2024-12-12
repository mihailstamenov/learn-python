def split_players_into_teams(players):
    # even_team, odd_team = players[0:len(players):2], players[1:len(players):2]
    even_team, odd_team = players[::2], players[1::2]
    return even_team, odd_team
    # print(even_team, odd_team)

# split_players_into_teams(        [
#             "Harry",
#             "Hermione",
#             "Ron",
#             "Ginny",
#             "Fred",
#             "Neville",
#             "Draco",
#             "Luna",
#             "Cho",
#             "Gregory",
#             "Lee",
#             "Michael",
#             "Lavender",
#             "Frank",
#             "Anthony",
#             "Allan",
#         ])