from dataclasses import dataclass, field
from typing import List
import datetime
from .match import Match


@dataclass
class Round:
    name: str
    matches: List[Match] = field(default_factory=list)
    start_time: datetime.datetime = None
    end_time: datetime.datetime = None

    def start_round(self):
        self.start_time = datetime.datetime.now()

    def end_round(self):
        self.end_time = datetime.datetime.now()

    def add_match(self, match: Match):
        self.matches.append(match)
        match.play_match()

    def __str__(self):
        round_details = f"{self.name} - Start: {self.start_time}, End: {self.end_time}\n"
        if self.matches:
            for match in self.matches:
                round_details += str(match) + "\n"
        else:
            round_details += "No matches played yet."
        return round_details

    def as_dict(self):
        return {
            "name": self.name,
            "matches": [match.as_dict() for match in self.matches],
            "start_time": self.start_time.isoformat() if self.start_time else None,
            "end_time": self.end_time.isoformat() if self.end_time else None
        }

    @classmethod
    def from_dict(cls, data):
        matches = [Match.from_dict(match_data) for match_data in data.get("matches", [])]
        start_time = datetime.datetime.fromisoformat(data["start_time"]) if data["start_time"] else None
        end_time = datetime.datetime.fromisoformat(data["end_time"]) if data["end_time"] else None
        return cls(name=data["name"], matches=matches, start_time=start_time, end_time=end_time)
