from src.exceptions import GameError
import random


class Game:
    def __init__(self):
        self.year = 1
        self.grains = 2800

        self.people_starved = 0
        self.people_came = 0
        self.population = 100

        self.acres = 1000
        self.acres_planted = 0
        self.harvest_rate = 3
        self.land_price = 20
        self.rats = 200

    def advance_year(self, acres_decision: int, feed_decision: int, plant_decision: int) -> str:
        """
        This function implements the decisions taken by the player and advances through the years

        :param acres_decision: int amount of acres to buy or sell
        :param feed_decision:  int amount of acres to feed
        :param plant_decision: int amount of acres to plant
        :return: returns a string that determines the which ending is achieved "STARVED ENDING"
                 if the starved ending is achieved and "CONTINUE" if the starved ending is not
                 achieved yet and the game continues
        """
        self.verify_decisions(acres_decision, feed_decision, plant_decision)

        # selling/buying land
        self.acres += acres_decision
        self.grains -= acres_decision * self.land_price

        # feeding the population
        people_fed = feed_decision // 20
        if people_fed > self.population:
            people_fed = self.population
        self.grains -= feed_decision
        if people_fed < self.population // 2:
            return "STARVE ENDING"

        self.people_starved = self.population - people_fed
        if self.people_starved == 0:
            self.people_came = random.randint(0, 10)

        # computing the total population
        self.population = self.population - self.people_starved + self.people_came

        # planting
        self.grains -= plant_decision
        self.acres_planted = plant_decision

        # randomize prices and harvest rate
        self.land_price = random.randint(15, 25)
        self.harvest_rate = random.randint(1, 6)

        # grains made from harvesting
        self.grains = self.acres_planted * self.harvest_rate

        # There is a 20% chance if we choose a number between 1 and 5
        rats_chance = random.randint(1, 5)
        if rats_chance == 1:
            percentage_ate = random.randint(1, 10)
            self.rats = percentage_ate // 100 * self.grains
            self.grains -= self.rats

        self.year += 1

        return "CONTINUE"

    def verify_decisions(self, acres_decision: int, feed_decision: int, plant_decision: int):
        total_grains_spent = acres_decision * self.land_price + feed_decision + plant_decision

        if self.grains - total_grains_spent < 0:
            raise GameError("You can't spend more grains than you own")

        if self.population * 10 < plant_decision:
            raise GameError("You don't have have enough people to plant the acres")

        if self.acres + acres_decision < plant_decision:
            raise GameError("You don't have enough acres to plant")

        if self.acres + acres_decision < 0:
            raise GameError("You can't sell more grains than you have")
