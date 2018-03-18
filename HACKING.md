
Each character's vital statistics and inventory are encoded in 106 bytes, one after the other,
starting with the front-left character at offset 0xB0CC.

Each character's inventory slots occupy a range of 32 bytes. The first two bytes define the helm slot;
the next two define the armour slot; and so on, through the left and right hand slots and the eight regular
inventory slots.

Each inventory slot is encoded in two bytes. The first byte defines the item type; the second byte
defines the number of items or charges in that slot (for stackable/chargeable items).
For nonstackable items, the second byte should be set to "0x01" (although the game seems to ignore that byte anyway).
For torches, the second byte should be set to the remaining life of the torch (between 0x00 and 0x15).
For backpacks, the second byte should be set to the "backpack number" (see below).
For empty slots, both bytes should be set to "0x00".

Each "shop item" is encoded in a single byte, for the item type. There is no "quantity" byte; instead,
all stackable items are available in infinite quantities, and otherwise there's an implicit quantity of "1".
Each shop contains a maximum of 7x4x2 = 56 items.

Locations are encoded as 2-byte little-endian quantities. Each square of the dungeon map is divided
into four quadrants for the purposes of item location. The quadrants (northwest being upper left)
are encoded in the high-order 2 bits of the little-endian quantity:

    0___ 4___
    8___ C___

So for example if 1ABC is the northwest quadrant of some tile, then 9ABC is the southwest quadrant of
that same tile. (But remember that these will appear in the file as "BC 1A" and "BC 9A" respectively.)
Locations on the current level (such as the player's position, and floor-items in the "current level"
cache) are represented as indices into the current level's map (so, 2*(y*LEVELWIDTH+x)). For example,
location C000 represents the southeast corner of the northeast corner of the map, and if the current
level is exactly 16 tiles wide, then 0022 represents the NE corner of the tile southeast of that one
(because 2*(1*16+1) = 0x22).

"Floor-items" are represented as lists of consecutive variable-length records in the following format:
    <location> <record-length> <item-slot...>
where "location" is an index into the current level's map (so, 2*(y*LEVELWIDTH+x), with the 0xC000 bits
indicating the quadrant of the tile), "record-length" is 4+2*ITEMCOUNT, and the next ITEMCOUNT "item-slots"
use the usual representation for inventory slots except that usually single keys get a count of 10
for some as-yet-unknown reason.

The player's facing is stored as a 2-byte little-endian quantity. 0000 is due south, 0040 is due west,
0080 is due north, and 00C0 is due east. Then it wraps around and keeps going; it actually tracks
how many full rotations you've made, so that 1234 is a valid facing and means "west-south-west,
having netted exactly 18 rightward full rotations over the course of the game."

Spell knowledge is encoded as a 32-bit bitfield. For example, if you know the first spell in each
of the four schools of magic, that's "80 80 80 80". If you know all of the Earth (Green) spells,
that's "FF 00 00 00".


Offsets [0x0000 .. 0x6100) ??? 24832 bytes

Offsets [0x6100 .. 0x8000) define the floor-items on all levels EXCEPT the current level; see offset 0xA038 for details

Offsets [0x8000 .. 0x8004) ??? 4 bytes "FC ED DA CB"
Offsets [0x8004 .. 0x8022) hold the name of the savegame as 29 bytes of space-padded ASCII plus a null terminator.

Offsets [0x8022 .. 0xA022) memory-mapped heap of monster records (32 bytes each)
- Offsets 0,1 store the "next record" pointer, as an offset into [0x8000 .. 0xA000). The special value "FF FF" means "done."
- ???

Offsets [0xA022 .. 0xA024) defines the current dungeon tower (0=Keep, 1=Grisslem, etc).
Offsets [0xA024 .. 0xA026) defines the current dungeon level within the tower (0 through 7).
Offsets [0xA026 .. 0xA028) defines the player's X coordinate, in units of 0x80ths of a tile.
Offsets [0xA028 .. 0xA02A) defines the player's Z coordinate (0B is normal; 8A is suspended; may be negative if falling through a pit).
Offsets [0xA02A .. 0xA02C) defines the player's Y coordinate, in units of 0x80ths of a tile.
Offsets [0xA02C .. 0xA02E) define the player's facing.
Offsets [0xA02E .. 0xA030) define the player's tile location, which must be in agreement with the X and Y coordinates defined above.
Offsets [0xA030 .. 0xA032) define the character whose spells are visible (0..3).
Offsets [0xA032 .. 0xA034) define the highlighted character (0..3, or 0x81 for "none").
Offsets [0xA034 .. 0xA038) ??? 4 bytes
Offsets [0xA038 .. 0xA03A) is the length of the global items list starting at 0x6100.
Offsets [0xA03A .. 0xA03C) is a pointer `p` where `0x8000 + p` is the head of the monster list (???).
Offsets [0xA03C .. 0xA03E) is a pointer `p` where `0x8000 + p` is 32 bytes past the tail of the monster list.
Offsets [0xA03E .. 0xA040) define the item "held in the cursor."

Offsets [0xA040 .. 0xA042) ??? 2 bytes

Offset 0xA042 is a countdown for Torch (max value 0xFF).

Offsets [0xA043 .. 0xA056) ??? 19 bytes

Offsets [0xA056 .. 0xA05D) are the strengths of continuous-effect spells in the spell bar:
- Offset A056 is the current strength of Armour.
- Offset A057 is the current strength of Levitate.
- Offset A058 is the current strength of Warpower.
- Offset A059 is the current strength of Deflect.
- Offset A05A is the current strength of Antimage.
- Offset A05B is the current strength of Trueview.
- Offset A05C is the current strength of Regen.

Offsets [0xA05D .. 0xA064) ??? 7 bytes

Offsets [0xA064 .. 0xA09C) define the items for sale in Ye Shoppe, one byte apiece. (7 per row x 4 rows x 2 pages = 56 bytes.)
Offsets [0xA09C .. 0xA0D4) define the items for sale in Ozzrik's
Offsets [0xA0D4 .. 0xA10C) define the items for sale in Ye Armoury.
Offsets [0xA10C .. 0xA144) define the items for sale in the Grog Shop.
Offsets [0xA144 .. 0xA17C) define the items for sale in the south shop in Shaspuok's tower.
Offsets [0xA17C .. 0xA1B4) define the items for sale in the north shop in Shaspuok's tower.

Offsets [0xA1B4 .. 0xA23C) ??? 136 bytes

Offsets [0xA23C .. 0xA240) define the width and height of the current dungeon level's map.

Offsets [0xA240 .. 0xA50A) ??? 714 bytes

Offsets [0xA50A .. 0xAC8C) define map data for the current level (up to 31x31x2 bytes).
Each dungeon tile is represented by a 2-byte little-endian value.
Flag 0080 is "monster(s) here"
Flag 0040 is "item(s) here"
Flag 0008 is "explored, i.e., show on map"
Bits 0101 indicate a wall decoration of some kind.

The banner designs are not controllable; they cycle based on (x,y) coordinates.
The obelisk/brazier designs are not controllable; they cycle every 4x4 tiles.

Offsets [0xAC8C .. 0xB0CC) ??? 1088 bytes


Offsets [0xB0CC .. 0xB136) define the front-left character (106 bytes):
- Offsets [0xB0CC .. 0xB0CD) defines which of the 16 characters this is.
- Offsets [0xB0CD .. 0xB0CF) ??? 2 bytes
- Offsets [0xB0CF .. 0xB0D0) define the character's current Level.
- Offsets [0xB0D0 .. 0xB0D2) define the character's current SP, little-endian, 2 bytes.
- Offsets [0xB0D2 .. 0xB0D4) define the character's max SP, little-endian, 2 bytes.
- Offsets [0xB0D4 .. 0xB0D6) define the character's current HP, little-endian, 2 bytes.
- Offsets [0xB0D6 .. 0xB0D8) define the character's max HP, little-endian, 2 bytes.
- Offsets [0xB0D8 .. 0xB0DA) define the character's current vitality (blue bar).
- Offsets [0xB0DA .. 0xB0DC) define the character's max vitality (blue bar).
- Offsets [0xB0DC .. 0xB0E0) define the character's GP, little-endian, 4 bytes.
- Offsets [0xB0E0 .. 0xB0E4) define the character's XP, little-endian, 4 bytes.
- Offsets [0xB0E4 .. 0xB0F0) define the character's worn items.
- Offsets [0xB0F0 .. 0xB0F4) define the character's wielded items.
- Offsets [0xB0F4 .. 0xB104) define the character's inventory.
- Offsets [0xB104 .. 0xB108) define the character's spell knowledge.
- Offsets [0xB108 .. 0xB109) define the character's current STR (including amulet boosts).
- Offsets [0xB109 .. 0xB10A) define the character's intrinsic STR.
- Offsets [0xB10A .. 0xB10B) define the character's current INT (including amulet boosts).
- Offsets [0xB10B .. 0xB10C) define the character's intrinsic INT.
- Offsets [0xB10C .. 0xB10D) define the character's current DEX.
- Offsets [0xB10D .. 0xB10E) define the character's intrinsic DEX.
- Offsets [0xB10E .. 0xB10F) define the character's current CON.
- Offsets [0xB10F .. 0xB110) define the character's intrinsic CON.
- Offsets [0xB110 .. 0xB111) define the character's current AC (00 = +10, 01 = +9, etc.)
- Offsets [0xB110 .. 0xB111) define the character's intrinsic AC.
- Offsets [0xB112 .. 0xB118) ??? 6 bytes
- Offsets [0xB118 .. 0xB119) defines the character's readied spell (00 = armour, 1F = mindrage, 20 = no spell)
- Offsets [0xB119 .. 0xB11A) defines the character's readied spellbook (00 = green, 03 = purple)
- Offsets [0xB11A .. 0xB11C) ??? 2 bytes
- Offsets [0xB11C .. 0xB124) contains the character's first name, padded with FF bytes on the end.
- Offsets [0xB124 .. 0xB130) contains the character's last name, padded with FF bytes on the end.
- Offsets [0xB130 .. 0xB131) define the character's hunger level (00 = starving, FF = stuffed).
- Offsets [0xB131 .. 0xB132) ??? usually 0xFF, but can be 0x00
- Offsets [0xB132 .. 0xB136) ??? usually zeros, but second byte can be 0x12

Offsets [0xB136 .. 0xB1A0) define the front-right character (106 bytes).
Offsets [0xB1A0 .. 0xB20A) define the rear-left character (106 bytes).
Offsets [0xB20A .. 0xB274) define the rear-right character (106 bytes).

Offsets [0xB274 .. 0xB278) ??? 4 bytes of zeros

There are four backpacks in the game, each with 12 inventory slots.
Offsets [0xB278 .. 0xB290) define the contents of backpack 0x00 (found just after "FAST ROUTE DOWN").
Offsets [0xB290 .. 0xB2A8) define the contents of backpack 0x01 (found in Grisslem's tower).
Offsets [0xB2A8 .. 0xB2C0) define the contents of backpack 0x02 (found in Shaspuok's tower).
Offsets [0xB2C0 .. 0xB2D8) define the contents of backpack 0x03 (found in Angrath's tower).

Offsets [0xB2D8 .. 0xE004) ??? 11564 bytes


Offsets [0xB2F4 .. 0xB2F6) define the number of bytes in the floor-item-list that follows.
- The next that-many bytes [0xB2F6 ...) define the floor-items on the current level.
- Blanking this data in a save file removes the items from the current level. When you change levels, this cached data
  is written back into the compressed global data, which means that the items disappear from there too, forever.
- Blanking the global data will NOT affect the items on the current level, but it can make the game crash when
  you change levels and the game tries to load items from global that aren't there anymore.

Offsets [0xC2F6 .. 0xDB6A) look like maybe more monster records???


Offsets [0xE004 .. 0xE1E8) are the front-left character's big thumbnail, as a 256-color 22x22 bitmap.
Offsets [0xE1E8 .. 0xE2E8) are the front-left character's small thumbnail, as a 256-color 16x16 bitmap.
Offsets [0xE2E8 .. 0xE4CC) are the front-right character's big thumbnail, as a 256-color 22x22 bitmap.
Offsets [0xE4CC .. 0xE5CC) are the front-right character's small thumbnail, as a 256-color 16x16 bitmap.
Offsets [0xE5CC .. 0xE7B0) are the rear-left character's big thumbnail, as a 256-color 22x22 bitmap.
Offsets [0xE7B0 .. 0xE8B0) are the rear-left character's small thumbnail, as a 256-color 16x16 bitmap.
Offsets [0xE8B0 .. 0xEA94) are the rear-right character's big thumbnail, as a 256-color 22x22 bitmap.
Offsets [0xEA94 .. 0xEB94) are the rear-right character's small thumbnail, as a 256-color 16x16 bitmap.
Offsets [0xEB94 .. 0xED78) are the big thumbnail used for dead characters, as a 256-color 22x22 bitmap.
Offsets [0xED78 .. 0xEE78) are the small thumbnail used for dead characters, as a 256-color 16x16 bitmap.
Offsets [0xEE78 .. 0xF670) are the save-game thumbnail image, as a 256-color 60x34 bitmap.


Item Numbers
------------

Byte | Item
----------------
  00 | empty
  01 | leather cap
  02 | helm
  03 | full helm
  04 | war helm
  05 | golden helm
  06 | blood helm
  07 | elven helm
  08 | doom helm
  09 | crystal helm
  0A | leathers
  0B | chain mail
  0C | plate mail
  0D | mithril chain
  0E | mithril plate
  0F | blood leathers
  10 | elven chain
  11 | elven plate
  12 | crystal chain
  13 | chaos plate
  14 | crystal plate
  15 | leather gloves
  16 | gauntlets
  17 | mithril gloves
  18 | battle gloves
  19 | elf gloves
  1A | chaos gloves
  1B | crystal gloves
  1C | leather buckler
  1D | buckler
  1E | large shield
  1F | arc shield
  20 | battle bane
  21 | moon shield
  22 | bane shield
  23 | golden shield
  24 | heron shield
  25 | war shield
  26 | dragon shield
  27 | the watcher
  28 | crystal shield
  29 | leather boots
  2A | iron boots
  2B | mithril boots
  2C | blood boots
  2D | elf boots
  2E | crystal boots
  2F | serpent amulet
  30 | night amulet
  31 | dragon amulet
  32 | chaos amulet
  33 | cloud amulet
  34 | moon amulet
  35 | amber amulet
  36 | dagger
  37 | stealth blade
  38 | death blade
  39 | stasis blade
  3A | short sword
  3B | long sword
  3C | mithril blade
  3D | mithril sword
  3E | heron blade
  3F | dragon doom
  40 | scream slicer
  41 | rune sword
  42 | vorpal blade
  43 | hand axe
  44 | battle axe
  45 | mithril axe
  46 | deathbringer
  47 | brainbiter
  48 | grey axe
  49 | slugger
  4A | staff
  4B | battle staff
  4C | etherial axe
  4D | etherial staff
  4E | etherial sword
  4F | etherial dagger
  50 | crossbow
  51 | long bow
  52 | elf bow
  53 | frost bow
  54 | harvester
  55 | arrows (x)
  56 | elf arrows (x)
  57 | hail of doom (x)
  58 | snake staff (c)
  59 | firestaff (c)
  5A | grim reaper (c)
  5B | power staff (c)
  5C | sun staff (c)
  5D | cloud staff (c)
  5E | serpent wand (c)
  5F | dragon wand (c)
  60 | night wand (c)
  61 | chaos wand (c)
  62 | amber wand (c)
  63 | cloud wand (c)
  64 | serpent ring (c)
  65 | chaos ring (c)
  66 | dragon ring (c)
  67 | night ring (c)
  68 | cloud ring (c)
  69 | moon ring (c)
  6A | amber ring (c)
  6B | scroll of formwall
  6C | scroll of vivify
  6D | scroll of fireward
  6E | scroll of ethblade
  6F | scroll of wizeye
  70 | scroll of suspend
  71 | scroll of trueview
  72 | scroll of renew
  73 | scroll of levitate
  74 | scroll of antimage
  75 | scroll of regen
  76 | hedjog venom
  77 | chymera blood
  78 | moon elixir
  79 | phoenix broth
  7A | dragon ale
  7B | power potion
  7C | orc's vomit
  7D | apple
  7E | biscuit
  7F | corn
  80 | drumstick
  81 | bread
  82 | cheese
  83 | blue n'egg
  84 | green n'egg
  85 | yellow n'egg
  86 | purple n'egg
  87 | red n'egg
  88 | gold key
  89 | silver key
  8A | serpent key
  8B | sun key
  8C | ruby key
  8D | night key
  8E | crystal key
  8F | common key (x)
  90 | Eye of Grisslem
  91 | Horn of Xtlaltic
  92 | Angrath's Heart
  93 | Shaspuok's Tear
  94 | gem gem (* same glyph as Shaspuok's Tear)
  95 | moon gem
  96 | gem gem (* same glyph as Shaspuok's Tear)
  97 | fire gem
  98 | backpack
  99 | torch (* unlit)
  9A | torch (* lighted)
  9B | bag of (x) gold

Items `9C` through `FF` are just garbage.
Notably, "EC" is an item that looks like a mithril axe but whose name is "Moon Moon".
