import math

# Базовий клас для фігур
class Shape:
    def dimension(self):
        raise NotImplementedError("Метод 'dimension' не реалізовано")

    def perimeter(self):
        raise NotImplementedError("Метод 'perimeter' не реалізовано")

    def area(self):
        raise NotImplementedError("Метод 'area' не реалізовано")

    def surface_area(self):
        raise NotImplementedError("Метод 'surface_area' не реалізовано")

    def base_area(self):
        raise NotImplementedError("Метод 'base_area' не реалізовано")

    def height(self):
        raise NotImplementedError("Метод 'height' не реалізовано")

    def volume(self):
        raise NotImplementedError("Метод 'volume' не реалізовано")

# Клас для трикутника
class Triangle(Shape):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def dimension(self):
        return 2  # Двовимірна фігура

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        # Формула Герона
        semi_perimeter = self.perimeter() / 2
        return math.sqrt(
            semi_perimeter *
            (semi_perimeter - self.side_a) *
            (semi_perimeter - self.side_b) *
            (semi_perimeter - self.side_c)
        )

    def volume(self):
        return self.area()

# Клас для прямокутника
class Rectangle(Shape):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def dimension(self):
        return 2  # Двовимірна фігура

    def perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def area(self):
        return self.side_a * self.side_b

    def volume(self):
        return self.area()

# Клас для круга
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def dimension(self):
        return 2  # Двовимірна фігура

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

    def volume(self):
        return self.area()

# Клас для кулі
class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def dimension(self):
        return 3  # Тривимірна фігура

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

# Функція для пошуку фігури з найбільшою мірою
def find_largest_shape(shapes):
    largest_shape = None
    max_volume = -1

    for shape in shapes:
        vol = shape.volume()
        if vol > max_volume:
            max_volume = vol
            largest_shape = shape

    return largest_shape

# Функція для читання фігур з файлу
def read_shapes_from_file(filename):
    shapes = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            shape_name = parts[0]
            params = list(map(float, parts[1:]))

            if shape_name == "Triangle":
                shapes.append(Triangle(*params))
            elif shape_name == "Rectangle":
                shapes.append(Rectangle(*params))
            elif shape_name == "Circle":
                shapes.append(Circle(*params))
            elif shape_name == "Sphere":
                shapes.append(Sphere(*params))
            # Додати інші фігури за необхідності

    return shapes

# Аналіз кількох файлів
def analyze_files(file_names):
    all_shapes = []

    # Читання фігур з кожного файлу
    for file_name in file_names:
        try:
            shapes = read_shapes_from_file(file_name)
            all_shapes.extend(shapes)
            print(f"Прочитано {len(shapes)} фігур з файлу {file_name}")
        except FileNotFoundError:
            print(f"Файл {file_name} не знайдено.")
        except Exception as e:
            print(f"Помилка при читанні файлу {file_name}: {e}")

    # Пошук фігури з найбільшою мірою
    if all_shapes:
        largest_shape = find_largest_shape(all_shapes)
        print(f"Фігура з найбільшою мірою: {type(largest_shape).__name__}, міра: {largest_shape.volume()}")
    else:
        print("Фігури не знайдено в жодному з файлів.")

# Список файлів для аналізу
file_names = ["input01.txt", "input02.txt", "input03.txt"]

# Запуск аналізу
analyze_files(file_names)