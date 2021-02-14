class AliasTimeOverlapError(Exception):
    """This exception raise when created Alias object overlapping existing object

     Attributes:
        message (str): Human readable string describing the exception.
    """

    def __init__(self, *args):
        """Init method for AliasTimeOverlapError

        Args:
            *args: Variable length argument list.
        """

        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        """Enable for str() build in function and by the print statement
        to compute the “informal” string representation of an object.
        """

        if self.message:
            return f'TimeOverlapError, {self.message}'
        else:
            return f'TimeOverlapError, new alias overlap existing alias'


class AliasInvalidTimeError(Exception):
    """This exception raise when attribute start in Alias object in front of attribute end

      Attributes:
         message (str): Human readable string describing the exception.
     """

    def __init__(self, *args):
        """Init method for AliasInvalidTimeError

                Args:
                    *args: Variable length argument list.
         """

        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        """Enable for str() build in function and by the print statement
        to compute the “informal” string representation of an object.
        """

        if self.message:
            return f'InvalidTimeError, {self.message}'
        else:
            return f'InvalidTimeError, some trouble with time'
