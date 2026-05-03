from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.agent_datum import AgentDatum





T = TypeVar("T", bound="AgentJobResultResponse")



@_attrs_define
class AgentJobResultResponse:
    """ 
        Attributes:
            agent_id (UUID): The ID of the base agent
            agent_version_id (UUID): The ID of the agent version
            inputs (list[Any]): The input data provided to the agent
            input_tokens (int | None): Number of input tokens used
            output_tokens (int | None): Number of output tokens generated
            outputs (list[AgentDatum]): The output data from the agent
     """

    agent_id: UUID
    agent_version_id: UUID
    inputs: list[Any]
    input_tokens: int | None
    output_tokens: int | None
    outputs: list[AgentDatum]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_datum import AgentDatum
        agent_id = str(self.agent_id)

        agent_version_id = str(self.agent_version_id)

        inputs = self.inputs



        input_tokens: int | None
        input_tokens = self.input_tokens

        output_tokens: int | None
        output_tokens = self.output_tokens

        outputs = []
        for outputs_item_data in self.outputs:
            outputs_item = outputs_item_data.to_dict()
            outputs.append(outputs_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "agent_id": agent_id,
            "agent_version_id": agent_version_id,
            "inputs": inputs,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "outputs": outputs,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_datum import AgentDatum
        d = dict(src_dict)
        agent_id = UUID(d.pop("agent_id"))




        agent_version_id = UUID(d.pop("agent_version_id"))




        inputs = cast(list[Any], d.pop("inputs"))


        def _parse_input_tokens(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        input_tokens = _parse_input_tokens(d.pop("input_tokens"))


        def _parse_output_tokens(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        output_tokens = _parse_output_tokens(d.pop("output_tokens"))


        outputs = []
        _outputs = d.pop("outputs")
        for outputs_item_data in (_outputs):
            outputs_item = AgentDatum.from_dict(outputs_item_data)



            outputs.append(outputs_item)


        agent_job_result_response = cls(
            agent_id=agent_id,
            agent_version_id=agent_version_id,
            inputs=inputs,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            outputs=outputs,
        )


        agent_job_result_response.additional_properties = d
        return agent_job_result_response

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
