#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bfs_jugs(initial, goal, sizes):
    """
    Решает задачу о льющихся кувшинах с использованием BFS.

    Параметры:
        initial (tuple) - Начальное состояние (количество воды в кувшине).
        goal (int) - Целевой объем воды.
        sizes (tuple) - Размеры (емкости) кувшинов.

    Возвращает:
        list - Последовательность действий для достижения цели.
        list - Последовательность состояний, соответствующих действиям.
    """
    from collections import deque

    if goal in initial:
        return [], [initial]

    queue = deque([(initial, [], [initial])])

    visited = set()
    visited.add(initial)

    while queue:
        state, actions, states = queue.popleft()

        for action in get_possible_actions(state, sizes):
            new_state = apply_action(state, action, sizes)
            if new_state not in visited:
                new_actions = actions + [action]
                new_states = states + [new_state]

                if goal in new_state:
                    return new_actions, new_states
                visited.add(new_state)
                queue.append((new_state, new_actions, new_states))

    return [], []


def get_possible_actions(state, sizes):
    """
    Возвращает список возможных действий для текущего состояния.

    Аргументы:
        state (tuple) - Текущее состояние (количество воды в каждом кувшине).
        sizes (tuple) - Размеры (емкости) кувшинов.

    Возвращает:
        list - Список возможных действий.
    """
    actions = []
    num_jugs = len(state)

    for i in range(num_jugs):
        if state[i] < sizes[i]:
            actions.append(('Fill', i))
        if state[i] > 0:
            actions.append(('Dump', i))

    for i in range(num_jugs):
        for j in range(num_jugs):
            if i != j and state[i] > 0 and state[j] < sizes[j]:
                actions.append(('Pour', i, j))

    return actions


def apply_action(state, action, sizes):
    """
    Применяет действие к текущему состоянию и возвращает новое состояние.

    Аргументы:
        state (tuple) - Текущее состояние (количество воды в каждом кувшине).
        action (tuple) - Действие (Fill, Dump или Pour).
        sizes (tuple) - Размеры (емкости) кувшинов.

    Возвращает:
        tuple - Новое состояние после применения действия.
    """
    state = list(state)
    action_type = action[0]

    if action_type == 'Fill':
        i = action[1]
        state[i] = sizes[i]
    elif action_type == 'Dump':
        i = action[1]
        state[i] = 0
    elif action_type == 'Pour':
        i, j = action[1], action[2]
        amount = min(state[i], sizes[j] - state[j])
        state[i] -= amount
        state[j] += amount

    return tuple(state)


def main():
    """
    Основная функция программы.
    """
    # Входные данные
    initial = (0, 0, 0)  # Изначальное состояние
    goal = 6  # Необходимая цель
    sizes = (3, 5, 8)  # Объём кувшинов

    actions, states = bfs_jugs(initial, goal, sizes)

    if actions:
        print("Последовательность действий:", actions)
        print("Последовательность состояний:", states)
    else:
        print("Решение не найдено.")


if __name__ == "__main__":
    main()
