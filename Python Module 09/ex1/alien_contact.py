from enum import Enum
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Optional
from datetime import datetime


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate(self):
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contacts must be verified.")
        if (self.contact_type == ContactType.telepathic
                and self.witness_count < 3):
            msg = "Telepathic contact requires at least 3 witnesses"
            raise ValueError(msg)
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals must have a message received.")
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'.")
        return self


def main():
    print("Alien Contact Log Validation")
    try:
        print("======================================")
        ac = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        print(f"ID: {ac.contact_id}")
        print(f"Type: {ac.contact_type.value}")
        print(f"Location: {ac.location}")
        print(f"Signal: {ac.signal_strength}/10")
        print(f"Duration: {ac.duration_minutes} minutes")
        print(f"Witnesses: {ac.witness_count}")
        print(f"Message: '{ac.message_received}'")

    except ValidationError as e:
        print("Validation error:")
        msg = e.errors()[0]["msg"].replace("Value error, ", "")
        print(msg)

    print("\n======================================")
    try:
        ac = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as e:
        print("Expected validation error:")
        msg = e.errors()[0]["msg"].replace("Value error, ", "")
        print(msg)


if __name__ == "__main__":
    main()
