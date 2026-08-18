from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ResendAgentJobWebhookRequest")



@_attrs_define
class ResendAgentJobWebhookRequest:
    """ Serializer for re-sending a job's completion webhook.

        Attributes:
            webhook_id (None | Unset | UUID): Send to only this webhook. Omit to send to every active webhook on the agent.
     """

    webhook_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        webhook_id: None | str | Unset
        if isinstance(self.webhook_id, Unset):
            webhook_id = UNSET
        elif isinstance(self.webhook_id, UUID):
            webhook_id = str(self.webhook_id)
        else:
            webhook_id = self.webhook_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if webhook_id is not UNSET:
            field_dict["webhook_id"] = webhook_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_webhook_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                webhook_id_type_0 = UUID(data)



                return webhook_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        webhook_id = _parse_webhook_id(d.pop("webhook_id", UNSET))


        resend_agent_job_webhook_request = cls(
            webhook_id=webhook_id,
        )


        resend_agent_job_webhook_request.additional_properties = d
        return resend_agent_job_webhook_request

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
