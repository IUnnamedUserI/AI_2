#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def shortest_path(maze, initial, goal):
    """
    Находит кратчайший путь в лабиринте от начальной точки до целевой.

    Аргументы:
        maze (list) - Бинарная матрица, представляющая лабиринт, где
            1 обозначает проход;
            0 обозначает стену.

        initial (tuple) - Координаты начальной точки (строка, столбец).
        goal (tuple) - Координаты целевой точки (строка, столбец).

    Возвращает:
        int - Длина кратчайшего пути. Если путь не найден, возвращает -1.
    """

    rows = len(maze)
    cols = len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if maze[initial[0]][initial[1]] != 1 or maze[goal[0]][goal[1]] != 1:
        return -1

    queue = [(initial[0], initial[1], 0)]

    visited = set()
    visited.add((initial[0], initial[1]))

    while queue:
        row, col, distance = queue.pop(0)

        if (row, col) == goal:
            return distance

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if (0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 1):
                if ((nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc, distance + 1))

    return -1


def main():
    """
    Основная функция программы.
    """
    # Пример лабиринта
    maze = [
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    ]
    initial = (0, 0)  # Начальная точка
    goal = (9, 9)  # Целевая точка

    path_length = shortest_path(maze, initial, goal)

    if path_length != -1:
        print(f"Длина кратчайшего пути: {path_length}")
    else:
        print("Путь не найден.")


if __name__ == "__main__":
    main()
