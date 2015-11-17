print "Belepsz egy szobaba, amiben 2 ajto van, az 1-es vagy a 2-es ajton haladsz at?"

door = raw_input("> ")

if door == "1":
    print "Egy hatalmas medve eppen tortat eszik lel."
    print "1. ELVISZED A TORTAT"
    print "2. A medvere orditasz."

    bear = raw_input("> ")

    if bear == "1":
        print "A medve megeszi az arcodat. Szep munka!"
    elif bear == "2":
        print "A medve leragja a labaidat. Szep munka!"
    else:
        print "Hat talan jobb %s . A medve elszalad." % bear

elif door == "2":
    print "Chutulhu szemeben levo vegtelen urbe tekintesz."
    print "1. Afonya"
    print "2. Sarga kabatos MI."
    print "3. Ki az a mosomedve?"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "A szent pudingnak koszonhetoen tulelted az esetet!"
    else:
        print "MEGHALTAL."

else:
    print "Elbotlasz, beleesel a kesedbe es meghalsz, szep munka!"