class TimeOverlapError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):

        if self.message:
            return f'TimeOverlapError, {self.message}'
        else:
            return f'TimeOverlapError, new alias overlap existing alias'


class InvalidTimeError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):

        if self.message:
            return f'InvalidTimeError, {self.message}'
        else:
            return f'InvalidTimeError, some trouble with time'
