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
  from ..models.agent_step_input_mapping import AgentStepInputMapping





T = TypeVar("T", bound="AgentStep")



@_attrs_define
class AgentStep:
    """ 
        Attributes:
            id (str):
            kind (Literal['agent']):  Default: 'agent'.
            base_agent_id (str):
            agent_version_id (str):
            input_mapping (AgentStepInputMapping | Unset):
     """

    id: str
    base_agent_id: str
    agent_version_id: str
    kind: Literal['agent'] = 'agent'
    input_mapping: AgentStepInputMapping | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_step_input_mapping import AgentStepInputMapping
        id = self.id

        kind = self.kind

        base_agent_id = self.base_agent_id

        agent_version_id = self.agent_version_id

        input_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_mapping, Unset):
            input_mapping = self.input_mapping.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "kind": kind,
            "base_agent_id": base_agent_id,
            "agent_version_id": agent_version_id,
        })
        if input_mapping is not UNSET:
            field_dict["input_mapping"] = input_mapping

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_step_input_mapping import AgentStepInputMapping
        d = dict(src_dict)
        id = d.pop("id")

        kind = cast(Literal['agent'] , d.pop("kind"))
        if kind != 'agent':
            raise ValueError(f"kind must match const 'agent', got '{kind}'")

        base_agent_id = d.pop("base_agent_id")

        agent_version_id = d.pop("agent_version_id")

        _input_mapping = d.pop("input_mapping", UNSET)
        input_mapping: AgentStepInputMapping | Unset
        if isinstance(_input_mapping,  Unset):
            input_mapping = UNSET
        else:
            input_mapping = AgentStepInputMapping.from_dict(_input_mapping)




        agent_step = cls(
            id=id,
            kind=kind,
            base_agent_id=base_agent_id,
            agent_version_id=agent_version_id,
            input_mapping=input_mapping,
        )

        return agent_step

