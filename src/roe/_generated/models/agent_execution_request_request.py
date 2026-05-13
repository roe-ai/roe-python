from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AgentExecutionRequestRequest")



@_attrs_define
class AgentExecutionRequestRequest:
    """ Serializer for agent execution requests with dynamic input fields.

        Attributes:
            metadata (Any | Unset): Optional metadata as JSON object or JSON string
            agent_input_key_example (str | Unset): Agent input keys are dynamic based on agent configuration. Can be text or
                file.
     """

    metadata: Any | Unset = UNSET
    agent_input_key_example: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        metadata = self.metadata

        agent_input_key_example = self.agent_input_key_example


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if agent_input_key_example is not UNSET:
            field_dict["agent_input_key_example"] = agent_input_key_example

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.metadata, Unset):
            files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))



        if not isinstance(self.agent_input_key_example, Unset):
            files.append(("agent_input_key_example", (None, str(self.agent_input_key_example).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        metadata = d.pop("metadata", UNSET)

        agent_input_key_example = d.pop("agent_input_key_example", UNSET)

        agent_execution_request_request = cls(
            metadata=metadata,
            agent_input_key_example=agent_input_key_example,
        )


        agent_execution_request_request.additional_properties = d
        return agent_execution_request_request

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
