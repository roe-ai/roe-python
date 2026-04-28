from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="AgentJobEvaluationItemRequest")



@_attrs_define
class AgentJobEvaluationItemRequest:
    """ Serializer for individual job evaluation item in bulk operation.

        Attributes:
            job_id (UUID):
            reference (Any | None | Unset):
            human_score (float | None | Unset):
            grader_score (float | None | Unset):
            feedback (str | Unset):
     """

    job_id: UUID
    reference: Any | None | Unset = UNSET
    human_score: float | None | Unset = UNSET
    grader_score: float | None | Unset = UNSET
    feedback: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        job_id = str(self.job_id)

        reference: Any | None | Unset
        if isinstance(self.reference, Unset):
            reference = UNSET
        else:
            reference = self.reference

        human_score: float | None | Unset
        if isinstance(self.human_score, Unset):
            human_score = UNSET
        else:
            human_score = self.human_score

        grader_score: float | None | Unset
        if isinstance(self.grader_score, Unset):
            grader_score = UNSET
        else:
            grader_score = self.grader_score

        feedback = self.feedback


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "job_id": job_id,
        })
        if reference is not UNSET:
            field_dict["reference"] = reference
        if human_score is not UNSET:
            field_dict["human_score"] = human_score
        if grader_score is not UNSET:
            field_dict["grader_score"] = grader_score
        if feedback is not UNSET:
            field_dict["feedback"] = feedback

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = UUID(d.pop("job_id"))




        def _parse_reference(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        reference = _parse_reference(d.pop("reference", UNSET))


        def _parse_human_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        human_score = _parse_human_score(d.pop("human_score", UNSET))


        def _parse_grader_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        grader_score = _parse_grader_score(d.pop("grader_score", UNSET))


        feedback = d.pop("feedback", UNSET)

        agent_job_evaluation_item_request = cls(
            job_id=job_id,
            reference=reference,
            human_score=human_score,
            grader_score=grader_score,
            feedback=feedback,
        )


        agent_job_evaluation_item_request.additional_properties = d
        return agent_job_evaluation_item_request

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
