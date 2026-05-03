from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreatePolicyRequest")



@_attrs_define
class CreatePolicyRequest:
    """ Serializer for creating a new policy with initial version

        Attributes:
            name (str):
            content (Any): Content for the initial policy version
            description (str | Unset):
            version_name (str | Unset): Name for the initial version (defaults to 'version 1') Default: 'version 1'.
     """

    name: str
    content: Any
    description: str | Unset = UNSET
    version_name: str | Unset = 'version 1'
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        content = self.content

        description = self.description

        version_name = self.version_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "content": content,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if version_name is not UNSET:
            field_dict["version_name"] = version_name

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))



        files.append(("content", (None, str(self.content).encode(), "text/plain")))



        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))



        if not isinstance(self.version_name, Unset):
            files.append(("version_name", (None, str(self.version_name).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        content = d.pop("content")

        description = d.pop("description", UNSET)

        version_name = d.pop("version_name", UNSET)

        create_policy_request = cls(
            name=name,
            content=content,
            description=description,
            version_name=version_name,
        )


        create_policy_request.additional_properties = d
        return create_policy_request

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
