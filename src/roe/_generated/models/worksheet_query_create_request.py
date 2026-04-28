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
from uuid import UUID






T = TypeVar("T", bound="WorksheetQueryCreateRequest")



@_attrs_define
class WorksheetQueryCreateRequest:
    """ Serializer for creating worksheet queries.

        Attributes:
            query (str):
            worksheet_id (None | Unset | UUID): Worksheet ID to associate with the query
            use_admin (bool | Unset): Whether to use admin privileges Default: False.
     """

    query: str
    worksheet_id: None | Unset | UUID = UNSET
    use_admin: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        query = self.query

        worksheet_id: None | str | Unset
        if isinstance(self.worksheet_id, Unset):
            worksheet_id = UNSET
        elif isinstance(self.worksheet_id, UUID):
            worksheet_id = str(self.worksheet_id)
        else:
            worksheet_id = self.worksheet_id

        use_admin = self.use_admin


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "query": query,
        })
        if worksheet_id is not UNSET:
            field_dict["worksheet_id"] = worksheet_id
        if use_admin is not UNSET:
            field_dict["use_admin"] = use_admin

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("query", (None, str(self.query).encode(), "text/plain")))



        if not isinstance(self.worksheet_id, Unset):
            if isinstance(self.worksheet_id, UUID):

                files.append(("worksheet_id", (None, str(self.worksheet_id), "text/plain")))
            else:
                files.append(("worksheet_id", (None, str(self.worksheet_id).encode(), "text/plain")))


        if not isinstance(self.use_admin, Unset):
            files.append(("use_admin", (None, str(self.use_admin).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        def _parse_worksheet_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                worksheet_id_type_0 = UUID(data)



                return worksheet_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        worksheet_id = _parse_worksheet_id(d.pop("worksheet_id", UNSET))


        use_admin = d.pop("use_admin", UNSET)

        worksheet_query_create_request = cls(
            query=query,
            worksheet_id=worksheet_id,
            use_admin=use_admin,
        )


        worksheet_query_create_request.additional_properties = d
        return worksheet_query_create_request

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
