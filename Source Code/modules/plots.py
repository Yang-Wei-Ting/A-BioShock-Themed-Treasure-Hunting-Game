from textwrap import dedent
from .cipher import decrypt


# Layouts
def decor():
    print("-" * 79)


def print_decor(*args):
    print(*args)
    decor()


def print_input(*args):
    print(*args)
    input()


YOU_SPEAK = "You:        "


# Plots
def intro():
    decor()
    skip_intro_ans = input("Skip intro? (y/n) ")
    if skip_intro_ans != "y":
        print_decor()
        print_input("Winter 1959, somewhere on the Atlantic ocean.")
        print_input("Gentleman:   Are you going to just sit there again?")
        print_input("Lady:        Yep, as I don't have any interest in rowing.")
        print_input("You groaned as you regained consciousness.")
        print_input("Gentleman:   He's finally awake.")
        print_input("The lady passed you a map. You read it.")
        print_input(dedent('''\
             -----------------------------------------------------------
            │ The island is square-shaped.                            │
            │ Its four corners are the four coordinates shown below.  │
            │                                                         │
            │           y (km)                                        │
            │ (-5, 5)   ^         (5, 5)                              │
            │ .         .         .                                   │
            │           .                                             │
            │           .                                             │
            │           .                                             │
            │           .                                             │
            │ . . . . . . . . . . . > x (km)                          │
            │           .                                             │
            │           .                                             │
            │           .                                             │
            │           .                                             │
            │ .         .         .                                   │
            │ (-5, -5)            (5, -5)                             │
            │                                                         │
            │ (-5, -5) will be the place we ashore.                   │
             -----------------------------------------------------------\
        '''))
        print_input("You:         Err... Excuse me. What exactly are we looking for?")
        print_input("Lady:        A treasure hidden on this island, of course.")
        print_input("Gentleman:   Can we get back to the rowing?")
        print_input("Lady:        I suggest you do because he DOESN'T ROW, either.")
        print_input("Gentleman:   ...")
        print_input("A while later...")
        print_input("Lady:        We've arrived.")
        print_input("You landed on the shore.")
        print_input("Gentleman:   It's quite an easy task.")
        print_input("Lady:        We will leave the boat here...")
        print_input("Gentleman:   As you might need it later.")
        print_input("You:         But how do I...")
        print_input("You turned around, but they were gone.")
        print_input("You:         Wha...?")
        print("You:         Guess I am on my own now.")
    print()
    decor()


def bad_guy_is_coming():
    print(dedent('''\
        A bad guy from the far north is coming to look for the treasure.
        Do not let him have his way.
        By the way, if I were you, I would stay away from him.
        Why? Because he's armed to the teeth and he looks unhappy...\n\
    '''))


def ending():
    print_decor("Congratulations! You found it!")
    print_input(decrypt("Lqvlgh wkh wuhdvxuh fkhvw lv d nhb dqg d slhfh ri sdshu, zklfk uhdgv:"))
    print_input(dedent(f'''\
         ----------------------------------------------------------------
        │                                                              │
        │ {decrypt("Brx kdyh frpsohwhg brxu iluvw plvvlrq dqg suryhq brxu zruwk.")} │
        │                                                              │
        │ {decrypt("Wkhuh'v d oljkwkrxvh")} at 63° 2' N, 29° 55' W.                 │
        │                                                              │
        │ {decrypt("Zrxog brx nlqgob eulqj wkh nhb zlwk brx dqg jr wkhuh?")}        │
        │                                                              │
        │ {decrypt("Zh vkdoo phhw djdlq vrrq.")}                                    │
        │                                                        {decrypt("U. O.")} │
         ----------------------------------------------------------------\
    '''))
    print_input(dedent(decrypt('''\
        Vxgghqob brx vwduw wr iroorz wkh gluhfwlrq, dv li vrph vxshuqdwxudo irufh
        pdgh brx gr vr. Brx zdqw wr vwrs exw wkhq brx uhdolch wkdw qrz brx
        FDQQRW FRQWURO BRXUVHOI!\
    ''')))
    print_input(decrypt("Wkhuhiruh, d qhz mrxuqhb ehjlqv..."))
    print(dedent('''\
        That's the ending for Part I.\n
        YOU WON!\
    '''))
    decor()
    input(dedent(decrypt('''\
        Qrz, suhvv hqwhu wr vkrz vsrlohuv iru ElrVkrfn, wkh ylghr jdph iudqfklvh,
        wkdw wkh sorw ri wklv vpdoo jdph wrrn vrph uhihuhqfhv iurp.

        (Wkh iroorzlqj sdudjudskv frqwdlq kxjh vsrlohuv iru ElrVkrfn 1, plog
        vsrlohuv iru ElrVkrfn Lqilqlwh, qr vsrlohuv iru ElrVkrfn 2)
    ''')))
    decor()
    input(dedent(decrypt('''\
        { Zrxog Brx Nlqgob? }

        Lq ElrVkrfn 1, Mdfn, wkh surwdjrqlvw, zdv jhqhwlfdoob prglilhg eb Bl Vxfkrqj
        wkdw kh zrxog rehb hyhub rughu frqwdlqlqj wkh skudvh "zrxog brx nlqgob?".
    ''')))
    decor()
    input(dedent(decrypt('''\
        { Errnhu Fdwfk! }

        Lq ElrVkrfn Lqilqlwh, zkhq brx, Errnhu Ghzlww, uxq rxw ri dppr ru duh derxw wr
        glh, Holcdehwk, brxu ehvw vlghnlfn, riwhq wkurzv hlwkhu d phglfdo nlw, d vdow
        erwwoh, ru vrph dppr wr brx dqg bhoov "Errnhu fdwfk!".

        Brx fdq lqsxw "Errnhu" dqg "Fdwfk!" wr khdo brxuvhoi lq wklv jdph.
    ''')))
    decor()
    input(dedent(decrypt('''\
        { Whduv }

        Lq ElrVkrfn Lqilqlwh, Holcdehwk fdq rshq whduv, sruwdov wkurxjk wlph dqg vsdfh.

        Brx fdq xvh "D" dqg "Whdu!" wr uhvhw wlph wr gdb 1 lq wklv jdph.
    ''')))
    decor()
    print_decor(dedent(decrypt('''\
        { Oljkwkrxvhv }

        Oljkwkrxvhv lq ElrVkrfn vhuyh dv grruv wr rwkhu uhdolwlhv.
        "Wkhuh'v dozdbv d oljkwkrxvh, wkhuh'v dozdbv d pdq, dqg wkhuh'v dozdbv d flwb."
                               - Holcdehwk gxulqj Wkh Vhd ri Grruv lq ElrVkrfn Lqilqlwh

        Brx fdq xvh "Oljkw" dqg "Krxvh" wr orfdwh wkh wuhdvxuh lq wklv jdph.
    ''')))
    print("That's it. Hope you enjoy my crazy creation. Thanks for playing!\n")
