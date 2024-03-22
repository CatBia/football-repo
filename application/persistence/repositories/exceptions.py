from typing import Optional
from persistence.repositories.constants import COMPETITION_DOES_NOT_EXISTS


class CompetitionDoesNotExists(Exception):
    def __init__(self, message: str = COMPETITION_DOES_NOT_EXISTS) -> None:
        super().__init__(message)
