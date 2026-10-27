from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="InputField")



@_attrs_define
class InputField:
    """ One input a step needs or a workflow declares.

        Attributes:
            key (str):
            data_type (str | Unset):  Default: 'text/plain'.
            description (str | Unset):  Default: ''.
            required (bool | Unset):  Default: True.
            accepts_multiple_files (bool | Unset):  Default: False.
     """

    key: str
    data_type: str | Unset = 'text/plain'
    description: str | Unset = ''
    required: bool | Unset = True
    accepts_multiple_files: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        data_type = self.data_type

        description = self.description

        required = self.required

        accepts_multiple_files = self.accepts_multiple_files


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
        })
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if description is not UNSET:
            field_dict["description"] = description
        if required is not UNSET:
            field_dict["required"] = required
        if accepts_multiple_files is not UNSET:
            field_dict["accepts_multiple_files"] = accepts_multiple_files

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        data_type = d.pop("data_type", UNSET)

        description = d.pop("description", UNSET)

        required = d.pop("required", UNSET)

        accepts_multiple_files = d.pop("accepts_multiple_files", UNSET)

        input_field = cls(
            key=key,
            data_type=data_type,
            description=description,
            required=required,
            accepts_multiple_files=accepts_multiple_files,
        )


        input_field.additional_properties = d
        return input_field

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
