from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="V1AgentsWebhooksTestCreateResponse200")



@_attrs_define
class V1AgentsWebhooksTestCreateResponse200:
    """ 
        Attributes:
            success (bool):
            status_code (int | Unset):
            message (str | Unset):
     """

    success: bool
    status_code: int | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status_code = self.status_code

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
        })
        if status_code is not UNSET:
            field_dict["status_code"] = status_code
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        status_code = d.pop("status_code", UNSET)

        message = d.pop("message", UNSET)

        v1_agents_webhooks_test_create_response_200 = cls(
            success=success,
            status_code=status_code,
            message=message,
        )


        v1_agents_webhooks_test_create_response_200.additional_properties = d
        return v1_agents_webhooks_test_create_response_200

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
