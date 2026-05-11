from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.agent_execution_request_request import AgentExecutionRequestRequest





T = TypeVar("T", bound="AgentRunAsyncManyRequestRequest")



@_attrs_define
class AgentRunAsyncManyRequestRequest:
    """ Serializer for agent async many execution requests.

        Attributes:
            inputs (list[AgentExecutionRequestRequest]): List of agent execution requests to process
     """

    inputs: list[AgentExecutionRequestRequest]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_execution_request_request import AgentExecutionRequestRequest
        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "inputs": inputs,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_execution_request_request import AgentExecutionRequestRequest
        d = dict(src_dict)
        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in (_inputs):
            inputs_item = AgentExecutionRequestRequest.from_dict(inputs_item_data)



            inputs.append(inputs_item)


        agent_run_async_many_request_request = cls(
            inputs=inputs,
        )


        agent_run_async_many_request_request.additional_properties = d
        return agent_run_async_many_request_request

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
