people = 30
cars = 40
trucks = 15


if cars > people:
    print "A kocsikat visszuk!!!"
elif cars < people:
    print "Nem kene kocsikat vinnunk"
else:
    print "Nem tudunk donteni..."

if trucks > cars:
    print "Tul sok a teherautp."
elif trucks < cars:
    print "VISSZUK A TEHERAUTOT."
else:
    print "Meg mindig nem tudunk donteni."

if people > trucks:
    print "Vigyuk a teherautokat."
else:
    print "INKABB MARADJUNK OTTHON ES KOCKULJUNK"