class Plant:
    def __init__(self, name: str, height: float,  age: int, growth: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth = growth

    def growth(self) -> None:
        self.height += self.growth

    def age(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def ft_plant_growth() -> None:
        