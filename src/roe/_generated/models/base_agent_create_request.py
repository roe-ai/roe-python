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






T = TypeVar("T", bound="BaseAgentCreateRequest")



@_attrs_define
class BaseAgentCreateRequest:
    """ Serializer for creating base agents with proper JSON field handling

        Attributes:
            name (str): Name of the base agent.
            engine_class_id (str): Engine class ID for the agent.
            organization_id (UUID): Organization ID where the agent belongs.
            input_definitions (Any): Input definitions for the first version.
            engine_config (Any): Engine configuration for the first version.
            version_name (str | Unset): Name of the first version.
            description (str | Unset): Description of the first version.
     """

    name: str
    engine_class_id: str
    organization_id: UUID
    input_definitions: Any
    engine_config: Any
    version_name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        engine_class_id = self.engine_class_id

        organization_id = str(self.organization_id)

        input_definitions = self.input_definitions

        engine_config = self.engine_config

        version_name = self.version_name

        description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "engine_class_id": engine_class_id,
            "organization_id": organization_id,
            "input_definitions": input_definitions,
            "engine_config": engine_config,
        })
        if version_name is not UNSET:
            field_dict["version_name"] = version_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))



        files.append(("engine_class_id", (None, str(self.engine_class_id).encode(), "text/plain")))



        files.append(("organization_id", (None, str(self.organization_id), "text/plain")))



        files.append(("input_definitions", (None, str(self.input_definitions).encode(), "text/plain")))



        files.append(("engine_config", (None, str(self.engine_config).encode(), "text/plain")))



        if not isinstance(self.version_name, Unset):
            files.append(("version_name", (None, str(self.version_name).encode(), "text/plain")))



        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        engine_class_id = d.pop("engine_class_id")

        organization_id = UUID(d.pop("organization_id"))




        input_definitions = d.pop("input_definitions")

        engine_config = d.pop("engine_config")

        version_name = d.pop("version_name", UNSET)

        description = d.pop("description", UNSET)

        base_agent_create_request = cls(
            name=name,
            engine_class_id=engine_class_id,
            organization_id=organization_id,
            input_definitions=input_definitions,
            engine_config=engine_config,
            version_name=version_name,
            description=description,
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
