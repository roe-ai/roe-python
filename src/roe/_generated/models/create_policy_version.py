from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="CreatePolicyVersion")



@_attrs_define
class CreatePolicyVersion:
    """ Serializer for creating a new policy version

        Attributes:
            id (UUID):
            content (Any):
            version_name (str | Unset): Version name (auto-generated if not provided)
     """

    id: UUID
    content: Any
    version_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        content = self.content

        version_name = self.version_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "content": content,
        })
        if version_name is not UNSET:
            field_dict["version_name"] = version_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        content = d.pop("content")

        version_name = d.pop("version_name", UNSET)

        create_policy_version = cls(
            id=id,
            content=content,
            version_name=version_name,
        )


        create_policy_version.additional_properties = d
        return create_policy_version

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
