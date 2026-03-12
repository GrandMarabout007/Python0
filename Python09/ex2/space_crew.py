from pydantic import Field, BaseModel, model_validator, ValidationError
from datetime import datetime
from typing import List
from enum import Enum


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_model(self):
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')
        leader_found = False
        experienced = 0
        all_active = True
        for member in self.crew:
            if member.rank in [Rank.CAPTAIN, Rank.COMMANDER]:
                leader_found = True
            if member.years_experience > 5:
                experienced += 1
            if member.is_active is False:
                all_active = False

        if not leader_found:
            raise ValueError("Mission must have at least one Captain \
or Commander")

        if self.duration_days > 365 and ((experienced/len(self.crew)) <= 0.5):
            raise ValueError("long missions must have an experienced crew")

        if all_active is False:
            raise ValueError('all crew members must be active')
        return self

    def __str__(self):
        res = (
            f"Mission: {self.mission_name}\n"
            f"ID: {self.mission_id}\n"
            f"Destination: {self.destination}\n"
            f"Duration: {self.duration_days} days\n"
            f"Budget: ${self.budget_millions}M\n"
            f"Crew size: {len(self.crew)}\n"
            f"Crew members:"
        )
        for member in self.crew:
            res += f"\n- {member.name} ({member.rank.value}) - \
{member.specialization}"

        return res


def main():
    print('Space Mission Crew Validation')
    print('=========================================')
    try:
        crew_list = [
            CrewMember(
                member_id="MEM001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=45,
                specialization="Mission Command",
                years_experience=20
            ),
            CrewMember(
                member_id="MEM002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=32,
                specialization="Navigation",
                years_experience=10
            ),
            CrewMember(
                member_id="MEM003",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=28,
                specialization="Engineering",
                years_experience=5
            )
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-07-12T10:00:00",
            duration_days=900,
            crew=crew_list,
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(mission)

    except ValidationError as e:
        error_msg = e.errors()[0]['msg']
        trunk_msg = error_msg.replace('Value error, ', '')
        print(trunk_msg)

    print('\n=========================================')
    try:
        crew_list = [
            CrewMember(
                member_id="MEM001",
                name="Sarah Connor",
                rank=Rank.CADET,
                age=45,
                specialization="Mission Command",
                years_experience=4
            ),
            CrewMember(
                member_id="MEM002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=32,
                specialization="Navigation",
                years_experience=10
            ),
            CrewMember(
                member_id="MEM003",
                name="Alice Johnson",
                rank=Rank.COMMANDER,
                age=28,
                specialization="Engineering",
                years_experience=50,
                is_active=True,
            )
        ]

        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-07-12T10:00:00",
            duration_days=900,
            crew=crew_list,
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(mission)

    except ValidationError as e:
        error_msg = e.errors()[0]['msg']
        trunk_msg = error_msg.replace('Value error, ', '')
        print(trunk_msg)


if __name__ == "__main__":
    main()
