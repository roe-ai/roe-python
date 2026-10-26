from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.combine_enum import CombineEnum
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.agent_step import AgentStep
  from ..models.approval_block import ApprovalBlock
  from ..models.condition import Condition
  from ..models.connection_step import ConnectionStep
  from ..models.edit_fields_step import EditFieldsStep
  from ..models.for_each_block import ForEachBlock
  from ..models.merge_step import MergeStep
  from ..models.parallel_block import ParallelBlock





T = TypeVar("T", bound="IfBlock")



@_attrs_define
class IfBlock:
    """ 
        Attributes:
            id (str):
            kind (Literal['if']):  Default: 'if'.
            conditions (list[Condition]):
            combine (CombineEnum | Unset):  Default: CombineEnum.ALL.
            then (list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep |
                ParallelBlock] | Unset):
            otherwise (list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep
                | ParallelBlock] | Unset):
     """

    id: str
    conditions: list[Condition]
    kind: Literal['if'] = 'if'
    combine: CombineEnum | Unset = CombineEnum.ALL
    then: list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep | ParallelBlock] | Unset = UNSET
    otherwise: list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep | ParallelBlock] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_step import AgentStep
        from ..models.approval_block import ApprovalBlock
        from ..models.condition import Condition
        from ..models.connection_step import ConnectionStep
        from ..models.edit_fields_step import EditFieldsStep
        from ..models.for_each_block import ForEachBlock
        from ..models.merge_step import MergeStep
        from ..models.parallel_block import ParallelBlock
        id = self.id

        kind = self.kind

        conditions = []
        for conditions_item_data in self.conditions:
            conditions_item = conditions_item_data.to_dict()
            conditions.append(conditions_item)



        combine: str | Unset = UNSET
        if not isinstance(self.combine, Unset):
            combine = self.combine.value


        then: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.then, Unset):
            then = []
            for then_item_data in self.then:
                then_item: dict[str, Any]
                if isinstance(then_item_data, AgentStep):
                    then_item = then_item_data.to_dict()
                elif isinstance(then_item_data, ConnectionStep):
                    then_item = then_item_data.to_dict()
                elif isinstance(then_item_data, EditFieldsStep):
                    then_item = then_item_data.to_dict()
                elif isinstance(then_item_data, MergeStep):
                    then_item = then_item_data.to_dict()
                elif isinstance(then_item_data, IfBlock):
                    then_item = then_item_data.to_dict()
                elif isinstance(then_item_data, ForEachBlock):
                    then_item = then_item_data.to_dict()
                elif isinstance(then_item_data, ApprovalBlock):
                    then_item = then_item_data.to_dict()
                else:
                    then_item = then_item_data.to_dict()

                then.append(then_item)



        otherwise: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.otherwise, Unset):
            otherwise = []
            for otherwise_item_data in self.otherwise:
                otherwise_item: dict[str, Any]
                if isinstance(otherwise_item_data, AgentStep):
                    otherwise_item = otherwise_item_data.to_dict()
                elif isinstance(otherwise_item_data, ConnectionStep):
                    otherwise_item = otherwise_item_data.to_dict()
                elif isinstance(otherwise_item_data, EditFieldsStep):
                    otherwise_item = otherwise_item_data.to_dict()
                elif isinstance(otherwise_item_data, MergeStep):
                    otherwise_item = otherwise_item_data.to_dict()
                elif isinstance(otherwise_item_data, IfBlock):
                    otherwise_item = otherwise_item_data.to_dict()
                elif isinstance(otherwise_item_data, ForEachBlock):
                    otherwise_item = otherwise_item_data.to_dict()
                elif isinstance(otherwise_item_data, ApprovalBlock):
                    otherwise_item = otherwise_item_data.to_dict()
                else:
                    otherwise_item = otherwise_item_data.to_dict()

                otherwise.append(otherwise_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "kind": kind,
            "conditions": conditions,
        })
        if combine is not UNSET:
            field_dict["combine"] = combine
        if then is not UNSET:
            field_dict["then"] = then
        if otherwise is not UNSET:
            field_dict["otherwise"] = otherwise

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_step import AgentStep
        from ..models.approval_block import ApprovalBlock
        from ..models.condition import Condition
        from ..models.connection_step import ConnectionStep
        from ..models.edit_fields_step import EditFieldsStep
        from ..models.for_each_block import ForEachBlock
        from ..models.merge_step import MergeStep
        from ..models.parallel_block import ParallelBlock
        d = dict(src_dict)
        id = d.pop("id")

        kind = cast(Literal['if'] , d.pop("kind"))
        if kind != 'if':
            raise ValueError(f"kind must match const 'if', got '{kind}'")

        conditions = []
        _conditions = d.pop("conditions")
        for conditions_item_data in (_conditions):
            conditions_item = Condition.from_dict(conditions_item_data)



            conditions.append(conditions_item)


        _combine = d.pop("combine", UNSET)
        combine: CombineEnum | Unset
        if isinstance(_combine,  Unset):
            combine = UNSET
        else:
            combine = CombineEnum(_combine)




        _then = d.pop("then", UNSET)
        then: list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep | ParallelBlock] | Unset = UNSET
        if _then is not UNSET:
            then = []
            for then_item_data in _then:
                def _parse_then_item(data: object) -> AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep | ParallelBlock:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        then_item_type_0 = AgentStep.from_dict(data)



                        return then_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        then_item_type_1 = ConnectionStep.from_dict(data)



                        return then_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        then_item_type_2 = EditFieldsStep.from_dict(data)



                        return then_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        then_item_type_3 = MergeStep.from_dict(data)



                        return then_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        then_item_type_4 = IfBlock.from_dict(data)



                        return then_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        then_item_type_5 = ForEachBlock.from_dict(data)



                        return then_item_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        then_item_type_6 = ApprovalBlock.from_dict(data)



                        return then_item_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    then_item_type_7 = ParallelBlock.from_dict(data)



                    return then_item_type_7

                then_item = _parse_then_item(then_item_data)

                then.append(then_item)


        _otherwise = d.pop("otherwise", UNSET)
        otherwise: list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep | ParallelBlock] | Unset = UNSET
        if _otherwise is not UNSET:
            otherwise = []
            for otherwise_item_data in _otherwise:
                def _parse_otherwise_item(data: object) -> AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep | ParallelBlock:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        otherwise_item_type_0 = AgentStep.from_dict(data)



                        return otherwise_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        otherwise_item_type_1 = ConnectionStep.from_dict(data)



                        return otherwise_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        otherwise_item_type_2 = EditFieldsStep.from_dict(data)



                        return otherwise_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        otherwise_item_type_3 = MergeStep.from_dict(data)



                        return otherwise_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        otherwise_item_type_4 = IfBlock.from_dict(data)



                        return otherwise_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        otherwise_item_type_5 = ForEachBlock.from_dict(data)



                        return otherwise_item_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        otherwise_item_type_6 = ApprovalBlock.from_dict(data)



                        return otherwise_item_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    otherwise_item_type_7 = ParallelBlock.from_dict(data)



                    return otherwise_item_type_7

                otherwise_item = _parse_otherwise_item(otherwise_item_data)

                otherwise.append(otherwise_item)


        if_block = cls(
            id=id,
            kind=kind,
            conditions=conditions,
            combine=combine,
            then=then,
            otherwise=otherwise,
        )

        return if_block

