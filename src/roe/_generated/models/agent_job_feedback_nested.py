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
import datetime






T = TypeVar("T", bound="AgentJobFeedbackNested")



@_attrs_define
class AgentJobFeedbackNested:
    """ 
        Attributes:
            reviewed_by (None | str):
            review_status (ReviewStatusEnum | Unset): * `pending` - Pending Review
                * `approved` - Approved
                * `rejected` - Rejected
            corrected_verdict (None | str | Unset): Human-selected correct verdict when they disagree with agent
            review_comment (str | Unset): Reviewer's comment explaining their decision
            reviewed_at (datetime.datetime | None | Unset): Timestamp when the review was completed
     """

    reviewed_by: None | str
    review_status: ReviewStatusEnum | Unset = UNSET
    corrected_verdict: None | str | Unset = UNSET
    review_comment: str | Unset = UNSET
    reviewed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        reviewed_by: None | str
        reviewed_by = self.reviewed_by

        review_status: str | Unset = UNSET
        if not isinstance(self.review_status, Unset):
            review_status = self.review_status.value


        corrected_verdict: None | str | Unset
        if isinstance(self.corrected_verdict, Unset):
            corrected_verdict = UNSET
        else:
            corrected_verdict = self.corrected_verdict

        review_comment = self.review_comment

        reviewed_at: None | str | Unset
        if isinstance(self.reviewed_at, Unset):
            reviewed_at = UNSET
        elif isinstance(self.reviewed_at, datetime.datetime):
            reviewed_at = self.reviewed_at.isoformat()
        else:
            reviewed_at = self.reviewed_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "reviewed_by": reviewed_by,
        })
        if review_status is not UNSET:
            field_dict["review_status"] = review_status
        if corrected_verdict is not UNSET:
            field_dict["corrected_verdict"] = corrected_verdict
        if review_comment is not UNSET:
            field_dict["review_comment"] = review_comment
        if reviewed_at is not UNSET:
            field_dict["reviewed_at"] = reviewed_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_reviewed_by(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reviewed_by = _parse_reviewed_by(d.pop("reviewed_by"))


        _review_status = d.pop("review_status", UNSET)
        review_status: ReviewStatusEnum | Unset
        if isinstance(_review_status,  Unset):
            review_status = UNSET
        else:
            review_status = ReviewStatusEnum(_review_status)




        def _parse_corrected_verdict(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        corrected_verdict = _parse_corrected_verdict(d.pop("corrected_verdict", UNSET))


        review_comment = d.pop("review_comment", UNSET)

        def _parse_reviewed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reviewed_at_type_0 = isoparse(data)



                return reviewed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reviewed_at = _parse_reviewed_at(d.pop("reviewed_at", UNSET))


        agent_job_feedback_nested = cls(
            reviewed_by=reviewed_by,
            review_status=review_status,
            corrected_verdict=corrected_verdict,
            review_comment=review_comment,
            reviewed_at=reviewed_at,
        )


        agent_job_feedback_nested.additional_properties = d
        return agent_job_feedback_nested

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
