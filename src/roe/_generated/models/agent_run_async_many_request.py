from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_execution_request import AgentExecutionRequest





T = TypeVar("T", bound="AgentRunAsyncManyRequest")



@_attrs_define
class AgentRunAsyncManyRequest:
    """ Serializer for agent async many execution requests.

        Attributes:
            inputs (list[AgentExecutionRequest]): List of agent execution requests to process
            max_concurrent_jobs (int | Unset): Optional cap on how many of these jobs run at once. The rest wait as pending
                and start as running jobs finish. Unset = no cap beyond the organization's concurrent job limit. An input that
                matches a job already in progress reuses that job, which keeps the cap it was started with.
     """

    inputs: list[AgentExecutionRequest]
    max_concurrent_jobs: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_execution_request import AgentExecutionRequest
        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)



        max_concurrent_jobs = self.max_concurrent_jobs


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "inputs": inputs,
        })
        if max_concurrent_jobs is not UNSET:
            field_dict["max_concurrent_jobs"] = max_concurrent_jobs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_execution_request import AgentExecutionRequest
        d = dict(src_dict)
        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in (_inputs):
            inputs_item = AgentExecutionRequest.from_dict(inputs_item_data)



            inputs.append(inputs_item)


        max_concurrent_jobs = d.pop("max_concurrent_jobs", UNSET)

        agent_run_async_many_request = cls(
            inputs=inputs,
            max_concurrent_jobs=max_concurrent_jobs,
        )


        agent_run_async_many_request.additional_properties = d
        return agent_run_async_many_request

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
