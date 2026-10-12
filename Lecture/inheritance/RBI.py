class RBI:
    intrest = 0

    def setIntreset(self):
        self.intrest = float(input("\nEnter intreset : "))


class SBI(RBI):
    balance = 0

    def setSBIBalance(self):
        self.balance = float(input("\nEnter sbi balance : "))

    def calSBIFinalBalance(self):
        amount = (self.balance * self.intrest) / 100
        self.balance += amount
        print("\n")
        print(f"SBI Final Balance : {self.balance}\n\n")


class ICICI(RBI):
    balance = 0

    def setICICIBalance(self):
        self.balance = float(input("\nEnter icici balance : "))

    def calICICIFinalBalance(self):
        amount = (self.balance * self.intrest) / 100
        self.balance += amount
        print("\n")
        print(f"ICICI Final Balance : {self.balance}\n\n")


sbi = SBI()
icici = ICICI()

sbi.setSBIBalance()
sbi.setIntreset()
sbi.calSBIFinalBalance()


icici.setICICIBalance()
icici.setIntreset()
icici.calICICIFinalBalance()
