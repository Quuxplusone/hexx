
Hexx: Heresy of the Wizard
==========================

Key Loss Bug
------------

If you are playing in DOSBox: Every time you change vertical levels, every pile of common keys
in every character's inventory will drop to size 1! Also, all common keys will vanish from the shops,
and any common keys dropped on the ground will vanish as well. This can easily make the game unwinnable!
Before descending or ascending stairs, or jumping into pits, take precautions to avoid key loss.

- You can "pick up" a pile of keys (up to 99 keys) and hold it in your mouse cursor as you make the transition.
  Keys held in the cursor will not be lost.
- You can store your keys in a backpack. Keys held in a backpack will not be lost.
- You could also "work around it" by carrying many piles of 1 key each; but this gives you a maximum of 40 common keys, which is not nearly enough to finish the game.

Before the first time you go downstairs, visit a shop and buy 99 common keys. Hold them in your cursor
every time you go up or down levels. Do this until you find your first backpack; then put your keys
in your backpack.

You can also use `python savegame.py --gain-common-keys HEXX1.SAV` to gain back keys if you've
managed to lose them by accident.


Cutscene Bug
------------

Picking up the talisman of a god triggers a cutscene. If you are playing
in DOSBox, this won't work and the game will just hang with a black screen.


Anti-piracy validation
----------------------

Placing the talisman of a god into its appropriate receptacle triggers an anti-piracy screen.
To answer the question(s) on this screen, you'll need the manual, which is available as
`hexx-manual.pdf` in this directory.

Combat
------

Put your best weapon in your left hand. This is counterintuitive, but the left-hand weapon seems to be the primary one.
You can attack (both melee and ranged/spell) through the diagonal gap between pillars, even though you cannot pass through that gap.
Beware: monsters can also attack (ranged, and with a great deal of difficulty) through the same gaps.


Experience Levels
-----------------

Sleep in a bed to level up at your first convenience after passing 2000 XP, 6000 XP, and so on.
The walkthrough will indicate when this happens during a normal playthrough.
Each monster grants an equal (and randomized per-death) amount of XP for *each* character who views its death.
Save-scumming for the best XP drops *is* possible.
Killing off characters will *not* cause the surviving characters to earn XP faster.
If nobody ever dies (which is quite possible), then all the characters' XP will remain in lockstep forever.

The following table comes from the manual.

Level    |       XP
-------------------
Level 1  |  (start)
Level 2  |     2000
Level 3  |     6000
Level 4  |    12000
Level 5  |    25000
Level 6  |    40000
Level 7  |    60000
Level 8  |    80000
Level 9  |   110000
Level 10 |   140000
Level 11 |   170000
Level 12 |   200000
Level 13 |   230000
Level 14 |   270000
Level 15 |   310000


Spell Prices
------------

This comes partly from the manual (spell names and schools) and partly from experimentation (prices).

### Green Spells (Earth Magic)
- Armour (100 GP)
- Healing (200 GP)
- Paralyse (200 GP)
- Levitate (300 GP)
- Warpower (400 GP)
- Arc Bolt (400 GP)
- Renew (400 GP)
- Formwall

### Yellow Spells (Chaos Magic)
- Deflect (100 GP)
- Terror (100 GP)
- Antimage (300 GP)
- Regen (400 GP)
- Ethblade (400 GP)
- Spelltap (500 GP)
- Vivify (800 GP)
- Disrupt (700 GP)

### Red Spells (Dragon Magic)
- Missile (100 GP)
- Torch (200 GP)
- Fireward (200 GP)
- Dispell (300 GP)
- Fireball (300 GP)
- Firepath
- Recharge (500 GP)
- Inferno (700 GP)

### Purple Spells (Night Magic)
- Confuse (100 GP)
- Phaze (200 GP)
- Suspend (200 GP)
- Trueview (300 GP)
- Wizeye (300 GP)
- Mindrock (400 GP)
- Wychwind (600 GP)
- Mindrage (1200 GP)


Useful Items
------------

Most items can be ignored or sold off for cash (to buy spells), but the following are permanently useful:

- Power Potion (increases SP above maximum, to enable learning spells whose starting SP cost is too high)
- Dragon Ale (increases INT by 1)
- Orc's Vomit (increases STR by 1)
- Cloud Amulet (???)
- Serpent Amulet (increases STR by 5 when worn)
- Chaos Amulet (increases INT by 5 when worn)
- Night Amulet (increases DEX by 5 when worn)
- Dragon Amulet (increases CON by 5 when worn)
- Moon Amulet (decreases AC by 5 when worn)



Walkthrough
===========

Area 1: The Starting Hall
-------------------------

Turn left. Open the wooden door with a common key. Kill the skaven.
Collect the silver key. (And torch, corn, dagger.)
Behind the other wooden door is free food (apple, biscuit) but nothing important.
Go back to the starting hall and open the grated door. Kill the skaven.
You'll find here Ye Shoppe and a Regen Chamber. Skip them for now.
Click the blue dot. Kill four skavens.
At the back of this area, open the wooden door with a common key. Kill the redbint. (Challenging!)
Collect the crystal key. (And crossbow, 10 arrows.)
Visit Ye Shoppe on your way out. Buy 20 common keys; otherwise you will run out.
If you are not planning to buy Trueview or Torch soon, buy a lot of torches. It should be getting dark by now.
Go back out to the starting hall, for the last time. Turn left. Open the blue door with the crystal key. Kill the mage.
Turn right, click the blue dot, step on the portal plate. (And get some leather armor.)

Area 2: "CHOOSE A PLATE TO CHOOSE A FATE"
-----------------------------------------

Face the sign. Step on the plate to your left. Kill the skaven.
Collect the gold key. (And leather buckler.)
Return via the plate.
Face the sign. Step on the plate to your right. Kill the orc.
Open the blue door with the gold key. Find and kill the orc.
You will end up at a dead end with a metal buckler and the silver key. Collect the silver key.
(As you leave, there will be a leather armor on your right.)
(Behind the wooden door by the exit is a Hedjog Venom and 10 elf arrows.)
Return via the plate.
Face the sign. Step on the plate to your left.
Open the blue door with the silver key. In this room is only a bed (and some leather boots).
Open the wooden door with a common key. Kill the mage and the skaven.
Don't open the grated door to your left just yet. (The knight is challenging!) Instead, go right.
Open the wooden door. Find and kill the orc and the redbint. (Challenging!)
(Down the long hallway is only a chainmail.)
Return to the wooden door.
Don't open the blue door straight ahead just yet. Instead, go right.
Click the gray dot to open Ozzrik's Unearthed Arcana. Collect the serpent key.
Visit Ozzrik's Unearthed Arcana. Exit and bear left.
Open the blue door. Kill the mage.
Veer to your left. Open the blue door with the serpent key. Kill the redbint.
Collect the night key (and the leather gloves to your left).
Exit back through the blue door and bear left past Ozzrik's Arcana to the end of the area.
Open the grated door with the night key. In this room is only a bed.
Visit the bed. It's time to level up to Level 2!

Before sleeping, give all your gold to one character. That'll tell how much you have to spend. The gods treat gold as communal property.
Before sleeping, unequip your torch so it doesn't burn down.
Before sleeping, make sure you have enough food for breakfast.
Sleep. When you wake up, all your characters will be at Level 2. This is a boost of about 50 HP!
Check your hunger levels and eat if needed.
Make sure the correct battle spells are selected in your spellbook.

This sign says, "TURN THE BLOCK TO TURN THE BLOCK".
Open the next grated door. Kill the orc.
This is your first puzzle! The goal is to access the green dot so you can proceed.
Straight ahead you see a green dot blocked off behind a brazier.
Click the red square next to the portal plate. This rotates the column (but would undo the effect of the gray square).
Click the gray square. This vanishes the obelisk and makes the green dot accessible.
Click the now-accessible green dot.
Click the red square across from the gray square. This rotates another column and makes the green square accessible.
Click the green square. This vanishes an obelisk to your right! Kill the skaven.
In this area is only a quarterstaff.
Step on the plate. Go down the hall and collect the ruby key (and 10 arrows, and a chainmail).
Return via the plate. Exit this area, past the bed.
Go back in through the blue door (between the wooden door and Ozzrik's Arcana). Go straight and turn right.
Open the grated door with the ruby key. Kill the knight. (Challenging!)
Collect the sun key (and a metal buckler).
Turn left, out the open blue door, bear right through the open wooden door, and then turn hard left to the grated door.

Before descending these stairs, beware! Read the section about key loss, above.

Open the grated door with the sun key. Descend the stairs!


Area 3: "ALL MORTALS BEWARE"
----------------------------

Immediately upon descending the stairs, you'll have an open door to your right. Kill the skaven.
(The blue door requires a crystal key.)
Go through the open door, stepping on the plate. The plate closes the door behind you.
Kill two more skavens.
Go down the short hall to your right. Turn around quick!
Turn around! Kill the gray skaven, the mage, and the bluebint.
Collect the crystal key (and leather gloves, and corn) from the end of the short hall.
Finally, explore the rest of this area. Collect a second crystal key.
Open the blue door with the crystal key.
(Beware of key loss! You need at least 3 common keys!)
Ascend the stairs. Turn left.
Open the grated door that you've been ignoring. Kill the knight. (You can skip this fight, but if you do, you likely will not be able to level up at the appropriate time below.)
The sign says, "BRING THE CRYSTALS, FIND THEM ALL, ONLY THEN WILL EVIL FALL".
(Collect a hand axe and a Phoenix Broth. The grated door at the other end of the room will not budge.)
Go back out, turn right, go through the room with the bed, and take the portal plate back to the "CHOOSE A PLATE" area.

Face the sign. Step on the plate behind you and to the left. Kill the skaven.
Open the blue door with the crystal key. Kill the mage, orc, and knight. (Challenging!)
(Collect a quarterstaff, a short sword, and an Amber Wand.)
Open the wooden door with a common key.
Open either of the double wooden doors. Kill the skaven.
The sign says, "FAST ROUTE DOWN".
Before you go down here, find a bed and level up to Level 3.
(Beware of key loss! You need at least 2 common keys!)
Jump down the pit and look out! Kill two bluebints, the mage, and the skaven.
The sign says, "DESCEND TO VIEW THE SHRINES OF THE LOST GODS OF MAGICK."
(The doors need a gold key and a ruby key, respectively.)
Open the wooden door behind you with a common key.
Collect the gold key (and 10 arrows, biscuit).

Open the left-hand grated door with the gold key. Kill the roundhead. (Collect a Phoenix Broth.)
Open the wooden door with a common key. Kill the skaven.
Collect the ruby key (and corn, and backpack, and torch).
Go back to the "DESCEND TO VIEW" sign.
Open the right-hand grated door with the ruby key.
(Beware of key loss! You need .... common keys!)
Descend the stairs. Kill the orc and mage.
There is a bed here. If you did not level up to Level 3 before taking the fast route down, level up to Level 3 now!
(Straight ahead is the Tower of Grisslem, requiring a serpent key.)
(To your left is the Realm of Xlaltic, requiring a sun key.)
(To your right is the Citadel of Angrath, requiring a ruby key.)
(Behind you is the Demesne of Shaspuok, requiring a night key.)
(To the left of Shaspuok's door is a grated door that requires a crystal key.)
To the right of Xlaltic's door is a grated door. Open it. Visit Ye Armoury.


Area 4: "ONLY THOSE WHO PROVE WORTHY WILL RETURN"
-------------------------------------------------

To the right of Grisslem's door is a grated door. Open the grated door.
This room has only a bed. Go in and turn left.
Open the wooden door. Kill the shrek. (Collect a leather helm.)
Descend the stairs. Go through the open door; it will lock behind you. Kill the orc and skaven.
Go around to the right. Collect the serpent key.
(The blue door near you, through which you can see the shed, requires a sun key.)
Go to the blue door straight ahead of where you came in.
Open it with a serpent key. Kill the roundhead. Collect the sun key.
The sign you passed says, "WELCOME BACK".
Visit the Grog Shop.
Go back out the open blue door and turn left.
Open the blue door with the sun key.
Open the wooden door. Open the wooden door. Kill the shrek.
(Collect a chainmail and a metal helm.)
To your right is a green dot. Turn around and click it three times. Kill the shrek. Collect the ruby key.
(The blue door in front of you requires a night key.)
Go back through the shed. Click the green dot twice.
Turn left. Open the blue door with the ruby key. Kill the roundhead. Collect the gold key (and bread).
Turn right and click the green dot next to the bed. This vanishes an obelisk to your right.
The sign says, "WELCOME BACK".
Turn left, then left again; go back through the shed.
Open the grated door with the gold key. Kill the mage, without stepping on any portal plates.

This is a puzzle! The layout of the plates is

      * X * * * o
      * * * X X X
      X * X * * *
    r * * X * X * b
      * X X * X X

    * - safe path
    X - teleport back to entrance
    r - amber ring
    o - obelisk
    b - brazier

There is a green square in the northwest corner. Click the green square to vanish the brazier.
Go where the brazier was. Click the blue square to vanish the obelisk. Kill the valkyrie.
Collect the night key (and shield, and torch).
Go out through the shed and bear right all the way back around to the side of the shed with the green dot.
Click the green dot twice. Go through the shed. Open the blue door with the night key.
(Collect a scroll of antimage.)
(The grated door to your right requires a silver key.)
Open the grated door to your left. Find and kill the orc, without stepping on the plate.
The plate flips your orientation without moving you.
Go up the left (north) branch of the fork. Collect the crystal key.
Go up the right (south) branch of the fork. Open the blue door with the crystal key. Kill the skaven.
Collect the silver key (and leather boots).
Go back out the way you came; go to the grated door in front of you.
Open the grated door with the silver key. Kill the greenbint. (Challenging! She casts fireballs.)
The sign says, "YOU HAVE PROVEN TO BE WORTHY. YOU MAY RETURN." (That noise is the door in the northeast corner of this level re-opening.)
Descend. Kill the mage and the shrek.
(The blue door will not budge.)
Open the left-hand grated door. Kill the roundhead and the valkyrie.
(In this area, moving across the invisible line between the two obelisks will flip your orientation.)
Cross carefully between the obelisks, backing up when you flip. (Collect a helm and some other stuff.)
Ascend the stairs. Kill the mage.
Collect the gold key (and the plate mail).
Visit the bed here and level up to Level 4.
Descend the stairs. Veer right, between the obelisks (carefully).
Step on the plate to teleport back to the three doors. Turn right.
Open the grated door with the gold key. Kill the skaven.
Click the green dot to open the blue door. Go through the blue door and jump into the pit.
Go down the long hall. (Moving across the center line will flip your orientation.)
Ascend the stairs. Kill the skaven.
Turn left and go down the hall. (The blue door on the right requires a sun key.)
Open the grated door. Kill two skavens. Collect the sun key (and leather boots, hand axe).
Open the blue door straight ahead of you with the sun key. Follow around. You've been here before!
Collect the crystal key. Step on the portal plate.
Behind you and left, there are stairs. Ascend the stairs. Follow around and left. Turn left.
Go through the shed. Go left past the bed and "WELCOME BACK". Turn left and straight to the northeast corner of the map.
Ascend the stairs. Go around to the right. To your right you'll see the Tower of Grisslem again.
Turn left (south) and go to the grated door to the left of Shaspuok's door.
Open the grated door with the crystal key. Kill the skaven and greenbint.
(To your right are leather boots and Hedjog Venom.)
To your left is a staircase. Ascend it. Kill the skaven and bluebint.
The sign says, "YOU HAVE EARNED ACCESS TO THE TOWER OF LORD GRISSLEM". Collect the serpent key.
(Click the green dot. This vanishes the obelisk to your right, creating a shortcut back to "Choose a Plate".)
Instead of taking the newly created shortcut, turn around and go down the stairs behind you.
Go around to your right and out. Find the Tower of Grisslem.

Open the blue door to the Tower of Grisslem using the serpent key.
Open the grated door to your left. (Collect 20 elf arrows.)
Open the wooden door. (Collect a blue n'egg, moon elixir, phoenix broth, full helm.)
You are now ready to tackle the Tower of Grisslem!


Area 5: The Tower of Grisslem, Left Branch
------------------------------------------

Before you step on the portal plate, make sure you have at least 5 common keys.
Put them in your backpack, so they don't get lost when you change levels!

Step on the portal plate. (This area is empty.)
You can go left or right. Whichever way you go, the door will lock behind you.

Go left. Collect the serpent key.
Ascend, ascend, ascend.
The sign says, "GREETINGS TO THEE, FOOLISH INTRUDERS."
Open the purple door with a serpent key. Kill the dwarf.
(The grated door to the left needs a silver key.)
Bear right. Open the wooden door with a common key. Kill the dwarf.
Collect the moon gem!
Bear left. Open the wooden door with a common key. Kill the dwarf.
Open the grated door. Kill the red lizardman. Collect the silver key (and moon elixir, mithril blade, biscuit).
Go back out and bear left.
Open the grated door with the silver key. Kill the dwarf, the mage, and two lizardmen.
(Optionally: Turn left. Open the wooden door. Collect 10 arrows.)
Turn right. Open the purple door.
(Crossing the midpoint of this figure-8-shaped room will flip your orientation.)
Step on the first plate. This releases a lizardman. Kill the lizardman.
Step on the second plate. Collect the sun key (and scroll of fireward and large shield).
Step on the plates an odd number of times to vanish the obelisk from the north end of the figure-8. Go north.
Click the blue dot to your right.
Open the grated door with the sun key. Kill the dwarf.
Open the purple door. (Collect a Hedjog Venom and a drumstick.)
Open the wooden door with a common key. Kill the lizardman, the brownbint, and the dwarf.
(Collect 10 elf arrows.)
The sign says, "FARE THEE WELL MY FRIENDS".
There is a bed here, but you are still far from Level 5. (You should have about 20,000 XP by now.)
Jump into the pit.
(Collect Hedjog Venom and bread.)
There is a wooden door to your west and a wooden door to your south.
Open the door to your west with a common key. Kill the mage and lizardman.
Go down the hall. Look left. Collect the gold key.
Turn left. Open the wooden door with a common key. Kill four dwarves. (Collect a n'egg and a scroll of ethblade.)
At the south end of this area is a purple door. Open it. (Collect a serpent wand.)
The sign says, "PLACE THE GEM IN THE HOLE TO REACH YOUR GOAL".
(Placing the moon gem in the hole takes you to a room with a bed and nothing else. Do it again to return.)
Go back north and east. (The purple door needs a ruby key.)
(Open the wooden door. Collect a full helm.)
Go back to the long hallway where you started this level. Go east.
Open the grated door with the gold key.
Open the wooden door. Collect the serpent key.
Descend the stairs. Open the purple door. Kill the lizardman.
Open the grated door.
Open the grated door. Kill the redbint. (Collect iron boots.)
Click the yellow dot to vanish a wall to your right. Kill the dwarf. Collect the ruby key (and 10 arrows).
Go back up the stairs.
(Ascend the stairs. Click the purple dot. This vanishes the pillar in front of you, creating a shortcut.)
Go back to the long hallway where you started this level. Go west and around until you're facing north in front of a purple door.
Open the purple door with the ruby key. (Collect 10 elf arrows.)
Ascend the stairs. (This area is empty.)
The sign says, "THOSE WHO SEEK THE EYE SHALL PERISH."
(The left-hand down-staircase is the one you came up to get here.)
Ascend either up-staircase; they go to the same place.
Open the grated door. Kill two lizardmen. (Collect a scroll of wizeye.)
Open the purple door. Collect the sun key and a cloud amulet. (I don't know what it does.)
Go back out, face north, and open the purple door with the sun key.
(Collect bread, phoenix broth, scroll of suspend.)
Open the grated door.
Open the wooden door. The sign says, "THE CRYSTALS CAGE THE POWER". (Collect an Orc's Vomit.)
Open the purple door. Kill the viking and the greenbint. Collect the gold key (and corn, scroll of trueview).
This room has two beds, and you've just hit 25,000 XP. Visit the bed and level up to Level 5!
To your south is a hallway with green squares at both ends. (Crossing the midpoint flips your orientation.)
Click either green square to temporarily vanish the wall south of the midpoint. Go south.
(The purple door to your left requires a silver key.)
Turn right, then face left.
Open the grated door. Kill the knight, mage, and death knight. (Collect a Hedjog Venom.)
Open both wooden doors. Collect the silver key behind one, and a mithril chainmail behind the other.
Open the purple door with the silver key. Open the grated door with the serpent key. Ascend.
Collect the crystal key. (The grated door requires a serpent key.)
Descend. Go north, then back to the down-stairs on this level.
On the east side of this level (Level 5 of the tower) is a wooden door. Behind it is only a bed.
Descend either down-staircase. (They go the same place.)
Open the wooden door. Kill the mage and the dwarf. (Collect a second backpack and a moon elixir.)
Open the grated door to the south. Open the next grated door with a crystal key. (Collect an apple.)
Jump down the pit.
Jump down the next pit. (You'll fall two levels this time, because the pits line up.)
Click the green square next to you to vanish the wall to your right.
You're back at the entrance to the Tower of Grisslem!
Don't go through the other branch just yet. Go back to Ye Armoury and sell off all your trade goods!


Area 6: The Tower of Grisslem, Right Branch
------------------------------------------
Go through the right-hand door. The door will lock behind you.
Collect the silver key.
Ascend. The sign says, "GREETINGS TO THEE, FOOLISH INTRUDERS".
(The right-hand door requires a serpent key.)
Open the left-hand grated door with the silver key.
(The purple door around to the left requires a sun key.)
Follow around to the right, past the regen chamber. Open the purple door. (Collect a purple n'egg.)
(Face east. Open the grated door. Open the next grated door. Kill the dwarf. Collect a long bow. Come back.)
Step on the portal plate to your south. This vanishes a pillar in an alcove west of the plate, releasing a dwarf. Kill the dwarf.
(Collect a green n'egg and a Chymera Blood.)
Visit the alcove to your west. Collect the serpent key.
Go back out past the regen chamber and straight ahead.
Open the wooden door with a common key. Kill two dwarves. Collect the fire gem. (Collect 10 elf arrows.)
Go back to the down-stairs; face north. Open the right-hand grated door with the serpent key. Kill two dwarves.
Follow the hall around and take the right branch when it forks.
The right fork dead-ends. The sign says, "LOOK BEHIND YOU". Turn around! Kill the dwarf.
(Collect plate mail and bread.)
Go through the door that opened to release the dwarf. Click the red dot to vanish a brazier elsewhere.
Go back to the left fork.
Open the grated door. Collect the ruby key. (Open the wooden door. It's just a bed.)
Open the wooden door. This area is empty.
Open the purple door with the ruby key. Kill the mage. (Collect a full helm.)
Collect the sun key. (It is behind the brazier which vanished when you clicked the red button. But you can actually sneak it diagonally if you want.)
Go back out to the down-stairs. Go through the left-hand door and around to the left.
Open the purple door with the sun key.
Open the right-hand wooden door. Kill the redbint and purplebint. (Collect a scroll of formwall.)
Open the grated door. Open the wooden door. (Collect cheese and Hedjog Venom.)
Turn right. Click the blue square. This vanishes a wall to your left, making a shortcut.
Don't take the shortcut. Instead, turn right and go south.
Open the wooden door with a common key.
Open the wooden door. Kill the mage. (This is a big mazey area and can flip your orientation. Seek the mage carefully.)
Collect the gold key.
Open either wooden door to the west. Kill the lizardman and the dwarf. (Collect a scroll of renew.)
(Open the wooden door to the south with a common key. Collect a mithril sword.)
(The wooden door you didn't open on this level hides only a bed. Don't waste a common key on it.)
The sign to your south says, "THE PRIZE YOU SEEK IS FAR ABOVE".
Open the grated door with the gold key.
Ascend. Kill the mage.
Go all the way east. Open the wooden door with a common key.
(Open the right-hand wooden door. It's just a bed.)
Open the left-hand wooden door. Go in.
Open the wooden door. (Collect gauntlets and phoenix broth.)
Go to the wooden door leading into the small "island" of unexplored map.
Open the wooden door with a common key. Kill the dwarf. Collect the silver key.
Go south and open the purple door with the silver key. This area is empty.
Collect the night key (and 10 elf arrows).
(The sign says, "PLACE THE GEM IN THE HOLE TO REACH YOUR GOAL." Do so. Collect 10 elf arrows, hedjog venom, two n'eggs.)
Go west and open the wooden door.
(You can sneak-attack the next four dwarves around this pillar. Do so if possible.)
Open the next wooden door with a common key.
The sign says, "ALL BELIEVERS ARE WELCOME".
Open the purple door. Kill four dwarves. Collect the serpent key.
(Collect a serpent ring, moon elixir, buckler, phoenix broth, 10 hail of doom.)
Go to the unopened door on this level, near the northeast corner.
Open the purple door with the night key. (Collect 10 arrows.)
Ascend. You have been here before!
Turn right and ascend again.
Follow around to the right and use the green squares to reopen the passage south; bear left to the stairs.
Ascend. Finally!
Open the grated door with the serpent key. Ascend.
The sign says, "ASCEND TO THE EYE OF LORD GRISSLEM". (Collect an arc shield.)
Make a U-turn and ascend. (This area is empty. Collect a scroll of vivify and a power potion.)
Go to the northwest corner of this area. Click the purple dot. This vanishes the pillar that appeared behind you when you arrived.
Descend again. Go forward and ascend.
(Collect a snake staff.)
Take the green Eye from the wall. (This should start a cutscene. If it doesn't, download WIZ.COM and try again.)
Getting close to the pillar on your left will vanish it. Look out! Kill three lizardmen and a skeleton.
Getting close to the northwest corner of the map will vanish the brazier on the right. Look out! Kill four lizardmen, a death knight, a skeleton, and a skaven.
Explore this area.
Click the green square to the east of the stairs. This vanishes a pillar and makes a door accessible.
Click the purple dot to the west of the stairs. This vanishes a brazier and makes a door accessible.
The two newly accessible doors both lead to plates in front of pits.
Go down the right-hand (east) pit.
Open the grated door.
Open the purple door. Kill the skeleton and death knight. (Collect a war helm and purple n'egg.)
Open the purple door.
Collect the crystal key.
Turn right and open the purple door. Kill two lizardmen. (Collect a war helm.)
Open the purple door. (Collect 10 elf arrows.)
Open the grated door. This room is empty. Go back out.
The sign says, "NOW YOU ARE IN TROUBLE".
Open the grated door to the right of the sign. Kill the death knight, the mage, and the two bints. (Use the door liberally!)
(Collect a moon elixir.)
Turn left. Open the purple door with the crystal key. Collect the silver key.
(Open the wooden door. Collect a battle axe.)
Open the grated door with the silver key. Kill the death knight.
Open the purple door. There are two pits here. Jump into either pit. (They go the same place.)
(Collect mithril gloves, moon elixir, yellow n'egg.)
Visit the bed and level up to Level 6.
Open the grated door.
(Collect the Battle Bane shield.)
Step on the first plate. Kill the skeleton.
Step on the next plate. Kill the skeleton.
Step on the next plate. Kill the lizardman. (Collect 10 elf arrows.)
Step on the next plate. Kill the skeleton mage.
Open the purple door. Immediately turn left and go down the hall. (It will flip your orientation.)
(Sneak the mithril plate from behind the brazier.)
Take two steps down the line of plates. Each step will shift a pillar into place behind you.
Now that there's a diagonal between the pillars, you can try to kill the mage and death knight on the other side.
Finish going down the line of plates.
Open the wooden door with a common key. Kill the lizardman.
Collect the serpent key (and 10 elf arrows).
You have another chance to kill the mage and death knight diagonally.
Step on the plate here to move this last brazier. Kill the mage and death knight. Beware! This hallway flips your orientation.
(Collect a Hedjog Venom.)
Open the purple door. Collect the gold key (and mithril boots).
Open the grated door. (Collect 10 arrows.)
Open the grated door with the gold key.
Follow around to the plate. Step on the plate. This causes a new plate to appear to your immediate south.
Step on that plate, and so on, creating a pathway of plates. The last plate you step on will vanish a pillar to the north.
Go back north and through the gap you just created.
Open the purple door with the serpent key. Kill the frogman. (Collect a sun staff and a moon elixir.)
Click the blue dot. This vanishes a wall to your left. You've been here before!
Go through the gap. Ascend.
Make a U-turn and ascend again.
Turn right. Find the purple door.
Open the purple door. Go in, turn right, and jump in the pit.
Check the map. Follow around to the two pits on this level. Jump in either one.
Find the downstairs (on tower level 6) and descend.
Find the downstairs (on tower level 5) and descend.
The sign says, "THOSE WHO SEEK THE EYE SHALL PERISH".
Face the sign. Behind you is a door. Go through it and turn right.
Jump in the pit.
Jump in the next pit; fall two levels.
You're back at the entrance to the Tower of Grisslem!
Take the portal plate back to the Keep.
Go back to Ye Armoury and sell all your trade goods!


Area 7: The Demesne of Shaspuok
-------------------------------
Find the up-stairs in the southeast corner of Keep Level 4. Ascend.
Go straight forward. Ascend.
Turn left and go to the room with the slots on the walls.
Place the Eye of Grisslem in the appropriate slot!
(This will bring up an antipiracy screen. Use hexx-manual.pdf to answer the questions.)
The grated door to your west has opened.
Go through. Turn left.
Open the wooden door. Kill the orc and the mage.
Collect the night key (and two n'eggs).
Go back down the stairs, straight, and down again.
Go around to the right and find the door to the Demesne of Shaspuok.
Open Shaspuok's blue door with the night key.
Open the grated door. (Collect 20 elf arrows and two n'eggs.)
Go back out the grated door. Step on the portal plate. This area is empty.
Ahead of you are two up-stairs. (They go the same place.)
Ascend either staircase. Kill two cyclopses and two mages.
(This big room has two shops and a regen chamber.)
To the south are some illusory walls hiding a sign that says "PARTING IS SUCH SWEET SORROW" and two gem slots.
(Collect a cloud staff in front of the sign.)
Place the moon gem in the slot.
Open the blue door. This area is empty.
Open the grated door. Kill the mage and two skavens. (Collect a scroll of levitate.)
Open the blue door straight ahead. Kill two valkyries. (Collect 10 elf arrows.)
Open the wooden door with a common key. Kill the knight. (Collect mithril gloves.)
Go back out to the east-facing wooden door you haven't opened yet.
Open the wooden door. This area is empty.
Open the blue door. Kill the mage.
Go straight. Open the blue door.
(Turn left. Open the blue door. This leads to the slot for the fire gem.)
Open the grated door to the south. Kill the viking.
Open the blue door. Kill two vikings and two valkyries. (Collect an apple and a moon elixir.)
Open the west-facing wooden door with a common key. Kill the cyclops. (Collect 10 elf arrows and a long bow.)
(Open the north-facing wooden door. Collect 10 arrows.)
Find the east-facing wooden door at the north end of the level.
Open the wooden door with a common key. (Collect a battle axe and a corn.)
Ascend. (Collect a Hedjog Venom and a drumstick.)
The sign says, "FOR THE FIRST YOU RISE / FOR THE SECOND BE WISE".
Face the sign; turn around. Open the blue door.

This is a puzzle!
The two pits in front of you deposit you right back at the bottom of the tower. You must cross both of them cleverly.
For the first pit, use Suspend or Levitate, or sneakily step diagonally.
Crossing the center line of the room will flip your orientation and fizzle all your spells. Watch your compass closely!
Here is the intended solution to the second-pit puzzle:
- Step onto, but not across, the west plate.
- Step across the east plate.
- Follow around the loop. Step onto the (northeast) plate.
- Retrace your steps; step across the east plate; then step onto it again, so you've hit it an odd number of times.
- Step across the west plate. (Watch your compass!)
- Step across the northwest plate to vanish the second pit.
Alternatively, you can just step diagonally past the pit and step on the northwest plate immediately.

Open the blue door. Kill the viking.
Go all the way around to the right.
The sign says, "THE RINGS WERE MADE FROM THE SHARDS OF PUREST CRYSTALS".
Open either grated door. Kill two valkyries.
Collect a night ring, a mithril boots, and a serpent key.
Come back around. (Open the wooden door. Collect 10 arrows.)
Visit a bed and level up to Level 7!
Continue to the west end of the hall.
Open the grated door with the serpent key. Kill the mage and the skeleton.
Open the grated door. Kill the knight.
Open the blue door. (This area is empty. Watch out for the pit!)
Sneak the gold key diagonally from behind the pit.
Open either grated door in this area. Kill the mage.
Open the blue door with the gold key. Bear west and south.
(The grated door here requires a silver key.)
Open the wooden door. Collect the serpent key (and bread).
Go north and west.
Open the south-facing wooden door. (Collect a mithril plate.)
Open the blue door with the serpent key. Kill four monsters. Collect the silver key (and a cheese).
Go out and out and bear right to the grated door.
Open the grated door with the silver key. Kill the skeleton and the viking.
Open the wooden door with a common key. Kill the mage. (Collect a Hedjog Venom.)
Very subtly, almost behind the pillar, there is a night key! Collect the night key.
Go out and out and immediately make a U-turn around to the right.
Open the wooden door with a common key. Kill the skeleton and the viking.
(Behind the wooden door in front of you is only a bed.)
Go right.
(Open the south-facing wooden door. Collect a mithril axe.)
(Collect a scroll of antimage.)
Open the grated door with the night key. (Collect a Chymera Blood.)
Ascend either staircase.
Beware: This entire level is anti-magic! All your combat spells will fizzle.

Go right cautiously! Kill eight monsters: viking, knight, valkyrie, valkyrie, shrek, dwarf, valkyrie, viking.
At the end of the right-hand passage is a grated door.
Open the grated door. Collect the night key and the third backpack.
(Also collect a scroll of renew and a Dragon Ale.)
Retrace your steps.
(Open the wooden door with a common key. Collect 20 elf arrows and a cheese.)
Go back past the down-stairs.
The sign says, "BEWARE THE PSYCHIC BARRIERS".
This is another puzzle!

          _
        _ B X X a
        X * * X *
        b X F * *
        * A * X X
      _ o * * * o
              *

    o - obelisk
    * - safe path
    F - flip orientation but otherwise safe
    X - teleport back to entrance
    A - teleport back to entrance
    B - teleport back to entrance
    a - plate replacing 'A' with '*'
    b - plate replacing 'B' with '*'

Step on plate 'a' to eliminate teleport 'A', or alternatively sneak diagonally past the obelisk.
Step on plate 'b' to eliminate teleport 'B'.
Go out the north exit.
(Your spells will work again here!)
Open the blue door with the night key. Kill the shrek and the dwarf.
Bear left. Open the wooden door with a common key. Kill the mage and the purplebint.
Collect the gold key.
(Open the wooden door. Kill the knight and the death knight. Collect a scroll of fireward.)
Open the grated door with the gold key.
Open the wooden door. Collect the serpent key (and a cloud wand).
Open the blue door with the serpent key. Kill the mage and the cyclops.
(Collect an apple, 10 arrows, and a night amulet.)
Follow the right-hand wall. Open the wooden door.
The sign says, "RUN THE GAUNTLET!"
Stepping on the first plate releases a dwarf. Kill it. (Collect a power potion.)
Stepping on the next plate releases a purplebint. Kill it. (Collect a bread.)
In the purplebint's niche, there is a very subtle button. Click it to open the door at the end of this gauntlet.
Stepping on the next plate releases a death knight. Kill it. (Collect a golden helm.)
Stepping on the last plate releases a knight. Kill it.
(If the blue door is still closed, check the map for the purplebint's button.)
(Collect a yellow n'egg.)
Ascend.
Crossing the midpoint of this room flips your orientation.
To the west, behind the wooden door, is a regen chamber.
To the east, behind the wooden door, is a room with a pit and two portal plates.
Step on the left-hand portal plate to teleport behind the west grated door (which will not budge).
Open the wooden door.
Open the next wooden door. Collect the ruby key (and a corn).
Open the blue door with the ruby key. Kill two skeletons.
Collect the gold key (and a cloud ring).
Go back out to the grated door.
Open the grated door. Kill eight monsters. Collect the sun key (and a scroll of suspend).
(Open the wooden door to your right. It's just a bed.)
Visit a bed and level up to Level 8!
Open the blue door with the sun key.
Open the grated door with the gold key.
Open the wooden door. Kill the cyclops. (Collect a chymera blood and a night wand.)
At the end of this area, collect the night key (and a Heron Blade and an Orc's Vomit).
Click the red square to (???).
Retrace your steps. Open the wooden door.
Open the blue door with the night key.
(The grated door will not budge.)
Open the first wooden door. Collect the serpent key (and blood leathers).
The sign here says, "THE GREAT BEAST DID COME FROM THE OTHER WORLD".
Open the second wooden door. Kill the mage. (Collect moon elixir, scroll of vivify.)
Go to the northeast corner of the map.
Open the grated door with the serpent key. (Collect a biscuit.)
Ascend.
Open the grated door. Kill the cyclops and two shreks.
The sign says, "LOOK AND THOU SHALT SEE".
(This area is full of illusory walls, and many invisible traps that cancel Trueview.)
Collect the silver key (and a battle staff, Hedjog Venom, yellow n'egg).
Click the red square on the north side of the room.
Click the red square on the south side of the room.
Go west. Open the left-hand blue door.
Open the grated door with the silver key. Go straight. Collect the gold key (and Hedjog Venom).
(Collect an elven chain from the other branch of this area.)
Go back out. Make a U-turn around to the left.
Open the right-hand blue door with the gold key.
(Collect a bane shield and 10 elf arrows.)
Open either of the wooden double doors here. Kill five monsters. Find and kill the roundhead.
Collect the silver key.
Open the blue door with the silver key. Kill the valkyrie.
Collect the night key.
Open the grated door. Kill the valkyrie. (Collect Dragon Doom, and a bread.)
(Behind the west-facing wooden door in the south part of the level is a Stealth Blade.)
Ascend.
Open the grated door with the night key.
Bear right. Open the blue door. Kill the cyclops, valkyrie, and minotaur.
(Collect a Chymera Blood.)
Go back out and around to the right.
Open the blue door. Kill the cyclops, valkyrie, and mage.
Click the blue button and the green square. (This vanishes obelisks between the two rooms you just cleared.)
Go back into the room you just cleared. (More illusory walls.)
Collect a Power Staff.
Take the purple Tear from the wall. (This should start a cutscene. If it doesn't, download WIZ.COM and try again.)
Descend the way you came up.
Veer around to the left. Find the down-stairs on level 6. Jump in the pit opposite the stairs.
Descend the down-stairs in front of you.
Bear right, past the gauntlet. Turn right. Find the down-stairs on this level.
(This is the anti-magic area with traps that cancel Torch and Trueview. You might need to use the map to feel your way out.)
Descend by either of the two adjacent down-staircases.
Make a U-turn around to the left. (Collect a scroll of antimage.)
Turn left. Go through the open door to the left at the end of this room.
Go out north, north, and jump in the pit.
You're back in the main area with shops! Sell off your trade goods, then descend.
Step on the portal plate to return to the Keep.


Area 8: The Citadel of Angrath, Part 1
--------------------------------------
Find the up-stairs in the southeast corner of Keep Level 4. Ascend.
Go straight forward. Ascend.
Turn left and go to the room with the slots on the walls.
Place the Tear of Shaspuok in the appropriate slot!
(This will bring up an antipiracy screen. Use hexx-manual.pdf to answer the questions.)
The grated door to your west has opened.
Go in and left. Open the wooden door. Kill the orc.
Open the wooden door. Kill the knight. Collect the ruby key (and a n'egg).
Go back down the stairs, straight, and down again.
Go around to the right and find the door to the Citadel of Angrath.
Open Angrath's blue door with the ruby key.
(Open the grated door. Collect 20 elf arrows and two n'eggs.)
Step on the portal plate! (This area is empty.)
Ascend the left-hand staircase.
Open the grated door. Kill four minotaurs.
(Open the grated door straight ahead of you; it just leads to the other staircase.)
Open the grated door to the east. Kill the frogman.
The sign says, "THE OLD ONES WARD THE LAIR OF LORD ANGRATH'S HEART".
This area is a huge maze with orientation-flipping traps! Explore it without opening any doors for now.
Find and kill two redbints in the north half of the map.
Find and kill a minotaur in the south half of the map.
Find and kill a frogman in the southwest corner of the map.
Find the pair of doors on the map. 4 tiles east and 2 tiles north of there, collect a pair of battle gloves well-hidden on the ground.
Near the northeast corner, collect a golden shield.
(Open the north-facing wooden door in the northeast corner of the map with a common key. Kill the minotaur and the mage.)
(Open the south-facing wooden door on the east edge of the map. Collect a drumstick.)
Find the north-facing wooden door on the north edge of the map.
Open the wooden door with a common key. Kill the redbint.
Go in and left. Kill the minotaur. (Collect a blood leathers at the end of this area.)
Open the wooden door with a common key. (This area is empty.)
Behind the wooden door to the right is a dragon amulet.
(Behind the wooden door straight ahead is a teleport trap that takes you to the south end of the level. Don't open it!)
Open the grated door to your left. Kill about four monsters.
Follow the left wall. Open the wooden door.
Keep following the left wall. Collect the silver key.
Keep following the left wall, back out.
(The grated door requires a ruby key.)
Open the wooden door to the teleport trap. Step on the trap to teleport to the south edge of the map.
Open the wooden door. Find and kill three minotaurs and a mage.
Go left and north.
Collect a golden helm at the end of this corridor.
Open the wooden door with a common key. Kill the frogman.
Go in and left. Collect the gold key!
Go back out to the central hub-thing. Go around via its north side. (There is a teleport trap blocking the south side.)
Open the grated door with the silver key.
Open the inner door with the gold key.
Go in and turn left. Collect the ruby key well-hidden on the floor, one space west and two south of the inner door.
Find your way back to the remaining door on this level.
Open the grated door with the ruby key.
The sign says, "ONWARDS TO THY GREATER GLORIES".
(Collect a biscuit.)
Open the wooden door. Kill the redbint and the frogman.
Ascend.

Area 9: The Citadel of Angrath, Part 2
--------------------------------------
Turn left. Collect the serpent key (and a cheese).
Open either of the dragon doors to the north. Turn left.
Open the dragon door with the serpent key.
Open the double wooden doors. Kill two minotaurs.
This hallway is full of teleport traps!

    XXXXX
    X..|.
    X..|.
    X.pXX
    X..O
    Xp.X
    X..XX_X
    X..XO.X
    X.pX..X
    X..X.pX
    X..X..X
    Xp.XO.X
    X...p.X
    X.....O
    XOXXXOX

    X - wall
    O - obelisk or brazier
    p - teleport trap (takes you back to the beginning of the hallway)
    . - safe path

Hug the right wall until you are at the bloodstain across from the obelisk.
Hug the left wall until you are at the dragon banner across from the wood panel.
Hug the right wall until you are across from the swords.
Go to the swords, then walk due south to the wall.
Walk due east to the corner.
Walk north until you are just past the obelisk; then cut diagonally to the space north of the obelisk.
Hug the left wall until you reach the brazier.
Cut diagonally to the dragon door.
You're home free!

Open the dragon door. Kill the death knight.
To your right is an alcove with a blue button, a moon elixir, and a well-hidden ruby key.
Collect the ruby key (and moon elixir, mithril boots, and yellow n'egg).
Click the blue button to vanish a brazier behind you, creating a shortcut.
Take the shortcut.
Open the dragon door with the ruby key. Kill the minotaur. (Collect a blue n'egg.)
Follow your nose. Kill another minotaur. (Collect a scroll of vivify.)
Open the grated door.
Open the left-hand wooden door with a common key. Kill the roundhead and the demon.
Find and kill another roundhead and a minotaur, then two minotaurs in a dead end.
(Collect a blood helm.)
This is a puzzle!
Step on the silver plate to rotate the block to your right.
Click the small red square that was just revealed there.
Turn left and open the wooden door. Collect the night key.
(By hanging out back of the other shed, you can blindly sneak the gold key and the Heron Shield from inside the shed.)
Follow the right wall all the way around to the grated door.
Open the grated door with the night key. (Collect a scroll of ethblade.)
The sign says, "TO PASS THE LOCK JUST TURN THE BLOCK".
Click the blue button to rotate the second shed.
If you have not already sneaked the gold key from the second shed, go back and collect it now (and a Heron Shield).
Open the dragon door with the gold key. Kill the frogman and the knight. (Collect a Hedjog Venom.)
Go around to the left and find the stairs.
Ascend.

Open the double wooden doors with a common key. Kill the orc and the frogman.
Turn left and kill the roundhead.
Follow the left wall. (Collect a battle gloves.)
(Open the wooden door with a common key. Kill the demon. Collect a dragon ring, a scroll of formwall, and 10 hail of doom.)
Open the dragon door. Kill the minotaur.
Don't touch anything! This is a puzzle!

Go all the way to the east edge of the map and click the blue square to vanish the obelisk to the right of the exit hallway.
(You might notice a new wall appear when you misstep on your way there. Don't worry about it.)
Go all the way west and click the blue button to vanish that wall again.
(You might notice a new brazier appear. Don't worry about it.)
Go carefully back east, hugging the wall near the portal plate where the vanished obelisk used to be.
If you misstep and the wall reappears, go click the blue button again.
Collect the silver key.
Go north. Open the grated door with the silver key.
Click the green square to vanish a brazier on the west side of the map.
Go click the yellow button to vanish the brazier that appeared earlier.
Go carefully north, hugging the left wall where the vanished brazier used to be.
Turn right and click the blue button.
There is a well-hidden ruby key in the alcove behind you. Collect the ruby key.
Click the original blue button to vanish the wall; go carefully east.
Open the grated door with the ruby key.
Open the left-hand wooden door. Collect the fourth backpack!
Open the right-hand wooden door. (Collect 10 elf arrows.)
Open the inner wooden doors to reveal gem slots.
Place the moon gem in the slot.
Collect the ruby key (and an elven chain).
Place the moon gem in the slot to come back.
Place the fire gem in the slot.
Open the dragon door with the ruby key. (Collect a battle staff.)
Go left. Open the grated door. Kill the death knight and the orc.
(The dragon door to your left is just a regen chamber.)
The sign says, "YOU WILL NEVER DEFEAT THE WIZARD IN HIS LAIR".
Ascend. (This area is empty.)

Just about every hallway on this level is filled with arc bolts.
You WILL die many many times.
Save your game.

In order to get hit by an arc bolt and not die, you need to have Antimage in effect.
Some squares on this level are anti-magic traps that will remove Antimage.
Therefore, select it and keep casting it (e.g. by entering combat with "space") as you move through the level.

Here is a map of the level, with the relatively safe spots marked:

    ###################
    #....I....#o.+6o.##
    ##o.o##...|..|.#.8#
    #......#.#..#..##I#
    ###o#..#^#..L#....#   o - obelisk
    #......###oo####..#   # - wall
    #.#o#.#....p...#..#   v - down stairs
    #....#.....#...o#.#   ^ - up stairs
    ####.o..o3#4......#   | - wooden partition
    #.......###.......#   + - door (requires common key)
    ####1~#...#.o##o###   I - door (will not budge)
    #o.x......#....#..#   L - bed
    #..###2#_#..##.#..#
    ##...o......o...#.#
    #v#.###.#o#####G#.#   G - needs a gold key
    #.....#.o...#...o.#
    #..o..#.#..o#.o.#.#
    ##..#L#5+...#.....#
    ###################

Click the green square to vanish an obelisk to your left.
Run to the niche on the left (1). Cast antimage.
Run to the niche on the right (2). Cast antimage.
Run north and hook around the obelisk (3). You'll be relatively safe here. Cast antimage.
Run across the plate (p) and make sure your antimage is holding.
Collect the gold key (4).
Run south. Make sure your antimage is holding.
At (5), make sure your antimage is holding, and switch to your combat spells.
Open the wooden door with a common key. Kill four monsters.
(This room is safe from arcbolts. Close the door if it makes you feel safer.)
(Collect Deathbringer.)
Switch back to antimage. Cast antimage.
Leave the room and run back across the plate to your hideout (3).

Optional digression:
- Run across the plate and north to (6).
- Open the wooden door with a common key. Kill the demon.
- (This room is safe from arcbolts. Close the door if it makes you feel safer.)
- (Collect a war shield.)
- Switch back to antimage. Cast antimage.

Equip the gold key.
Run south to the door at (8).
All your spells will fizzle everywhere in this area. It is imperative that you get through the door and close it as soon as possible!
At (8), open the grated door with the gold key. Go through. Close the door.
Kill the orc.
Collect the serpent key (and elf bow, 10 hail of doom).
The sign says, "NORTHWARD YOU MUST TRAVEL TO CAGE THE ARC".
Click the green button to open the door in the northeast corner of the map.
Return to the grated door, which you had closed earlier.
Cast antimage. It will probably fizzle anyway.
Hug the right wall and run north.
Go through the now-open grated door.
Click the green button to cause an obelisk to appear in front of the arc-bolt machine in the northwest corner of the map. The level is now safe!

Go to the northwest corner of the map. (Collect a scroll of antimage.)
Open the grated door with the serpent key. Kill the orc. (Collect a biscuit.)
Ascend. (Collect a scroll of wizeye.)
Open the wooden door. Open the dragon door.
(The east door needs a ruby key.)
Open the grated door to the west. Kill the death knight.
(Collect a Chymera Blood, elf gloves, Phoenix Broth, bread.)
In the alcove to the right of the dragon door is a well-hidden ruby key. Collect the ruby key.
Go back out. Open the grated door with the ruby key. Kill the frogman, mage, minotaur, and roundhead.
(Turn right. Open the wooden door with a common key. Open the next wooden door. Kill the knight. Collect Scream Slicer.)
The sign says, "WITHIN THE DRAGON LIES THE POWER".
Go to the left of the sign. Collect the night key (and a power potion).
Go back out and west (beware the orientation-flipping trap!) and to the dragon door.
Open the dragon door with the night key.
There is an open wooden door at the end of this room. Kill the minotaur.
(Collect a corn.)
Ascend.
Open the wooden door to your left.
Collect the gold key. (And elven helm, and cheese.)
Open the wooden door to your right with a common key. Kill the cyclops.
Collect the night key. (And elven plate.)
Open the grated door with the gold key. Kill the frogman.
The sign in the middle of this area says, "THE DRAGON HEART AWAKES".
(The door on the west side of the level requires a serpent key.)
(The door upstairs requires a ruby key.)
Go to the door on the east side of this level.
Open the dragon door with the night key. Kill the demon.
Collect the serpent key (and 10 arrows, a biscuit, blood boots, Phoenix Broth).
Go out and across the level to the west door.
Open the dragon door with the serpent key. Kill the demon.
Collect the silver key (and an apple, dragon shield, moon elixir).
Go to the dragon door in the middle of this level.
Open the dragon door with the silver key. Kill the roundhead, orc, two minotaurs.
Collect the ruby key (and Brainbiter, Orc's Vomit).
Ascend. Open the grated door with the ruby key. Kill the roundhead.
Collect a Chymera Blood, a firestaff, 10 elf arrows, and a moon amulet.
Collect Angrath's Heart!
Go out and left. Descend.
Follow around to the left. Descend.
Follow the right wall, then turn left and straight. Descend to level 5.
Follow the right wall. Descend to level 4.
Follow around. Use the fire gem. Find the stairs and descend.
Follow the right wall. Find the stairs and descend to level 2.
Turn right. Go through the open wooden door.
When you go through the next door, head straight northwest.
Make a U-turn around to the right. Hug the north side of the map.
(Watch out for an orientation-flipping trap in the northeast corner!)
Make your way to the north outer wall of the central circular room.
Face the sign; turn around; go through the door; turn left.
Descend to level 1.
Turn right. Take the portal plate back to the Keep.


Area 10: The Realm of Xtlaltic
------------------------------
Find the up-stairs in the southeast corner of Keep Level 4. Ascend.
Go straight forward. Ascend.
Turn left and go to the room with the slots on the walls.
Place the Tear of Shaspuok in the appropriate slot!
(This will bring up an antipiracy screen. Use hexx-manual.pdf to answer the questions.)
Yet another grated door to your west has opened.
Go in and left. Open the wooden door. Kill the knight.
Open the wooden door. Kill the mage.
Collect the sun key.
Descend; descend. Find Xtlaltic's door.
Open Xtlaltic's door with the sun key.
Turn left. Open the grated door. Open the grated door.
(Collect a red n'egg and 10 hail of doom.)
Visit the bed and level up to Level 10!

Step on the portal plate. (This area is empty.)
Ascend either staircase.
The barred door at the end of the hall requires a crystal key.
The sign says, "THE LORDS OF CHAOS AWAIT YOU". Do not pass it!
Kill five minotaurs coming from behind the sign.
Pass to the right of the sign. (Collect an apple and a Hedjog Venom.)
Pass to the left of the sign. You'll hit a teleport trap! Turn right! Kill a minotaur.
(You are now behind the barred door requiring a crystal key.)
Wait at the entrance to the big room in front of you (to the west). Kill the orc.
Go straight west, watching your compass for orientation-flipping traps.
(Turn left. Open the skull-themed wooden door. Inside is only a scroll of formwall.)
Go north. Open the barred door. Kill the death knight. (Collect a chaos wand.)
Open the wooden door with a common key. Collect the night key (and Chymera Blood).
Go to the southeast corner of the map. Kill the minotaur. (Collect a scroll of vivify.)
Go west down the long hall. (Look right. Collect a blood boots.)
Open the barred door. Kill the death knight.
The sign says, "CHAOS CAN NOT BE RULED BY MAN".
Open the ape door in the southwest corner of the map with the night key.
(Collect a bread and an Orc's Vomit. The ape door at the end of this area requires a ruby key.)

Bear left to the southern staircase. Ascend.
The sign says, "YOU MUST RISE BEFORE YOU FALL".
Ascend.
Ascend.
(The barred door requires a gold key.)
Step on the portal plate.
Click the green button to vanish an obelisk blocking the gold key.
Step on the portal plate to return.
Open the wooden door, being careful not to fall in the pit. Collect the gold key.
Open the barred door with the gold key. Kill the death knight and the skeleton.
(The ape door ahead of you requires a night key.)
Make a U-turn to your right and jump in the pit.
(Collect a blue n'egg.)
Jump in the pit. Kill the death knight. Collect the serpent key and the crystal key.
Jump in the pit.
Ascend by the southern staircase again; go through the gold-key door; jump in the pit.
Open the barred door with the serpent key.
Open the skull-themed wooden door. Go in and turn left. Open the wooden door. (Collect a scroll of levitate.)
Turn right. Step on the portal plate.
The sign says, "ONLY THEY WITH THE QUICKEST HAND AND KEENEST EYE WILL PREVAIL".
Bear right and jump in the pit. Kill the death knight and the mage.
(Collect 10 elf arrows.)
In front of you are three portal plates. Step on the middle plate.
Collect the sun key. Step on the plate to return.
This is a puzzle!

You're on level 3. Three plates, no buttons.
Left plate goes to level 6 (north). Three plates and buttons.
Middle plate goes to level 6 (middle). Obelisks blocking the way to upstairs. Current configuration: X,X,_.
Right plate goes to level 6 (south). Three plates and buttons.
There is also a button to the east of level 6 (middle), currently facing south.
There is also a button to the east of level 6 (south), currently facing south.

Step on the (south) right-hand plate to rotate the wall in front of you. Do it four times.
Click the blue button to rotate the wall east of level 6 (middle).
Go to level 6 (middle). Click the blue button to vanish an obelisk. Current configuration: _,X,_.
Step on the (north) left-hand plate and click the red button to vanish the (south) middle plate.
Click the (south) green button to vanish the (north) middle plate.
Click the (north) green button to vanish the (south) left-hand plate.
Click the (south) red button to rotate the shed.
Turn right. Face the wooden door that has just appeared.
Open the wooden door with a common key. Collect the night key (and elven plate and a chaos ring).
Click the (north) blue button to vanish an obelisk. Current configuration: _,_,_.

Step on the middle portal plate.
Collect the sun key.
Descend.
Open the ape door with the night key. You've been here before!
(You should still be carrying a sun key and a crystal key, by the way.)
Descend. Descend. Descend to level 2.
Go out the door and north.
Click the red button next to the bed to vanish a wall to your left. Go through.
(Collect an elf gloves.)
(Open the barred door. Kill a demon, a frogman, and two minotaurs. Collect an elven helm and a scroll of fireward.)
Face the barred door. The wall to your right is illusory. Go east.
(Collect 10 hail of doom. Visit the Potions shop.)
Open the wooden door with a common key. Ascend.
Open the ape door with the sun key.
The sign says, "YOU HAVE DONE WELL / NOW THE CHALLENGE BEGINS".
(Collect 10 hail of doom.)
Open the double doors with a common key. Kill a death knight, an orc, and a demon.
(The barred door to your right requires a serpent key.)
Bear left and around. Kill two death knights and a roundhead.
(Collect a frost bow and 10 hail of doom.)
(Open the wooden door with a common key. Collect a mithril chain.)
This is a good time to visit the bed and level up to Level 11!
Open the barred door on the left. Kill the knight. (Collect a Hedjog Venom.)
Make a U-turn to the right. Collect the silver key. Go back out.
Open the barred door to the right. Kill the mage.
Open the ape door with the silver key. Collect the serpent key (and a war shield).
Go back south and out almost to the double doors.
Open the barred door with the serpent key.
Ascend.
Explore this area.
Descend. Kill a minotaur, an orc, a knight, a demon, and two more minotaurs.
(Collect a Chymera Blood and a scroll of ethblade.)
(At the end of this area, collect an apple and a Chaos Amulet.)
(Open the wooden door in the southeast corner with a common key. Collect an elf gloves.)
Ascend again.
Use the moon gem in the slot. (Collect 10 elf arrows.)
Open the barred door. Kill two death knights and a minotaur. (Collect a power potion.)
Open the wooden door with a common key. Kill the knight, death knight, and minotaur.
(Collect an Orc's Vomit, a cheese, and The Watcher.)
Collect the silver key.
Go back the way you came. Use the moon gem to return.
Use the fire gem in the slot. (Collect 10 elf arrows and a moon elixir.)
Open the barred door. Turn left. Kill the orc, death knight, and demon. Collect the Grey Axe and the gold key.
Open the wooden door with a common key. (Collect a scroll of wizeye.)
Open the next wooden door. Kill the roundhead, orc, and frogman. (Collect a Dragon Ale.)
Open the ape door with the gold key.
Open the ape door with the silver key.
Click the green button to vanish the obelisk opposite. Turn around! Kill the knight.
Face the pit and turn right. Collect a well-disguised ruby key (and a power potion).
Watch out for the pit here. Open the ape door.
Go back to the green button and turn left. Ascend to level 5.
Open the barred door. Kill the orc, two shreks, a minotaur and a roundhead.
Explore this area. (Watch for orientation-flipping traps!)
(Collect 10 elf arrows. Collect a Hedjog Venom.)
The sign says, "THE WIZARD HAS LOST CONTROL".
In the northwest corner, collect a second ruby key.
In the southwest corner, go through the illusory wall. Kill the orc.
Open the barred door with one of your ruby keys.
==HERE== (saved 1-Q.sav)
Step on the plate three times to rotate the shed. Open the wooden door. (The barred door requires a gold key.)
Step on the plate one more time. Go through the shed.
(Open the wooden door. Nothing here but a bed.)
(Open the wooden door in the southeast corner. Collect a doom helm.)
(The barred door requires a sun key.)
Go out the way you came. Turn right. Collect the night key.
(Collect a scroll of suspend. Collect crystal chain.)
Go back to the northeast corner and descend to level 4.
(You should be carrying a night key, a ruby key, and a crystal key.)
Go to the knight's pit and jump in.
(Collect 10 elf arrows and a cheese.)
Open the wooden door. Kill two minotaurs.
Open the wooden door with a common key. Descend. You've been here before!
Make a U-turn to the right.
Open the ape door with the ruby key. Go forward and kill an orc, a minotaur, and a demon.
The sign says, "THE GREAT BLADE".
Open the barred door. Collect the Rune Sword.
Go back out the way you came.
Ascend the south staircase. Ascend. Ascend to level 5.
Go straight and U-turn right. Jump in the pit.
U-turn right. Go into the shed and step on the portal plate.
The sign says, "ONLY THEY WITH THE QUICKEST HAND AND KEENEST EYE WILL PREVAIL".
Bear left and ascend. Kill the death knight.
(Collect an apple and a red n'egg.)
The sign says, "BE BRAVE AND PRESS ONWARDS".
Step through the door. It will lock behind you.
Jump forwards into the pit. Click the green button as you fall!
(This vanishes a pillar to the north of the fallthrough. Jumping backwards and clicking the yellow button also works.)
When you get to the bottom, step on the plate to return to the top.
Jump in again. This time, use a scroll of levitate or cast levitate
as soon as you enter the top of the level below the pit. You'll land "on top of" the pit.
Go north. Ahead of you is the knight's pit.
Bear left at the green button. Ascend to level 5.
Make your way to the southwest corner.
Step on the plate three times to rotate the shed. Go through.
==HACK== At this point I cheated to gain a sun key.
Open the barred door with the sun key. Kill the death knight.
Collect the gold key (and a scroll of trueview).
Go back through the shed. Step on the plate three more times.
Open the barred door with the gold key. Kill the minotaur.
Ascend. Monsters come from both directions! Kill two skavens and two frogmen.
(Collect a Chymera Blood. At the end of this hall, collect a Death Blade.)
Open the wooden door with a common key.
Straight ahead is an illusory wall hiding an orc. Kill the orc.
Kill the death knight and the skeleton.
(This area is full of orientation-flipping traps.)
Open the wooden door to the west. Kill the roundhead. (Collect elf boots.)
Open the wooden door to the north. Collect the serpent key.
(Open the wooden doors to the east and south. Nothing.)
Go west. Open the north-facing ape door with the serpent key.
Open the ape door with the night key.
Ascend to level 7.
The sign says, "PREPARE TO DIE ACCURSED DEFILERS". But this area is empty.
(Collect a biscuit.)
Ascend.
Descend.
(To your north there are two ape doors, both requiring sun keys; and a barred door that does not budge.)
Turn left. Open the wooden door. Jump in the pit.
Open the barred door. (Collect a corn.)
Open the wooden door.
Open the wooden door with a common key. Kill the roundhead and the death knight.
Hug the left wall. Collect the sun key (and Grim Reaper and scroll of renew).
Open the wooden door with a common key. Kill the demon and the death knight.
Hug the left wall. Collect the silver key.
Go to the southeast corner. Open the ape door with the silver key.
Ascend. Kill the ogre. Collect a second sun key (and 10 hail of doom and a power potion).
Click the yellow button to vanish the obelisk to your left. Go through the gap.
Open the ape door to the left with a sun key. Kill the minotaur. (Collect chaos gloves and a red n'egg.)
Click the yellow button to your left to open the barred door leading to the Horn of Xtlaltic.
Open the ape door to the right with a sun key. Kill the minotaur. (Collect a purple n'egg and chaos plate.)
Click the yellow button to vanish an obelisk to the left of the Horn and release four monsters.
Kill four monsters.
Go through the barred door and bear left. (There is a teleport trap in front of it.)
Collect an Amber Amulet.
Click the yellow button to disable the teleport trap.
Take the Horn of Xtlaltic from the wall!
Go back and jump in the pit.
Go to the unopened north-facing wooden door on the east side of this level. Open it with a common key.
Jump in the pit.
Go to the northeast corner and descend.
Go west to the knight's pit and jump in the pit.
Go south through the wooden doors and descend.
Go straight and turn left through the open door. Make your way to the closed door on the east side just north of the stairs.
Open the barred door with the crystal key.
Descend.
Take the portal back to the Keep.
Sell off your trade goods.
Make your way to the stairs and ascend; go straight and ascend; turn left.
Place the Horn of Xtlaltic in the last slot!
(This will bring up an antipiracy screen. Use hexx-manual.pdf to answer the questions.)
The final grated door to your west has opened.


Area 11: The Wizard's Castle
----------------------------

The sign says, "THE WIZARD WILL NOT SUFFER ANY MORTAL TO TRESPASS / -KEEP OUT-".
Step on the portal plate. Kill the demon and the death knight.
Go north. Collect the gold key from the alcove to your right.
Open the gold door.
(Turn left. Open the wooden door. It's just a bed.)
(Collect 10 elf arrows.)
Open the grated door with the gold key. Kill the red ogre. (Collect a scroll of formwall.)
Turn right. Open the wooden door with a common key. Collect the sun key.
Open the grated door with the sun key. Kill two skeletons.
Follow the left wall. Open the wooden door. Collect the serpent key.
Go back to the big room you started in. Go south.
The sign says, "THE WIZARD BIDS YOU ENTER".
Open the gold door with the serpent key. Kill the death knight.
Follow around to the left. Kill the demon and the ogre.
Open the south-facing wooden door with a common key. Kill two skeletons.
Collect the silver key (and a scroll of vivify).
Continue east. (Collect a Chymera Blood.)
Open the gold door with the silver key. Ascend.
(This whole level is anti-magic.)
Turn right. Kill the skeleton.
(Collect 10 hail of doom.)
Open the door to the big shed in the northeast corner of the map. Collect the gold key.
(Open the west-facing wooden door. Collect a stasis blade.)
Return southward.
(The gold door requires a night key.)
The sign says, "BEWARE THE LEGION OF THE UNDEAD".
Open the grated door with the gold key. Kill six skeletons. (Use the door strategically!)
Enter and kill five more skeletons.
(Collect crystal boots.)
Open the wooden door at the end of this area. (Collect 10 elf arrows.)
Click the green square to vanish a brazier in front of the blue square in the previous area.
Click the blue square. (???)
Click the purple dot to vanish a brazier at the west end of this area.
Go through the gap. Collect the night key (and 10 elf arrows).
Go back out and U-turn to your left. Open the gold door with the night key. This area is empty.
(Open the wooden door at the end of the hall; it's just a bed.)
The sign says, "NONE SHALL PASS".

    1 h 3
    4 5 6
    7 8 9

Stepping on any plate toggles the pit at "h". Don't worry about this for now.
(The doors ahead and right will not budge. The door to the left needs a ruby key.)
Going down the pit drops you into a new area! Find and kill the skeleton.
(Collect 10 elf arrows and a red n'egg.)
Open the wooden door. Kill the skeleton.
Open the wooden door with a common key. Kill two ogres and two skeletons. Collect the crystal helm.
In the northwest corner of this room, collect a well-hidden ruby key.
(Go out and northeast. Open the south-facing wooden door. Kill two skeletons. Collect two n'eggs.)
Go to the north side of the level. Open the gold door. Ascend.
Click the red square to vanish a brazier in the south passage. You've been here before!
Open the left-hand door with the ruby key.
Step on the plate to change the vanishing pit at "h" into a vanishing plate at "h".
Step on the plate at "h" to open the right-hand door. Kill the two skeletons.
Click the red square to open the gold door. Go through the open door. This area is empty.
Open the wooden door straight ahead. Collect the silver key, the Harvester, and 10 hail of doom.
Go left. Open the gold door with the silver key. (Collect a red n'egg.)
Open the wooden door with a common key. Kill the ogre.
The sign says, "DRAGON TO CHAOS AND THEN THE LAST".
(Collect a scroll of ethblade and a scroll of suspend.)
Open the wooden door with a common key. Ascend.
Open the barred door. (Collect a moon elixir.)
Open the wooden door with a common key. Kill the death knight, two ogres, and a demon.
Collect the sun key.
Open the grated door with the sun key. Kill the orc.
Open the gold door.
(The grated door to your left requires a serpent key.)
Open the grated door to your right. Kill two demons, a skeleton, and an ogre.
The sign says, "USING THE MOON WILL OPEN THE TOMB".
Collect the serpent key.
Open the grated door with the serpent key.
(Turn left. Open the wooden door with a common key. Kill two skeletons. Collect 10 arrows.)
(Open the south-facing wooden door. Kill the skeleton and the orc. Collect crystal gloves.)
(In the middle of this area is an orientation-flipping trap.)
Go east. Open the wooden door with a common key. Kill the blue skeleton.
Open the wooden door with a common key.
When you hit the orientation-flipping trap, face west. Go down to the already-open wooden door.
Collect the ruby key.
Go back to the orientation-flipping trap. Face east. Go up to the gold door.
Open the gold door with the ruby key. Kill the death knight and the demon.
