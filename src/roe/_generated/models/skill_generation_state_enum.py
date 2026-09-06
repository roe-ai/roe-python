from enum import Enum

class SkillGenerationStateEnum(str, Enum):
    FAILED = "failed"
    GENERATING = "generating"

    def __str__(self) -> str:
        return str(self.value)
