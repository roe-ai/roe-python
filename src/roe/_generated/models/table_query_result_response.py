from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.table_query_status_enum import TableQueryStatusEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.table_query_result_response_columns_item import TableQueryResultResponseColumnsItem
  from ..models.table_query_result_response_rows_item import TableQueryResultResponseRowsItem





T = TypeVar("T", bound="TableQueryResultResponse")



@_attrs_define
class TableQueryResultResponse:
    """ Response payload for polling or fetching a public Roe table query.

        Attributes:
            table_query_id (UUID):
            status (TableQueryStatusEnum): * `PENDING` - PENDING
                * `STARTED` - STARTED
                * `RETRY` - RETRY
                * `SUCCESS` - SUCCESS
                * `FAILURE` - FAILURE
                * `REVOKED` - REVOKED
            error (None | str | Unset):
            columns (list[TableQueryResultResponseColumnsItem] | Unset):
            rows (list[TableQueryResultResponseRowsItem] | Unset): Rows keyed by column name. When truncated is true, an
                oversized cell may be returned as a shortened string even if the original ClickHouse value was a nested object
                or array.
            row_count (int | Unset):
            truncated (bool | Unset): True when the result hit the row limit, backend result byte cap, or an individual huge
                cell was shortened. In truncated responses, any oversized cell may be represented as a string regardless of its
                original ClickHouse type.
            execution_time_ms (float | Unset):
     """

    table_query_id: UUID
    status: TableQueryStatusEnum
    error: None | str | Unset = UNSET
    columns: list[TableQueryResultResponseColumnsItem] | Unset = UNSET
    rows: list[TableQueryResultResponseRowsItem] | Unset = UNSET
    row_count: int | Unset = UNSET
    truncated: bool | Unset = UNSET
    execution_time_ms: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_query_result_response_columns_item import TableQueryResultResponseColumnsItem
        from ..models.table_query_result_response_rows_item import TableQueryResultResponseRowsItem
        table_query_id = str(self.table_query_id)

        status = self.status.value

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        columns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.columns, Unset):
            columns = []
            for columns_item_data in self.columns:
                columns_item = columns_item_data.to_dict()
                columns.append(columns_item)



        rows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rows, Unset):
            rows = []
            for rows_item_data in self.rows:
                rows_item = rows_item_data.to_dict()
                rows.append(rows_item)



        row_count = self.row_count

        truncated = self.truncated

        execution_time_ms = self.execution_time_ms


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "table_query_id": table_query_id,
            "status": status,
        })
        if error is not UNSET:
            field_dict["error"] = error
        if columns is not UNSET:
            field_dict["columns"] = columns
        if rows is not UNSET:
            field_dict["rows"] = rows
        if row_count is not UNSET:
            field_dict["row_count"] = row_count
        if truncated is not UNSET:
            field_dict["truncated"] = truncated
        if execution_time_ms is not UNSET:
            field_dict["execution_time_ms"] = execution_time_ms

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_query_result_response_columns_item import TableQueryResultResponseColumnsItem
        from ..models.table_query_result_response_rows_item import TableQueryResultResponseRowsItem
        d = dict(src_dict)
        table_query_id = UUID(d.pop("table_query_id"))




        status = TableQueryStatusEnum(d.pop("status"))




        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        _columns = d.pop("columns", UNSET)
        columns: list[TableQueryResultResponseColumnsItem] | Unset = UNSET
        if _columns is not UNSET:
            columns = []
            for columns_item_data in _columns:
                columns_item = TableQueryResultResponseColumnsItem.from_dict(columns_item_data)



                columns.append(columns_item)


        _rows = d.pop("rows", UNSET)
        rows: list[TableQueryResultResponseRowsItem] | Unset = UNSET
        if _rows is not UNSET:
            rows = []
            for rows_item_data in _rows:
                rows_item = TableQueryResultResponseRowsItem.from_dict(rows_item_data)



                rows.append(rows_item)


        row_count = d.pop("row_count", UNSET)

        truncated = d.pop("truncated", UNSET)

        execution_time_ms = d.pop("execution_time_ms", UNSET)

        table_query_result_response = cls(
            table_query_id=table_query_id,
            status=status,
            error=error,
            columns=columns,
            rows=rows,
            row_count=row_count,
            truncated=truncated,
            execution_time_ms=execution_time_ms,
        )


        table_query_result_response.additional_properties = d
        return table_query_result_response

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
