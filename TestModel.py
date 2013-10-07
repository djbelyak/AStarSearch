__author__ = 'Belyavtsev'

import AStarSearchModel

class TestModel(AStarSearchModel):
    """
    Test implementation of model AStarSearchModel.
    It contains pole 5x5 with
    """
    def __init__(self):
        """
        Constructor.
        Here will be initialize internal state of object.

        @return: Created object TestModel.
        """
        self.pole = [[1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
        self.cursor = (0, 0)

    def __changeCursor__(self, position):
        """
        Method for change cursor position.

        @return: None.
        """
        (x, y) = self.cursor
        self.pole[x][y] = 0
        (x, y) = position
        self.pole[x][y] = 1
        self.cursor = (x, y)

    def __MoveUp__(self):
        """
        Method for upping cursor position.

        @return: Is operation was performed.
        """
        (x, y) = self.cursor
        if x > 0:
            self.__changeCursor__((x-1, y))
            return True
        return False
