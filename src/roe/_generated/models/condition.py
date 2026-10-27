from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.operator_enum import OperatorEnum
from ..types import UNSET, Unset






T = TypeVar("T", bound="Condition")



@_attrs_define
class Condition:
    """ 
        Attributes:
            field (str):
            operator (OperatorEnum | Unset):  Default: OperatorEnum.EQUALS.
            value (Any | Unset):
     """

    field: str
    operator: OperatorEnum | Unset = OperatorEnum.EQUALS
    value: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        field = self.field

        operator: str | Unset = UNSET
        if not isinstance(self.operator, Unset):
            operator = self.operator.value


        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "field": field,
        })
        if operator is not UNSET:
            field_dict["operator"] = operator
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        _operator = d.pop("operator", UNSET)
        operator: OperatorEnum | Unset
        if isinstance(_operator,  Unset):
            operator = UNSET
        else:
            operator = OperatorEnum(_operator)




        value = d.pop("value", UNSET)

        condition = cls(
            field=field,
            operator=operator,
            value=value,
        )

        return condition

