from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.organization_slim import OrganizationSlim
  from ..models.user_info import UserInfo





T = TypeVar("T", bound="Worksheet")



@_attrs_define
class Worksheet:
    """ 
        Attributes:
            id (UUID):
            name (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            creator (None | Unset | UserInfo):
            organization (OrganizationSlim | Unset): Simple organization serializer for nested use.
     """

    id: UUID
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    creator: None | Unset | UserInfo = UNSET
    organization: OrganizationSlim | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_slim import OrganizationSlim
        from ..models.user_info import UserInfo
        id = str(self.id)

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        creator: dict[str, Any] | None | Unset
        if isinstance(self.creator, Unset):
            creator = UNSET
        elif isinstance(self.creator, UserInfo):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if creator is not UNSET:
            field_dict["creator"] = creator
        if organization is not UNSET:
            field_dict["organization"] = organization

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_slim import OrganizationSlim
        from ..models.user_info import UserInfo
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        def _parse_creator(data: object) -> None | Unset | UserInfo:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                creator_type_0 = UserInfo.from_dict(data)



                return creator_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserInfo, data)

        creator = _parse_creator(d.pop("creator", UNSET))


        _organization = d.pop("organization", UNSET)
        organization: OrganizationSlim | Unset
        if isinstance(_organization,  Unset):
            organization = UNSET
        else:
            organization = OrganizationSlim.from_dict(_organization)




        worksheet = cls(
            id=id,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            creator=creator,
            organization=organization,
        )


        worksheet.additional_properties = d
        return worksheet

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
