class Field:
    def __init__(self, name: str, value=None):
        self.name: str = name
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
