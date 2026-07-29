from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.agent_job_evaluation import AgentJobEvaluation
  from ..models.agent_job_feedback_nested import AgentJobFeedbackNested
  from ..models.job_input import JobInput
  from ..models.list_agent_job_metadata import ListAgentJobMetadata
  from ..models.public_agent_job_status_event import PublicAgentJobStatusEvent
  from ..models.user_info import UserInfo





T = TypeVar("T", bound="ListAgentJob")



@_attrs_define
class ListAgentJob:
    """ 
        Attributes:
            id (UUID):
            agent_version_name (None | str): Get the agent version name, handling null agent and annotation.
            status_events (list[PublicAgentJobStatusEvent]):
            status_code (int): Current status code of the job (0=PENDING, 1=STARTED, 2=RETRY, 3=SUCCESS, 4=FAILURE,
                5=CANCELLED, 6=CACHED)
            created_at (datetime.datetime): When the job was created
            last_updated_at (datetime.datetime):
            duration_ms (int | None): Job duration in milliseconds, computed from status_events. End time is the last non-
                CACHED event so trailing cache hits don't inflate duration. Null while the job is still running or when
                timestamps are missing.
            ui_fields (Any): Denormalized fields from agent output for list/metrics without loading S3
            evaluation (AgentJobEvaluation | None):
            feedback_review (AgentJobFeedbackNested | None):
            creator (None | UserInfo):
            job_inputs (list[JobInput] | Unset): List of input data provided to the agent job
            metadata (ListAgentJobMetadata | Unset): Key-value pairs of metadata associated with the job
     """

    id: UUID
    agent_version_name: None | str
    status_events: list[PublicAgentJobStatusEvent]
    status_code: int
    created_at: datetime.datetime
    last_updated_at: datetime.datetime
    duration_ms: int | None
    ui_fields: Any
    evaluation: AgentJobEvaluation | None
    feedback_review: AgentJobFeedbackNested | None
    creator: None | UserInfo
    job_inputs: list[JobInput] | Unset = UNSET
    metadata: ListAgentJobMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_job_evaluation import AgentJobEvaluation
        from ..models.agent_job_feedback_nested import AgentJobFeedbackNested
        from ..models.job_input import JobInput
        from ..models.list_agent_job_metadata import ListAgentJobMetadata
        from ..models.public_agent_job_status_event import PublicAgentJobStatusEvent
        from ..models.user_info import UserInfo
        id = str(self.id)

        agent_version_name: None | str
        agent_version_name = self.agent_version_name

        status_events = []
        for status_events_item_data in self.status_events:
            status_events_item = status_events_item_data.to_dict()
            status_events.append(status_events_item)



        status_code = self.status_code

        created_at = self.created_at.isoformat()

        last_updated_at = self.last_updated_at.isoformat()

        duration_ms: int | None
        duration_ms = self.duration_ms

        ui_fields = self.ui_fields

        evaluation: dict[str, Any] | None
        if isinstance(self.evaluation, AgentJobEvaluation):
            evaluation = self.evaluation.to_dict()
        else:
            evaluation = self.evaluation

        feedback_review: dict[str, Any] | None
        if isinstance(self.feedback_review, AgentJobFeedbackNested):
            feedback_review = self.feedback_review.to_dict()
        else:
            feedback_review = self.feedback_review

        creator: dict[str, Any] | None
        if isinstance(self.creator, UserInfo):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        job_inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.job_inputs, Unset):
            job_inputs = []
            for job_inputs_item_data in self.job_inputs:
                job_inputs_item = job_inputs_item_data.to_dict()
                job_inputs.append(job_inputs_item)



        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "agent_version_name": agent_version_name,
            "status_events": status_events,
            "status_code": status_code,
            "created_at": created_at,
            "last_updated_at": last_updated_at,
            "duration_ms": duration_ms,
            "ui_fields": ui_fields,
            "evaluation": evaluation,
            "feedback_review": feedback_review,
            "creator": creator,
        })
        if job_inputs is not UNSET:
            field_dict["job_inputs"] = job_inputs
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_job_evaluation import AgentJobEvaluation
        from ..models.agent_job_feedback_nested import AgentJobFeedbackNested
        from ..models.job_input import JobInput
        from ..models.list_agent_job_metadata import ListAgentJobMetadata
        from ..models.public_agent_job_status_event import PublicAgentJobStatusEvent
        from ..models.user_info import UserInfo
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        def _parse_agent_version_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_version_name = _parse_agent_version_name(d.pop("agent_version_name"))


        status_events = []
        _status_events = d.pop("status_events")
        for status_events_item_data in (_status_events):
            status_events_item = PublicAgentJobStatusEvent.from_dict(status_events_item_data)



            status_events.append(status_events_item)


        status_code = d.pop("status_code")

        created_at = isoparse(d.pop("created_at"))




        last_updated_at = isoparse(d.pop("last_updated_at"))




        def _parse_duration_ms(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        duration_ms = _parse_duration_ms(d.pop("duration_ms"))


        ui_fields = d.pop("ui_fields")

        def _parse_evaluation(data: object) -> AgentJobEvaluation | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                evaluation_type_0 = AgentJobEvaluation.from_dict(data)



                return evaluation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentJobEvaluation | None, data)

        evaluation = _parse_evaluation(d.pop("evaluation"))


        def _parse_feedback_review(data: object) -> AgentJobFeedbackNested | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                feedback_review_type_0 = AgentJobFeedbackNested.from_dict(data)



                return feedback_review_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentJobFeedbackNested | None, data)

        feedback_review = _parse_feedback_review(d.pop("feedback_review"))


        def _parse_creator(data: object) -> None | UserInfo:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                creator_type_0 = UserInfo.from_dict(data)



                return creator_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserInfo, data)

        creator = _parse_creator(d.pop("creator"))


        _job_inputs = d.pop("job_inputs", UNSET)
        job_inputs: list[JobInput] | Unset = UNSET
        if _job_inputs is not UNSET:
            job_inputs = []
            for job_inputs_item_data in _job_inputs:
                job_inputs_item = JobInput.from_dict(job_inputs_item_data)



                job_inputs.append(job_inputs_item)


        _metadata = d.pop("metadata", UNSET)
        metadata: ListAgentJobMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = ListAgentJobMetadata.from_dict(_metadata)




        list_agent_job = cls(
            id=id,
            agent_version_name=agent_version_name,
            status_events=status_events,
            status_code=status_code,
            created_at=created_at,
            last_updated_at=last_updated_at,
            duration_ms=duration_ms,
            ui_fields=ui_fields,
            evaluation=evaluation,
            feedback_review=feedback_review,
            creator=creator,
            job_inputs=job_inputs,
            metadata=metadata,
        )


        list_agent_job.additional_properties = d
        return list_agent_job

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
