from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
  from ..models.merge_step import MergeStep





T = TypeVar("T", bound="ParallelBlock")



@_attrs_define
class ParallelBlock:
    """ 
        Attributes:
            id (str):
            kind (Literal['parallel']):  Default: 'parallel'.
            lanes (list[list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock |
                MergeStep | ParallelBlock]]):
     """

    id: str
    lanes: list[list[AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep | ParallelBlock]]
    kind: Literal['parallel'] = 'parallel'





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_step import AgentStep
        from ..models.approval_block import ApprovalBlock
        from ..models.connection_step import ConnectionStep
        from ..models.edit_fields_step import EditFieldsStep
        from ..models.for_each_block import ForEachBlock
        from ..models.if_block import IfBlock
        from ..models.merge_step import MergeStep
        id = self.id

        kind = self.kind

        lanes = []
        for lanes_item_data in self.lanes:
            lanes_item = []
            for lanes_item_item_data in lanes_item_data:
                lanes_item_item: dict[str, Any]
                if isinstance(lanes_item_item_data, AgentStep):
                    lanes_item_item = lanes_item_item_data.to_dict()
                elif isinstance(lanes_item_item_data, ConnectionStep):
                    lanes_item_item = lanes_item_item_data.to_dict()
                elif isinstance(lanes_item_item_data, EditFieldsStep):
                    lanes_item_item = lanes_item_item_data.to_dict()
                elif isinstance(lanes_item_item_data, MergeStep):
                    lanes_item_item = lanes_item_item_data.to_dict()
                elif isinstance(lanes_item_item_data, IfBlock):
                    lanes_item_item = lanes_item_item_data.to_dict()
                elif isinstance(lanes_item_item_data, ForEachBlock):
                    lanes_item_item = lanes_item_item_data.to_dict()
                elif isinstance(lanes_item_item_data, ApprovalBlock):
                    lanes_item_item = lanes_item_item_data.to_dict()
                else:
                    lanes_item_item = lanes_item_item_data.to_dict()

                lanes_item.append(lanes_item_item)


            lanes.append(lanes_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "kind": kind,
            "lanes": lanes,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_step import AgentStep
        from ..models.approval_block import ApprovalBlock
        from ..models.connection_step import ConnectionStep
        from ..models.edit_fields_step import EditFieldsStep
        from ..models.for_each_block import ForEachBlock
        from ..models.if_block import IfBlock
        from ..models.merge_step import MergeStep
        d = dict(src_dict)
        id = d.pop("id")

        kind = cast(Literal['parallel'] , d.pop("kind"))
        if kind != 'parallel':
            raise ValueError(f"kind must match const 'parallel', got '{kind}'")

        lanes = []
        _lanes = d.pop("lanes")
        for lanes_item_data in (_lanes):
            lanes_item = []
            _lanes_item = lanes_item_data
            for lanes_item_item_data in (_lanes_item):
                def _parse_lanes_item_item(data: object) -> AgentStep | ApprovalBlock | ConnectionStep | EditFieldsStep | ForEachBlock | IfBlock | MergeStep | ParallelBlock:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        lanes_item_item_type_0 = AgentStep.from_dict(data)



                        return lanes_item_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        lanes_item_item_type_1 = ConnectionStep.from_dict(data)



                        return lanes_item_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        lanes_item_item_type_2 = EditFieldsStep.from_dict(data)



                        return lanes_item_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        lanes_item_item_type_3 = MergeStep.from_dict(data)



                        return lanes_item_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        lanes_item_item_type_4 = IfBlock.from_dict(data)



                        return lanes_item_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        lanes_item_item_type_5 = ForEachBlock.from_dict(data)



                        return lanes_item_item_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        lanes_item_item_type_6 = ApprovalBlock.from_dict(data)



                        return lanes_item_item_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    lanes_item_item_type_7 = ParallelBlock.from_dict(data)



                    return lanes_item_item_type_7

                lanes_item_item = _parse_lanes_item_item(lanes_item_item_data)

                lanes_item.append(lanes_item_item)

            lanes.append(lanes_item)


        parallel_block = cls(
            id=id,
            kind=kind,
            lanes=lanes,
        )

        return parallel_block

