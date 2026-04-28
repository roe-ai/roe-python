from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="SearchIndexQueryResponse")



@_attrs_define
class SearchIndexQueryResponse:
    """ 
        Attributes:
            column_names (list[str]): Column names
            column_types (list[str]): Column types
            result_rows (list[list[str]]): Result rows
     """

    column_names: list[str]
    column_types: list[str]
    result_rows: list[list[str]]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        column_names = self.column_names



        column_types = self.column_types



        result_rows = []
        for result_rows_item_data in self.result_rows:
            result_rows_item = result_rows_item_data


            result_rows.append(result_rows_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "column_names": column_names,
            "column_types": column_types,
            "result_rows": result_rows,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        column_names = cast(list[str], d.pop("column_names"))


        column_types = cast(list[str], d.pop("column_types"))


        result_rows = []
        _result_rows = d.pop("result_rows")
        for result_rows_item_data in (_result_rows):
            result_rows_item = cast(list[str], result_rows_item_data)

            result_rows.append(result_rows_item)


        search_index_query_response = cls(
            column_names=column_names,
            column_types=column_types,
            result_rows=result_rows,
        )


        search_index_query_response.additional_properties = d
        return search_index_query_response

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
