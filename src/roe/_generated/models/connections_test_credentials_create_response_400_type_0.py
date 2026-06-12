from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="ConnectionsTestCredentialsCreateResponse400Type0")



@_attrs_define
class ConnectionsTestCredentialsCreateResponse400Type0:
    """ Credential validation or connection test failed (TestConnection result with success=false).

        Attributes:
            success (bool):
            message (str):
            tested_at (datetime.datetime):
     """

    success: bool
    message: str
    tested_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        tested_at = self.tested_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
            "message": message,
            "tested_at": tested_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        tested_at = isoparse(d.pop("tested_at"))




        connections_test_credentials_create_response_400_type_0 = cls(
            success=success,
            message=message,
            tested_at=tested_at,
        )


        connections_test_credentials_create_response_400_type_0.additional_properties = d
        return connections_test_credentials_create_response_400_type_0

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
