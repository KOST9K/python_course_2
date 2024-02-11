class Tree:
    def __init__(self, height: float, branches: int):
        """
            Создание и подготовка к работе объекта "Дерево"

            :param height: Высота дерева
            :param branches: Количество веток дерева

            Пример:
            >>> tree_testo = Tree(322.1337, 100500)
        """

        self.height_ = height
        self.branches_ = branches

    def __str__(self):
        return f"Высота {self.height_}. Количество веток {self.branches_}"

    def __repr__(self):
        return f"{self.__class__.__name__}(height={self.height_!r}, branches={self.branches_!r})"

    def make_tree_higher(self, increment_size: float = 10.0):
        """
            Увеличение высоты дерева
            :param increment_size: Значение увеличения высоты

            Примеры:
            >>> tree_testo = Tree(322.1337, 100500)
            >>> tree_testo.make_tree_higher(18)

        """

        self.height_ += increment_size

    def change_attribute(self, new_branches_number: int):
        """
           Увеличение высоты дерева
           :param new_branches_number: Новое значение количества веток

           Примеры:
           >>> tree_testo = Tree(322.1337, 100500)
           >>> tree_testo.change_attribute(300)

       """
        self.branches_ = new_branches_number


class Birch(Tree):
    def __init__(self, height: float, branches: int, black_spots: int):
        """
            Создание и подготовка к работе объекта "Берёза"

            :param height: Высота дерева
            :param branches: Количество веток дерева
            :param black_spots: Количество чёрных пятен

            Пример:
            >>> birch_testo = Birch(812.0, 52, 29)
        """

        super().__init__(height, branches)
        if not isinstance(black_spots, int):
            raise ValueError("Количество страниц должно быть типа int")
        if black_spots <= 0:
            raise ValueError("Количество страниц должно быть положительным числом типа int")

        self.black_spots_ = black_spots

    def __str__(self):
        return f"Высота {self.height_}. Количество веток {self.branches_}." \
               f" Количество чёрных пятен {self.black_spots_}"

    def __repr__(self):
        return f"{self.__class__.__name__}(height={self.height_!r}, branches={self.branches_!r}," \
               f" black_spots={self.black_spots_})"

    def make_tree_higher(self, increment_size: float = 10.0):
        """
            Увеличение высоты дерева
            :param increment_size: Значение увеличения высоты

            Примеры:
            >>> birch_testo = Birch(812.0, 52, 29)
            >>> birch_testo.make_tree_higher(25)

        """
        return super().make_tree_higher(increment_size)

    def change_attribute(self, new_black_spots_number: int):
        """
            Функция для изменения количества чёрных пятен берёзы

            param new_black_spots_number: количество новых чёрных пятен

            >>> birch_testo = Birch(812.0, 52, 29)
            >>> birch_testo.change_attribute(715)
        """

        self.black_spots_ = new_black_spots_number

    # Write your solution here
    # pass


if __name__ == "__main__":
    Tree1 = Tree(192.0, 44)
    Tree1.change_attribute(34)
    print(Tree1)

    birch1 = Birch(200.0, 55, 77)
    birch1.change_attribute(23)
    print(birch1)
