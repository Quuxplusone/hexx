
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

Locations are encoded as 2-byte little-endian quantities. Each square of the dungeon map is divided
into four quadrants for the purposes of item location. The quadrants (northwest being upper left)
are encoded in the high-order 2 bits of the little-endian quantity:

    0___ 4___
    8___ C___

So for example if 1ABC is the northwest quadrant of some tile, then 9ABC is the southwest quadrant of
that same tile. (But remember that these will appear in the file as "BC 1A" and "BC 9A" respectively.)

                            062E
                            066C
    06A0  06A2  06A4  06A6  06A8  06AA  06AC
    06DE  06E0              06E8

    (053A is the far corner)
    (0758 is the dagger dead-end)

0758 = "58 x7"

Facing is stored as a 2-byte little-endian quantity. 0000 is due south, 0040 is due west, 0080 is
due north, and 00C0 is due east. Then it wraps around and keeps going; it actually tracks how many
full rotations you've made, so that 1234 is a valid facing and means "west-south-west, having netted
exactly 18 rightward full rotations over the course of the game."

Spell knowledge is encoded as a 32-bit bitfield. For example, if you know the first spell in each
of the four schools of magic, that's "80 80 80 80". If you know all of the Earth (Green) spells,
that's "FF 00 00 00".


Offsets [0x0000 .. 0x6100) ??? 24832 bytes

Offsets [0x6100 .. 0x8000) memory-mapped heap of floor-item records
- Offsets 0,1 define the location of the object in the dungeon.
- Offset 2 defines the length of this record in bytes (i.e., this byte must be at least 06).
- Offset 3 is invariably zero.
- Offsets 4,5 define the first item at this location; offsets 6,7 define the second item, and so on.
However, there's some funny business occasionally. I think this is a memory-mapped data structure of some sort,
and contains occasional garbage bytes in the interstices.


Offsets [0x8000 .. 0x8004) ??? 4 bytes "FC ED DA CB"
Offsets [0x8004 .. 0x8022) hold the name of the savegame as 29 bytes of space-padded ASCII plus a null terminator.

Offsets [0x8022 .. 0xA022) memory-mapped heap of monster records (32 bytes each)
- Offsets 0,1 store the "next record" pointer, as an offset into [0x8000 .. 0xA000). The special value "FF FF" means "done."
- ???
Offsets [0xA022 .. 0xA02E) ??? 10 bytes
Offsets [0xA02C .. 0xA02E) define the player's facing. (But modifying this is deadly.)
Offsets [0xA02E .. 0xA030) define the player's location. (But modifying this is deadly.)
Offsets [0xA030 .. 0xA032) define the character whose spells are visible (0..3).
Offsets [0xA032 .. 0xA034) define the highlighted character (0..3, or 0x81 for "none").
Offsets [0xA034 .. 0xA03A) ??? 6 bytes
Offsets [0xA03A .. 0xA03C) is a pointer `p` where `0x8000 + p` is the head of the monster list (???).
Offsets [0xA03C .. 0xA03E) is a pointer `p` where `0x8000 + p` is 32 bytes past the tail of the monster list.
Offsets [0xA03E .. 0xA040) define the item "held in the cursor."

Offsets [0xA040 .. 0xB0CC) ??? 4236 bytes

Offsets [0xA50A .. 0xAC8C) define map data for the current level (up to 31x31x2 bytes).
Each dungeon tile is represented by a 2-byte little-endian value.
Flag 0080 is "monster(s) here"
Flag 0040 is "item(s) here"
Flag 0008 is "explored, i.e., show on map"
Bits 0101 indicate a wall decoration of some kind.

The banner designs are not controllable; they cycle based on (x,y) coordinates.
The obelisk/brazier designs are not controllable; they cycle every 4x4 tiles.


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
- Offsets [0xB110 .. 0xB118) ??? 8 bytes
- Offsets [0xB118 .. 0xB119) defines the character's readied spell (00 = armour, 1F = mindrage, 20 = no spell)
- Offsets [0xB119 .. 0xB11A) defines the character's readied spellbook (00 = green, 03 = purple)
- Offsets [0xB11A .. 0xB11C) ??? 2 bytes
- Offsets [0xB11C .. 0xB124) contains the character's first name, padded with FF bytes on the end.
- Offsets [0xB124 .. 0xB130) contains the character's last name, padded with FF bytes on the end.
- Offsets [0xB130 .. 0xB131) define the character's hunger level (00 = starving, FF = stuffed).
- Offsets [0xB131 .. 0xB132) seems to always be FF.
- Offsets [0xB132 .. 0xB136) ??? 4 bytes of zeros

Offsets [0xB136 .. 0xB1A0) define the front-right character (106 bytes).
Offsets [0xB1A0 .. 0xB20A) define the rear-left character (106 bytes).
Offsets [0xB20A .. 0xB274) define the rear-right character (106 bytes).

Offsets [0xB274 .. 0xB278) ??? 4 bytes of zeros

Offsets [0xB278 .. 0xB298) define the contents of backpack 0x00 (found just after "FAST ROUTE DOWN").
Offsets [0xB298 .. 0xB2B8) define the contents of backpack 0x01 (found in the Tower of Grisslem).
Offsets [0xB2B8 .. 0xB2D8) define the contents of backpack 0x02 (probably???)

Offsets [0xB2D8 .. 0xE004) ??? 11564 bytes

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
