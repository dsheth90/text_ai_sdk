from enum import Enum


class JobStatus(Enum):
    IN_PROGRESS = 1
    TRANSCRIBED = 2
    FAILED = 3

    @classmethod
    def from_string(cls, status):
        return cls[status.upper()]
