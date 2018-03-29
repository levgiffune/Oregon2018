"""
  ___                               _____          _ _ 
 / _ \ _ __ ___  __ _  ___  _ __   |_   _| __ __ _(_) |
| | | | '__/ _ \/ _` |/ _ \| '_ \    | || '__/ _` | | |
| |_| | | |  __/ (_| | (_) | | | |   | || | | (_| | | |
 \___/|_|  \___|\__, |\___/|_| |_|   |_||_|  \__,_|_|_|
                |___/        

MINNESOTA EDUCATIONAL COMPUTING CONSORTIUM STAFF
PROGRAMMING REVISIONS BY DON RAWITSCH - 1975
CURRENT VERSION - 3/27/75


Adapted to python by Lev Giffune - 2018

List of variables at end of file
"""

cashleft = 700
fortflag = -1
injuryflag = illnessflag = southpassflag = bluemountainsflag = totalmilage = southpassmilageflag = turnnumber = 0

def instructions():

    print "DO YOU NEED INSTRUCTIONS  (YES/NO)"

    answer = raw_input()
    
    if answer == "YES":
        print "THIS PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM"
        print "INDEPENDENCE, MISSOURI TO OREGON CITY, OREGON IN 1847."
        print "YOUR FAMILY OF FIVE WILL COVER THE 2000 MILE OREGON TRAIL"
        print "IN 5-6 MONTHS --- IF YOU MAKE IT ALIVE."
        print "\n"
        print "YOU HAD SAVED $900 TO SPEND FOR THE TRIP, AND YOU'VE JUST"
        print " PAID $200 FOR A WAGON."
        print "YOU WILL NEED TO SPEND THE REST OF YOUR MONEY ON THE"
        print " FOLLOWING ITEMS:"
        print "\n"
        print " OXEN - YOU CAN SPEND $200-$300 ON YOUR TEAM"
        print " THE MORE YOU SPEND, THE FASTER YOU'LL GO"
        print " BECAUSE YOU'LL HAVE BETTER ANIMALS"
        print "\n"
        print " FOOD - THE MORE YOU HAVE, THE LESS CHANCE THERE"
        print " IS OF GETTING SICK"
        print "\n"
        print " AMMUNITION - $1 BUYS A BELT OF 50 BULLETS"
        print " YOU WILL NEED BULLETS FOR ATTACKS BY ANIMALS"
        print " AND BANDITS, AND FOR HUNTING FOOD"
        print "\n"
        print " CLOTHING - THIS IS ESPECIALLY IMPORTANT FOR THE COLD"
        print " WEATHER YOU WILL ENCOUNTER WHEN CROSSING"
        print " THE MOUNTAINS"
        print "\n"
        print " MISCELLANEOUS SUPPLIES - THIS INCLUDES MEDICINE AND"
        print " OTHER THINGS YOU WILL NEED FOR SICKNESS"
        print " AND EMERGENCY REPAIRS"
        print "\n\n"
        print "YOU CAN SPEND ALL YOUR MONEY BEFORE YOU START YOUR TRIP -"
        print "OR YOU CAN SAVE SOME OF YOUR CASH TO SPEND AT FORTS ALONG"
        print "THE WAY WHEN YOU RUN LOW. HOWEVER, ITEMS COST MORE AT"
        print "THE FORTS. YOU CAN ALSO GO HUNTING ALONG THE WAY TO GET"
        print "MORE FOOD."
        print "WHENEVER YOU HAVE TO USE YOUR TRUSTY RIFLE ALONG THE WAY,"
        print "YOU WILL SEE THE WORDS: TYPE BANG. THE FASTER YOU TYPE"
        print "IN THE WORD 'BANG' AND HIT THE 'RETURN' KEY, THE BETTER"
        print "LUCK YOU'LL HAVE WITH YOUR GUN."
        print "\n"
        print "WHEN ASKED TO ENTER MONEY AMOUNTS, DON'T USE A '$'."
        print "\n"
        print "GOOD LUCK!!!"
    elif answer == "NO":
        pass
    else:
        instructions()

def askanimals():
    print "HOW MUCH DO YOU WANT TO SPEND ON YOUR OXEN TEAM"
    global animals
    animals = input()
    if animals < 200:
        print "NOT ENOUGH"
        askanimals()
    elif animals > 300:
        print "TOO MUCH"
        askanimals()

def askfood():
    print "HOW MUCH DO YOU WANT TO SPEND ON FOOD"
    global food
    food = input()
    if food >=0:
        pass
    else:
        print "IMPOSSIBLE"
        askfood()
        
def askammo():
    print "HOW MUCH DO YOU WANT TO SPEND ON AMMUNITION"
    global ammo
    ammo = input()
    if ammo >=0:
        pass
    else:
        print "IMPOSSIBLE"
        askammo()

def askclothing():
    print "HOW MUCH DO YOU WANT TO SPEND ON CLOTHING"
    global clothing
    clothing = input()
    if clothing >=0:
        pass
    else:
        print "IMPOSSIBLE"
        askclothing()
        
def askmisc():
    print "HOW MUCH DO YOU WANT TO SPEND ON MISCELANEOUS SUPPLIES"
    global misc
    misc = input()
    if misc >=0:
        pass
    else:
        print "IMPOSSIBLE"
        askmisc()

def purchases():
    print "\n\n"
    askanimals()
    askfood()
    askammo()
    askclothing()
    askmisc()
    global cashleft
    global ammo
    cashleft = cashleft - animals - food - ammo - clothing - misc
    if cashleft < 0:
        print "\n\n"
        print "YOU OVERSPENT--YOU ONLY HAD $700 TO SPEND.  BUY AGAIN"
        purchases()
    ammo = 50 * ammo
    print "AFTER ALL YOUR PURCHASES, YOU NOW HAVE", cashleft, "DOLLARS LEFT"
    print "\n"
    print "MONDAY MARCH 29 1847"
instructions()
purchases()


"""
A = AMOUNT SPENT ON ANIMALS
B = AMOUNT SPENT ON AMMUNITION
B1 = ACTUAL RESPONSE TIME FOR INPUTING 'BANG'
B2 = MAXIMUM RESPONSE TIME FOR INPUTING 'BANG'
C = AMOUNT SPENT ON CLOTHING
C1 = FLAG FOR INSUFFICIENT CLOTHING IN COLD WEATHER
CS = YES/NO RESPONSE TO QUESTIONS - note: this was C$ in the original program, but python doesn't like that so we use CS
D1 = COUNTER IN GENERATING EVENTS
D3 = TURN NUMBER FOR SETTING DATE
D4 = CURRENT DATE
E = CHOICE OF EATING
F = AMOUNT SPENT ON FOOD
F1 = FLAG FOR CLEARING SOUTH PASS
F2 = FLAG FOR CLEARING BLUE MOUNTAINS
F9 = FRACTION OF 2 WEEKS TRAVELED ON FINAL TURN
K8 = FLAG FOR INJURY
L1 = FLAG FOR BLIZZARD
M = TOTAL MILEAGE WHOLE TRIP
M1 = AMOUNT SPENT ON MISCELLANEOUS SUPPLIES
M2 = TOTAL MILEAGE UP THROUGH PREVIOUS TURN
M9 = FLAG FOR CLEARING SOUTH PASS IN SETTING MILEAGE
P = AMOUNT SPENT ON ITEMS AT FORT
R1 = RANDOM NUMBER IN CHOOSING EVENTS
S4 = FLAG FOR ILLNESS
S5 = 'HOSTILITY OF RIDERS' FACTOR
T = CASH LEFT OVER AFTER INITIAL PURCHASES
T1 = CHOICE OF TACTICS WHEN ATTACKED
X = CHOICE OF ACTION FOR EACH TURN
X1 = FLAG FOR FORT OPTION
"""