from sys import exit

def gold_room():
    print "Ez a szoba tele van arannyal! Mennyit viszel el?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Tanulj meg gepelni, te majom.")

    if how_much < 50:
        print "Lama..."
        exit(0)
    else:
        dead("Te telhetetlen leny!")


def bear_room():
    print "Itt van egy medve."
    print "A medvenek van egy rakat penze."
    print "A kover medve elallja az utat."
    print "Hogy viszed arrebb a medvet?"
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "elviszed a mezet":
            dead("A medve radnez es lepofozza az arcod a helyerol. lol")
        elif choice == "ingerled a medvet" and not bear_moved:
            print "A medve arrebbmegy, athaladsz az ajton."
            bear_moved = True
        elif choice == "ingerled a medvet" and bear_moved:
            dead("A medve merges lesz, es leharapja a labaidat.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "Nem tudom ez mi."


def cthulhu_room():
    print "Itt lathato a nagy es gonosz Chutulhu"
    print "O, vagy az, vagy valami radnez, es megbolondulsz tole."
    print "Imadkozol az eletedert, vagy megeszed a fejed? WAT"

    choice = raw_input("> ")

    if "imadkozol" in choice:
        start()
    elif "fej" in choice:
        dead("HAT ez igazan finom volt!")
    else:
        cthulhu_room()


def dead(why):
    print why, "SZEP MUNKA!!"
    exit(0)

def start():
    print "Egy sotet szobaban vagy."
    print "Mehetsz jobbra vagy balra."
    print "Merre mesz?"

    choice = raw_input("> ")

    if choice == "bal":
        bear_room()
    elif choice == "jobb":
        cthulhu_room()
    else:
        dead("A szobaban vergodsz amig ehen nem halsz. Imadom a happy endeket.")


start()