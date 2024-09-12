from enum import Enum
class BlockPosition(Enum):
    TOP_LEFT = (0, 0)
    TOP_CENTER = (0, 3)
    TOP_RIGHT = (0, 6)
    MIDDLE_LEFT = (3, 0)
    MIDDLE_CENTER = (3, 3)
    MIDDLE_RIGHT = (3, 6)
    BOTTOM_LEFT = (6, 0)
    BOTTOM_CENTER = (6, 3)
    BOTTOM_RIGHT = (6, 6)
