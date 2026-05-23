from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.agent_engine_type_list_engines_item import AgentEngineTypeListEnginesItem





T = TypeVar("T", bound="AgentEngineTypeList")



@_attrs_define
class AgentEngineTypeList:
    """ Serializer for public agent engine type discovery.

        Attributes:
            engine_types (list[str]): Valid agent engine_class_id values accepted by create-agent APIs
            total_count (int): Number of engine types returned
            engines (list[AgentEngineTypeListEnginesItem]): Production agent engine metadata, including descriptions, input
                schemas, and default engine_config values
     """

    engine_types: list[str]
    total_count: int
    engines: list[AgentEngineTypeListEnginesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_engine_type_list_engines_item import AgentEngineTypeListEnginesItem
        engine_types = self.engine_types



        total_count = self.total_count

        engines = []
        for engines_item_data in self.engines:
            engines_item = engines_item_data.to_dict()
            engines.append(engines_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "engine_types": engine_types,
            "total_count": total_count,
            "engines": engines,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_engine_type_list_engines_item import AgentEngineTypeListEnginesItem
        d = dict(src_dict)
        engine_types = cast(list[str], d.pop("engine_types"))


        total_count = d.pop("total_count")

        engines = []
        _engines = d.pop("engines")
        for engines_item_data in (_engines):
            engines_item = AgentEngineTypeListEnginesItem.from_dict(engines_item_data)



            engines.append(engines_item)


        agent_engine_type_list = cls(
            engine_types=engine_types,
            total_count=total_count,
            engines=engines,
        )


        agent_engine_type_list.additional_properties = d
        return agent_engine_type_list

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
