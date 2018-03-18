
class DungeonTowers:
    KEEP = 0
    GRISSLEM = 1
    SHASPUOK = 2
    ANGRATH = 3
    XTLALTIC = 4
    ZENDIK = 5

    @staticmethod
    def tower_height(tower):
        return {
            DungeonTowers.KEEP: 6,
            DungeonTowers.GRISSLEM: 8,
            DungeonTowers.SHASPUOK: 7,
            DungeonTowers.ANGRATH: None,
            DungeonTowers.XTLALTIC: None,
            DungeonTowers.ZENDIK: None,
        }[tower]

    @staticmethod
    def map_dimensions(tower, level):
        """Returns a tuple of (width, height)."""
        return {
            (DungeonTowers.KEEP, 1): (7, 1),
            (DungeonTowers.KEEP, 2): (11, 12),
            (DungeonTowers.KEEP, 3): (18, 18),
            (DungeonTowers.KEEP, 4): (20, 20),
            (DungeonTowers.KEEP, 5): (14, 14),
            (DungeonTowers.KEEP, 6): (31, 31),
            (DungeonTowers.GRISSLEM, 1): (5, 9),
            (DungeonTowers.GRISSLEM, 2): (21, 21),
            (DungeonTowers.GRISSLEM, 3): (21, 21),
            (DungeonTowers.GRISSLEM, 4): (17, 17),
            (DungeonTowers.GRISSLEM, 5): (15, 15),
            (DungeonTowers.GRISSLEM, 6): (15, 15),
            (DungeonTowers.GRISSLEM, 7): (13, 13),
            (DungeonTowers.GRISSLEM, 8): (13, 13),
            (DungeonTowers.SHASPUOK, 1): (5, 9),
            (DungeonTowers.SHASPUOK, 2): (21, 21),
            (DungeonTowers.SHASPUOK, 3): (21, 21),
            (DungeonTowers.SHASPUOK, 4): (19, 19),
            (DungeonTowers.SHASPUOK, 5): (19, 19),
            (DungeonTowers.SHASPUOK, 6): (17, 17),
            (DungeonTowers.SHASPUOK, 7): (9, 9),
            (DungeonTowers.ANGRATH, 1): (9, 5),
            (DungeonTowers.ANGRATH, 2): (27, 27),
            (DungeonTowers.ANGRATH, 3): (19, 19),
            (DungeonTowers.ANGRATH, 4): (17, 17),
            (DungeonTowers.ANGRATH, 5): (17, 17),
            (DungeonTowers.ANGRATH, 6): None,
            (DungeonTowers.ANGRATH, 7): None,
            (DungeonTowers.ANGRATH, 8): None,
            (DungeonTowers.XTLALTIC, 1): None,
            (DungeonTowers.XTLALTIC, 2): None,
            (DungeonTowers.XTLALTIC, 3): None,
            (DungeonTowers.XTLALTIC, 4): None,
            (DungeonTowers.XTLALTIC, 5): None,
            (DungeonTowers.XTLALTIC, 6): None,
            (DungeonTowers.XTLALTIC, 7): None,
            (DungeonTowers.XTLALTIC, 8): None,
            (DungeonTowers.ZENDIK, 1): None,
            (DungeonTowers.ZENDIK, 2): None,
            (DungeonTowers.ZENDIK, 3): None,
            (DungeonTowers.ZENDIK, 4): None,
            (DungeonTowers.ZENDIK, 5): None,
            (DungeonTowers.ZENDIK, 6): None,
            (DungeonTowers.ZENDIK, 7): None,
            (DungeonTowers.ZENDIK, 8): None,
        }[(tower, level)]
