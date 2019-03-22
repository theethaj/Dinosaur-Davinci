class Dinosaurs:
    def __init__(self, bid, lp):
        self.bid = bid
        self.lp = lp

    def update(self, delta):
        pass

class PlayerDino:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.dinosaur = Dinosaurs(self, width // 2, height // 2)

    def update(self, delta):
        self.dinosaur.update(delta)

class ComDino:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.dinosaur = Dinosaurs(self, width // 2, height // 2)

    def update(self, delta):
        self.dinosaur.update(delta)

