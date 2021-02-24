import itertools


day_count_iterator = itertools.count(1)

treasure_hint_far_away_tuple = (
    "There's nothing to be found here.",
    "Nothing special around here.",
    "I didn't find anything special.",
    "Better keep looking.",
    "It's not here.",
    "Hmm nothing.",
    "I wonder where it might be.",
    "Guess I have to check somewhere else.",
    "It must be somewhere, definitely not here though.",
)

treasure_hint_2_km_tuple = (
    "I think it's close!",
    "It's not far!",
)

treasure_hint_1_km_tuple = (
    "I can tell it's really close!",
    "Almost there!",
)

weapon_upgrade_msg_tuple = (
    "The bad guy had his weapon upgraded!",
    "The bad guy is getting stronger!",
)

get_shot_msg_iterator = itertools.cycle((
    "The bad guy is shooting me!",
    "OMG I'm bleeding...",
    "I am under attack!",
    "Ouch!",
    "That's really hurt!",
))

slightly_injured_msg_iterator = itertools.cycle((
    "I feel weak.",
    "It's cold.",
    "My legs are becoming heavy.",
))

severely_wounded_msg_iterator = itertools.cycle((
    "I am dying...",
    "Vision is getting darker...",
    "The only thing I can hear now is my own heartbeat...",
    "It's almost over...",
))

dead_hint_tuple = (
    "Hint: Draw it down on a piece of paper, move tactically, it will be easier.",
    "Hint: The bad guy will appear on day 5 and get stronger after day 10.",
    "Hint: The farthest distance the bad guy can move a day is 3√2 km.",
    "Hint: Note that your mobility drops if you are heavily injured.",
    "Don't give up. You can make it!",
)
