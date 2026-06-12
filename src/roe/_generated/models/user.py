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






T = TypeVar("T", bound="User")



@_attrs_define
class User:
    """ 
        Attributes:
            id (int):
            email (str):
            first_name (str):
            last_name (str):
            display_name (str):
            date_joined (datetime.datetime):
            is_staff (bool | Unset):  Default: False.
            is_superuser (bool | Unset):  Default: False.
            is_active (bool | Unset):  Default: True.
            is_first_login (bool | Unset):  Default: True.
            is_email_verified (bool | Unset):  Default: False.
            is_mfa_enabled (bool | Unset):  Default: True.
     """

    id: int
    email: str
    first_name: str
    last_name: str
    display_name: str
    date_joined: datetime.datetime
    is_staff: bool | Unset = False
    is_superuser: bool | Unset = False
    is_active: bool | Unset = True
    is_first_login: bool | Unset = True
    is_email_verified: bool | Unset = False
    is_mfa_enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        email = self.email

        first_name = self.first_name

        last_name = self.last_name

        display_name = self.display_name

        date_joined = self.date_joined.isoformat()

        is_staff = self.is_staff

        is_superuser = self.is_superuser

        is_active = self.is_active

        is_first_login = self.is_first_login

        is_email_verified = self.is_email_verified

        is_mfa_enabled = self.is_mfa_enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "display_name": display_name,
            "date_joined": date_joined,
        })
        if is_staff is not UNSET:
            field_dict["is_staff"] = is_staff
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_first_login is not UNSET:
            field_dict["is_first_login"] = is_first_login
        if is_email_verified is not UNSET:
            field_dict["is_email_verified"] = is_email_verified
        if is_mfa_enabled is not UNSET:
            field_dict["is_mfa_enabled"] = is_mfa_enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        email = d.pop("email")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        display_name = d.pop("display_name")

        date_joined = isoparse(d.pop("date_joined"))




        is_staff = d.pop("is_staff", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_first_login = d.pop("is_first_login", UNSET)

        is_email_verified = d.pop("is_email_verified", UNSET)

        is_mfa_enabled = d.pop("is_mfa_enabled", UNSET)

        user = cls(
            id=id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            display_name=display_name,
            date_joined=date_joined,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            is_first_login=is_first_login,
            is_email_verified=is_email_verified,
            is_mfa_enabled=is_mfa_enabled,
        )


        user.additional_properties = d
        return user

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
