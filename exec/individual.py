#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


# Пример входных данных (можно заменить своими)
cities = {
    'Лонгфорд': {
        'Ньюнхем': 31.4,
        'Экстон': 37.1,
        'Бреона': 51.4,
        'Конара': 43.2,
        'Дерби': 111.9
    },
    'Конара': {'Сент-Мэрис': 73.9, 'Кэмпбелл-Таун': 12.5},
    'Кэмпбелл-Таун': {'Танбридж': 27.1, 'Лейк Лик': 34.8},
    'Лейк Лик': {'Бичено': 57, 'Суонси': 33.8},
    'Ньюнхем': {'Джордж Таун': 44.3, 'Лилидейл': 21.3},
    'Джордж Таун': {},
    'Лилидейл': {'Лебрина': 8.7},
    'Лебрина': {'Пайперс Брук': 13.3, 'Бридпорт': 27},
    'Экстон': {'Элизабет Таун': 18.4, 'Мол Крик': 30.8, 'Бреона': 38.4},
    'Элизабет Таун': {'Шеффилд': 28, 'Девонпорт': 42.5},
    'Девонпорт': {},
    'Шеффилд': {'Мойна': 31.7},
    'Мойна': {},
    'Бреона': {'Рейнольдс Лейк': 11.2, 'Шеннон': 26.5, 'Ботуэлл': 66.7},
    'Рейнольдс Лейк': {'Миена': 18.5},
    'Мол Крик': {'Шеффилд': 51.5},
    'Миена': {'Тарралия': 59.2},
    'Шеннон': {'Миена': 17.2},
    'Тарралия': {'Уэйятина': 16.5},
    'Уэйятина': {},
    'Ботуэлл': {},
    'Танбридж': {},
    'Литл Суонпорт': {},
    'Суонси': {'Литл Суонпорт': 27.7},
    'Сент-Мэрис': {'Гарденс': 55.8},
    'Гарденс': {'Дерби': 61.1},
    'Дерби': {},
    'Пайперс Брук': {},
    'Бридпорт': {},
}

start_city = 'Сент-Мэрис'  # Исходный город
end_city = 'Мойна'    # Целевой город


# Создание симметричного графа
def create_symmetric_graph(cities):
    symmetric_cities = {}

    for city, neighbors in cities.items():
        if city not in symmetric_cities:
            symmetric_cities[city] = {}

        for neighbor, distance in neighbors.items():
            symmetric_cities[city][neighbor] = distance

            if neighbor not in symmetric_cities:
                symmetric_cities[neighbor] = {}

            symmetric_cities[neighbor][city] = distance

    return symmetric_cities


symmetric_cities = create_symmetric_graph(cities)


# Поиск кратчайшего пути с использованием BFS
def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])  # Очередь: (текущий город, путь)
    visited = set()

    while queue:
        current_city, path = queue.popleft()

        if current_city == end:
            return path

        if current_city not in visited:
            visited.add(current_city)

            for neighbor in graph.get(current_city, {}):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None


# Вычисление длины маршрута
def calculate_distance(route, graph):
    distance = 0

    for i in range(len(route) - 1):
        distance += graph[route[i]][route[i + 1]]

    return distance


# Построение графа и отображение маршрутов
def plot_graph(cities, shortest_route):
    G = nx.DiGraph()

    # Добавление рёбер с весами
    for city, neighbors in cities.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(city, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # Позиционирование узлов

    # Отображение графа
    plt.figure(figsize=(12, 8))
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=700,
            node_color='lightblue', font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Подсветка самого короткого маршрута
    if shortest_route:
        shortest_edges = [
            (shortest_route[i], shortest_route[i + 1])
            for i in range(len(shortest_route) - 1)
        ]

        nx.draw_networkx_edges(G, pos, edgelist=shortest_edges,
                               edge_color='red', width=2)

    plt.title("Граф маршрутов")
    plt.show()


# Основной код
shortest_route = bfs_shortest_path(symmetric_cities, start_city, end_city)

if shortest_route:
    shortest_distance = calculate_distance(shortest_route, symmetric_cities)
    print(f"Самый короткий маршрут: {' -> '.join(shortest_route)}, "
          f"Расстояние: {round(shortest_distance, 1)} км")
    plot_graph(symmetric_cities, shortest_route)
else:
    print("Маршрут не найден.")
