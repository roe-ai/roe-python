from enum import Enum

class KnowledgeBaseStatusEnum(str, Enum):
    ACTIVE = "active"
    DRAFTING = "drafting"
    ORPHANED = "orphaned"

    def __str__(self) -> str:
        return str(self.value)
