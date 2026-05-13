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






T = TypeVar("T", bound="CreatePolicyVersionRequest")



@_attrs_define
class CreatePolicyVersionRequest:
    """ Serializer for creating a new policy version

        Attributes:
            content (Any):
            version_name (str | Unset): Version name (auto-generated if not provided)
            base_version_id (UUID | Unset): ID of the version this was derived from
     """

    content: Any
    version_name: str | Unset = UNSET
    base_version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        content = self.content

        version_name = self.version_name

        base_version_id: str | Unset = UNSET
        if not isinstance(self.base_version_id, Unset):
            base_version_id = str(self.base_version_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "content": content,
        })
        if version_name is not UNSET:
            field_dict["version_name"] = version_name
        if base_version_id is not UNSET:
            field_dict["base_version_id"] = base_version_id

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("content", (None, str(self.content).encode(), "text/plain")))



        if not isinstance(self.version_name, Unset):
            files.append(("version_name", (None, str(self.version_name).encode(), "text/plain")))



        if not isinstance(self.base_version_id, Unset):
            files.append(("base_version_id", (None, str(self.base_version_id), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content")

        version_name = d.pop("version_name", UNSET)

        _base_version_id = d.pop("base_version_id", UNSET)
        base_version_id: UUID | Unset
        if isinstance(_base_version_id,  Unset):
            base_version_id = UNSET
        else:
            base_version_id = UUID(_base_version_id)




        create_policy_version_request = cls(
            content=content,
            version_name=version_name,
            base_version_id=base_version_id,
        )


        create_policy_version_request.additional_properties = d
        return create_policy_version_request

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
