from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AgentJobWebhookResendResponse")



@_attrs_define
class AgentJobWebhookResendResponse:
    """ 
        Attributes:
            status (str):
            queued (int): How many deliveries were queued. 0 means the agent has no active webhook subscription, which is
                the usual reason a callback never arrives.
     """

    status: str
    queued: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status = self.status

        queued = self.queued


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "queued": queued,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        queued = d.pop("queued")

        agent_job_webhook_resend_response = cls(
            status=status,
            queued=queued,
        )


        agent_job_webhook_resend_response.additional_properties = d
        return agent_job_webhook_resend_response

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
