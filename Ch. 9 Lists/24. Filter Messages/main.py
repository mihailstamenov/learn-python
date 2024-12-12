def filter_messages(messages):
    clean_messages = []
    dangs = []
    for msg in messages:
        counter = 0
        filtered_arr = []
        arr = msg.split()
        for word in arr:
            if word == "dang":
                counter += 1
            else:
                filtered_arr.append(word)
        clean_messages.append(" ".join(filtered_arr))
        dangs.append(counter)
    return clean_messages, dangs
#     pass


# messages = ["That's the bloody dang Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a dang razor!"]
# messages = ["dang it bobby!", "look at it go"]
# messages =  [
#             "well dang it",
#             "dang the whole dang thing",
#             "kill that knight, dang it",
#             "get him!",
#             "donkey kong",
#             "oh come on, get them",
#             "run away from the dang baddies",
#         ]

# clean_messages = []
# dangs = []

# for msg in messages:
#     counter = 0
#     filtered_arr = []
#     arr = msg.split()
#     for word in arr:
#         if word == "dang":
#             counter += 1
#         else:
#             filtered_arr.append(word)
    
#     clean_messages.append(" ".join(filtered_arr))
#     dangs.append(counter)


# print(clean_messages, dangs)

