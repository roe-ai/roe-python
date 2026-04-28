from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="AgentDatum")



@_attrs_define
class AgentDatum:
    """ 
        Attributes:
            key (str): The key of the output
            data_type (str): The MIME data type of the output
            value (str): The value of the output, serialized as a string
            description (str | Unset): The description of the output
            cost (float | Unset): The cost of the agent job execution
     """

    key: str
    data_type: str
    value: str
    description: str | Unset = UNSET
    cost: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key = self.key

        data_type = self.data_type

        value = self.value

        description = self.description

        cost = self.cost


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "data_type": data_type,
            "value": value,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if cost is not UNSET:
            field_dict["cost"] = cost

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        data_type = d.pop("data_type")

        value = d.pop("value")

        description = d.pop("description", UNSET)

        cost = d.pop("cost", UNSET)

        agent_datum = cls(
            key=key,
            data_type=data_type,
            value=value,
            description=description,
            cost=cost,
        )


        agent_datum.additional_properties = d
        return agent_datum

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
