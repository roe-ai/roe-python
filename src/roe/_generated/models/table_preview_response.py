from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.table_column import TableColumn
  from ..models.table_preview_response_rows_item import TablePreviewResponseRowsItem





T = TypeVar("T", bound="TablePreviewResponse")



@_attrs_define
class TablePreviewResponse:
    """ Response payload for previewing a public Roe table.

        Attributes:
            table_name (str): Name of the table
            columns (list[TableColumn]): List of columns in the table
            rows (list[TablePreviewResponseRowsItem]): Sample rows keyed by column name
            row_count (int): Number of sample rows returned
     """

    table_name: str
    columns: list[TableColumn]
    rows: list[TablePreviewResponseRowsItem]
    row_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_column import TableColumn
        from ..models.table_preview_response_rows_item import TablePreviewResponseRowsItem
        table_name = self.table_name

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)



        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)



        row_count = self.row_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "table_name": table_name,
            "columns": columns,
            "rows": rows,
            "row_count": row_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_column import TableColumn
        from ..models.table_preview_response_rows_item import TablePreviewResponseRowsItem
        d = dict(src_dict)
        table_name = d.pop("table_name")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in (_columns):
            columns_item = TableColumn.from_dict(columns_item_data)



            columns.append(columns_item)


        rows = []
        _rows = d.pop("rows")
        for rows_item_data in (_rows):
            rows_item = TablePreviewResponseRowsItem.from_dict(rows_item_data)



            rows.append(rows_item)


        row_count = d.pop("row_count")

        table_preview_response = cls(
            table_name=table_name,
            columns=columns,
            rows=rows,
            row_count=row_count,
        )


        table_preview_response.additional_properties = d
        return table_preview_response

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
