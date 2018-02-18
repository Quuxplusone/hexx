#!/usr/bin/env python

import argparse
import math
import operator
import os
import struct
import sys

# This is the 256-color palette used by HEXX. Colors are in in 0xRRGGBB format.
thumbnail_palette = [
    0x000000, 0x220607, 0x2F070B, 0x3C0F13, 0x4E1616, 0x5A1E1E, 0x662B26, 0x773132,
    0x83403A, 0x904C42, 0xA1584E, 0xAD645A, 0xBD7466, 0xCA8272, 0xD6927F, 0xE6A38F,
    0x835EFF, 0x8663FF, 0x8E6FFF, 0x947AFF, 0x9B84FF, 0x9F88FF, 0xA692FF, 0xAD9CFF,
    0xB0A0FF, 0xB8AAFF, 0xBFB3FF, 0xC7BDFF, 0xCBC1FF, 0xD2CAFF, 0xDAD3FF, 0xE1DCFF,
    0x001600, 0x002300, 0x003400, 0x004600, 0x005700, 0x006800, 0x007900, 0x008B00,
    0x009C00, 0x00A800, 0x00B900, 0x00CA00, 0x00DC00, 0x00ED00, 0x00FE00, 0x00FF00,
    0x170015, 0x240021, 0x350032, 0x480043, 0x590054, 0x6A0064, 0x7C0074, 0x8E0086,
    0x9F0096, 0xAC00A2, 0xBD00B3, 0xCE00C3, 0xE000D4, 0xF100E5, 0xFF15F5, 0xFF38FF,
    0x020015, 0x020022, 0x060032, 0x0D0044, 0x120054, 0x180065, 0x200075, 0x280087,
    0x310097, 0x3800A3, 0x4100B4, 0x4C14C4, 0x5928D6, 0x6437E6, 0x7045F6, 0x7F58FF,
    0x141502, 0x1F2105, 0x2F3205, 0x3F4304, 0x4F5403, 0x5F6400, 0x6E7500, 0x7F8600,
    0x8E9700, 0x9AA300, 0xAAB400, 0xB9C400, 0xCAD600, 0xD9E600, 0xE9F700, 0xF9FF00,
    0x170000, 0x230000, 0x340000, 0x460000, 0x570000, 0x680000, 0x790000, 0x8B0000,
    0x9C0000, 0xA90000, 0xBA0000, 0xCB0000, 0xDD0000, 0xEE0000, 0xFF0000, 0xFF0000,
    0x220F07, 0x2E170A, 0x3F230C, 0x502A14, 0x5C3717, 0x6D441E, 0x7D5025, 0x8A6127,
    0x9A6D2E, 0xAA7D37, 0xB58F3D, 0xC69F44, 0xD6B04B, 0xE1C152, 0xF0D258, 0xFFE764,
    0x001602, 0x002206, 0x022F0D, 0x003B0F, 0x044917, 0x165523, 0x1D622B, 0x2B6E37,
    0x3A7A45, 0x468751, 0x599361, 0x659F6E, 0x78AB7F, 0x8FB694, 0xA0C1A4, 0xB6CDB9,
    0x220607, 0x2B080B, 0x371013, 0x45171B, 0x521F23, 0x5E272B, 0x662F33, 0x723D40,
    0x7E494C, 0x8C5558, 0x976568, 0x9F7274, 0xAB8385, 0xB69496, 0xC2A4A6, 0xCEB9BA,
    0x170115, 0x230221, 0x30072D, 0x3D073A, 0x4B0E47, 0x571D53, 0x64245F, 0x70316B,
    0x7C3F77, 0x8A4B84, 0x955D90, 0xA1699C, 0xAD7BA8, 0xB891B4, 0xC3A2BF, 0xCFB7CC,
    0x011514, 0x022120, 0x062D2C, 0x063A38, 0x0D4745, 0x1B5351, 0x235F5D, 0x306B6A,
    0x3E7776, 0x4A8483, 0x5C908F, 0x689C9B, 0x7BA8A7, 0x91B4B2, 0xA2BFBE, 0xB7CCCB,
    0x050215, 0x0A0521, 0x130B2E, 0x180E3A, 0x201647, 0x2C2253, 0x342A60, 0x40366C,
    0x4D4478, 0x585085, 0x686191, 0x746D9D, 0x847EA9, 0x9893B4, 0xA8A4C0, 0xBBB8CC,
    0x230000, 0x380000, 0x4F0000, 0x640000, 0x7D0000, 0x930000, 0xA80200, 0xC11E00,
    0xC93F00, 0xD15D00, 0xD77900, 0xE29500, 0xE7B000, 0xECD000, 0xF0EA00, 0xF9FF00,
    0x220600, 0x2F0800, 0x400F01, 0x511C00, 0x5E2403, 0x6E300A, 0x7F3D12, 0x8B4E19,
    0x9C5A27, 0xAC6B33, 0xB87B45, 0xC98D51, 0xD99D61, 0xE3B276, 0xF3C38C, 0xFFD7A0,
    0x101010, 0x1C1C1C, 0x2C2C2C, 0x3C3C3C, 0x494949, 0x595959, 0x696969, 0x757575,
    0x868686, 0x969696, 0xA2A2A2, 0xB2B2B2, 0xC3C3C3, 0xCFCFCF, 0xDFDFDF, 0xEFEFEF,
]
thumbnail_palette = zip(
    ((rgb & 0xFF0000) >> 16 for rgb in thumbnail_palette),
    ((rgb & 0x00FF00) >> 8 for rgb in thumbnail_palette),
    ((rgb & 0x0000FF) >> 0 for rgb in thumbnail_palette),
)
assert len(thumbnail_palette) == 256

def rgb_distance(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

def thumbnail_palette_closest(rgb):
    def key(p):
        return rgb_distance(rgb, thumbnail_palette[p])
    return sorted(range(256), key=key)[0]

def hexx_thumbnail_from_file(png_fname, w, h):
    try:
        from PIL import Image
    except ImportError:
        assert False, "Run 'pip install pillow' to install the PIL module"
    input_image = Image.open(png_fname).convert('RGB').resize((w, h), Image.LANCZOS)
    assert input_image.size == (w, h)
    input_data = [
        [input_image.getpixel((x, y)) for x in range(w)] for y in range(h)
    ]
    output_data = [None] * (w * h)
    for y in range(h):
        for x in range(w):
            rgb = input_data[y][x]
            p = thumbnail_palette_closest(rgb)
            output_data[y*w+x] = p
            error = map(operator.div, map(operator.sub, thumbnail_palette[p], rgb), [16.0]*3)
            if (x+1 < w):
                input_data[y][x+1] = tuple(map(operator.add, input_data[y][x+1], map(operator.mul, error, [7]*3)))
            if (y+1 < h):
                if (0 <= x-1):
                    input_data[y+1][x-1] = tuple(map(operator.add, input_data[y+1][x-1], map(operator.mul, error, [3]*3)))
                input_data[y+1][x] = tuple(map(operator.add, input_data[y+1][x], map(operator.mul, error, [5]*3)))
                if (x+1 < w):
                    input_data[y+1][x+1] = tuple(map(operator.add, input_data[y+1][x+1], map(operator.mul, error, [1]*3)))
    return ''.join(map(chr, output_data))

def dump_hexx_thumbnail(png_fname, content, w):
    try:
        from PIL import Image
    except ImportError:
        assert False, "Run 'pip install pillow' to install the PIL module"
    h = (len(content) + w - 1) / w
    content = content.ljust(w * h, '\0')
    output_image = Image.new('RGB', (w, h))
    for y in range(h):
        for x in range(w):
            p = ord(content[y*w+x])
            output_image.putpixel((x, y), thumbnail_palette[p])
    output_image.save(png_fname, 'PNG')

def as_hex(s):
    return ' '.join('%02X' % ord(ch) for ch in s)

def as_pixel(s):
    result = ''
    for ch in s:
        if ord(ch) < 0x10: result += ' '
        elif ord(ch) < 0x10: result += '.'
        elif ord(ch) < 0x20: result += ','
        elif ord(ch) < 0x30: result += ':'
        elif ord(ch) < 0x40: result += ';'
        elif ord(ch) < 0x50: result += '~'
        elif ord(ch) < 0x60: result += '/'
        elif ord(ch) < 0x70: result += '+'
        elif ord(ch) < 0x80: result += 'i'
        elif ord(ch) < 0x90: result += 't'
        elif ord(ch) < 0xA0: result += 'f'
        elif ord(ch) < 0xB0: result += 'g'
        elif ord(ch) < 0xC0: result += 'F'
        elif ord(ch) < 0xD0: result += 'K'
        elif ord(ch) < 0xE0: result += 'E'
        elif ord(ch) < 0xF0: result += '8'
        elif ord(ch) < 0x100: result += '#'
    return result

class Spells:
    ALL =      0xFFFFFFFF
    ARMOUR =   0x80000000
    HEALING =  0x40000000
    PARALYSE = 0x20000000
    LEVITATE = 0x10000000
    WARPOWER = 0x08000000
    ARC_BOLT = 0x04000000
    RENEW =    0x02000000
    FORMWALL = 0x01000000
    DEFLECT =  0x00800000
    TERROR =   0x00400000
    ANTIMAGE = 0x00200000
    REGEN =    0x00100000
    ETHBLADE = 0x00080000
    SPELLTAP = 0x00040000
    VIVIFY =   0x00020000
    DISRUPT =  0x00010000
    MISSILE =  0x00008000
    TORCH =    0x00004000
    FIREWARD = 0x00002000
    DISPELL =  0x00001000
    FIREBALL = 0x00000800
    FIREPATH = 0x00000400
    RECHARGE = 0x00000200
    INFERNO =  0x00000100
    CONFUSE =  0x00000080
    PHAZE =    0x00000040
    SUSPEND =  0x00000020
    TRUEVIEW = 0x00000010
    WIZEYE =   0x00000008
    MINDROCK = 0x00000004
    WYCHWIND = 0x00000002
    MINDRAGE = 0x00000001

class Items:
    @staticmethod
    def is_helm(item): return 0x01 <= item <= 0x09
    @staticmethod
    def is_armour(item): return 0x0A <= item <= 0x14
    @staticmethod
    def is_gloves(item): return 0x15 <= item <= 0x1B
    @staticmethod
    def is_shield(item): return 0x1C <= item <= 0x28
    @staticmethod
    def is_boots(item): return 0x29 <= item <= 0x2E
    @staticmethod
    def is_amulet(item): return 0x2F <= item <= 0x35
    @staticmethod
    def is_blade(item): return 0x36 <= item <= 0x42
    @staticmethod
    def is_axe(item): return 0x43 <= item <= 0x49
    @staticmethod
    def is_quarterstaff(item): return 0x4A <= item <= 0x4B
    @staticmethod
    def is_etherial(item): return 0x4C <= item <= 0x4F
    @staticmethod
    def is_bow(item): return 0x50 <= item <= 0x54
    @staticmethod
    def is_arrows(item): return 0x55 <= item <= 0x57
    @staticmethod
    def is_magic_staff(item): return 0x58 <= item <= 0x5D
    @staticmethod
    def is_magic_wand(item): return 0x5E <= item <= 0x63
    @staticmethod
    def is_magic_ring(item): return 0x64 <= item <= 0x6A
    @staticmethod
    def is_scroll(item): return 0x6B <= item <= 0x75
    @staticmethod
    def is_potion(item): return 0x76 <= item <= 0x7C
    @staticmethod
    def is_food(item): return 0x7D <= item <= 0x87
    @staticmethod
    def is_special_key(item): return 0x88 <= item <= 0x8E
    @staticmethod
    def is_common_key(item): return item == 0x8F
    @staticmethod
    def is_talisman(item): return 0x90 <= item <= 0x93
    @staticmethod
    def is_gem(item): return item in [0x95, 0x97]
    @staticmethod
    def is_backpack(item): return item == 0x98
    @staticmethod
    def is_torch(item): return 0x99 <= item <= 0x9A
    @staticmethod
    def is_bag_of_gold(item): return item == 0x9B
    @staticmethod
    def is_glitch(item): return item in [0x94, 0x96] or (0x9C <= item <= 0xFF)

    @staticmethod
    def is_stackable(item):
        return any(
            Items.is_arrows(item),
            Items.is_common_key(item),
        )

    @staticmethod
    def is_chargeable(item):
        return any(
            Items.is_torch(item),
            Items.is_magic_staff(item),
            Items.is_magic_wand(item),
            Items.is_magic_ring(item),
        )

    @staticmethod
    def is_unique(item):
        return any(
            Items.is_talisman(item),
            Items.is_gem(item),
        )

    NONE                = 0x00
    LEATHER_CAP         = 0x01
    HELM                = 0x02
    FULL_HELM           = 0x03
    WAR_HELM            = 0x04
    GOLDEN_HELM         = 0x05
    BLOOD_HELM          = 0x06
    ELVEN_HELM          = 0x07
    DOOM_HELM           = 0x08
    CRYSTAL_HELM        = 0x09
    LEATHERS            = 0x0A
    CHAIN_MAIL          = 0x0B
    PLATE_MAIL          = 0x0C
    MITHRIL_CHAIN       = 0x0D
    MITHRIL_PLATE       = 0x0E
    BLOOD_LEATHERS      = 0x0F
    ELVEN_CHAIN         = 0x10
    ELVEN_PLATE         = 0x11
    CRYSTAL_CHAIN       = 0x12
    CHAOS_PLATE         = 0x13
    CRYSTAL_PLATE       = 0x14
    LEATHER_GLOVES      = 0x15
    GAUNTLETS           = 0x16
    MITHRIL_GLOVES      = 0x17
    BATTLE_GLOVES       = 0x18
    ELF_GLOVES          = 0x19
    CHAOS_GLOVES        = 0x1A
    CRYSTAL_GLOVES      = 0x1B
    LEATHER_BUCKLER     = 0x1C
    BUCKLER             = 0x1D
    LARGE_SHIELD        = 0x1E
    ARC_SHIELD          = 0x1F
    BATTLE_BANE         = 0x20
    MOON_SHIELD         = 0x21
    BANE_SHIELD         = 0x22
    GOLDEN_SHIELD       = 0x23
    HERON_SHIELD        = 0x24
    WAR_SHIELD          = 0x25
    DRAGON_SHIELD       = 0x26
    THE_WATCHER         = 0x27
    CRYSTAL_SHIELD      = 0x28
    LEATHER_BOOTS       = 0x29
    IRON_BOOTS          = 0x2A
    MITHRIL_BOOTS       = 0x2B
    BLOOD_BOOTS         = 0x2C
    ELF_BOOTS           = 0x2D
    CRYSTAL_BOOTS       = 0x2E
    SERPENT_AMULET      = 0x2F
    NIGHT_AMULET        = 0x30
    DRAGON_AMULET       = 0x31
    CHAOS_AMULET        = 0x32
    CLOUD_AMULET        = 0x33
    MOON_AMULET         = 0x34
    AMBER_AMULET        = 0x35
    DAGGER              = 0x36
    STEALTH_BLADE       = 0x37
    DEATH_BLADE         = 0x38
    STASIS_BLADE        = 0x39
    SHORT_SWORD         = 0x3A
    LONG_SWORD          = 0x3B
    MITHRIL_BLADE       = 0x3C
    MITHRIL_SWORD       = 0x3D
    HERON_BLADE         = 0x3E
    DRAGON_DOOM         = 0x3F
    SCREAM_SLICER       = 0x40
    RUNE_SWORD          = 0x41
    VORPAL_BLADE        = 0x42
    HAND_AXE            = 0x43
    BATTLE_AXE          = 0x44
    MITHRIL_AXE         = 0x45
    DEATHBRINGER        = 0x46
    BRAINBITER          = 0x47
    GREY_AXE            = 0x48
    SLUGGER             = 0x49
    STAFF               = 0x4A
    BATTLE_STAFF        = 0x4B
    ETHERIAL_AXE        = 0x4C
    ETHERIAL_STAFF      = 0x4D
    ETHERIAL_SWORD      = 0x4E
    ETHERIAL_DAGGER     = 0x4F
    CROSSBOW            = 0x50
    LONG_BOW            = 0x51
    ELF_BOW             = 0x52
    FROST_BOW           = 0x53
    HARVESTER           = 0x54
    ARROWS              = 0x55
    ELF_ARROWS          = 0x56
    HAIL_OF_DOOM        = 0x57
    SNAKE_STAFF         = 0x58
    FIRESTAFF           = 0x59
    GRIM_REAPER         = 0x5A
    POWER_STAFF         = 0x5B
    SUN_STAFF           = 0x5C
    CLOUD_STAFF         = 0x5D
    SERPENT_WAND        = 0x5E
    DRAGON_WAND         = 0x5F
    NIGHT_WAND          = 0x60
    CHAOS_WAND          = 0x61
    AMBER_WAND          = 0x62
    CLOUD_WAND          = 0x63
    SERPENT_RING        = 0x64
    CHAOS_RING          = 0x65
    DRAGON_RING         = 0x66
    NIGHT_RING          = 0x67
    CLOUD_RING          = 0x68
    MOON_RING           = 0x69
    AMBER_RING          = 0x6A
    SCROLL_OF_FORMWALL  = 0x6B
    SCROLL_OF_VIVIFY    = 0x6C
    SCROLL_OF_FIREWARD  = 0x6D
    SCROLL_OF_ETHBLADE  = 0x6E
    SCROLL_OF_WIZEYE    = 0x6F
    SCROLL_OF_SUSPEND   = 0x70
    SCROLL_OF_TRUEVIEW  = 0x71
    SCROLL_OF_RENEW     = 0x72
    SCROLL_OF_LEVITATE  = 0x73
    SCROLL_OF_ANTIMAGE  = 0x74
    SCROLL_OF_REGEN     = 0x75
    HEDJOG_VENOM        = 0x76
    CHYMERA_BLOOD       = 0x77
    MOON_ELIXIR         = 0x78
    PHOENIX_BROTH       = 0x79
    DRAGON_ALE          = 0x7A
    POWER_POTION        = 0x7B
    ORCS_VOMIT          = 0x7C
    APPLE               = 0x7D
    BISCUIT             = 0x7E
    CORN                = 0x7F
    DRUMSTICK           = 0x80
    BREAD               = 0x81
    CHEESE              = 0x82
    BLUE_NEGG           = 0x83
    GREEN_NEGG          = 0x84
    YELLOW_NEGG         = 0x85
    PURPLE_NEGG         = 0x86
    RED_NEGG            = 0x87
    GOLD_KEY            = 0x88
    SILVER_KEY          = 0x89
    SERPENT_KEY         = 0x8A
    SUN_KEY             = 0x8B
    RUBY_KEY            = 0x8C
    NIGHT_KEY           = 0x8D
    CRYSTAL_KEY         = 0x8E
    COMMON_KEY          = 0x8F
    EYE_OF_GRISSLEM     = 0x90
    HORN_OF_XTLALTIC    = 0x91
    ANGRATHS_HEART      = 0x92
    SHASPUOKS_TEAR      = 0x93
    GEM_GEM_1           = 0x94
    MOON_GEM            = 0x95
    GEM_GEM_2           = 0x96
    FIRE_GEM            = 0x97
    BACKPACK            = 0x98
    UNLIGHTED_TORCH     = 0x99
    LIGHTED_TORCH       = 0x9A
    BAG_OF_GOLD         = 0x9B

    @classmethod
    def textual_description(cls, item, count):
        result = None
        for a in dir(cls):
            if type(getattr(cls, a)) is int and item == getattr(cls, a):
                result = a
                break
        if result is None:
            result = 'GLITCH_%02X' % item
        if Items.is_backpack(item):
            result += ' %d' % count
        elif count != 1:
            result += ' (%d)' % count
        return result


class Inventory:
    def __init__(self, is_character_inventory, contents):
        assert len(contents) == 32, 'Inventory data has odd length'
        self.is_character_inventory = is_character_inventory
        self.items_ = [ord(contents[2*i]) for i in xrange(len(contents)/2)]
        self.counts_ = [ord(contents[2*i+1]) for i in xrange(len(contents)/2)]

    def dumps(self):
        return ''.join(chr(k) for kk in zip(self.items_, self.counts_) for k in kk)

    @staticmethod
    def tuplize(item_and_count):
        if item_and_count is None:
            return (0x00, 0)
        elif type(item_and_count) is int:
            return (item_and_count, 1)
        return item_and_count

    def __setitem__(self, index, item_and_count):
        self.items_[index] = self.tuplize(item_and_count)[0]
        self.counts_[index] = self.tuplize(item_and_count)[1]

    def __getitem__(self, index):
        return (self.items_[index], self.counts_[index])

    def find_empty_slot(self):
        # In character inventories, the first 6 slots are specialized.
        slots = self.items_[6:] if self.is_character_inventory else self.items_
        for i, item in enumerate(slots):
            if item == 0x00:
                return i
        return None

    def set_helm(self, item_and_count):
        assert self.is_character_inventory
        assert Items.is_helm(self.tuplize(item_and_count)[0])
        self[0] = item_and_count

    def set_armour(self, item_and_count):
        assert self.is_character_inventory
        assert Items.is_armour(self.tuplize(item_and_count)[0])
        self[1] = item_and_count

    def set_gloves(self, item_and_count):
        assert self.is_character_inventory
        assert Items.is_gloves(self.tuplize(item_and_count)[0])
        self[2] = item_and_count

    def set_shield(self, item_and_count):
        assert self.is_character_inventory
        assert Items.is_shield(self.tuplize(item_and_count)[0])
        self[3] = item_and_count

    def set_boots(self, item_and_count):
        assert self.is_character_inventory
        assert Items.is_boots(self.tuplize(item_and_count)[0])
        self[4] = item_and_count

    def set_amulet(self, item_and_count):
        assert self.is_character_inventory
        assert Items.is_amulet(self.tuplize(item_and_count)[0])
        self[5] = item_and_count

    def set_left_hand(self, item_and_count):
        assert self.is_character_inventory
        self[6] = item_and_count

    def set_right_hand(self, item_and_count):
        assert self.is_character_inventory
        self[7] = item_and_count

    def get_helm(self):
        assert self.is_character_inventory
        return self[0]

    def get_armour(self):
        assert self.is_character_inventory
        return self[1]

    def get_gloves(self):
        assert self.is_character_inventory
        return self[2]

    def get_shield(self):
        assert self.is_character_inventory
        return self[3]

    def get_boots(self):
        assert self.is_character_inventory
        return self[4]

    def get_amulet(self):
        assert self.is_character_inventory
        return self[5]

    def get_left_hand(self):
        assert self.is_character_inventory
        return self[6]

    def get_right_hand(self):
        assert self.is_character_inventory
        return self[7]


class Character:
    def __init__(self, position, contents):
        assert len(contents) == 106, 'Character data has the wrong length'
        self.position_ = position
        (
            self.character_index,
            self.bytes_B0CD_B0CF,
            self.level,
            self.current_sp,
            self.max_sp,
            self.current_hp,
            self.max_hp,
            self.bytes_B0D8_B0DC,
            self.gp,
            self.xp,
            inventory_contents,
            self.spells,
            self.current_str, self.intrinsic_str,
            self.current_int, self.intrinsic_int,
            self.current_dex, self.intrinsic_dex,
            self.current_con, self.intrinsic_con,
            self.bytes_B110_B11C,
            self.first_name,
            self.last_name,
            self.hunger,
            self.byte_B131,
            self.bytes_B132_B136,
        ) = struct.unpack(
            '<B2sBHHHH4sII32sIbBbBbBbB12s8s12sBB4s',
            contents,
        )
        self.spells = struct.unpack("<I", struct.pack(">I", self.spells))[0]  # swap endianness
        self.first_name = self.first_name.rstrip('\xFF')
        self.last_name = self.last_name.rstrip('\xFF')
        self.inventory = Inventory(True, inventory_contents)
        assert self.byte_B131 == 0xFF
        assert self.bytes_B132_B136 == '\0\0\0\0'

    def dumps(self):
        return struct.pack(
            '<B2sBHHHH4sII32sIbBbBbBbB12s8s12sBB4s',
            self.character_index,
            self.bytes_B0CD_B0CF,
            self.level,
            self.current_sp,
            self.max_sp,
            self.current_hp,
            self.max_hp,
            self.bytes_B0D8_B0DC,
            self.gp,
            self.xp,
            self.inventory.dumps(),
            struct.unpack("<I", struct.pack(">I", self.spells))[0],  # swap endianness
            self.current_str, self.intrinsic_str,
            self.current_int, self.intrinsic_int,
            self.current_dex, self.intrinsic_dex,
            self.current_con, self.intrinsic_con,
            self.bytes_B110_B11C,
            self.first_name.ljust(8, '\xFF'),
            self.last_name.ljust(12, '\xFF'),
            self.hunger,
            self.byte_B131,
            self.bytes_B132_B136,
        )

    def find_empty_inventory_slot(self):
        i = self.inventory.find_empty_slot()
        if i is not None:
            return InventorySlot(self.position_, i)
        return None

    def learn_spells(self, which):
        self.spells |= which

    def unlearn_spells(self, which):
        self.spells &= ~which


class SaveGame:
    def __init__(self, contents):
        assert len(contents) == 0xF670, 'Savefile has the wrong length'
        self.bytes_0000_8000 = contents[0x0000:0x8000]
        self.bytes_8000_8004 = contents[0x8000:0x8004]
        assert contents[0x8000:0x8004] == '\xFC\xED\xDA\xCB'
        self.name = contents[0x8004:0x8021].rstrip('\x20')
        assert contents[0x8021] == '\0'
        self.bytes_8022_A02E = contents[0x8022:0xA02E]
        (
            self.player_position,
            self.player_facing,
        ) = struct.unpack('<HH', contents[0xA02E:0xA032])
        self.bytes_A032_A03E = contents[0xA032:0xA03E]
        self.held_in_cursor = struct.unpack('<BB', contents[0xA03E:0xA040])
        self.bytes_A040_B0CC = contents[0xA040:0xB0CC]
        self.characters = [
            Character(0, contents[0xB0CC:0xB136]),
            Character(1, contents[0xB136:0xB1A0]),
            Character(2, contents[0xB1A0:0xB20A]),
            Character(3, contents[0xB20A:0xB274]),
        ]
        self.bytes_B274_B278 = contents[0xB274:0xB278]
        self.backpacks = [
            Inventory(False, contents[0xB278:0xB298]),
            Inventory(False, contents[0xB298:0xB2B8]),
            Inventory(False, contents[0xB2B8:0xB2D8]),  # not sure if this is real
        ]
        self.bytes_B2D8_EE78 = contents[0xB2D8:0xEE78]
        self.thumbnail = contents[0xEE78:0xF670]

        assert self.bytes_8000_8004 == '\xFC\xED\xDA\xCB'
        assert self.bytes_B274_B278 == '\0\0\0\0'

    def dumps(self):
        contents = ''
        contents += self.bytes_0000_8000
        contents += self.bytes_8000_8004
        contents += self.name.ljust(29, '\x20')
        contents += '\0'
        contents += self.bytes_8022_A02E
        contents += struct.pack('<HH', self.player_position, self.player_facing)
        contents += self.bytes_A032_A03E
        contents += ''.join(map(chr, self.held_in_cursor))
        contents += self.bytes_A040_B0CC
        for character in self.characters:
            contents += character.dumps()
        contents += self.bytes_B274_B278
        for backpack in self.backpacks:
            contents += backpack.dumps()
        contents += self.bytes_B2D8_EE78
        contents += self.thumbnail
        assert len(contents) == 0xF670
        return contents

    @staticmethod
    def from_file(fname):
        with open(fname, "rb") as f:
            contents = f.read()
        return SaveGame(contents)

    def accessible_backpacks(self):
        packs = set()
        newpacks = set()
        for character in self.characters:
            for slot in range(6, 16):
                item, count = character.inventory[slot]
                if item == Items.BACKPACK:
                    newpacks.add(count)
        while newpacks != packs:
            # Check for backpacks nested within backpacks.
            packs = newpacks
            newpacks = set()
            for packno in packs:
                for slot in range(0, 16):
                    item, count = self.backpacks[packno][slot]
                    if item == Items.BACKPACK:
                        newpacks.add(count)
        return sorted(packs)

    def gain_common_keys(self):
        # First, try increasing the number of keys in all stacks you already have.
        done = False
        for character in self.characters:
            for slot in range(6, 16):
                if character.inventory[slot][0] == Items.COMMON_KEY:
                    character.inventory[slot] = (Items.COMMON_KEY, 99)
                    done = True
        for packno in self.accessible_backpacks():
            for slot in range(0, 16):
                if self.backpacks[packno][slot][0] == Items.COMMON_KEY:
                    self.backpacks[packno][slot] = (Items.COMMON_KEY, 99)
                    done = True
        if done:
            return
        # Next, look for an empty slot in a character's main inventory, or in a backpack.
        for character in self.characters:
            for slot in range(6, 16):
                if character.inventory[slot][0] == Items.NONE:
                    character.inventory[slot] = (Items.COMMON_KEY, 99)
                    return
        for packno in self.accessible_backpacks():
            for slot in range(0, 16):
                if self.backpacks[packno][slot][0] == Items.NONE:
                    self.backpacks[packno][slot] = (Items.COMMON_KEY, 99)
                    return
        assert False, 'no inventory slots available'

    def gain_item(self, item, count=1):
        # Avoid duplicating unique items, such as talismans.
        if Items.is_unique(item):
            for character in self.characters:
                for slot in range(6, 16):
                    if character.inventory[slot][0] == item:
                        return
            for packno in self.accessible_backpacks():
                for slot in range(0, 16):
                    if self.backpacks[packno][slot][0] == item:
                        return
        # Look for an empty slot in a character's main inventory, or in a backpack.
        for character in self.characters:
            for slot in range(6, 16):
                if character.inventory[slot][0] == Items.NONE:
                    character.inventory[slot] = (item, count)
                    return
        for packno in self.accessible_backpacks():
            for slot in range(0, 16):
                if self.backpacks[packno][slot][0] == Items.NONE:
                    self.backpacks[packno][slot] = (item, count)
                    return
        assert False, 'no inventory slots available'

    def gain_crystal_kit(self):
        for character in self.characters:
            character.inventory.set_helm(Items.CRYSTAL_HELM)
            character.inventory.set_armour(Items.CRYSTAL_PLATE)
            character.inventory.set_gloves(Items.CRYSTAL_GLOVES)
            character.inventory.set_shield(Items.CRYSTAL_SHIELD)
            character.inventory.set_boots(Items.CRYSTAL_BOOTS)

def dump_file(fname, start, end, by, art=False, to_png=None):
    with open(fname, "rb") as f:
        contents = f.read()
    contents = contents[start:end]
    if to_png is not None:
        dump_hexx_thumbnail(to_png, contents, by)
    elif art:
        for i in range(0, len(contents), by):
            print '0x%04x %s' % (start + i, as_pixel(contents[i:i + by]))
    else:
        for i in range(0, len(contents), by):
            print '0x%04x %s' % (start + i, as_hex(contents[i:i + by]))

def describe_items(fname):
    with open(fname, "rb") as f:
        contents = f.read()
    counted = 0x6100
    contents = contents[counted:0x8000].rstrip('\0')
    while contents:
        loc = struct.unpack('>H', contents[:2])[0]
        nitems = (ord(contents[2]) / 2) - 2
        if contents[3] != '\0':
            contents = '  ' + contents
            print 'shit, something fucked up'
            nitems = (ord(contents[2]) / 2) - 2
        contents = contents[4:]
        counted += 4
        descriptions = []
        for i in range(nitems):
            item = ord(contents[0])
            count = ord(contents[1])
            contents = contents[2:]
            counted += 2
            descriptions += [Items.textual_description(item, count)]
        print '%04X: %s' % (loc, ', '.join(descriptions))

def describe_monsters(fname):
    with open(fname, "rb") as f:
        contents = f.read()
    tail = struct.unpack('<H', contents[0xA03C:0xA03E])[0]
    ptr = 0x8022
    while ptr < 0xA000:
        if contents[ptr:ptr+32] == '\0' * 32:
            break
        record = list(struct.unpack('<HHHHHHHHHHHHHHHH', contents[ptr:ptr+32]))
        nextptr = 0x8000 + record[0]
        record = record[1:]
        record_str = ' '.join('%04X' % i for i in record)
        print '%04X: (%s) next=%04X' % (ptr, record_str, nextptr)
        ptr += 32

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group(title='plus exactly one of the following actions').add_mutually_exclusive_group(required=True)
    group.add_argument('--dump', action='store_true', help='dump the file as hex')
    group.add_argument('--dump-range', type=str, metavar='1234:1238', help='dump just a portion of the file(s) as hex')
    group.add_argument('--describe-items', action='store_true', help='list all items on the dungeon floor')
    group.add_argument('--describe-monsters', action='store_true', help='list all tracked monsters')
    group.add_argument('--edit', action='store_true', help='make changes to the file (and save a backup if necessary)')
    group.add_argument('--blank-range', type=str, metavar='1234:1238', help='zero out a portion of the file')
    group.add_argument('--gain-common-keys', action='store_true', help='make changes to the file (and save a backup if necessary)')
    group.add_argument('--gain-crystal-kit', action='store_true', help='make changes to the file (and save a backup if necessary)')
    group.add_argument('--gain-talismans', action='store_true', help='make changes to the file (and save a backup if necessary)')
    group.add_argument('--replace-thumbnail', metavar='IMAGE.PNG', type=str, help='make changes to the file (and save a backup if necessary)')
    parser.add_argument('--by', type=int, default=32, help='column width for --dump and --dump-range')
    parser.add_argument('--art', action='store_true', help='dump as ASCII art instead of hex')
    parser.add_argument('--to-png', type=str, help='dump as PNG image instead of hex')
    parser.add_argument('filename', nargs='+', help='File(s) to manipulate')
    options = parser.parse_args()
    options.edit = options.edit or any([
        options.gain_common_keys,
        options.gain_crystal_kit,
        options.gain_talismans,
        options.replace_thumbnail,
        options.blank_range,
    ])

    if options.dump:
        for fname in options.filename:
            dump_file(fname, 0x0000, 0xFFFF, by=options.by, art=options.art, to_png=options.to_png)
    elif options.dump_range:
        start, end = (int(x, 16) for x in options.dump_range.split(':'))
        for fname in options.filename:
            dump_file(fname, start, end, by=options.by, art=options.art, to_png=options.to_png)
    elif options.describe_items:
        for fname in options.filename:
            describe_items(fname)
    elif options.describe_monsters:
        for fname in options.filename:
            describe_monsters(fname)
    elif options.edit:
        if len(options.filename) != 1:
            parser.error('For safety, editing is restricted to only one file at a time')
        for fname in options.filename:
            if not os.path.exists(fname + '.original'):
                os.rename(fname, fname + '.original')
            sg = SaveGame.from_file(fname + '.original')
            if options.gain_common_keys:
                sg.gain_common_keys()
            elif options.gain_crystal_kit:
                sg.gain_crystal_kit()
            elif options.gain_talismans:
                sg.gain_item(Items.EYE_OF_GRISSLEM)
                sg.gain_item(Items.ANGRATHS_HEART)
                sg.gain_item(Items.SHASPUOKS_TEAR)
                sg.gain_item(Items.HORN_OF_XTLALTIC)
            elif options.replace_thumbnail is not None:
                sg.thumbnail = hexx_thumbnail_from_file(options.replace_thumbnail, w=60, h=34)
            else:
                pass # assert False, 'no edits were specified'
            contents = sg.dumps()
            if options.blank_range:
                start, end = (int(x, 16) for x in options.blank_range.split(':'))
                contents = contents[:start] + ('\0' * (end - start)) + contents[end:]
            with open(fname, "wb") as f:
                f.write(contents)
