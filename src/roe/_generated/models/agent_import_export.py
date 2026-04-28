from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_import_export_version import AgentImportExportVersion





T = TypeVar("T", bound="AgentImportExport")



@_attrs_define
class AgentImportExport:
    """ Serializer for agent data shared by import and export

        Attributes:
            name (str): Agent name
            engine_class_id (str): Engine class ID
            versions (list[AgentImportExportVersion]): List of agent versions (at least one required)
            disable_cache (bool | Unset): Whether to disable cache for this agent Default: False.
            cache_failed_jobs (bool | Unset): Whether to cache failed jobs Default: False.
     """

    name: str
    engine_class_id: str
    versions: list[AgentImportExportVersion]
    disable_cache: bool | Unset = False
    cache_failed_jobs: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_import_export_version import AgentImportExportVersion
        name = self.name

        engine_class_id = self.engine_class_id

        versions = []
        for versions_item_data in self.versions:
            versions_item = versions_item_data.to_dict()
            versions.append(versions_item)



        disable_cache = self.disable_cache

        cache_failed_jobs = self.cache_failed_jobs


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "engine_class_id": engine_class_id,
            "versions": versions,
        })
        if disable_cache is not UNSET:
            field_dict["disable_cache"] = disable_cache
        if cache_failed_jobs is not UNSET:
            field_dict["cache_failed_jobs"] = cache_failed_jobs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_import_export_version import AgentImportExportVersion
        d = dict(src_dict)
        name = d.pop("name")

        engine_class_id = d.pop("engine_class_id")

        versions = []
        _versions = d.pop("versions")
        for versions_item_data in (_versions):
            versions_item = AgentImportExportVersion.from_dict(versions_item_data)



            versions.append(versions_item)


        disable_cache = d.pop("disable_cache", UNSET)

        cache_failed_jobs = d.pop("cache_failed_jobs", UNSET)

        agent_import_export = cls(
            name=name,
            engine_class_id=engine_class_id,
            versions=versions,
            disable_cache=disable_cache,
            cache_failed_jobs=cache_failed_jobs,
        )


        agent_import_export.additional_properties = d
        return agent_import_export

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
