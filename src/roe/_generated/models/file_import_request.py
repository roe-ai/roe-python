from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="FileImportRequest")



@_attrs_define
class FileImportRequest:
    """ Serializer for file import (CSV or Parquet).

        Attributes:
            table_name (str):
            file (File):
            with_headers (bool | Unset):  Default: True.
            organization_id (None | Unset | UUID): Organization ID
     """

    table_name: str
    file: File
    with_headers: bool | Unset = True
    organization_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        table_name = self.table_name

        file = self.file.to_tuple()


        with_headers = self.with_headers

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "table_name": table_name,
            "file": file,
        })
        if with_headers is not UNSET:
            field_dict["with_headers"] = with_headers
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("table_name", (None, str(self.table_name).encode(), "text/plain")))



        files.append(("file", self.file.to_tuple()))



        if not isinstance(self.with_headers, Unset):
            files.append(("with_headers", (None, str(self.with_headers).encode(), "text/plain")))



        if not isinstance(self.organization_id, Unset):
            if isinstance(self.organization_id, UUID):

                files.append(("organization_id", (None, str(self.organization_id), "text/plain")))
            else:
                files.append(("organization_id", (None, str(self.organization_id).encode(), "text/plain")))



        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        table_name = d.pop("table_name")

        file = File(
             payload = BytesIO(d.pop("file"))
        )




        with_headers = d.pop("with_headers", UNSET)

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)



                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))


        file_import_request = cls(
            table_name=table_name,
            file=file,
            with_headers=with_headers,
            organization_id=organization_id,
        )


        file_import_request.additional_properties = d
        return file_import_request

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
