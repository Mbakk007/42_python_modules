from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


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
    crew: list[CrewMember] = Field(min_items=1, max_items=12)
    mission_status: str = Field(default="planned")
    budget_million: float = Field(ge=1.0, le=10000.0)


@model_validator(mode="after")
def validate_mission(mission: SpaceMission) -> SpaceMission:
    if not mission.mission_id.startswith("M"):
        raise ValueError("Mission ID must start with 'M'.")
    for crew in mission.crew:
        if not crew.is_active:
            raise ValueError("All crew members must be active.")
    if ([Rank.commander, Rank.captain] not
            in [member.rank for member in mission.crew]):
        raise ValueError("Mission must have at least one Commander or Captain")
    if mission.duration_days > 365:
        crew_count = len(mission.crew)
        is_experienced = 0
        for crew in mission.crew:
            if crew.years_experience > 5:
                is_experienced += 1
        if is_experienced < crew_count / 2:
            raise ValueError("Long missions need 50 percent experienced crew")
    return mission


def main():
    print("Space Mission Crew Validation")
    try:
        print("======================================")
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_million=2500.0,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.commander,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=35,
                    specialization="Navigation",
                    years_experience=10
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=30,
                    specialization="Engineering",
                    years_experience=8
                )
            ]
        )
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_million}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) "
                  f"- {member.specialization}")
    except ValidationError as e:
        print("Validation error:")
        msg = e.errors()[0]["msg"].replace("Value error, ", "")
        print(msg)
    print("\n======================================")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            budget_million=2500.0,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.lieutenant,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.lieutenant,
                    age=35,
                    specialization="Navigation",
                    years_experience=10
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.officer,
                    age=30,
                    specialization="Engineering",
                    years_experience=8
                )
            ]
        )
    except ValidationError as e:
        print("Expected validation error:")
        msg = e.errors()[0]["msg"].replace("Value error, ", "")
        print(msg)


if __name__ == "__main__":
    main()
