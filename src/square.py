from src.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side: float):
        super().__init__(side, side)

