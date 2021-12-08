print('''
  _____
                           )   (
                          / oOo \
                         /_______\
                         L       A
                         E  .-.  M
                         S  |~|  C
 I-I-I-I-I-I-I-I-I-I-I-I-T  |_|  |I-I-I-I-I-I-I-I-I-I-I-I-I
 ).**.(~~~~~~~~~~~~~~~~~~E       |~~~~~~~~~~~~~~~~~~~).**.(
/ |  | \                 R       |                  / |  | \
) |__| (                _|_.---._|_                 ) |__| (
|______|_________________|' .-. '|__________________|______|
|      |  .-.  .-.       |,-|~|-,|        .-.  .-.  |      |
\ .    /  |~|  |~|       || | | ||        |~|  |~|  \    . /
 )H   (   |_|  |_|       ||_|_|_||        |_|  |_|   )   H(
 |    |                  |       |                   |    |
 |    |                  |       |                   |    |
 \    /   ...  ...       |_.=~=._|        ...  ...   \    /
  ). (    |~|  |~|       |I|   |I|        |~|  |~|    ) .(
  |H |    |_|  |_|       |I|  .|I|        |_|  |_|    | H|
  |  |                   |I|___|I|                    |  |
  '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
''')
print("Welcome to SURVIVAL GAME.")
print("Your mission is to survive.") 


no1 = input('You got lost while you went trekking with your friends.It stareted raining and you saw a mansion up in the hills. Do you want to wait in the rain for rescue or take shelter in the mansion? \nType "Wait" or "shelter": ')
no1 = no1.lower()
if no1=="shelter":
  print("You have entered the mansion.  ")
  
  no2 = input('You observed that the mansion had all the things and it looked like a person lived there. Do you want to look for some clothes to wear or sit near the fireplace?\nType "clothes" or "fireplace": ')
  no2 = no2.lower()
  if no2 =="clothes":
    print("You went upstairs.")
    
    no3 = input('You saw three doors with different colours. "RED", "YELLOW" and "GREEN".\nType which colored door you want to open: ')
    no3 = no3.lower()
    if no3 == "red":
      print("Good Choice. You found the clothes.YOU SURVIVED!!")
    elif no3 == "yellow" and no3 == "green":
      print("You/'ve opened a door full of snakes. The snakes bit you and you died. BAM! GAME OVER!!'")
  else:
    print("You lighted the firewoods and fell asleep without opening any of the windows. So you died by inhaling carbon monoxide. GAME OVER!!")
else:
  print("The rescue team did not come and you died of hypothermia. GAME OVER!!")



