from .lidstone import Lidstone


class Laplace(Lidstone):
    def __init__(self, corpus, n):
        super().__init__(corpus, n, gamma=1.0)
