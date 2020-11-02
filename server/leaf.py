class Leaf:
    def __init__(self, rows, headers):
        self.predictions = rows

    def print(self, spacing, boolean):
        print(spacing, str(boolean) + "-->", self.predictions)

    def toJson(self):
        return {
            'type': 'leaf',
            'prob': self.predictions
        }