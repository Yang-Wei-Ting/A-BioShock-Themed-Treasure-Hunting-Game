'''© 2020 Wei-Ting Yang. All rights reserved.'''


import random, itertools, subprocess, sys, os
from modules import plots, classes, messages, gui


player = classes.Player(-5, -5)
treasure, *fruit_list = (classes.Item() for _ in range(31))
secret = classes.Cheat()


plots.print_decor("\n")
print(__doc__, "\n")
plots.intro()


while True:
    today = next(messages.day_count_iterator)
    print(f"Day {today}\n")

    # Introducing an antagonist on day 5.
    if today == 5:
        gui.add_bad_guy_boat()
        bad_guy = classes.BadGuy(5, 5)
        plots.bad_guy_is_coming()

    # On day 6 and afterwards, executing the bad guy's actions and checking
    # the player's health.
    elif today >= 6:
        if today >= 10 and today % 2 == 0:
            bad_guy.weapon_upgrade()
            print(random.choice(messages.weapon_upgrade_msg_tuple))

        bad_guy.random_move()
        print(f"The bad guy is now at {bad_guy}.")

        if bad_guy.distance_between(treasure) == 0:
            print("Nooo... The bad guy found the treasure.")
            if today <= 9:
                print("\nHe's just lucky. You can beat him next time.")
            plots.decor()
            break
        print()

        if bad_guy.distance_between(player) == 0:
            player.health -= bad_guy.weapon_damage + 2
            print(plots.YOU_SPEAK, "Ouch! The bad guy stabbed me...")
        elif 0 < bad_guy.distance_between(player) <= bad_guy.weapon_range:
            player.health -= bad_guy.weapon_damage
            print(plots.YOU_SPEAK, next(messages.get_shot_msg_iterator))

        if player.health <= 0:
            player.label.grid_remove()
            plots.print_decor("You are dead.")
            plots.print_decor(random.choice(messages.dead_hint_tuple))
            break
        if 0 < player.health < 5:
            print(f"{player.health} health point left.")
            if player.health < 2:
                player.mobility = 2
                print(plots.YOU_SPEAK, next(messages.severely_wounded_msg_iterator), "\n")
            elif 2 <= player.health < 4:
                player.mobility = 3
                print(plots.YOU_SPEAK, next(messages.slightly_injured_msg_iterator), "\n")
            else:
                player.mobility = 3
                print()
        else:
            player.mobility = 3

    print(plots.YOU_SPEAK, f"I am at {player}.")

    # Checking the distance between the player and the treasure.
    if player.distance_between(treasure) == 0:
        plots.ending()
        break
    if player.distance_between(treasure) == 1:
        print(plots.YOU_SPEAK, random.choice(messages.treasure_hint_1_km_tuple))
    elif 1 < player.distance_between(treasure) <= 2:
        print(plots.YOU_SPEAK, random.choice(messages.treasure_hint_2_km_tuple))
    else:
        print(plots.YOU_SPEAK, random.choice(messages.treasure_hint_far_away_tuple))

    # Taking player inputs.
    player_mobility_range = "-{0} to {0}".format(player.mobility)
    print()
    player_input = (
        input(f"Movement in x = ? ({player_mobility_range}) "),
        input(f"Movement in y = ? ({player_mobility_range}) ")
    )
    print()

    # Checking if the correct cheat codes were entered.
    if player_input == secret.code_1:
        player.health, player.mobility = 5, 3
        print(plots.YOU_SPEAK, "I am fully healed!")
        plots.print_decor(plots.YOU_SPEAK, random.choice((
            "Much obliged!",
            "Great!",
            "Perfect timing!",
            "Thanks!",
        )))
        continue
    if player_input == secret.code_2:
        messages.day_count_iterator = itertools.count(1)
        try:
            gui.remove_label(bad_guy)
        except NameError:
            pass
        gui.add_landscape(gui.water_ne, 0, 12)
        plots.print_decor(plots.YOU_SPEAK, "What... What had just happened?")
        continue
    if player_input == secret.code_3:
        plots.print_decor(f"You're at {player}. The treasure is located at {treasure}.")
        continue

    # Dealing with strange inputs or moving the player.
    try:
        input_1, input_2 = int(player_input[0]), int(player_input[1])
    except ValueError:
        plots.print_decor(plots.YOU_SPEAK, f"I should enter integers. I'm still at {player}.")
        continue
    if abs(input_1) > player.mobility or abs(input_2) > player.mobility:
        plots.print_decor(plots.YOU_SPEAK, f"I should enter {player_mobility_range} only.",
            f"I'm still at {player}.")
        continue
    player.move(input_1, input_2)
    print(plots.YOU_SPEAK, f"I am now at {player}.")

    # Checking if the player is drowned.
    if player.is_drowned():
        player.label.grid_remove()
        plots.print_decor("You are drowned...")
        plots.print_decor("Hint: You cannot move outside the boundary.")
        break

    # Offering chances for the player to heal.
    for fruit in fruit_list:
        if player.distance_between(fruit) == 0:
            print(plots.YOU_SPEAK, "There is an apple tree.")
            if player.health <= 4.5:
                player.health += 0.5
                fruit_list.remove(fruit)
                print(plots.YOU_SPEAK, random.choice((
                    "Apples tasted good.",
                    "I like to eat apples.",
                )))
            break
    plots.decor()


while True:
    restart_ans = input("Restart? (y/n) ")
    if restart_ans == "y":
        gui.window.destroy()
        subprocess.Popen([sys.executable, os.path.realpath(sys.argv[0])])
        break
    if restart_ans == "n":
        gui.window.destroy()
        break


gui.window.mainloop()
