class IteratorTeam:
    def __init__(self):
        self.team = Team()
        self.i = 0
        self.juniors = self.team.juniors
        self.seniors = self.team.seniors

    def __next__(self):
        if self.i < len(self.team.juniors):
            index = self.i
            self.i += 1
            return self.team.juniors[index]
        elif self.i < len(self.seniors) + len(self.juniors):
            index = self.i - len(self.juniors)
            self.i += 1
            return self.seniors[index]
        else:
            raise StopIteration

class Team:
    def __init__(self):
        self.juniors = ["JPlayer 1", "JPlayer 2", "JPlayer 3", "JPlayer 4", "JPlayer 5"]
        self.seniors = ["Player 1", "Player 2", "Player 3", "Player 4"]

    def __iter__(self):
        return IteratorTeam()

for x in Team():
    print(x)