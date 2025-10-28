from enum import Enum



class CandidateStatus(Enum):
    NEW = "new"
    INTERVIEWED = "interviewed"
    REJECTED = "rejected"
    HIRED = "hired"