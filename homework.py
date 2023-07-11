class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self, training_type, duration, distance, speed, calories):
        self.trainigtype = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return (
            f'Тип тренировки: {self.training_type};'
            f'Длительность: {self.duration} ч.;'
            f'Дистанция: {self.distance} км;'
            f'Ср. скорость: {self.speed} км/ч; '
            f'Потрачено ккал: {self.calories}.'
        )


class Training:
    """Базовый класс тренировки."""

    LEN_STEP = 0.65    # длина шага в метрах
    LEN_GREBOK = 1.38  # длина гребка в метрах
    M_IN_KM = 1000     # константа для перевода значений из метров в километры(и иобратно)
    MIN_IN_HOUR = 60   # кол-во минут в часе
    SEC_IN_HOUR = 3600 # кол-во секунд в часе
    SM_IN_M = 100      # колво сантимертов в метре

    def __init__(
        self,
        action: int,     # колличество совершенных действий гребков или шагов
        duration: float, # время в часах
        weight: float,   # вес в Кг?
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
        message = InfoMessage.get_message(
            self.__class__.__name__,
            self.duration,
            self.distance,
            self.speed,
            self.calories,
        )
        return message


class Running(Training):
    """Тренировка: бег."""
    CALORIES_MEAN_SPEED_MULT = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79 
    def get_spent_calories(self) -> float:
        calories = ((self.CALORIES_MEAN_SPEED_MULT * self.get_mean_speed()*self.M_IN_KM  + self.CALORIES_MEAN_SPEED_SHIFT) 
                    * self.weight / self.M_IN_KM * (self.duration * self.MIN_IN_HOUR) )
        return calories
    


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_MEAN_WEIGTH_MULT = 0.035
    CALORIES_MEAN_WEIGTH_MULT_2 = 0.029
    def __init__(
        self,
        action: int,  # колличество совершенных действий гребков или шагов
        duration: float,  # время в часах
        weight: float,  # вес в Кг?
        height: int # Рост в сантиметрах
    ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

     def get_spent_calories(self) -> float:   
        calories = ((self.CALORIES_MEAN_WEIGTH_MULT * self.weight + 
                     ((self.get_mean_speed()*self.M_IN_KM/self.SEC_IN_HOUR)**2 / рост_в_метрах)
            * self.CALORIES_MEAN_WEIGTH_MULT_2 * self.height) * self.duration*self.MIN_IN_HOUR)
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
