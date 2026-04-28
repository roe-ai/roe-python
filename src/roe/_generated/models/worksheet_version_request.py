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
  from ..models.user_info_request import UserInfoRequest
  from ..models.worksheet_slim_request import WorksheetSlimRequest





T = TypeVar("T", bound="WorksheetVersionRequest")



@_attrs_define
class WorksheetVersionRequest:
    """ 
        Attributes:
            worksheet (WorksheetSlimRequest | Unset): Simple worksheet serializer for nested use.
            creator (UserInfoRequest | Unset):
            content (str | Unset):
     """

    worksheet: WorksheetSlimRequest | Unset = UNSET
    creator: UserInfoRequest | Unset = UNSET
    content: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_info_request import UserInfoRequest
        from ..models.worksheet_slim_request import WorksheetSlimRequest
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
        })
        if worksheet is not UNSET:
            field_dict["worksheet"] = worksheet
        if creator is not UNSET:
            field_dict["creator"] = creator
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        from ..models.user_info_request import UserInfoRequest
        from ..models.worksheet_slim_request import WorksheetSlimRequest
        files: types.RequestFiles = []

        if not isinstance(self.worksheet, Unset):
            files.append(("worksheet", (None, json.dumps( self.worksheet.to_dict()).encode(), "application/json")))



        if not isinstance(self.creator, Unset):
            files.append(("creator", (None, json.dumps( self.creator.to_dict()).encode(), "application/json")))



        if not isinstance(self.content, Unset):
            files.append(("content", (None, str(self.content).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_info_request import UserInfoRequest
        from ..models.worksheet_slim_request import WorksheetSlimRequest
        d = dict(src_dict)
        _worksheet = d.pop("worksheet", UNSET)
        worksheet: WorksheetSlimRequest | Unset
        if isinstance(_worksheet,  Unset):
            worksheet = UNSET
        else:
            worksheet = WorksheetSlimRequest.from_dict(_worksheet)




        _creator = d.pop("creator", UNSET)
        creator: UserInfoRequest | Unset
        if isinstance(_creator,  Unset):
            creator = UNSET
        else:
            creator = UserInfoRequest.from_dict(_creator)




        content = d.pop("content", UNSET)

        worksheet_version_request = cls(
            worksheet=worksheet,
            creator=creator,
            content=content,
        )


        worksheet_version_request.additional_properties = d
        return worksheet_version_request

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
