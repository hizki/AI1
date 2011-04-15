from problem import ProblemState, ProblemAction


class MultiRobotState(ProblemState):
    '''
    A multi-robot problem state.

    Contains:
    - The room's X and Y dimensions (excluding walls).
    - A tuple of all the robots' locations. Each robot is denoted by its index in the list.
    - A frozenset of all the piles of dirt.
    - A frozenset of all the impassable obstacles, including room borders.

    Note that this class is immutable.
    '''

    def __init__(self, width, height, robots, dirt_locations, obstacle_locations):
        '''
        Creates a new multi-robot problem state.
        @param width: The room's X dimension (excluding walls).
        @param height: The room's Y dimension (excluding walls).
        @param robots: A tuple of all the robots' locations. Each robot is denoted by its index in the list.
        @param dirt_locations: A frozenset of all the piles of dirt.
        @param obstacle_locations: A frozenset of all the impassable obstacles.
        '''
        self.width = width
        self.height = height
        self.robots = robots
        self.dirt_locations = dirt_locations
        self.obstacle_locations = obstacle_locations

    def __cmp__(self, other):
        '''
        The comparison method must be implemented to ensure deterministic results.
        @return: Negative if self < other, zero if self == other and strictly
        positive if self > other.
        '''
        return cmp((self.robots, self.dirt_locations), (other.robots, other.dirt_locations))

    def __hash__(self):
        '''
        The hash method must be implemented for states to be inserted into sets
        and dictionaries.
        @return: The hash value of the state.
        '''
        return hash((self.robots, self.dirt_locations))

    def __str__(self):
        '''
        The string representation of the state. ASCII art FTW!
        '''
        map = []
        for y in xrange(0, self.height):
            row = []
            for x in xrange(0, self.width):
                row += [' ']
            map += [row]

        for i, robot in enumerate(self.robots):
            map[robot[1]][robot[0]] = str(i)
        for dirt in self.dirt_locations:
            map[dirt[1]][dirt[0]] = '*'
        for obstacle in self.obstacle_locations:
            map[obstacle[1]][obstacle[0]] = 'X'

        for y in xrange(0, self.height):
            map[y] = ['X'] + map[y]
            map[y] = map[y] + ['X']
        map = ['X' * (self.width + 2)] + map
        map = map + ['X' * (self.width + 2)]

        s = ''
        for row in map:
            for char in row:
                s += char
            s += '\n'

        return s

    def getSuccessors(self):
        '''
        Generates all the actions that can be performed from this state, and
        the States those actions will create.

        @return: A dictionary containing each action as a key, and it's state.
        '''
        successors = {}
        self.getPartialSuccessors(successors, [], self)
        return successors

    def getPartialSuccessors(self, successors, partial_directions, partial_state):
        '''
        Recursively generates all successors and adds them to the given dictionary.
        @param successors: A dictionary that maps actions to successor states.
        @param partial_directions: A list assigning movements to each of the first few robots.
        @param partial_state: A partly-modified version of the current state,
        taking into account the modifications in partial_directions.
        '''
        if len(partial_directions) == len(self.robots):
            successors[MoveAction(tuple(partial_directions))] = partial_state
            return

        robot = len(partial_directions)
        for direction in (UP, RIGHT, DOWN, LEFT, NOP):
            new_location = direction.move(partial_state.robots[robot])
            new_robots = partial_state.robots[:robot]

            if new_location[0] < 0 or new_location[0] >= self.width:
                continue
            if new_location[1] < 0 or new_location[1] >= self.height:
                continue
            if new_location in self.obstacle_locations:
                continue
            if new_location in new_robots:
                continue

            new_robots += tuple([new_location]) + partial_state.robots[(robot+1):]

            new_dirt_locations = set(partial_state.dirt_locations)
            if new_location in new_dirt_locations:
                new_dirt_locations.remove(new_location)
            new_dirt_locations = frozenset(new_dirt_locations)

            new_partial_state = MultiRobotState(self.width, self.height, new_robots, new_dirt_locations, self.obstacle_locations)

            self.getPartialSuccessors(successors, partial_directions + [direction], new_partial_state)

    def isGoal(self):
        '''
        @return: Whether all the dirt has been cleaned.
        '''
        return (len(self.dirt_locations) == 0)

    def nextState(self,moveAction):
        '''
        Applies action to the state to create next one
        @param moveAction : MoveAction
        '''
        new_robots = ()
        new_dirt_locations = set(self.dirt_locations)

        for d,r in zip(moveAction.getDirections(), self.robots):
            new_location = d.move(r)
            if new_location in new_dirt_locations:
                new_dirt_locations.remove(new_location)
            new_robots += tuple([new_location])

        new_dirt_locations = frozenset(new_dirt_locations)

        self.robots = new_robots
        self.dirt_locations = new_dirt_locations

class MoveAction(ProblemAction):
    '''
    Describes the concurrent movement of all robots.
    '''


    def getDirections(self):
        return self.directions

    def __init__(self, directions):
        '''
        Creates a new MoveAction.
        @param directions: A tuple assigning each robot its direction.
        '''
        ProblemAction.__init__(self)
        self.directions = directions

    def __cmp__(self, other):
        '''
        The comparison method must be implemented to ensure deterministic results.
        @return: Negative if self < other, zero if self == other and strictly
        positive if self > other.
        '''
        return cmp(self.directions, other.directions)

    def __hash__(self):
        '''
        The hash method must be implemented for actions to be inserted into sets
        and dictionaries.
        @return: The hash value of the action.
        '''
        return hash(self.directions)

    def __str__(self):
        '''
        @return: The string representation of this object when *str* is called.
        '''
        return str(self.directions)


class Direction():
    '''
    A direction of movement.
    '''

    def __init__(self, name, delta):
        '''
        Creates a new direction.
        @param name: The direction's name.
        @param delta: The coordinate modification needed for moving in the specified direction.
        '''
        self.name = name
        self.delta = delta

    def __cmp__(self, other):
        '''
        The comparison method must be implemented to ensure deterministic results.
        @return: Negative if self < other, zero if self == other and strictly
        positive if self > other.
        '''
        return cmp(self.name, other.name)

    def __hash__(self):
        '''
        The hash method must be implemented for actions to be inserted into sets
        and dictionaries.
        @return: The hash value of the action.
        '''
        return hash(self.name)

    def __str__(self):
        '''
        @return: The string representation of this object when *str* is called.
        '''
        return str(self.name)

    def __repr__(self):
        return self.__str__()

    def move(self, location):
        '''
        @return: Moving from the given location in this direction will result in the returned location.
        '''
        return (location[0] + self.delta[0], location[1] + self.delta[1])

#Global Directions
UP = Direction("up", (0, -1))
RIGHT = Direction("right", (1, 0))
DOWN = Direction("down", (0, 1))
LEFT = Direction("left", (-1, 0))
NOP = Direction("nop", (0, 0))
