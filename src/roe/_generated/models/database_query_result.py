from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.database_query_result_summary import DatabaseQueryResultSummary





T = TypeVar("T", bound="DatabaseQueryResult")



@_attrs_define
class DatabaseQueryResult:
    """ 
        Attributes:
            query (str): The query that was run.
            summary (DatabaseQueryResultSummary):
            row_count (int): The number of rows returned by the query.
            column_names (list[str]): A list of strings representing the column names
            column_types (list[str]): A list of strings representing the column types
            result_rows (list[list[str]]): A matrix of the data returned in the form of a Sequence of rows, with each row
                element being a sequence of column values.
            start_timestamp (float): The timestamp when the query started running.
            end_timestamp (float): The timestamp when the query finished running.
            query_id (str | Unset): The query UUID.
     """

    query: str
    summary: DatabaseQueryResultSummary
    row_count: int
    column_names: list[str]
    column_types: list[str]
    result_rows: list[list[str]]
    start_timestamp: float
    end_timestamp: float
    query_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.database_query_result_summary import DatabaseQueryResultSummary
        query = self.query

        summary = self.summary.to_dict()

        row_count = self.row_count

        column_names = self.column_names



        column_types = self.column_types



        result_rows = []
        for result_rows_item_data in self.result_rows:
            result_rows_item = result_rows_item_data


            result_rows.append(result_rows_item)



        start_timestamp = self.start_timestamp

        end_timestamp = self.end_timestamp

        query_id = self.query_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "query": query,
            "summary": summary,
            "row_count": row_count,
            "column_names": column_names,
            "column_types": column_types,
            "result_rows": result_rows,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
        })
        if query_id is not UNSET:
            field_dict["query_id"] = query_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_query_result_summary import DatabaseQueryResultSummary
        d = dict(src_dict)
        query = d.pop("query")

        summary = DatabaseQueryResultSummary.from_dict(d.pop("summary"))




        row_count = d.pop("row_count")

        column_names = cast(list[str], d.pop("column_names"))


        column_types = cast(list[str], d.pop("column_types"))


        result_rows = []
        _result_rows = d.pop("result_rows")
        for result_rows_item_data in (_result_rows):
            result_rows_item = cast(list[str], result_rows_item_data)

            result_rows.append(result_rows_item)


        start_timestamp = d.pop("start_timestamp")

        end_timestamp = d.pop("end_timestamp")

        query_id = d.pop("query_id", UNSET)

        database_query_result = cls(
            query=query,
            summary=summary,
            row_count=row_count,
            column_names=column_names,
            column_types=column_types,
            result_rows=result_rows,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp,
            query_id=query_id,
        )


        database_query_result.additional_properties = d
        return database_query_result

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
