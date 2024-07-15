class TelecomColorCode:
    MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
    MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

    def __init__(self, major_index, minor_index):
        self.major_color = self.MAJOR_COLORS[major_index]
        self.minor_color = self.MINOR_COLORS[minor_index]

    def __str__(self):
        # Return a string representation of the color code
        return f'{self.major_color} {self.minor_color}'
