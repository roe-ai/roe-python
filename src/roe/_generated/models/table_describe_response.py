from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.table_column import TableColumn





T = TypeVar("T", bound="TableDescribeResponse")



@_attrs_define
class TableDescribeResponse:
    """ Response payload for describing a public Roe table.

        Attributes:
            table_name (str): Name of the table
            columns (list[TableColumn]): List of columns in the table
            row_count (int | None): Total row count if ClickHouse can determine it from metadata without scanning the table
            updated_at (datetime.datetime | None): Latest ClickHouse table metadata modification timestamp if available
     """

    table_name: str
    columns: list[TableColumn]
    row_count: int | None
    updated_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_column import TableColumn
        table_name = self.table_name

        columns = []
        for columns_item_data in self.columns:
            columns_item = columns_item_data.to_dict()
            columns.append(columns_item)



        row_count: int | None
        row_count = self.row_count

        updated_at: None | str
        if isinstance(self.updated_at, datetime.datetime):
            updated_at = self.updated_at.isoformat()
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "table_name": table_name,
            "columns": columns,
            "row_count": row_count,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_column import TableColumn
        d = dict(src_dict)
        table_name = d.pop("table_name")

        columns = []
        _columns = d.pop("columns")
        for columns_item_data in (_columns):
            columns_item = TableColumn.from_dict(columns_item_data)



            columns.append(columns_item)


        def _parse_row_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        row_count = _parse_row_count(d.pop("row_count"))


        def _parse_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                updated_at_type_0 = isoparse(data)



                return updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        updated_at = _parse_updated_at(d.pop("updated_at"))


        table_describe_response = cls(
            table_name=table_name,
            columns=columns,
            row_count=row_count,
            updated_at=updated_at,
        )


        table_describe_response.additional_properties = d
        return table_describe_response

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
