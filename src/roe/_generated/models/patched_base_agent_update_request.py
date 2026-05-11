from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PatchedBaseAgentUpdateRequest")



@_attrs_define
class PatchedBaseAgentUpdateRequest:
    """ Serializer for updating BaseAgent

        Attributes:
            name (str | Unset): New name for the agent. Must not be empty if provided.
            disable_cache (bool | Unset): Whether to disable job cache fetching for this agent.
            cache_failed_jobs (bool | Unset): Whether to cache failed jobs for this agent.
     """

    name: str | Unset = UNSET
    disable_cache: bool | Unset = UNSET
    cache_failed_jobs: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        disable_cache = self.disable_cache

        cache_failed_jobs = self.cache_failed_jobs


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if disable_cache is not UNSET:
            field_dict["disable_cache"] = disable_cache
        if cache_failed_jobs is not UNSET:
            field_dict["cache_failed_jobs"] = cache_failed_jobs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        disable_cache = d.pop("disable_cache", UNSET)

        cache_failed_jobs = d.pop("cache_failed_jobs", UNSET)

        patched_base_agent_update_request = cls(
            name=name,
            disable_cache=disable_cache,
            cache_failed_jobs=cache_failed_jobs,
        )


        patched_base_agent_update_request.additional_properties = d
        return patched_base_agent_update_request

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
