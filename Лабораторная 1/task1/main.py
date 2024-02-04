# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Tree:
    def __init__(self, height, brenches_number):
        """
                Создание и подготовка к работе объекта "Дерево"

                :param height: Высота дерева
                :param brenches_number: Количество веток на дереве

                Примеры:
                >>> tree = Tree(500.23, 15)  # инициализация экземпляра класса
        """
        if not isinstance(height, float):
            raise TypeError("Высота дерева должна быть типа float")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        self.height = height

        if not isinstance(brenches_number, int):
            raise TypeError("Количество веток дерева должно быть типа float")
        if brenches_number < 0:
            raise ValueError("Количество веток дерева должно быть положительным числом")
        self.brenches_number = brenches_number

    def change_height(self, height: float):
        """
        Изменение высоты дерева.
        :param height: Обновлённая высота дерева

        :raise ValueError: Если введённая высота отрицательна, то вызывается ошибка

        Примеры:
        >>> tree = Tree(500.0, 0)
        >>> tree.change_height(200.0)
        """
        if not isinstance(height, float):
            raise TypeError("Высота дерева должна быть типа float")
        if height < 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        ...

    def change_brenches_number(self, brenches_number: int):
        """
        Изменение количества веток дерева.
        param brenches_number: Обновлённое количество веток на дереве

        :raise ValueError: Если введённое количество веток отрицательно, то вызывается ошибка

        Примеры:
        >>> tree = Tree(500.0, 0)
        >>> tree.change_brenches_number(32)
        """
        if not isinstance(brenches_number, int):
            raise TypeError("Количество веток должно быть типа int")
        if brenches_number < 0:
            raise ValueError("Количество веток должно быть положительным числом")
        ...


class Box:
    def __init__(self, width, height):
        """
                Создание и подготовка к работе объекта "Коробка"

                :param width: Высота коробки
                :param height: Ширина коробки

                Примеры:
                >>> box = Box(500.23, 15.44)  # инициализация экземпляра класса
        """
        if not isinstance(height, float):
            raise TypeError("Высота коробки должна быть типа float")
        if height <= 0:
            raise ValueError("Высота коробки должна быть положительным числом")
        self.height = height

        if not isinstance(width, float):
            raise TypeError("Ширина коробки должна быть типа float")
        if width < 0:
            raise ValueError("Ширина коробки должно быть положительным числом")
        self.width = width

    def change_height(self, height: float):
        """
        Изменение высоты коробки.
        :param height: Обновлённая высота коробки

        :raise ValueError: Если введённая высота отрицательна, то вызывается ошибка

        Примеры:
        >>> box = Box(500.0, 32.2)
        >>> box.change_height(200.0)
        """
        if not isinstance(height, float):
            raise TypeError("Высота коробки должна быть типа float")
        if height < 0:
            raise ValueError("Высота коробки должна быть положительным числом")
        ...


class Cat:
    def __init__(self, starve, is_happy):
        """
               Создание и подготовка к работе объекта "Кот"

               :param starve: Степень голодности кота
               :param is_happy: Счастлив ли кот

               Примеры:
               >>> Barsik = Cat(1703.0, True)  # инициализация экземпляра класса
        """

        if not isinstance(starve, float):
            raise TypeError("Степень голодности кота должна быть типа float")

        if starve < 0:
            raise ValueError("Степень голодности кота должна быть положительным числом")
        self.starviness = starve

        if not isinstance(is_happy, bool):
            raise TypeError("Счастье кота должно быть типа bool")

        self.is_happy = is_happy

    def feed_cat(self, food: float):

        """
        Изменение степени сытости кота.
        :param food: Количество съеденной котом еды

        :raise ValueError: Если введённое количество еды отрицательно, то вызывается ошибка

        Примеры:
        >>> Kotik = Cat(500.0, False)
        >>> Kotik.feed_cat(200.0)
        """

        if not isinstance(food, float):
            raise TypeError("Количество съеденной еды должно быть типа float")
        if food < 0:
            raise ValueError("Количество съеденной еды должно быть положительным числом")
        ...

    def change_happiness(self, is_happy: bool):
        """
        Изменение статуса счастья кота.
        param is_happy: Обновлённый статус счастья


        римеры:
        >>> Kot9ra = Cat(500.0, False)
        >>> Kot9ra.change_happiness(True)
        """
        if not isinstance(is_happy, bool):
            raise TypeError("Количество веток должно быть типа bool")

        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
