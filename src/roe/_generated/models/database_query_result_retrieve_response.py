from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.database_query_result import DatabaseQueryResult





T = TypeVar("T", bound="DatabaseQueryResultRetrieveResponse")



@_attrs_define
class DatabaseQueryResultRetrieveResponse:
    """ 
        Attributes:
            worksheet_query_id (UUID): The query task UUID.
            status (str): The status of the query task.
            results (list[DatabaseQueryResult] | Unset): The results of the query.
            error (None | str | Unset): An error message if the query failed.
     """

    worksheet_query_id: UUID
    status: str
    results: list[DatabaseQueryResult] | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.database_query_result import DatabaseQueryResult
        worksheet_query_id = str(self.worksheet_query_id)

        status = self.status

        results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()
                results.append(results_item)



        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "worksheet_query_id": worksheet_query_id,
            "status": status,
        })
        if results is not UNSET:
            field_dict["results"] = results
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.database_query_result import DatabaseQueryResult
        d = dict(src_dict)
        worksheet_query_id = UUID(d.pop("worksheet_query_id"))




        status = d.pop("status")

        _results = d.pop("results", UNSET)
        results: list[DatabaseQueryResult] | Unset = UNSET
        if _results is not UNSET:
            results = []
            for results_item_data in _results:
                results_item = DatabaseQueryResult.from_dict(results_item_data)



                results.append(results_item)


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        database_query_result_retrieve_response = cls(
            worksheet_query_id=worksheet_query_id,
            status=status,
            results=results,
            error=error,
        )


        database_query_result_retrieve_response.additional_properties = d
        return database_query_result_retrieve_response

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
