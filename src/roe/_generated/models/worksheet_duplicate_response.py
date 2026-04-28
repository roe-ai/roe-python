from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.worksheet import Worksheet
  from ..models.worksheet_version import WorksheetVersion





T = TypeVar("T", bound="WorksheetDuplicateResponse")



@_attrs_define
class WorksheetDuplicateResponse:
    """ Response serializer for worksheet duplication.

        Attributes:
            worksheet (Worksheet):
            version (WorksheetVersion):
     """

    worksheet: Worksheet
    version: WorksheetVersion
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.worksheet import Worksheet
        from ..models.worksheet_version import WorksheetVersion
        worksheet = self.worksheet.to_dict()

        version = self.version.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "worksheet": worksheet,
            "version": version,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.worksheet import Worksheet
        from ..models.worksheet_version import WorksheetVersion
        d = dict(src_dict)
        worksheet = Worksheet.from_dict(d.pop("worksheet"))




        version = WorksheetVersion.from_dict(d.pop("version"))




        worksheet_duplicate_response = cls(
            worksheet=worksheet,
            version=version,
        )


        worksheet_duplicate_response.additional_properties = d
        return worksheet_duplicate_response

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
