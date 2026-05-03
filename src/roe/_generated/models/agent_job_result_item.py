from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.agent_datum import AgentDatum





T = TypeVar("T", bound="AgentJobResultItem")



@_attrs_define
class AgentJobResultItem:
    """ Serializer for individual agent job result item.

        Attributes:
            id (str): Agent job ID
            status (int | None): Job status code (0=PENDING, 1=STARTED, 2=RETRY, 3=SUCCESS, 4=FAILURE, 5=CANCELLED,
                6=CACHED)
            result (list[AgentDatum] | None): List of job outputs, or error code if job failed
            agent_id (None | UUID): Base agent ID
            agent_version_id (None | UUID): Agent version ID
            cost (float | None): Cost of the agent job execution
            inputs (list[Any] | None): The input data provided to the agent (full version from blob if available, truncated
                from DB otherwise)
            input_tokens (int | None): Number of input tokens used
            output_tokens (int | None): Number of output tokens generated
            corrected_outputs (list[AgentDatum] | None | Unset): List of corrected outputs if any corrections were made
     """

    id: str
    status: int | None
    result: list[AgentDatum] | None
    agent_id: None | UUID
    agent_version_id: None | UUID
    cost: float | None
    inputs: list[Any] | None
    input_tokens: int | None
    output_tokens: int | None
    corrected_outputs: list[AgentDatum] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_datum import AgentDatum
        id = self.id

        status: int | None
        status = self.status

        result: list[dict[str, Any]] | None
        if isinstance(self.result, list):
            result = []
            for result_type_0_item_data in self.result:
                result_type_0_item = result_type_0_item_data.to_dict()
                result.append(result_type_0_item)


        else:
            result = self.result

        agent_id: None | str
        if isinstance(self.agent_id, UUID):
            agent_id = str(self.agent_id)
        else:
            agent_id = self.agent_id

        agent_version_id: None | str
        if isinstance(self.agent_version_id, UUID):
            agent_version_id = str(self.agent_version_id)
        else:
            agent_version_id = self.agent_version_id

        cost: float | None
        cost = self.cost

        inputs: list[Any] | None
        if isinstance(self.inputs, list):
            inputs = self.inputs


        else:
            inputs = self.inputs

        input_tokens: int | None
        input_tokens = self.input_tokens

        output_tokens: int | None
        output_tokens = self.output_tokens

        corrected_outputs: list[dict[str, Any]] | None | Unset
        if isinstance(self.corrected_outputs, Unset):
            corrected_outputs = UNSET
        elif isinstance(self.corrected_outputs, list):
            corrected_outputs = []
            for corrected_outputs_type_0_item_data in self.corrected_outputs:
                corrected_outputs_type_0_item = corrected_outputs_type_0_item_data.to_dict()
                corrected_outputs.append(corrected_outputs_type_0_item)


        else:
            corrected_outputs = self.corrected_outputs


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "status": status,
            "result": result,
            "agent_id": agent_id,
            "agent_version_id": agent_version_id,
            "cost": cost,
            "inputs": inputs,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
        })
        if corrected_outputs is not UNSET:
            field_dict["corrected_outputs"] = corrected_outputs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_datum import AgentDatum
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_status(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        status = _parse_status(d.pop("status"))


        def _parse_result(data: object) -> list[AgentDatum] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                result_type_0 = []
                _result_type_0 = data
                for result_type_0_item_data in (_result_type_0):
                    result_type_0_item = AgentDatum.from_dict(result_type_0_item_data)



                    result_type_0.append(result_type_0_item)

                return result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AgentDatum] | None, data)

        result = _parse_result(d.pop("result"))


        def _parse_agent_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_id_type_0 = UUID(data)



                return agent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        agent_id = _parse_agent_id(d.pop("agent_id"))


        def _parse_agent_version_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_version_id_type_0 = UUID(data)



                return agent_version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        agent_version_id = _parse_agent_version_id(d.pop("agent_version_id"))


        def _parse_cost(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        cost = _parse_cost(d.pop("cost"))


        def _parse_inputs(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                inputs_type_0 = cast(list[Any], data)

                return inputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        inputs = _parse_inputs(d.pop("inputs"))


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


        def _parse_corrected_outputs(data: object) -> list[AgentDatum] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                corrected_outputs_type_0 = []
                _corrected_outputs_type_0 = data
                for corrected_outputs_type_0_item_data in (_corrected_outputs_type_0):
                    corrected_outputs_type_0_item = AgentDatum.from_dict(corrected_outputs_type_0_item_data)



                    corrected_outputs_type_0.append(corrected_outputs_type_0_item)

                return corrected_outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AgentDatum] | None | Unset, data)

        corrected_outputs = _parse_corrected_outputs(d.pop("corrected_outputs", UNSET))


        agent_job_result_item = cls(
            id=id,
            status=status,
            result=result,
            agent_id=agent_id,
            agent_version_id=agent_version_id,
            cost=cost,
            inputs=inputs,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            corrected_outputs=corrected_outputs,
        )


        agent_job_result_item.additional_properties = d
        return agent_job_result_item

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
