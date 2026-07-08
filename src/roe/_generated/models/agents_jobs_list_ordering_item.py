from enum import Enum

class AgentsJobsListOrderingItem(str, Enum):
    AGENT_VERSION_NAME = "agent_version_name"
    COST = "cost"
    CREATED_AT = "created_at"
    DURATION = "duration"
    GRADER_SCORE = "grader_score"
    ID = "id"
    LAST_UPDATED_AT = "last_updated_at"
    STATUS_CODE = "status_code"
    VALUE_0 = "-agent_version_name"
    VALUE_1 = "-cost"
    VALUE_2 = "-created_at"
    VALUE_3 = "-duration"
    VALUE_4 = "-grader_score"
    VALUE_5 = "-id"
    VALUE_6 = "-last_updated_at"
    VALUE_7 = "-status_code"

    def __str__(self) -> str:
        return str(self.value)
