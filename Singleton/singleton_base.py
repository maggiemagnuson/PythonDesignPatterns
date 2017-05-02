class SingletonBase(object):
    _instances = {}    # dict([cls, instance])

    # Dunder new is call when class is instantiated but
    # before Dunder init is called.
    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

