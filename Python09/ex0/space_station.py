from pydantic import Field, BaseModel, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main():

    print('Space Station Data Validation')
    print('========================================')
    try:
        valid_station = SpaceStation(
            station_id='ISS001',
            name='International Space Station',
            crew_size=6,
            power_level=85.5,
            oxygen_level=91.3,
            last_maintenance='1990-03-02 08:30:00',
            )
    except ValidationError as e:
        print(e)
    if valid_station:
        print('Valid station created:')
        print(f'ID: {valid_station.station_id}')
        print(f'Name: {valid_station.name}')
        print(f'Crew: {valid_station.crew_size} people')
        print(f'Power: {valid_station.power_level}%')
        print(f'Oxygen: {valid_station.oxygen_level}%')
        if valid_station.is_operational is True:
            print('Status: Operational')
        else:
            print('Status: Not operational')
        print(valid_station.last_maintenance)
    print('\n========================================')
    print('Invalid station created:\n')

    try:
        invalid_station = SpaceStation(
            station_id='01',
            name='88',
            crew_size=19,
            power_level=200,
            oxygen_level=90,
            last_maintenance='1990-03-02 08:30:00.010000000000',
            )
        print(invalid_station)
    except ValidationError as e:
        print(f'Total errors: {e.error_count()}')
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()