from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AgentImportExportVersion")



@_attrs_define
class AgentImportExportVersion:
    """ Serializer for agent version data shared by import and export

        Attributes:
            input_definitions (Any): Input definitions for this version
            engine_config (Any): Engine configuration for this version
            version_name (str | Unset): Version name (optional, will auto-generate if not provided)
            description (str | Unset): Version description Default: ''.
            is_current (bool | Unset): Whether this should be the current version Default: False.
     """

    input_definitions: Any
    engine_config: Any
    version_name: str | Unset = UNSET
    description: str | Unset = ''
    is_current: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        input_definitions = self.input_definitions

        engine_config = self.engine_config

        version_name = self.version_name

        description = self.description

        is_current = self.is_current


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
        if is_current is not UNSET:
            field_dict["is_current"] = is_current

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        input_definitions = d.pop("input_definitions")

        engine_config = d.pop("engine_config")

        version_name = d.pop("version_name", UNSET)

        description = d.pop("description", UNSET)

        is_current = d.pop("is_current", UNSET)

        agent_import_export_version = cls(
            input_definitions=input_definitions,
            engine_config=engine_config,
            version_name=version_name,
            description=description,
            is_current=is_current,
        )


        agent_import_export_version.additional_properties = d
        return agent_import_export_version

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
