"""this class keeps the location of the object"""


class Location:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)


"""this method calculate the number of remaining mashrooms"""


def number_of_remaining_mashrooms():
    i = 2 * k
    if len(blue_mashrooms) < k:
        i -= (k - len(blue_mashrooms))
    if len(red_mashrooms) < k:
        i -= (k - len(red_mashrooms))
    return i


"""this class is for result table in LRTA*"""


class Result:
    def __init__(self, s, a, sp):
        self.s = s
        self.a = a
        self.sp = sp


"""this method return the huristic of the the location"""


def huristic():
    return number_of_remaining_mashrooms()


"""this checks whether we have reached our goal or not"""


def goal_test():
    if len(blue_mashrooms) < k and len(red_mashrooms) < k:
        print(current_location.x, current_location.y)
        print("you have reached the goal!")
        exit()


"""this method finds the minimum cost action"""


def min_action(s):
    x = s.x
    y = s.y
    """tm as temp should be an integer bigger than 2"""
    tm = 8
    ac = None
    if x != 1:
        x -= 1
        available = False
        for j in H:
            if j[0].x == x and j[0].y == y:
                tm = 1 + j[1]
                available = True
                ac = 'l'
                break
        if not available:
            barrier = False
            for result in results:
                if result.s.x == current_location.x and result.s.y == current_location.y \
                        and result.a == 'l' and result.sp.x == current_location.x and result.sp.y == current_location.y:
                    barrier = True

                    break
            if not barrier:
                tm = huristic()
                ac = 'l'
        x += 1
    if y != 1:
        y -= 1
        available = False
        for j in H:
            if j[0].x == x and j[0].y == y:
                if 1 + j[1] <= tm:
                    tm = 1 + j[1]
                    ac = 'd'
                available = True
                break
        if not available:
            if huristic() <= tm:
                barrier = False
                for result in results:
                    if result.s.x == current_location.x and result.s.y == current_location.y \
                            and result.a == 'd' and result.sp.x == current_location.x and result.sp.y == current_location.y:
                        barrier = True

                        break
                if not barrier:
                    tm = huristic()
                    ac = 'd'
        y += 1
    if x != m:
        x += 1
        available = False
        for j in H:
            if j[0].x == x and j[0].y == y:
                if 1 + j[1] <= tm:
                    tm = 1 + j[1]
                    ac = 'r'
                available = True
                break
        if not available:
            if huristic() <= tm:
                barrier = False
                for result in results:
                    if result.s.x == current_location.x and result.s.y == current_location.y \
                            and result.a == 'r' and result.sp.x == current_location.x and result.sp.y == current_location.y:
                        barrier = True

                        break
                if not barrier:
                    tm = huristic()
                    ac = 'r'
        x -= 1
    if y != n:
        y += 1
        available = False
        for j in H:
            if j[0].x == x and j[0].y == y:
                if 1 + j[1] <= tm:
                    tm = 1 + j[1]
                    ac = 'u'
                available = True
                break
        if not available:
            if huristic() <= tm:
                barrier = False
                for result in results:
                    if result.s.x == current_location.x and result.s.y == current_location.y \
                            and result.a == 'u' and result.sp.x == current_location.x and result.sp.y == current_location.y:
                        barrier = True

                        break
                if not barrier:
                    tm = huristic()
                    ac = 'u'
        y -= 1
    return tm, ac


"""this method checks the mashrooms to see if they exist or not"""


def check_for_mashrooms():
    i = 0
    while i < len(red_mashrooms):
        if red_mashrooms[i].y == current_location.y and red_mashrooms[i].x == current_location.x:
            del red_mashrooms[i]
            continue
        i += 1
    i = 0
    while i < len(blue_mashrooms):
        if blue_mashrooms[i].y == current_location.y and blue_mashrooms[i].x == current_location.x:
            del blue_mashrooms[i]
            continue
        i += 1


"""this method move the mashroom_eater to upper location"""


def up():
    if current_location.y != n:
        y_temp = current_location.y + 1
        for i in barriers:
            if i.y == y_temp and i.x == current_location.x:
                results.append(Result(Location(current_location.x, current_location.y), 'u',
                                      Location(current_location.x, current_location.y)))
                return
        current_location.y += 1
        check_for_mashrooms()


"""this method move the mashroom_eater to the below location"""


def down():
    if current_location.y != 1:
        y_temp = current_location.y - 1
        for i in barriers:
            if i.y == y_temp and i.x == current_location.x:
                results.append(Result(Location(current_location.x, current_location.y), 'd',
                                      Location(current_location.x, current_location.y)))
                return
        current_location.y -= 1
        check_for_mashrooms()


"""this method move the mashroom_eater to the right location"""


def right():
    if current_location.x != m:
        x_temp = current_location.x + 1
        for i in barriers:
            if i.x == x_temp and i.y == current_location.y:
                results.append(Result(Location(current_location.x, current_location.y), 'r',
                                      Location(current_location.x, current_location.y)))
                return

        current_location.x += 1
        check_for_mashrooms()


"""this method move the mashroom_eater to the left location"""


def left():
    if current_location.x != 1:
        x_temp = current_location.x - 1
        for i in barriers:
            if i.x == x_temp and i.y == current_location.y:
                results.append(Result(Location(current_location.x, current_location.y), 'l',
                                      Location(current_location.x, current_location.y)))
                return
        current_location.x -= 1
        check_for_mashrooms()


if __name__ == "__main__":
    mario = open("Mario.txt", "r")
    lines = mario.readlines()
    mario.close()
    n = int(lines[0])
    m = int(lines[1])
    l = lines[2].split(" ")
    previous_location = None
    action = None
    current_location = Location(l[0], l[1])
    k = int(lines[3])
    blue_mashrooms = []
    red_mashrooms = []
    barriers = []
    results = []

    for i in range(4, 4 + k):
        temp = lines[i].split(" ")
        red_mashrooms.append(Location(temp[0], temp[1]))

    for i in range(4 + k, 4 + 2 * k):
        temp = lines[i].split(" ")
        blue_mashrooms.append(Location(temp[0], temp[1]))

    for i in range(4 + 2 * k, len(lines)):
        temp = lines[i].split(" ")
        barriers.append(Location(temp[0], temp[1]))
    """location , H, ActionMakesH"""
    H = [[Location(current_location.x, current_location.y), huristic(), None]]

    """it does LRTA* until we reach our goal"""
    while True:
        goal_test()
        print(current_location.x, current_location.y)
        flag = False
        for j in H:
            if j[0].x == current_location.x and j[0].y == current_location.y:
                flag = True
                break
        if not flag:
            H.append([Location(current_location.x, current_location.y), huristic(), None])

        if previous_location is not None:
            results.append(Result(Location(previous_location.x, previous_location.y), action,
                                  Location(current_location.x, current_location.y)))
            for i in H:
                if i[0].x == previous_location.x and i[0].y == previous_location.y:
                    i[1], i[2] = min_action(previous_location)
                    break
        else:
            previous_location = Location(1, 1)
        t, action = min_action(current_location)
        print("H: ", t)
        previous_location.x = current_location.x
        previous_location.y = current_location.y
        if action == 'u':
            print('u')
            up()
        elif action == 'd':
            down()
            print('d')
        elif action == 'r':
            right()
            print('r')
        else:
            left()
            print('l')
