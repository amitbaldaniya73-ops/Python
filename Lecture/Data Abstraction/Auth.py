from abc import ABC, abstractmethod


class Auth(ABC):

    @abstractmethod
    def sign_up(self, username, email, password):
        pass

    @abstractmethod
    def sign_in(self, email, password):
        pass

    @abstractmethod
    def sign_out(self):
        pass


class FitnessApp(Auth):

    def sign_up(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

        print("\nUser Registed Successfully..")

    def sign_in(self, email, password):
        if self.email == email:
            if self.password == password:
                print("\nUser Login Successfully..")
            else:
                print("\nPassword is wrong")
        else:
            print("\nEmail is wrong")

    def sign_out(self):
        self.username = ""
        self.email = ""
        self.password = ""

        print("\nLogout successfully..")


amit = FitnessApp()

amit.sign_up("Amit", "amit@gmail.com", "Amit@123")
amit.sign_in("amit@gmail.com", "Amit@123")

amit.sign_out()
