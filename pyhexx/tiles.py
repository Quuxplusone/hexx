
import itertools

class Directions:
    SOUTH = 0
    WEST = 1
    NORTH = 2
    EAST = 3
    def is_valid(facing):
        return 0 <= facing <= 3


class Tile:
    @staticmethod
    def describe_flags(visited, has_monster, has_item):
        if visited: yield 'visited'
        if has_monster: yield 'has_monster'
        if has_item: yield 'has_item'

    @staticmethod
    def describe_wooden_structure(part, direction):
        if part == 1:
            yield 'wooden partition' + direction
        elif part == 2:
            yield 'open wooden door' + direction
        elif part == 3:
            yield 'closed wooden door' + direction

    @staticmethod
    def describe_door(tile):
        needs = (tile & 0x00F8) >> 3
        if needs == 0: yield 'mage-locked'
        yield 'open' if (tile & 0x0100) else 'closed'
        yield 'E/W' if (tile & 0x0400) else 'N/S'
        if (tile & 0x0200): yield 'grated'
        yield 'door'
        if needs == 1:
            yield "that won't budge"
        elif needs >= 3:
            item = Items.GOLD_KEY + (needs - 3)
            yield '(needs a %s)' % Items.textual_description(item)

    def textual_description(self):
        tile = self.value
        visited = (tile & 0x0008) != 0
        tile &= ~0x0008
        if (tile & 0x000F) in [0, 2, 6, 7]:
            has_monster = (tile & 0x0080) != 0
            has_item = (tile & 0x0040) != 0
            tile &= ~0x00C0
        else:
            has_monster = False
            has_item = False
        if tile == 0x0081:
            result = 'formwall'
        elif (tile & 0x000F) == 0:
            assert tile == 0x0000, "Unknown tile %04X" % tile
            result = 'floor'
        elif (tile & 0x000F) == 1:
            assert tile == 0x0001, "Unknown tile %04X" % tile
            result = 'wall'
        elif (tile & 0x000F) == 2:
            assert (tile & 0xFF02) == tile, "Unknown tile %04X" % tile
            result = ', '.join(itertools.chain(
                Tile.describe_wooden_structure((tile & 0x0300) >> 8, ' to the south'),
                Tile.describe_wooden_structure((tile & 0x0C00) >> 10, ' to the west'),
                Tile.describe_wooden_structure((tile & 0x3000) >> 12, ' to the north'),
                Tile.describe_wooden_structure((tile & 0xC000) >> 14, ' to the east'),
            ))
            if (tile & 0x0010):
                result += ' (needs a common key)'
        elif (tile & 0x000F) == 3:
            assert (tile & 0x0103) == tile, "Unknown tile %04X" % tile
            result = 'brazier' if (tile & 0x0100) else 'bed'
        elif (tile & 0x000F) == 4:
            assert tile == 0x0104, "Unknown tile %04X" % tile
            result = 'down stairs'
        elif (tile & 0x000F) == 5:
            result = ' '.join(Tile.describe_door(tile))
        elif (tile & 0x000F) == 6:
            if tile == 0x0106:
                result = 'pit'
            else:
                result = 'portal plate'
        elif (tile & 0x000F) == 7:
            if tile == 0x0187:
                result = 'fireward'
            elif (tile & 0xF0FF) == 0x0007:
                result = 'firepath square %d' % (tile >> 8)
            else:
                result = 'illusory wall'
        else:
            assert False, "Unknown tile %04X" % tile
        if visited or has_monster or has_item:
            result += ' (%s)' % ','.join(Tile.describe_flags(visited, has_monster, has_item))
        return result

    @staticmethod
    def wall():
        return Tile(0x0001)

    @staticmethod
    def brazier():
        return Tile(0x0103)

    @staticmethod
    def banner(facing=None):
        assert Directions.is_valid(facing)
        result = 0x0101
        result |= (direction << 7)
        return Tile(result)

    @staticmethod
    def door(open=False, grated=False, facing=None, mage_locked = False, wont_budge=False, needs=None):
        assert Directions.is_valid(facing)
        result = 0x0015
        if not open:
            result |= 0x0100
        if grated:
            result |= 0x0200
        if facing in [Directions.EAST, Directions.WEST]:
            result |= 0x0400
        if mage_locked:
            result |= 0 << 3
        elif wont_budge:
            result |= 1 << 3
        elif requires is None:
            result |= 2 << 3
        else:
            result |= ((needs - Items.GOLD_KEY) + 3) << 3
        return Tile(result)

    @staticmethod
    def sign(message=None, facing=None):
        assert 0 <= message <= 58
        assert Directions.is_valid(facing)
        result = 0x15B1
        result += (0x400 * message)
        result |= (direction << 7)
        return Tile(result)

    def sign_text(self):
        return {
            0: 'YE SHOPPE.\nTHE BEST PRICES IN TOWN',
            1: "OZZRIK'S UNEARTHED ARCANA",
            2: 'YE ARMOURY\nYOUR LAST CHANCE TO STOCK UP!\nBUY HERE',
            3: 'GROG SHOP',
            4: 'REFORGE THY BONES',
            5: 'WELCOME BACK',
            6: 'BRING THE CRYSTALS, FIND THEM ALL, ONLY THEN WILL EVIL FALL',
            7: 'ONLY THOSE WHO PROVE WORTHY MAY RETURN',
            8: 'YOU HAVE PROVEN TO BE WORTHY YOU MAY RETURN',
            9: 'ALL MORTALS BEWARE!',
            10: 'CHOOSE A PLATE TO CHOOSE A FATE',
            11: 'THE WIZARD WILL NOT SUFFER ANY MORTAL TO TRESPASS\n-KEEP OUT-',
            12: 'THE TOWER OF GRISSLEM',
            13: 'TURN THE BLOCK TO TURN THE BLOCK.',
            14: 'THE REALM OF LORD XTLALTIC',
            15: 'THE CITADEL OF ANGRATH',
            16: 'THE DEMESNE OF LORD SHASPUOK',
            17: 'ONLY A BED WILL GRANT THEE REST.',
            18: 'FAST ROUTE DOWN!',
            19: 'YOU HAVE EARNED ACCESS TO THE TOWER OF LORD GRISSLEM',
            20: 'DESCEND TO VIEW THE SHRINES OF THE LOST GODS OF MAGICK',
            21: 'GREETINGS TO THEE FOOLISH INTRUDERS',
            22: 'LOOK BEHIND YOU!',
            23: 'THE PRIZE YOU SEEK IS FAR ABOVE',
            24: 'ALL BELIEVERS ARE WELCOME',
            25: 'PLACE THE GEM IN THE HOLE TO REACH YOUR GOAL',
            26: 'YOU CAN REACH THE PRIZE BUT WILL YOU ESCAPE?',
            27: 'FARE THEE WELL MY FRIENDS',
            28: '',
            29: 'THOSE WHO SEEK THE EYE SHALL PERISH',
            30: 'THE CRYSTALS CAGE THE POWER',
            31: 'ASCEND TO THE EYE OF LORD GRISSLEM',
            32: 'NOW YOU ARE IN TROUBLE',
            33: 'PARTING IS SUCH SWEET SORROW',
            34: 'WE SELL THE BEST THAT MONEY CAN BUY',
            35: 'FOR THE FIRST YOU RISE\nFOR THE SECOND BE WISE',
            36: 'THE RINGS WERE MADE FROM THE SHARDS OF PUREST CRYSTALS',
            37: 'BEWARE THE PSYCHIC BARRIERS',
            38: 'RUN THE GAUNTLET!',
            39: 'THE GREAT BEAST DID COME FROM THE OTHER WORLD',
            40: 'LOOK HARD AND THOU SHALT SEE',
            41: 'TO PASS THE LOCK JUST TURN THE BLOCK',
            42: 'ONWARDS TO THY GREATER GLORIES',
            43: "THE OLD ONES WARD THE LAIR OF LORD ANGRATH'S HEART",
            44: 'YOU WILL NEVER DEFEAT THE WIZARD IN HIS LAIR',
            45: 'GOING FURTHER WILL ENSURE YOUR DEATHS',
            46: 'WITHIN THE DRAGON LIES THE POWER',
            47: 'NORTHWARD YOU MUST TRAVEL TO CAGE THE ARC',
            48: 'THE DRAGON HEART AWAKES',
            49: 'THE LORDS OF CHAOS AWAIT YOU',
            50: 'CHAOS CAN NOT BE RULED BY MAN',
            51: 'THE GREAT BLADE',
            52: 'YOU MUST RISE BEFORE YOU FALL',
            53: 'ONLY THEY WITH THE QUICKEST HAND AND KEENEST EYE WILL PREVAIL',
            54: 'BE BRAVE AND PRESS ONWARDS',
            55: 'YOU HAVE DONE WELL\nNOW THE CHALLENGE BEGINS',
            56: 'THE WIZARD HAS LOST CONTROL',
            57: 'PREPARE TO DIE ACCURSED DEFILERS',
            58: 'POTIONS\nALE    500\nVENOM   10\nELIXIR  20\nBROTH   25'
        }[(self.value - 0x15B1) / 0x400]

    def __init__(self, value):
        if type(value) is str:
            value = struct.unpack('<H', value)[0]
        assert type(value) is int
        self.value = value

    def dumps(self):
        return struct.pack('<H', self.value)
