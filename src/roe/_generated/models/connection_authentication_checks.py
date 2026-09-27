from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.connection_authentication_check import ConnectionAuthenticationCheck





T = TypeVar("T", bound="ConnectionAuthenticationChecks")



@_attrs_define
class ConnectionAuthenticationChecks:
    """ 
        Attributes:
            api (ConnectionAuthenticationCheck):
            dashboard (ConnectionAuthenticationCheck):
     """

    api: ConnectionAuthenticationCheck
    dashboard: ConnectionAuthenticationCheck
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_authentication_check import ConnectionAuthenticationCheck
        api = self.api.to_dict()

        dashboard = self.dashboard.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "api": api,
            "dashboard": dashboard,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_authentication_check import ConnectionAuthenticationCheck
        d = dict(src_dict)
        api = ConnectionAuthenticationCheck.from_dict(d.pop("api"))




        dashboard = ConnectionAuthenticationCheck.from_dict(d.pop("dashboard"))




        connection_authentication_checks = cls(
            api=api,
            dashboard=dashboard,
        )


        connection_authentication_checks.additional_properties = d
        return connection_authentication_checks

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
