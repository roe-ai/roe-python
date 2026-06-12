from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="DependentAgentInfo")



@_attrs_define
class DependentAgentInfo:
    """ An agent version that references a policy (see get_agents_using_policy).

        Attributes:
            base_agent_id (UUID):
            agent_name (str):
            version_id (UUID):
            version_name (str):
     """

    base_agent_id: UUID
    agent_name: str
    version_id: UUID
    version_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        base_agent_id = str(self.base_agent_id)

        agent_name = self.agent_name

        version_id = str(self.version_id)

        version_name = self.version_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "base_agent_id": base_agent_id,
            "agent_name": agent_name,
            "version_id": version_id,
            "version_name": version_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        base_agent_id = UUID(d.pop("base_agent_id"))




        agent_name = d.pop("agent_name")

        version_id = UUID(d.pop("version_id"))




        version_name = d.pop("version_name")

        dependent_agent_info = cls(
            base_agent_id=base_agent_id,
            agent_name=agent_name,
            version_id=version_id,
            version_name=version_name,
        )


        dependent_agent_info.additional_properties = d
        return dependent_agent_info

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
