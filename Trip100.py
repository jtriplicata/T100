


average = float(input("Enter the average for the season decimal first:  "))
if average > .300:
    score = 10
elif average > .290:
    score = 9
elif average > .285:
    score = 8
elif average > .280:
    score = 7
elif average > .275:
    score = 6
elif average > .260:
    score = 5
elif average > .250:
    score = 4
elif average > .235:
    score = 3
else:
    score = 1

print("The score for Average is", score)


obp = float(input("Enter the OBP for the season decimal first: "))
if obp > .400:
    score2 = 10
elif obp > .390:
    score2 = 9
elif obp > .385:
    score2 = 8
elif obp > .380:
    score2 = 7
elif obp > .365:
    score2 = 6
elif obp > .350:
    score2 = 5
elif obp > .335:
    score2 = 4
elif obp > .305:
    score2 = 3
else:
    score2 = 1

print("The score for On Base Percentage is", score2)

slg = float(input("Enter the SLG for the season decimal first: "))
if slg > .515:
    score4 = 10
elif slg > .505:
    score4 = 9
elif slg > .495:
    score4 = 8
elif slg > .470:
    score4 = 7
elif slg > .430:
    score4 = 6
elif slg > .420:
    score4 = 5
elif slg > .410:
    score4 = 4
elif slg > .405:
    score4 = 3
else:
    score4 = 1

print("The score for Slugging is", score4)

hr = float(input("Enter the number of homeruns hit in the season: "))
if hr > 40:
    score3 = 10
elif hr > 38:
    score3 = 9
elif hr > 35:
    score3 = 8
elif hr > 32:
    score3 = 7
elif hr > 28:
    score3 = 6
elif hr > 22:
    score3 = 5
elif hr > 15:
    score3 = 4
elif hr > 10:
    score3 = 3
else:
    score3 = 1

print("The score for Homeruns is", score3)

rbi = float(input("Enter the number of RBI for the season: "))
if rbi > 115:
    score5 = 10
elif rbi > 105:
    score5 = 9
elif rbi > 100:
    score5 = 8
elif rbi > 95:
    score5 = 7
elif rbi > 85:
    score5 = 6
elif rbi > 75:
    score5 = 5
elif rbi > 65:
    score5 = 4
elif rbi > 55:
    score5 = 3
else:
    score5 = 1

print("The score for Runs Batted In is", score5)

run = float(input("Enter the  number of runs for the season: "))
if run > 105:
    score6 = 10
elif run > 100:
    score6 = 9
elif run > 95:
    score6 = 8
elif run > 90:
    score6 = 7
elif run > 85:
    score6 = 6
elif run > 75:
    score6 = 5
elif run > 70:
    score6 = 4
elif run > 65:
    score6 = 3
else:
    score6 = 1

print("The score for Runs is", score6)


opsp = float(input("Enter the OPS+ for the season: "))
if opsp > 145:
    score7 = 10
elif opsp > 140:
    score7 = 9
elif opsp > 135:
    score7 = 8
elif opsp > 130:
    score7 = 7
elif opsp > 125:
    score7 = 6
elif opsp > 115:
    score7 = 5
elif opsp > 105:
    score7 = 4
elif opsp > 100:
    score7 = 3
else:
    score7 = 1

print("The score for OPS+ is", score7)


wrcp = float(input("Enter the WRC+ for the season: "))
if wrcp > 120:
    score8 = 10
elif wrcp > 115:
    score8 = 9
elif wrcp > 110:
    score8 = 8
elif wrcp > 105:
    score8 = 7
elif wrcp > 100:
    score8 = 6
elif wrcp > 95:
    score8 = 5
elif wrcp > 90:
    score8 = 4
elif wrcp > 80:
    score8 = 3
else:
    score8 = 1

print("The score for OPS+ is", score8)

owar = float(input("Enter the oWar for the season: "))
if  owar > 8:
    score9 = 10
elif owar > 7:
    score9 = 9
elif owar > 6:
    score9 = 8
elif owar > 5:
    score9 = 7
elif owar > 4:
    score9 = 6
elif owar > 3:
    score9 = 5
elif owar > 2:
    score9 = 4
elif owar > 1:
    score9 = 3
else:
    score9 = 1

print("The score for oWAR is", score9)

total_bases = float(input("Enter the number of total bases for the season: "))
if total_bases > 300:
    score10 = 10
elif total_bases > 290:
    score10 = 9
elif total_bases > 280:
    score10 = 8
elif total_bases > 270:
    score10 = 7
elif total_bases > 260:
    score10 = 6
elif total_bases > 250:
    score10 = 5
elif total_bases > 240:
    score10 = 4
elif total_bases > 200:
    score10 = 3
else:
    score10 = 1

print("The score for Total Bases is", score10)

trip100 = (score + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10)

print("")
print("Your Trip 100 total is: " + str(trip100))


