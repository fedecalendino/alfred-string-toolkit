class Action:
    def __init__(self, name: str):
        self.name = name

    def __call__(self, string: str) -> str:
        raise NotImplementedError("Subclasses should implement this method.")

    def __str__(self):
        return self.name
