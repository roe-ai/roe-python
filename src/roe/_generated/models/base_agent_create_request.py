from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="BaseAgentCreateRequest")



@_attrs_define
class BaseAgentCreateRequest:
    """ Serializer for creating base agents with proper JSON field handling

        Attributes:
            name (str): Name of the base agent.
            engine_class_id (str): Engine class ID for the agent.
            organization_id (UUID | Unset): Optional. Ignored by the API — the organization is derived from the
                authenticated API key/token. Accepted for backwards compatibility.
            version_name (str | Unset): Name of the first version.
            description (str | Unset): Description of the first version.
            input_definitions (Any | Unset): Input definitions for the first version.
            engine_config (Any | Unset): Engine configuration for the first version.
     """

    name: str
    engine_class_id: str
    organization_id: UUID | Unset = UNSET
    version_name: str | Unset = UNSET
    description: str | Unset = UNSET
    input_definitions: Any | Unset = UNSET
    engine_config: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        engine_class_id = self.engine_class_id

        organization_id: str | Unset = UNSET
        if not isinstance(self.organization_id, Unset):
            organization_id = str(self.organization_id)

        version_name = self.version_name

        description = self.description

        input_definitions = self.input_definitions

        engine_config = self.engine_config


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "engine_class_id": engine_class_id,
        })
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if version_name is not UNSET:
            field_dict["version_name"] = version_name
        if description is not UNSET:
            field_dict["description"] = description
        if input_definitions is not UNSET:
            field_dict["input_definitions"] = input_definitions
        if engine_config is not UNSET:
            field_dict["engine_config"] = engine_config

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        engine_class_id = d.pop("engine_class_id")

        _organization_id = d.pop("organization_id", UNSET)
        organization_id: UUID | Unset
        if isinstance(_organization_id,  Unset):
            organization_id = UNSET
        else:
            organization_id = UUID(_organization_id)




        version_name = d.pop("version_name", UNSET)

        description = d.pop("description", UNSET)

        input_definitions = d.pop("input_definitions", UNSET)

        engine_config = d.pop("engine_config", UNSET)

        base_agent_create_request = cls(
            name=name,
            engine_class_id=engine_class_id,
            organization_id=organization_id,
            version_name=version_name,
            description=description,
            input_definitions=input_definitions,
            engine_config=engine_config,
        )


        base_agent_create_request.additional_properties = d
        return base_agent_create_request

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
