from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.public_agent_job_status_event_error_details import PublicAgentJobStatusEventErrorDetails





T = TypeVar("T", bound="PublicAgentJobStatusEvent")



@_attrs_define
class PublicAgentJobStatusEvent:
    """ Customer-facing view of a status event.

    Same stored shape, but error text and error_details are passed through the
    read-time sanitizer so raw technical detail never reaches a customer. Use this
    on any endpoint a customer can reach; use the parent for staff-only surfaces
    (e.g. diagnostic runs) and for writes.

        Attributes:
            timestamp (datetime.datetime):
            status_code (int):
            error_message (str | Unset):
            error_details (PublicAgentJobStatusEventErrorDetails | Unset): Error details as key-value pairs
            count (int | Unset):
     """

    timestamp: datetime.datetime
    status_code: int
    error_message: str | Unset = UNSET
    error_details: PublicAgentJobStatusEventErrorDetails | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.public_agent_job_status_event_error_details import PublicAgentJobStatusEventErrorDetails
        timestamp = self.timestamp.isoformat()

        status_code = self.status_code

        error_message = self.error_message

        error_details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_details, Unset):
            error_details = self.error_details.to_dict()

        count = self.count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "timestamp": timestamp,
            "status_code": status_code,
        })
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if error_details is not UNSET:
            field_dict["error_details"] = error_details
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.public_agent_job_status_event_error_details import PublicAgentJobStatusEventErrorDetails
        d = dict(src_dict)
        timestamp = isoparse(d.pop("timestamp"))




        status_code = d.pop("status_code")

        error_message = d.pop("error_message", UNSET)

        _error_details = d.pop("error_details", UNSET)
        error_details: PublicAgentJobStatusEventErrorDetails | Unset
        if isinstance(_error_details,  Unset):
            error_details = UNSET
        else:
            error_details = PublicAgentJobStatusEventErrorDetails.from_dict(_error_details)




        count = d.pop("count", UNSET)

        public_agent_job_status_event = cls(
            timestamp=timestamp,
            status_code=status_code,
            error_message=error_message,
            error_details=error_details,
            count=count,
        )


        public_agent_job_status_event.additional_properties = d
        return public_agent_job_status_event

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
