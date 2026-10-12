"""
Multilevel Inheritance

Min => 3
Max => Unlimited

A  => B  => C  => D  => E
"""


class Admin:
    features = None

    def setAdminFeatures(self):
        self.features = input("Enter admin features : ")

    def getAdminFeatures(self):
        print(f"Admin Features : {self.features}")


class SubAdmin(Admin):
    subAdminFeatures = None

    def setSubAdminFeatures(self):
        self.subAdminFeatures = input("Enter sub admin features : ")

    def getSubAdminFeatures(self):
        print(f"Sub Admin Features : {self.subAdminFeatures}")


class User(SubAdmin):
    userFeatures = None

    def setUserFeatures(self):
        self.userFeatures = input("Enter user features : ")

    def getUserFeatures(self):
        print(f"User Features : {self.userFeatures}")


keval = User()

keval.setAdminFeatures()
keval.setSubAdminFeatures()
keval.setUserFeatures()

keval.getAdminFeatures()
keval.getSubAdminFeatures()
keval.getUserFeatures()
