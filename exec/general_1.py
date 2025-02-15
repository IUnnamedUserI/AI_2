#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def count_islands(grid):
    '''
    Метод подсчёта количества островов при помощи метода поиска в ширину.

    Аргументы:
        grid (list) - бинарная матрица, где 1 - остров, 0 - вода

    Возвращает:
        int - количество островов
    '''

    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    def bfs(r, c):
        queue = [(r, c)]
        while queue:
            row, col = queue.pop(0)

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append((nr, nc))

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                island_count += 1
                grid[i][j] = 0
                bfs(i, j)

    return island_count


def main():
    """
    Основная функция программы.
    """
    # Исходные данные
    grid = [
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
    ]

    island_count = count_islands(grid)
    print(f"Общее количество островов: {island_count}")


if __name__ == "__main__":
    main()
