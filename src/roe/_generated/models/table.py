from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.table_column import TableColumn





T = TypeVar("T", bound="Table")



@_attrs_define
class Table:
    """ Serializer for table information.

        Attributes:
            name (str): Name of the table
            columns (list[TableColumn]): List of columns in the table
     """

    name: str
    columns: list[TableColumn]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_column import TableColumn
        name = self.name

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "columns": columns,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_column import TableColumn
        d = dict(src_dict)
        name = d.pop("name")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in (_columns):
            columns_item = TableColumn.from_dict(columns_item_data)



            columns.append(columns_item)


        table = cls(
            name=name,
            columns=columns,
        )


        table.additional_properties = d
        return table

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
