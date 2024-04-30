import datetime


class DVD:
    def __init__(self, name: str,id: int, creation_year: int, creation_month: int, age_restriction : int) -> None:
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month_number, year = date.split('.')
        month_integer = int(month_number)
        month = datetime.date(1900, month_integer, 1).strftime('%B')

        return cls(name, id, int(year), month, age_restriction)

    def __repr__(self) -> str:
        return (f"{self.id}: {self.name} ({self.creation_month} "
                f"{self.creation_year}) has age restriction "
                f"{self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}")
