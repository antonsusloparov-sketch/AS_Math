import math


def line_eq(a, b):
    """Находит решение линейного уравнения"""

    # Поиск решения
    if a != 0:
        roots = -b / a
    else:
        roots = None
    return roots


def quad_eq(a, b, c):
    """Вычисляет корни квадратного уравнения"""
    # Находим дискриминант
    d = b * b - 4 * a * c

    # Поиск корней
    roots = []
    if d > 0:
        roots.append((-b + math.sqrt(d)) / (2 * a))
        roots.append((-b - math.sqrt(d)) / (2 * a))
    elif d == 0:
        roots.append(-b / (2 * a))
    else:
        pass
    return roots