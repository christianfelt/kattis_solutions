"""
Christian Felt
December 2019
Solves the ants problem on Kattis.
Solution strategy: Simulate the problem using object-oriented programming.
"""


class Ant:
    """Represent an ant."""

    def __init__(self, location, direction, has_fallen=False, name="Bobby"):
        self.location = location
        self.direction = direction
        self.has_fallen = has_fallen
        self.name = name

    def display(self):
        """Show info about ant."""
        print("Name:", self.name)
        print("Location:", self.location)
        print("Direction:", self.direction)
        print("Has fallen:", self.has_fallen)


class Log:
    """Represent a log with ants on it."""

    def __init__(self, ants, length):
        self.ants = ants
        self.length = length

    def display(self):
        """Print ant info."""
        print("Length:", self.length)
        print("Current ants on log:", len(self.ants))
        for ant in self.ants:
            ant.display()

    def has_ants(self):
        """Return whether log has ants."""
        return len(self.ants) > 0

    def detect_midturn_collision(self, ant1, ant2):
        """Detect a collision between ant1 and ant2 a the middle of this second and update their instance variables
        appropriately."""
        if (ant1.location == ant2.location - 1 and ant1.direction == 1 and ant2.direction == -1) \
                or (ant2.location == ant1.location - 1 and ant2.direction == 1 and ant1.direction == -1):
            ant1.direction = -ant1.direction
            ant2.direction = -ant2.direction
            return ant1, ant2
        else:
            return None, None

    def detect_endturn_collision(self, ant1, ant2):
        """Detect a collision at the end of a turn, i.e. when two ants now occupy the same spot, and reverse
        their directions."""
        if ant1.location == ant2.location:
            ant1.direction = -ant1.direction
            ant2.direction = -ant2.direction

    def elapse_second(self):
        """Do everything with ants on a log that happens in one second."""
        ants_to_remove = set()
        midturn_ants = set()
        for ant1 in self.ants:
            for ant2 in self.ants:
                if ant1 != ant2:
                    col1, col2 = self.detect_midturn_collision(ant1, ant2)
                    if col1 is not None:
                        midturn_ants.add(col1)
                        midturn_ants.add(col2)
        for ant1 in self.ants:
            if ant1 not in midturn_ants:  # The midturn ants have already moved; they were the only ones that might
                # experience a collision in the middle, rather than at the end of a turn.
                ant1.location += ant1.direction  # Any collisions that occur here will be dealt with at end of turn.
                if ant1.location == 0 or ant1.location == self.length:
                    ant1.has_fallen = True
                    ants_to_remove.add(ant1)
        for ant1 in self.ants:
            for ant2 in self.ants:
                if ant1 != ant2:
                    self.detect_endturn_collision(ant1, ant2)
        for ant in ants_to_remove:
            self.ants.remove(ant)


def test():
    """Run a single ants on log simulation."""
    a = Ant(2, 1, False, "Jodey")
    b = Ant(3, -1, False, "Latisha")
    ants = set((a, b))
    log = Log(ants, 7)
    while len(log.ants) > 0:
        log.display()
        log.elapse_second()
    log.display()


def main():
    """Solve the Kattis Ants problem."""
    num_cases = int(input())
    for i in range(num_cases):
        length, n = map(int, input().split())
        positions = list(map(int, input().split()))
        directions_permutations = []
        for j in range(2 ** n):
            this_directions_permutation = bin(j)[2:].zfill(n)
            these_directions = list(map(int, list(this_directions_permutation)))
            for k, direction in enumerate(these_directions):
                if direction == 0:
                    these_directions[k] = -1
            directions_permutations.append(these_directions)
        min_time = float("inf")
        max_time = 0
        for directions in directions_permutations:
            elapsed_time = 0
            ants = set()
            for k in range(n):
                ants.add(Ant(positions[k], directions[k], False, "Bobby_" + str(k)))
            log = Log(ants, length)
            while len(log.ants) > 0:
                # log.display()
                log.elapse_second()
                elapsed_time += 1
            # log.display()
            min_time = min(min_time, elapsed_time)
            max_time = max(max_time, elapsed_time)
        print(min_time)
        print(max_time)


if __name__ == '__main__':
    main()
    # test()
