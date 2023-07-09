class InfoMessage:
    """Информационное сообщение о тренировке."""

    pass


class Training:
    """Базовый класс тренировки."""

    LEN_STEP = 0.65  # длина шага в метрах
    LEN_GREBOK = 1.38  # длина гребка в метрах
    M_IN_KM = 1000  # константа для перевода значений из метров в километры

    def __init__(
        self,
        action: int,  # колличество совершенных действий гребков или шагов
        duration: float,  # время в часах
        weight: float,  # вес в Кг?
    ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        dist = self.action * self.LEN_STEP / self.M_IN_KM
        return dist

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    """Тренировка: бег."""

    pass


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    pass


class Swimming(Training):
    """Тренировка: плавание."""

    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
