from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connection_authentication_check_status_enum import ConnectionAuthenticationCheckStatusEnum






T = TypeVar("T", bound="ConnectionAuthenticationCheck")



@_attrs_define
class ConnectionAuthenticationCheck:
    """ 
        Attributes:
            status (ConnectionAuthenticationCheckStatusEnum): * `passed` - passed
                * `failed` - failed
                * `not_configured` - not_configured
                * `unsupported` - unsupported
            message (str):
     """

    status: ConnectionAuthenticationCheckStatusEnum
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ConnectionAuthenticationCheckStatusEnum(d.pop("status"))




        message = d.pop("message")

        connection_authentication_check = cls(
            status=status,
            message=message,
        )


        connection_authentication_check.additional_properties = d
        return connection_authentication_check

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
