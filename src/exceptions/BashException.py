class BashException(RuntimeError):
    name:str = "BashException"

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "{0}".format(self.message)
        else:
            return self.name + " has been raised"