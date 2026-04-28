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






T = TypeVar("T", bound="WorksheetCreateRequest")



@_attrs_define
class WorksheetCreateRequest:
    """ Serializer for creating worksheets with initial content.

        Attributes:
            name (str):
            content (str | Unset): Initial content for the worksheet
            organization_id (None | Unset | UUID): Organization ID for the worksheet
     """

    name: str
    content: str | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        content = self.content

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
            "name": name,
        })
        if content is not UNSET:
            field_dict["content"] = content
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))



        if not isinstance(self.content, Unset):
            files.append(("content", (None, str(self.content).encode(), "text/plain")))



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
        name = d.pop("name")

        content = d.pop("content", UNSET)

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


        worksheet_create_request = cls(
            name=name,
            content=content,
            organization_id=organization_id,
        )


        worksheet_create_request.additional_properties = d
        return worksheet_create_request

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
