from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="DatabaseQueryRequestRequest")



@_attrs_define
class DatabaseQueryRequestRequest:
    """ 
        Attributes:
            query (str): SQL query to execute
            worksheet_id (UUID | Unset): Optional worksheet ID
            use_admin (bool | Unset): Use admin privileges Default: False.
            organization_id (UUID | Unset): Organization ID
     """

    query: str
    worksheet_id: UUID | Unset = UNSET
    use_admin: bool | Unset = False
    organization_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        query = self.query

        worksheet_id: str | Unset = UNSET
        if not isinstance(self.worksheet_id, Unset):
            worksheet_id = str(self.worksheet_id)

        use_admin = self.use_admin

        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "query": query,
        })
        if worksheet_id is not UNSET:
            field_dict["worksheet_id"] = worksheet_id
        if use_admin is not UNSET:
            field_dict["use_admin"] = use_admin
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("query", (None, str(self.query).encode(), "text/plain")))



        if not isinstance(self.worksheet_id, Unset):
            files.append(("worksheet_id", (None, str(self.worksheet_id), "text/plain")))



        if not isinstance(self.use_admin, Unset):
            files.append(("use_admin", (None, str(self.use_admin).encode(), "text/plain")))



        if not isinstance(self.organization_id, Unset):
            files.append(("organization_id", (None, str(self.organization_id), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        _worksheet_id = d.pop("worksheet_id", UNSET)
        worksheet_id: UUID | Unset
        if isinstance(_worksheet_id,  Unset):
            worksheet_id = UNSET
        else:
            worksheet_id = UUID(_worksheet_id)




        use_admin = d.pop("use_admin", UNSET)

        _organization_id = d.pop("organization_id", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id,  Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)




        database_query_request_request = cls(
            query=query,
            worksheet_id=worksheet_id,
            use_admin=use_admin,
            organization_id=organization_id,
        )


        database_query_request_request.additional_properties = d
        return database_query_request_request

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
