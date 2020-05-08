import collections
import copy
import functools
from typing import List, Tuple

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def get_neighbors(coordinate: Coordinate) -> Tuple[Coordinate]:
    return (
        Coordinate(coordinate.x + 1, coordinate.y),
        Coordinate(coordinate.x - 1, coordinate.y),
        Coordinate(coordinate.x, coordinate.y + 1),
        Coordinate(coordinate.x, coordinate.y - 1),
    )


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    q = collections.deque([(s, None),])
    visited = {}
    path = []
    while q:
        now, parent = q.popleft()
        visited[now] = parent
        if now == e: break

        for neighbor in get_neighbors(now):
            if neighbor not in visited and path_element_is_feasible(maze, now, neighbor):
                q.append((neighbor, now))
    
    if e not in visited:
        return path

    cur = e
    while cur:
        path.append(cur)
        cur = visited[cur]
    path.reverse()
    return path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
