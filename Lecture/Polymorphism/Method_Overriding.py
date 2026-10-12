class City:
    cityName = "Rajkot"

    def greetings(self):
        print("Welcome to the City")


class Surat(City):
    # greetings() => City parent class

    def greerings(self):
        super().greetings()
        print(super().cityName)
        print("Welcome to the Surat City")


s = Surat()

s.greerings()
