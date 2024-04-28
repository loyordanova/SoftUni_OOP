class Profile:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    @property
    def username(self) -> str:
        return self.__username

    @property
    def password(self) -> str:
        return self.__password

    @username.setter
    def username(self, username: str) -> None:
        if not 5 <= len(username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        self.__username = username

    @password.setter
    def password(self, password: str) -> None:
        uppercase_letter = any(ele.isupper() for ele in password)
        digits = any(ele.isdigit() for ele in password)

        if not len(password) >= 8 or not uppercase_letter or not digits:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__password = password

    def __str__(self) -> str:
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


profile_with_invalid_password = Profile('My_username', 'My-password')
