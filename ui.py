from src.game import Game


class UI:

    def __init__(self, game: Game):
        self.game = game

    def run_ui(self):
        while self.game.year <= 5:
            self.print_status()

            try:
                acres_decision, feed_decision, plant_decision = self.get_decisions()
                outcome = self.game.advance_year(acres_decision, feed_decision, plant_decision)

                if outcome == "STARVE ENDING":
                    self.game_over(True)

            except Exception as error:
                print("\nInvalid input!", error)

        self.game_over(False)

    @staticmethod
    def get_decisions() -> tuple[int, int, int]:
        acres_decision = int(input("\nAcres to buy/sell (+/-) -> "))
        feed_decision = int(input("Units to feed the population -> "))
        plant_decision = int(input("Acres to plant -> "))

        return acres_decision, feed_decision, plant_decision

    def print_status(self):
        print(f"\nIn year {self.game.year}, {self.game.people_starved} people starved.\n"
              f"{self.game.people_came} people came to the city.\n"
              f"City population is {self.game.population}\n"
              f"City owns {self.game.acres} acres of land.\n"
              f"Harvest was {self.game.harvest_rate} units per acre\n"
              f"Rats ate {self.game.rats} units\n"
              f"Land price is {self.game.land_price} units per acre\n"
              f"Grain stocks are {self.game.grains} units\n")

    def game_over(self, starve_ending: bool):
        if starve_ending:
            print("\n GAME OVER! Your people starved to death")
        else:
            good_ending = self.game.population >= 100 and self.game.acres >= 1000

            if good_ending:
                print("\n Game over! You did well")
            else:
                print("\n Game over! You didn't do well")



