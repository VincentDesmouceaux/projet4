from dataclasses import dataclass
import datetime


@dataclass
class Player:
    first_name: str
    last_name: str
    birth_date: datetime.date
    chess_id: str
    score: float = 0.0

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Score: {self.score}"

    def as_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date.isoformat(),
            "chess_id": self.chess_id,
            "score": self.score
        }

    @classmethod
    def from_dict(cls, data):
        birth_date = datetime.datetime.strptime(data["birth_date"], "%Y-%m-%d").date()
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            birth_date=birth_date,
            chess_id=data["chess_id"],
            score=data.get("score", 0.0)
        )
