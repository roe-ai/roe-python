from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.review_status_enum import ReviewStatusEnum
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="AgentJobFeedbackResponse")



@_attrs_define
class AgentJobFeedbackResponse:
    """ Serializer for agent job feedback response.

        Attributes:
            job_id (UUID):
            review_status (ReviewStatusEnum): * `pending` - Pending Review
                * `approved` - Approved
                * `rejected` - Rejected
            review_comment (str):
            reviewed_at (datetime.datetime | None):
            reviewed_by (None | str):
            corrected_verdict (None | str | Unset):
     """

    job_id: UUID
    review_status: ReviewStatusEnum
    review_comment: str
    reviewed_at: datetime.datetime | None
    reviewed_by: None | str
    corrected_verdict: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        job_id = str(self.job_id)

        review_status = self.review_status.value

        review_comment = self.review_comment

        reviewed_at: None | str
        if isinstance(self.reviewed_at, datetime.datetime):
            reviewed_at = self.reviewed_at.isoformat()
        else:
            reviewed_at = self.reviewed_at

        reviewed_by: None | str
        reviewed_by = self.reviewed_by

        corrected_verdict: None | str | Unset
        if isinstance(self.corrected_verdict, Unset):
            corrected_verdict = UNSET
        else:
            corrected_verdict = self.corrected_verdict


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "job_id": job_id,
            "review_status": review_status,
            "review_comment": review_comment,
            "reviewed_at": reviewed_at,
            "reviewed_by": reviewed_by,
        })
        if corrected_verdict is not UNSET:
            field_dict["corrected_verdict"] = corrected_verdict

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_id = UUID(d.pop("job_id"))




        review_status = ReviewStatusEnum(d.pop("review_status"))




        review_comment = d.pop("review_comment")

        def _parse_reviewed_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_at_type_0 = isoparse(data)



                return reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewed_at"))


        def _parse_reviewed_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reviewed_by = _parse_reviewed_by(d.pop("reviewed_by"))


        def _parse_corrected_verdict(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        corrected_verdict = _parse_corrected_verdict(d.pop("corrected_verdict", UNSET))


        agent_job_feedback_response = cls(
            job_id=job_id,
            review_status=review_status,
            review_comment=review_comment,
            reviewed_at=reviewed_at,
            reviewed_by=reviewed_by,
            corrected_verdict=corrected_verdict,
        )


        agent_job_feedback_response.additional_properties = d
        return agent_job_feedback_response

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
