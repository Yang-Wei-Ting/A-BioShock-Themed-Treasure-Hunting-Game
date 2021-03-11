from textwrap import dedent
from .cipher import decrypt
from .layouts import (
    YELLOW,
    RED,
    CYAN,
    END_COLOR,
    CLEAR_SCREEN,
    print_input,
)


def intro():
    skip_intro_ans = input("Skip intro? (y/n) ")
    if skip_intro_ans != "y":
        print_input(f"{CLEAR_SCREEN}Winter 1959, somewhere on the Atlantic ocean.")
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
        print_input("You:         Guess I am on my own now.")
    print(CLEAR_SCREEN, end="")


def bad_guy_is_coming():
    print(dedent(f'''\
        {RED}A bad guy from the far north is coming to look for the treasure.
        Do not let him have his way.
        By the way, if I were you, I would stay away from him.
        Why? Because he's armed to the teeth and he looks unhappy...
    '''))


def ending():
    print_input(f"{CLEAR_SCREEN}{CYAN}Congratulations! You found it!")
    print_input(decrypt("\033[2MLqvlgh wkh wuhdvxuh fkhvw lv d nhb dqg d slhfh ri sdshu, zklfk uhdgv:"))
    print_input(dedent(f'''\
         ----------------------------------------------------------------
        │                                                              │
        │ {decrypt("Brx kdyh frpsohwhg brxu iluvw plvvlrq dqg suryhq brxu zruwk.")} │
        │                                                              │
        │ {decrypt("Wkhuh'v d oljkwkrxvh")} at 63° 2' N, 29° 55' W.                 │
        │                                                              │
        │ {YELLOW}{decrypt("Zrxog brx nlqgob")}{END_COLOR} {decrypt("eulqj wkh nhb zlwk brx dqg jr wkhuh?")}        │
        │                                                              │
        │ {decrypt("Zh vkdoo phhw djdlq vrrq.")}                                    │
        │                                                    {YELLOW}{decrypt("U. Oxwhfh")}{END_COLOR} │
         ----------------------------------------------------------------\
    '''))
    print_input(dedent(decrypt('''\
        Vxgghqob brx vwduw wr iroorz wkh gluhfwlrq, dv li vrph vxshuqdwxudo irufh\n
        pdgh brx gr vr. Brx zdqw wr vwrs exw wkhq brx uhdolch wkdw qrz brx\n
        FDQQRW FRQWURO BRXUVHOI!\
    ''')))
    print_input(decrypt("Wkhuhiruh, d qhz mrxuqhb ehjlqv..."))
    print_input("That's the ending for Part I.")
    print_input(f"{CYAN}YOU WON!")
    print_input(dedent(decrypt('''\
        \033[2MQrz, suhvv hqwhu wr vkrz vsrlohuv iru ElrVkrfn, wkh ylghr jdph iudqfklvh,\n
        wkdw wkh sorw ri wklv vpdoo jdph wrrn vrph uhihuhqfhv iurp.\n
        \033[1;33pZduqlqj! Wkh iroorzlqj sdudjudskv frqwdlq kxjh vsrlohuv iru ElrVkrfn 1 dqg\n
        plog vsrlohuv iru ElrVkrfn Lqilqlwh.\
    ''')))
    print_input(dedent(decrypt('''\
        \033[2M\033[1;33pZrxog Brx Nlqgob?\033[0p\n
        Lq ElrVkrfn 1, Mdfn, wkh surwdjrqlvw, zdv jhqhwlfdoob prglilhg eb Bl Vxfkrqj\n
        wkdw kh zrxog rehb hyhub rughu frqwdlqlqj wkh skudvh "zrxog brx nlqgob?".\
    ''')))
    print_input(dedent(decrypt('''\
        \033[2M\033[1;33pErrnhu Fdwfk!\033[0p\n
        Lq ElrVkrfn Lqilqlwh, zkhq brx, Errnhu Ghzlww, uxq rxw ri dppr ru duh derxw wr\n
        glh, Holcdehwk, brxu ehvw vlghnlfn, riwhq wkurzv hlwkhu d phglfdo nlw, d vdow\n
        erwwoh, ru vrph dppr wr brx dqg bhoov "Errnhu fdwfk!".\n\n
        Brx fdq lqsxw \033[1;36pErrnhu\033[0p dqg \033[1;36pFdwfk!\033[0p wr \033[1;36pkhdo brxuvhoi\033[0p lq wklv jdph.\
    ''')))
    print_input(dedent(decrypt('''\
        \033[2M\033[1;33pWhduv\033[0p\n
        Lq ElrVkrfn Lqilqlwh, Holcdehwk fdq rshq whduv, sruwdov wkurxjk wlph dqg vsdfh.\n\n
        Brx fdq xvh \033[1;36pD\033[0p dqg \033[1;36pWhdu!\033[0p wr \033[1;36puhvhw wlph wr gdb 1\033[0p lq wklv jdph.\
    ''')))
    print_input(dedent(decrypt('''\
        \033[2M\033[1;33pOljkwkrxvhv\033[0p\n
        Oljkwkrxvhv lq ElrVkrfn vhuyh dv grruv wr rwkhu uhdolwlhv.\n
        Wkhuh'v dozdbv d oljkwkrxvh, wkhuh'v dozdbv d pdq, dqg wkhuh'v dozdbv d flwb.\n
                             - Holcdehwk gxulqj Wkh Vhd ri Grruv lq ElrVkrfn Lqilqlwh\n\n
        Brx fdq xvh \033[1;36pOljkw\033[0p dqg \033[1;36pKrxvh\033[0p wr \033[1;36porfdwh wkh wuhdvxuh\033[0p lq wklv jdph.\
    ''')))
    print(f"{CLEAR_SCREEN}That's it.\n\nHope you enjoy my crazy creation.\n\nThanks for playing!\n")
