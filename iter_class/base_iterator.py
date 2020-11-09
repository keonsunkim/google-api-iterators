



# import from tools directory
from tools.time_tools import random_sleep



class BaseIterator:
    """
    API Base Iterator. Iterates through a Given API.
    Stops iteration inside the condition function.
    Thus, all conditions must be functions!
    All functions will have the class instance passed to its argument.
    Thus, function created to check conditions must presuppose that it will
    check with conditions that can be found inside the class instance!

    Index starts on 0! And it increments after conditions are checked!

    If you want it to sleep, set your pass set_sleep_time = {min, max} to
    your initialization argument!
    """
    cls_stop_condition_functions = []

    def __init__(self, *args, **kwargs):
        #get index, if not set as 0
        self._index = kwargs.get('index', 0)

        #stop_conditions must be added by a list!

        self._stop_conditions = list(
            self.cls_stop_condition_functions
            + kwargs.get('stop_condition_functions', list())
        )

        if 'set_sleep_time' in kwargs:
            self._sleep_range = kwargs.get('set_sleep_time')


    def __iter__(self):
        return self

    def _stop_condition_check(self):
        for function in self._stop_conditions:
            function(self)

    def index(self):
        return self._index

    def set_index(self, num):
        if isinstance(num, int) and num >= 1:
            self._index = int(num)
        else:
            raise ValueError(f"Index can only be integers starting from 0! \
                                Given value of index is {num}")

    def __next__(self):
        """
        Parent Class __next__ does not return anything.
        It is here just to ensure stop condition checking works.
        All Iterator Child classes must call super().__next__(self) first!
        """
        self._stop_condition_check()

        #make sure index is counting!
        self.set_index(self.index() + 1)

        if self._sleep_range:
            random_sleep(**self._sleep_range)
