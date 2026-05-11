from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AgentVersionCreateRequest")



@_attrs_define
class AgentVersionCreateRequest:
    """ Serializer for creating new agent versions

        Attributes:
            input_definitions (Any): List of input definitions for this agent version.
            engine_config (Any): Engine configuration as a dictionary of string key-value pairs.
            version_name (str | Unset): Version name for the agent version. Defaults to 'unnamed version' if not provided.
            description (None | str | Unset): Description for the agent version.
     """

    input_definitions: Any
    engine_config: Any
    version_name: str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        input_definitions = self.input_definitions

        engine_config = self.engine_config

        version_name = self.version_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "input_definitions": input_definitions,
            "engine_config": engine_config,
        })
        if version_name is not UNSET:
            field_dict["version_name"] = version_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_definitions = d.pop("input_definitions")

        engine_config = d.pop("engine_config")

        version_name = d.pop("version_name", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        agent_version_create_request = cls(
            input_definitions=input_definitions,
            engine_config=engine_config,
            version_name=version_name,
            description=description,
        )


        agent_version_create_request.additional_properties = d
        return agent_version_create_request

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
