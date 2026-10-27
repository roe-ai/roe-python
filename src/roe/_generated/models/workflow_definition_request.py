from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.agent_step import AgentStep
  from ..models.approval_block import ApprovalBlock
  from ..models.connection_step import ConnectionStep
  from ..models.edit_fields_step import EditFieldsStep
  from ..models.for_each_block import ForEachBlock
  from ..models.if_block import IfBlock
  from ..models.input_field import InputField
  from ..models.merge_step import MergeStep
  from ..models.parallel_block import ParallelBlock





T = TypeVar("T", bound="WorkflowDefinitionRequest")



@_attrs_define
class WorkflowDefinitionRequest:
    """ 
        Attributes:
            steps (list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep |
                ParallelBlock]):
            result (str):
            format_version (Literal[2] | Unset):  Default: 2.
            inputs (list[InputField] | Unset):
     """

    steps: list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep | ParallelBlock]
    result: str
    format_version: Literal[2] | Unset = 2
    inputs: list[InputField] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_step import AgentStep
        from ..models.approval_block import ApprovalBlock
        from ..models.connection_step import ConnectionStep
        from ..models.edit_fields_step import EditFieldsStep
        from ..models.for_each_block import ForEachBlock
        from ..models.if_block import IfBlock
        from ..models.input_field import InputField
        from ..models.merge_step import MergeStep
        from ..models.parallel_block import ParallelBlock
        steps = []
        for steps_item_data in self.steps:
            steps_item: dict[str, Any]
            if isinstance(steps_item_data, AgentStep):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, ConnectionStep):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, EditFieldsStep):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, MergeStep):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, IfBlock):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, ForEachBlock):
                steps_item = steps_item_data.to_dict()
            elif isinstance(steps_item_data, ApprovalBlock):
                steps_item = steps_item_data.to_dict()
            else:
                steps_item = steps_item_data.to_dict()

            steps.append(steps_item)



        result = self.result

        format_version = self.format_version

        inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = []
            for inputs_item_data in self.inputs:
                inputs_item = inputs_item_data.to_dict()
                inputs.append(inputs_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "steps": steps,
            "result": result,
        })
        if format_version is not UNSET:
            field_dict["format_version"] = format_version
        if inputs is not UNSET:
            field_dict["inputs"] = inputs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_step import AgentStep
        from ..models.approval_block import ApprovalBlock
        from ..models.connection_step import ConnectionStep
        from ..models.edit_fields_step import EditFieldsStep
        from ..models.for_each_block import ForEachBlock
        from ..models.if_block import IfBlock
        from ..models.input_field import InputField
        from ..models.merge_step import MergeStep
        from ..models.parallel_block import ParallelBlock
        d = dict(src_dict)
        steps = []
        _steps = d.pop("steps")
        for steps_item_data in (_steps):
            def _parse_steps_item(data: object) -> AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep | ParallelBlock:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_0 = AgentStep.from_dict(data)



                    return steps_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_1 = ConnectionStep.from_dict(data)



                    return steps_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_2 = EditFieldsStep.from_dict(data)



                    return steps_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_3 = MergeStep.from_dict(data)



                    return steps_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_4 = IfBlock.from_dict(data)



                    return steps_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_5 = ForEachBlock.from_dict(data)



                    return steps_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    steps_item_type_6 = ApprovalBlock.from_dict(data)



                    return steps_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                steps_item_type_7 = ParallelBlock.from_dict(data)



                return steps_item_type_7

            steps_item = _parse_steps_item(steps_item_data)

            steps.append(steps_item)


        result = d.pop("result")

        format_version = cast(Literal[2] | Unset , d.pop("format_version", UNSET))
        if format_version != 2and not isinstance(format_version, Unset):
            raise ValueError(f"format_version must match const 2, got '{format_version}'")

        _inputs = d.pop("inputs", UNSET)
        inputs: list[InputField] | Unset = UNSET
        if _inputs is not UNSET:
            inputs = []
            for inputs_item_data in _inputs:
                inputs_item = InputField.from_dict(inputs_item_data)



                inputs.append(inputs_item)


        workflow_definition_request = cls(
            steps=steps,
            result=result,
            format_version=format_version,
            inputs=inputs,
        )

        return workflow_definition_request

