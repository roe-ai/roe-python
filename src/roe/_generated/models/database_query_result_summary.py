from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DatabaseQueryResultSummary")



@_attrs_define
class DatabaseQueryResultSummary:
    """ 
        Attributes:
            read_rows (int | Unset):
            read_bytes (int | Unset):
            written_rows (int | Unset):
            written_bytes (int | Unset):
            total_rows_to_read (int | Unset):
            result_rows (int | Unset):
            result_bytes (int | Unset):
            elapsed_ns (int | Unset):
            query_id (str | Unset):
     """

    read_rows: int | Unset = UNSET
    read_bytes: int | Unset = UNSET
    written_rows: int | Unset = UNSET
    written_bytes: int | Unset = UNSET
    total_rows_to_read: int | Unset = UNSET
    result_rows: int | Unset = UNSET
    result_bytes: int | Unset = UNSET
    elapsed_ns: int | Unset = UNSET
    query_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        read_rows = self.read_rows

        read_bytes = self.read_bytes

        written_rows = self.written_rows

        written_bytes = self.written_bytes

        total_rows_to_read = self.total_rows_to_read

        result_rows = self.result_rows

        result_bytes = self.result_bytes

        elapsed_ns = self.elapsed_ns

        query_id = self.query_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if read_rows is not UNSET:
            field_dict["read_rows"] = read_rows
        if read_bytes is not UNSET:
            field_dict["read_bytes"] = read_bytes
        if written_rows is not UNSET:
            field_dict["written_rows"] = written_rows
        if written_bytes is not UNSET:
            field_dict["written_bytes"] = written_bytes
        if total_rows_to_read is not UNSET:
            field_dict["total_rows_to_read"] = total_rows_to_read
        if result_rows is not UNSET:
            field_dict["result_rows"] = result_rows
        if result_bytes is not UNSET:
            field_dict["result_bytes"] = result_bytes
        if elapsed_ns is not UNSET:
            field_dict["elapsed_ns"] = elapsed_ns
        if query_id is not UNSET:
            field_dict["query_id"] = query_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        read_rows = d.pop("read_rows", UNSET)

        read_bytes = d.pop("read_bytes", UNSET)

        written_rows = d.pop("written_rows", UNSET)

        written_bytes = d.pop("written_bytes", UNSET)

        total_rows_to_read = d.pop("total_rows_to_read", UNSET)

        result_rows = d.pop("result_rows", UNSET)

        result_bytes = d.pop("result_bytes", UNSET)

        elapsed_ns = d.pop("elapsed_ns", UNSET)

        query_id = d.pop("query_id", UNSET)

        database_query_result_summary = cls(
            read_rows=read_rows,
            read_bytes=read_bytes,
            written_rows=written_rows,
            written_bytes=written_bytes,
            total_rows_to_read=total_rows_to_read,
            result_rows=result_rows,
            result_bytes=result_bytes,
            elapsed_ns=elapsed_ns,
            query_id=query_id,
        )


        database_query_result_summary.additional_properties = d
        return database_query_result_summary

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
