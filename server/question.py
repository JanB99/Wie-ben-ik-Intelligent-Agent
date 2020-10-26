class Question:
    def __init__(self, col, value, headers):
        self.column = col
        self.value = value
        self.headers = headers

    def match(self, example):
        value = example[self.column]
        if self.is_int():
            return value >= self.value
        else:
            return value == self.value

    def match_value(self, value):
        if self.is_int():
            return float(value) >= self.value
        else:
            return value == self.value

    def is_int(self):
        return isinstance(self.value, int) or isinstance(self.value, float)

    def __repr__(self):
        return "is {} {} {}?".format(self.headers[self.column], ">=" if self.is_int() else "==", self.value)

    def toJson(self):
        return {
            "question": self.__repr__(),
            "label": self.headers[self.column],
            "value": self.value
        }