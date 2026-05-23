from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="TableUploadResponse")



@_attrs_define
class TableUploadResponse:
    """ Response payload for a public CSV table upload.

        Attributes:
            table_name (str): Created Roe table name
            organization_id (UUID): Organization that owns the table
            summary (Any | Unset): ClickHouse import summary for the uploaded file
     """

    table_name: str
    organization_id: UUID
    summary: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        table_name = self.table_name

        organization_id = str(self.organization_id)

        summary = self.summary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "table_name": table_name,
            "organization_id": organization_id,
        })
        if summary is not UNSET:
            field_dict["summary"] = summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        table_name = d.pop("table_name")

        organization_id = UUID(d.pop("organization_id"))




        summary = d.pop("summary", UNSET)

        table_upload_response = cls(
            table_name=table_name,
            organization_id=organization_id,
            summary=summary,
        )


        table_upload_response.additional_properties = d
        return table_upload_response

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
