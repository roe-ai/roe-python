from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="JobInput")



@_attrs_define
class JobInput:
    """ Serializer for individual job input data

        Attributes:
            key (str): The input key
            description (str): Description of the input
            data_type (str): The data type of the input
            value (str): The input value
            file_name (str | Unset): File name if this input is a file
     """

    key: str
    description: str
    data_type: str
    value: str
    file_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        description = self.description

        data_type = self.data_type

        value = self.value

        file_name = self.file_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "description": description,
            "data_type": data_type,
            "value": value,
        })
        if file_name is not UNSET:
            field_dict["file_name"] = file_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        description = d.pop("description")

        data_type = d.pop("data_type")

        value = d.pop("value")

        file_name = d.pop("file_name", UNSET)

        job_input = cls(
            key=key,
            description=description,
            data_type=data_type,
            value=value,
            file_name=file_name,
        )


        job_input.additional_properties = d
        return job_input

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
