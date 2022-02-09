from functools import lru_cache
from math import inf as INFINITY

ROOM_DISTANCE = (
    (2, 1, 1, 3, 5, 7, 8), # from/to room 0
    (4, 3, 1, 1, 3, 5, 6), # from/to room 1
    (6, 5, 3, 1, 1, 3, 4), # from/to room 2
    (8, 7, 5, 3, 1, 1, 2), # from/to room 3
)


def Amphipods():
    fin = open("input day 23.txt", "r")
    hallway = (None,) * 7
    rooms = parse_rooms(fin)
    min_cost = solve(rooms, hallway)

    print('Part 1:', min_cost)

    newobjs = [(3, 3), (2, 1), (1, 0), (0, 2)]
    newrooms = []

    for room, new in zip(rooms, newobjs):
        newrooms.append((room[0], *new, room[-1]))

    rooms = tuple(newrooms)
    min_cost = solve(rooms, hallway, len(rooms[0]))

    print('Part 2:', min_cost)

@lru_cache(maxsize=None)
def solve(rooms, hallway, room_size=2):
    if done(rooms, room_size):
        return 0

    best = INFINITY

    for cost, next_state in possible_moves(rooms, hallway, room_size):
        cost += solve(*next_state, room_size)

        if cost < best:
            best = cost

    return best

def moves_to_room(rooms, hallway, room_size):
    # For any object in the hallway...
    for h, obj in enumerate(hallway):
        # Skip empty hallway spots.
        if obj is None:
            continue

        # Check the corresponding room: if it contains any other kind of object,
        # skip it, can't move this obj there yet.
        room = rooms[obj]
        if any(o != obj for o in room):
            continue

        # Calculate the cost of moving this object from this hallway spot
        # to its room.
        cost = move_cost(room, hallway, obj, h, room_size, True)

        # If it's impossible to move the object to the room (i.e. there is some
        # other object in the way from this spot to the room), skip it.
        if cost == INFINITY:
            continue

        # Create a new state where this object has been moved from slot h of the
        # hallway to its room, and yield it along with the cost.
        new_rooms   = rooms[:obj] + ((obj,) + room,) + rooms[obj + 1:]
        new_hallway = hallway[:h] + (None,) + hallway[h + 1:]
        yield cost, (new_rooms, new_hallway)

def moves_to_hallway(rooms, hallway, room_size):
    # For any room...
    for r, room in enumerate(rooms):
        # If the room we are looking at only contains the right objects,
        # those objects will not move from there, skip them.
        if all(o == r for o in room):
            continue

        # For any hallway spot...
        for h in range(len(hallway)):
            # Calculate the cost of moving this object from this room to this
            # hallway spot (h).
            cost = move_cost(room, hallway, r, h, room_size, False)

            # If it's impossible to move the object to this hallway spot (i.e.
            # there is some other object in the way), skip it.
            if cost == INFINITY:
                continue

            # Create a new state where this object has been moved from room r to
            # slot h of the hallway, and yield it along with the cost.
            new_rooms   = rooms[:r] + (room[1:],) + rooms[r + 1:]
            new_hallway = hallway[:h] + (room[0],) + hallway[h + 1:]
            yield cost, (new_rooms, new_hallway)

def possible_moves(rooms, hallway, room_size):
    try:
        yield next(moves_to_room(rooms, hallway, room_size))
    except StopIteration:
        yield from moves_to_hallway(rooms, hallway, room_size)

def move_cost(room, hallway, r, h, room_size, to_room=False):
    # Here h is the hallway spot index and r the room index.

    if r + 1 < h:
        start = r + 2
        end   = h + (not to_room)
    else:
        start = h + to_room
        end   = r + 2

    # Ceck if hallway path is clear.
    if any(x is not None for x in hallway[start:end]):
        return INFINITY

    # If moving to the room, the obj is in the hallway at spot h,
    # otherwise it's the first in the room.
    obj = hallway[h] if to_room else room[0]

    return 10**obj * (ROOM_DISTANCE[r][h] + (to_room + room_size - len(room)))

def done(rooms, room_size):
    for r, room in enumerate(rooms):
        if len(room) != room_size or any(obj != r for obj in room):
            return False
    return True

def parse_rooms(fin):
    next(fin)
    next(fin)
    rooms = []

    for _ in range(2):
        l = next(fin)
        rooms.append(map('ABCD'.index, (l[3], l[5], l[7], l[9])))

    return tuple(zip(*rooms))