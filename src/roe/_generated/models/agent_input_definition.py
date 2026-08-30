from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AgentInputDefinition")



@_attrs_define
class AgentInputDefinition:
    """ 
        Attributes:
            key (str): The unique identifier for this input definition
            data_type (str): MIME type of the input, from the closed DataType set. Use 'text/plain' for ordinary strings
                such as URLs, names and free text; other values include 'application/pdf', 'application/json', 'image/png',
                'audio/mpeg', 'video/mp4' and the wildcards 'text/*', 'image/*', 'audio/*', 'video/*', '*/*'.
            description (str): Description of what this input is for
            example (str | Unset): An example value for this input
            accepts_multiple_files (bool | Unset): Whether this input accepts multiple files
     """

    key: str
    data_type: str
    description: str
    example: str | Unset = UNSET
    accepts_multiple_files: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        data_type = self.data_type

        description = self.description

        example = self.example

        accepts_multiple_files = self.accepts_multiple_files


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "data_type": data_type,
            "description": description,
        })
        if example is not UNSET:
            field_dict["example"] = example
        if accepts_multiple_files is not UNSET:
            field_dict["accepts_multiple_files"] = accepts_multiple_files

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        data_type = d.pop("data_type")

        description = d.pop("description")

        example = d.pop("example", UNSET)

        accepts_multiple_files = d.pop("accepts_multiple_files", UNSET)

        agent_input_definition = cls(
            key=key,
            data_type=data_type,
            description=description,
            example=example,
            accepts_multiple_files=accepts_multiple_files,
        )


        agent_input_definition.additional_properties = d
        return agent_input_definition

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
