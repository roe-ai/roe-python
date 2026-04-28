from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AgentJobStatus")



@_attrs_define
class AgentJobStatus:
    """ 
        Attributes:
            status (int): Status code. 0: PENDING, 1: STARTED, 2: RETRY, 3: SUCCESS, 4: FAILURE, 5: CANCELLED, 6: CACHED
            timestamp (int): Unix timestamp in seconds
            error_message (str | Unset): Error message if status is RETRY or FAILURE
     """

    status: int
    timestamp: int
    error_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status = self.status

        timestamp = self.timestamp

        error_message = self.error_message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "timestamp": timestamp,
        })
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        timestamp = d.pop("timestamp")

        error_message = d.pop("error_message", UNSET)

        agent_job_status = cls(
            status=status,
            timestamp=timestamp,
            error_message=error_message,
        )


        agent_job_status.additional_properties = d
        return agent_job_status

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
