"""Модуль, который содержит реализацию шахматных координат."""


class Coord:
    """Реализация шахматных координат."""

    def __init__(self, y: int = None, x: int = None) -> None:
        """Инициализирует поля x и y числами или значениями по умолчанию.

        Args:
            y(int) : Координата по вертикали;
            x(int) : Координата по горизонтали.
        """
        self.y = y
        self.x = x

    def __eq__(self, other: "Coord") -> bool:
        return self.y == other.y and self.x == other.x

    def __str__(self) -> str:
        return f"({self.y}, {self.x})"

    def __repr__(self) -> str:
        return f"Coord({self.y}, {self.x})"


class CoordWithTransform(Coord):
    """Реализация шахматных координат с превращением для пешек."""
    def __init__(self, y: int = None, x: int = None, figure: str = None) -> None:
        """Вызывает родительский конструктор и инициализирует атрибут figure.

        Args:
            y(int) : Координата по вертикали;
            x(int) : Координата по горизонтали;
            figure(str) : Фигура, которая может быть получена при реализации такого хода.

        """
        super().__init__(y, x)
        self.figure = figure

    def __repr__(self) -> str:
        return f"Coord({self.y}, {self.x}, {self.figure})"
