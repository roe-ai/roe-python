from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.gate_kind import GateKind
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.agent_step import AgentStep
  from ..models.connection_step import ConnectionStep
  from ..models.edit_fields_step import EditFieldsStep
  from ..models.for_each_block import ForEachBlock
  from ..models.if_block import IfBlock
  from ..models.merge_step import MergeStep
  from ..models.parallel_block import ParallelBlock





T = TypeVar("T", bound="ApprovalBlock")



@_attrs_define
class ApprovalBlock:
    """ Steps that run once someone approves the agent step just before.

        Attributes:
            id (str):
            kind (Literal['approval']):  Default: 'approval'.
            steps (list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep |
                ParallelBlock]):
            approval (GateKind | Unset): What opens a gate: an org admin's explicit approval (manual) or the
                reviewer's verdict decision on the source agent's result (feedback).
     """

    id: str
    steps: list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep | ParallelBlock]
    kind: Literal['approval'] = 'approval'
    approval: GateKind | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_step import AgentStep
        from ..models.connection_step import ConnectionStep
        from ..models.edit_fields_step import EditFieldsStep
        from ..models.for_each_block import ForEachBlock
        from ..models.if_block import IfBlock
        from ..models.merge_step import MergeStep
        from ..models.parallel_block import ParallelBlock
        id = self.id

        kind = self.kind

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



        approval: str | Unset = UNSET
        if not isinstance(self.approval, Unset):
            approval = self.approval.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "kind": kind,
            "steps": steps,
        })
        if approval is not UNSET:
            field_dict["approval"] = approval

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_step import AgentStep
        from ..models.connection_step import ConnectionStep
        from ..models.edit_fields_step import EditFieldsStep
        from ..models.for_each_block import ForEachBlock
        from ..models.if_block import IfBlock
        from ..models.merge_step import MergeStep
        from ..models.parallel_block import ParallelBlock
        d = dict(src_dict)
        id = d.pop("id")

        kind = cast(Literal['approval'] , d.pop("kind"))
        if kind != 'approval':
            raise ValueError(f"kind must match const 'approval', got '{kind}'")

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


        _approval = d.pop("approval", UNSET)
        approval: GateKind | Unset
        if isinstance(_approval,  Unset):
            approval = UNSET
        else:
            approval = GateKind(_approval)




        approval_block = cls(
            id=id,
            kind=kind,
            steps=steps,
            approval=approval,
        )

        return approval_block

