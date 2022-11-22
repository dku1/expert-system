class Widget:
    def __init__(self):
        self.widget = None

    def draw(self, **kwargs):
        self.widget.pack(**kwargs)
