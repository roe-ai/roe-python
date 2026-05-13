from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="BaseAgentUpdateRequest")



@_attrs_define
class BaseAgentUpdateRequest:
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


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))



        if not isinstance(self.disable_cache, Unset):
            files.append(("disable_cache", (None, str(self.disable_cache).encode(), "text/plain")))



        if not isinstance(self.cache_failed_jobs, Unset):
            files.append(("cache_failed_jobs", (None, str(self.cache_failed_jobs).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        disable_cache = d.pop("disable_cache", UNSET)

        cache_failed_jobs = d.pop("cache_failed_jobs", UNSET)

        base_agent_update_request = cls(
            name=name,
            disable_cache=disable_cache,
            cache_failed_jobs=cache_failed_jobs,
        )


        base_agent_update_request.additional_properties = d
        return base_agent_update_request

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
