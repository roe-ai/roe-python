from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.organization_slim_request import OrganizationSlimRequest
  from ..models.user_info_request import UserInfoRequest





T = TypeVar("T", bound="PatchedWorksheetRequest")



@_attrs_define
class PatchedWorksheetRequest:
    """ 
        Attributes:
            name (str | Unset):
            creator (UserInfoRequest | Unset):
            organization (OrganizationSlimRequest | Unset): Simple organization serializer for nested use.
     """

    name: str | Unset = UNSET
    creator: UserInfoRequest | Unset = UNSET
    organization: OrganizationSlimRequest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_slim_request import OrganizationSlimRequest
        from ..models.user_info_request import UserInfoRequest
        name = self.name

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if creator is not UNSET:
            field_dict["creator"] = creator
        if organization is not UNSET:
            field_dict["organization"] = organization

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        from ..models.organization_slim_request import OrganizationSlimRequest
        from ..models.user_info_request import UserInfoRequest
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))



        if not isinstance(self.creator, Unset):
            files.append(("creator", (None, json.dumps( self.creator.to_dict()).encode(), "application/json")))



        if not isinstance(self.organization, Unset):
            files.append(("organization", (None, json.dumps( self.organization.to_dict()).encode(), "application/json")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_slim_request import OrganizationSlimRequest
        from ..models.user_info_request import UserInfoRequest
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _creator = d.pop("creator", UNSET)
        creator: UserInfoRequest | Unset
        if isinstance(_creator,  Unset):
            creator = UNSET
        else:
            creator = UserInfoRequest.from_dict(_creator)




        _organization = d.pop("organization", UNSET)
        organization: OrganizationSlimRequest | Unset
        if isinstance(_organization,  Unset):
            organization = UNSET
        else:
            organization = OrganizationSlimRequest.from_dict(_organization)




        patched_worksheet_request = cls(
            name=name,
            creator=creator,
            organization=organization,
        )


        patched_worksheet_request.additional_properties = d
        return patched_worksheet_request

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
