# Зададим глобальную переменную,
# чтобы можно было использовать ее внутри всех классов
M_IN_KM = 1000


class Training:
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 len_step: float = 0.65) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
        self.len_step = len_step

    def get_distance(self):
        return (self.action * self.len_step / M_IN_KM)

    def get_mean_speed(self):
        return (self.get_distance() / self.duration)

    def get_spent_calories(self):
        pass

    def show_training_info(self):
        info = InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())
        return info.get_message()


class Running(Training):
    def get_spent_calories(self):
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        return ((coeff_calorie_1 * self.get_mean_speed() -
                 coeff_calorie_2)
                * self.weight / M_IN_KM * self.duration * 60)


class SportsWalking(Training):
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self):
        coeff_calorie_1 = 0.035
        coeff_calorie_2 = 0.029
        return ((coeff_calorie_1 * self.weight
                 + (self.get_mean_speed() ** 2 // self.height)
                 * coeff_calorie_2 * self.weight) * self.duration * 60)


class Swimming(Training):
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float,
                 len_step: float = 1.38) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self):
        return (self.length_pool * self.count_pool / M_IN_KM / self.duration)

    def get_spent_calories(self):
        coeff_calorie_1 = 1.1
        coeff_calorie_2 = 2
        return ((self.get_mean_speed() + coeff_calorie_1) *
                coeff_calorie_2 * self.weight)


class InfoMessage:
    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {round(self.duration, 3)} ч.; '
                f'Дистанция: {round(self.distance, 3)} км; '
                f'Ср. скорость: {round(self.speed, 3)} км/ч; '
                f'Потрачено ккал: {round(self.calories, 3)}.')


workout_type = {'SWM': Swimming,
                'RUN': Running,
                'WLK': SportsWalking}


def read_packages(workout_type: str, data: list) -> Training:
    if workout_type == 'SWM':
        return Swimming(data[0], data[1], data[2], data[3], data[4])
    elif workout_type == 'RUN':
        return Running(data[0], data[1], data[2])
    elif workout_type == 'WLK':
        return SportsWalking(data[0], data[1], data[2], data[3])
    else:
        print('Данный тип тренировки не задан.')


def main(training: Training) -> None:
    print(training.show_training_info())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_packages(workout_type, data)
        main(training)
