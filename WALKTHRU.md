
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
- You could also work around it by carrying many piles of 1 key each; but this is not good enough to finish the game.

Before the first time you go downstairs, visit a shop and buy 99 common keys. Hold them in your cursor
every time you go up or down levels. Do this until you find your first backpack; then put your keys
in your backpack.

Reportedly you can hack 99 keys into your front right character's left hand by hex-editing the bytes "8F 63"
into offset 0xB15A of your save file. I have not tested this.

Cutscene Bug
------------

Picking up the talisman of a god triggers a cutscene (and anti-piracy verification). If you are playing
in DOSBox, this won't work and the game will just hang with a black screen.

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
- Regen
- Ethblade
- Spelltap
- Vivify
- Disrupt

### Red Spells (Dragon Magic)
- Missile (100 GP)
- Torch (200 GP)
- Fireward (200 GP)
- Dispell (300 GP)
- Fireball
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

Most items can be ignored and sold off for cash (to buy spells), but the following are permanently useful:

- Power Potion (increases SP above maximum, to enable learning spells whose starting SP cost is too high)
- Dragon Ale (increases INT by 1)
- Orc's Vomit (increases STR by 1)
- Cloud Amulet (???)
- Serpent Amulet (increases STR by 5 when worn)


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
This room has two beds, and you've just hit 25,000 XP. Sleep to level up to Level 5!
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
(Take the green Eye from the wall. This should start a cutscene. If it doesn't, download WIZ.COM and try again.)
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
==HERE== (saved 1-J.sav)
To the north are some illusory walls hiding a sign that says "PARTING IS SUCH SWEET SORROW" and two gem slots.
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
Crossing the center line of the room will flip your orientation and fizzle all your spells.
Step diagonally past the second pit. Step on the portal plate. The pit vanishes.
