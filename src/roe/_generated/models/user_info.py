from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UserInfo")



@_attrs_define
class UserInfo:
    """ 
        Attributes:
            id (int):
            email (str):
            display_name (str):
            first_name (str | Unset):
            last_name (str | Unset):
     """

    id: int
    email: str
    display_name: str
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        display_name = self.display_name

        first_name = self.first_name

        last_name = self.last_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "email": email,
            "display_name": display_name,
        })
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        display_name = d.pop("display_name")

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        user_info = cls(
            id=id,
            email=email,
            display_name=display_name,
            first_name=first_name,
            last_name=last_name,
        )


        user_info.additional_properties = d
        return user_info

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
