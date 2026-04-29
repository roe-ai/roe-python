from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.user_info import UserInfo





T = TypeVar("T", bound="DatasetInfo")



@_attrs_define
class DatasetInfo:
    """ 
        Attributes:
            id (UUID):
            name (str):
            creator (None | UserInfo):
            created_at (datetime.datetime):
            organization (UUID):
     """

    id: UUID
    name: str
    creator: None | UserInfo
    created_at: datetime.datetime
    organization: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_info import UserInfo
        id = str(self.id)

        name = self.name

        creator: dict[str, Any] | None
        if isinstance(self.creator, UserInfo):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        created_at = self.created_at.isoformat()

        organization = str(self.organization)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "creator": creator,
            "created_at": created_at,
            "organization": organization,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_info import UserInfo
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        name = d.pop("name")

        def _parse_creator(data: object) -> None | UserInfo:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                creator_type_0 = UserInfo.from_dict(data)



                return creator_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserInfo, data)

        creator = _parse_creator(d.pop("creator"))


        created_at = isoparse(d.pop("created_at"))




        organization = UUID(d.pop("organization"))




        dataset_info = cls(
            id=id,
            name=name,
            creator=creator,
            created_at=created_at,
            organization=organization,
        )


        dataset_info.additional_properties = d
        return dataset_info

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
