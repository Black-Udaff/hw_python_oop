from dataclasses import dataclass


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    MESSAGE: str = (
        'Тип тренировки: {training_type}; '
        'Длительность: {duration:.3f} ч.; '
        'Дистанция: {distance:.3f} км; '
        'Ср. скорость: {speed:.3f} км/ч; '
        'Потрачено ккал: {calories:.3f}.'
    )

    def get_message(self) -> str:
        return self.MESSAGE.format(**vars(self))


class Training:
    """Базовый класс тренировки."""

    LEN_STEP: float = 0.65  # длина шага в метрах
    M_IN_KM: int = 1000  # кол-во метров в километре
    MIN_IN_HOUR: int = 60  # кол-во минут в часе

    def __init__(
        self,
        action: int,  # колличество совершенных действий гребков или шагов
        duration: float,  # время в часах
        weight: float,  # вес в кг
    ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        dist: float = self.action * self.LEN_STEP / self.M_IN_KM
        return dist

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed: float = self.get_distance() / self.duration
        return mean_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        message: InfoMessage = InfoMessage(
            self.__class__.__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories(),
        )
        return message


class Running(Training):
    """Тренировка: бег."""

    CALORIES_MEAN_SPEED_MULT: int = 18
    CALORIES_MEAN_SPEED_SHIFT: float = 1.79

    def get_spent_calories(self) -> float:
        calories: float = (
            (
                self.CALORIES_MEAN_SPEED_MULT * self.get_mean_speed()
                + self.CALORIES_MEAN_SPEED_SHIFT
            )
            * self.weight
            / self.M_IN_KM
            * (self.duration * self.MIN_IN_HOUR)
        )
        return calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""

    C_M_W_M: float = 0.035
    CAL_MEAN_WEIGTH_MULT_2: float = 0.029
    SPEED_IN_M_S: float = 0.278  # константа для перевода км\ч в м\с
    SM_IN_M: int = 100  # колво сантимертов в метре

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,
        height: int,  # Рост в сантиметрах
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        calories: float = (
            (
                self.C_M_W_M * self.weight
                + (
                    (self.get_mean_speed() * self.SPEED_IN_M_S) ** 2
                    / (self.height / self.SM_IN_M)
                )
                * self.CAL_MEAN_WEIGTH_MULT_2
                * self.weight
            )
            * self.duration
            * self.MIN_IN_HOUR
        )
        return calories


class Swimming(Training):
    """Тренировка: плавание."""

    SWIM_MULT: float = 1.1
    LEN_STEP: float = 1.38
    SPEED_FORCE: int = 2

    def __init__(
        self,
        action: int,
        duration: float,
        weight: float,  # Рост в сантиметрах
        length_pool: int,  # Длина бассейна
        count_pool: int,  # Кол-во переплытий бассейна
    ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        mean_speed: float = (
            self.length_pool * self.count_pool / self.M_IN_KM / self.duration
        )
        return mean_speed

    def get_spent_calories(self) -> float:
        calories: float = (
            (self.get_mean_speed() + self.SWIM_MULT)
            * self.SPEED_FORCE
            * self.weight
            * self.duration
        )
        return calories


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    training_type: dict[str, type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking,
    }
    if workout_type not in training_type:
        raise KeyError(f'{workout_type}: Такой тренировки нет!')
    train: Training = training_type[workout_type](*data)
    return train


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
