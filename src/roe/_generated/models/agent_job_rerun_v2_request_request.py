from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="AgentJobRerunV2RequestRequest")



@_attrs_define
class AgentJobRerunV2RequestRequest:
    """ 
        Attributes:
            agent_version_id (None | Unset | UUID): Agent version to re-run against. Defaults to the base agent's current
                version.
     """

    agent_version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        agent_version_id: None | str | Unset
        if isinstance(self.agent_version_id, Unset):
            agent_version_id = UNSET
        elif isinstance(self.agent_version_id, UUID):
            agent_version_id = str(self.agent_version_id)
        else:
            agent_version_id = self.agent_version_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if agent_version_id is not UNSET:
            field_dict["agent_version_id"] = agent_version_id

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.agent_version_id, Unset):
            if isinstance(self.agent_version_id, UUID):

                files.append(("agent_version_id", (None, str(self.agent_version_id), "text/plain")))
            else:
                files.append(("agent_version_id", (None, str(self.agent_version_id).encode(), "text/plain")))



        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_agent_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_version_id_type_0 = UUID(data)



                return agent_version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        agent_version_id = _parse_agent_version_id(d.pop("agent_version_id", UNSET))


        agent_job_rerun_v2_request_request = cls(
            agent_version_id=agent_version_id,
        )


        agent_job_rerun_v2_request_request.additional_properties = d
        return agent_job_rerun_v2_request_request

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
