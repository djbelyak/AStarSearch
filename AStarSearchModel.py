__author__ = 'Belyavtsev'

class AStarSearchModel:
    """
    Abstract model for implementation A-Star Search.
    """

    def __init__(self):
        """
        Default constructor.

        @return: Created object AStarSearchModel.
        """
        pass

    def getActionListWithMetric(self):
        """
        Method for getting list of available action with it's time metrics.

        @return: List of available actions (time metric, action name).
        """
        pass

    def doAction(self, action):
        """
        Method for do action and changing internal state of object.

        @param action: String with action for doing.
        @return: Boolean status of doing.
        """
        pass
