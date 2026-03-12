from pydantic import Field, BaseModel, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_model(self):
        if not self.contact_id.startswith('AC'):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (self.contact_type == ContactType.TELEPATHIC
           and self.witness_count < 3):
            raise ValueError('Telepathic contact requires at least 3 witnesses\
')

        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError("Strong signals (> 7.0) \
should include received messages")

        return self


def main():

    print('Alien Contact Log Validation')
    print('======================================')
    try:
        alien_message = AlienContact(
            contact_id='AC_005',
            timestamp='1990-03-02 08:30:00',
            location='Area 51, Nevada',
            contact_type='radio',
            signal_strength=7.1,
            duration_minutes=12,
            witness_count=14,
            message_received='Greetings from Zeta Reticuli'
            )
        print("Valid contact report:")
        print(f"ID: {alien_message.contact_id}")
        print(f"Type: {alien_message.contact_type.value}")
        print(f"Location: {alien_message.location}")
        print(f"Signal: {alien_message.signal_strength}/10")
        print(f"Duration: {alien_message.duration_minutes} minutes")
        print(f"Witnesses: {alien_message.witness_count}")
        if alien_message.message_received:
            print(f"Message: '{alien_message.message_received}'")
    except ValueError as e:
        print(e.errors()[0]['msg'])

    print('\n======================================')
    try:
        alien_message = AlienContact(
            contact_id='AC_005',
            timestamp='1990-03-02 08:30:00',
            location='Area 51, Nevada',
            contact_type='physical',
            signal_strength=7.1,
            duration_minutes=12,
            witness_count=14,
            message_received='Greetings from Zeta Reticuli'
            )

    except ValueError as e:
        print(e.errors()[0]['msg'])

    try:
        alien_message = AlienContact(
            contact_id='AC_005',
            timestamp='1990-03-02 08:30:00',
            location='Area 51, Nevada',
            contact_type='radio',
            signal_strength=7.1,
            duration_minutes=12,
            witness_count=14,
            # message_received='Greetings from Zeta Reticuli'
            )

    except ValueError as e:
        error_msg = e.errors()[0]['msg']
        trunk_msg = error_msg.replace('Value error, ', '')
        print(trunk_msg)


if __name__ == "__main__":
    main()
