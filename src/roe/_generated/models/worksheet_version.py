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
  from ..models.user_info import UserInfo
  from ..models.worksheet_slim import WorksheetSlim





T = TypeVar("T", bound="WorksheetVersion")



@_attrs_define
class WorksheetVersion:
    """ 
        Attributes:
            id (UUID):
            created_at (datetime.datetime):
            worksheet (WorksheetSlim | Unset): Simple worksheet serializer for nested use.
            creator (UserInfo | Unset):
            content (str | Unset):
     """

    id: UUID
    created_at: datetime.datetime
    worksheet: WorksheetSlim | Unset = UNSET
    creator: UserInfo | Unset = UNSET
    content: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_info import UserInfo
        from ..models.worksheet_slim import WorksheetSlim
        id = str(self.id)

        created_at = self.created_at.isoformat()

        worksheet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.worksheet, Unset):
            worksheet = self.worksheet.to_dict()

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        content = self.content


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "created_at": created_at,
        })
        if worksheet is not UNSET:
            field_dict["worksheet"] = worksheet
        if creator is not UNSET:
            field_dict["creator"] = creator
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_info import UserInfo
        from ..models.worksheet_slim import WorksheetSlim
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        created_at = isoparse(d.pop("created_at"))




        _worksheet = d.pop("worksheet", UNSET)
        worksheet: WorksheetSlim | Unset
        if isinstance(_worksheet,  Unset):
            worksheet = UNSET
        else:
            worksheet = WorksheetSlim.from_dict(_worksheet)




        _creator = d.pop("creator", UNSET)
        creator: UserInfo | Unset
        if isinstance(_creator,  Unset):
            creator = UNSET
        else:
            creator = UserInfo.from_dict(_creator)




        content = d.pop("content", UNSET)

        worksheet_version = cls(
            id=id,
            created_at=created_at,
            worksheet=worksheet,
            creator=creator,
            content=content,
        )


        worksheet_version.additional_properties = d
        return worksheet_version

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
