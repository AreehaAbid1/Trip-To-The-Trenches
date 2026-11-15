class Creatures():
    def __init__(self, name, zone, depth, danger_level, bioluminescent, fact):
        self.name = name
        self.zone = zone
        self.depth = depth
        self.danger_level = danger_level
        self.bioluminescent = bioluminescent
        self.fact = fact

# Constructor order: Creatures(name, zone, depth, danger_level, bioluminescent, fact)
# depth is in meters (a number); danger_level is a game rating from 1 (harmless) to 5 (extreme)

