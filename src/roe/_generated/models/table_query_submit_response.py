from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="TableQuerySubmitResponse")



@_attrs_define
class TableQuerySubmitResponse:
    """ Response payload for submitting a public Roe table query.

        Attributes:
            table_query_id (UUID):
            status (str):
            created_at (datetime.datetime):
     """

    table_query_id: UUID
    status: str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        table_query_id = str(self.table_query_id)

        status = self.status

        created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "table_query_id": table_query_id,
            "status": status,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        table_query_id = UUID(d.pop("table_query_id"))




        status = d.pop("status")

        created_at = isoparse(d.pop("created_at"))




        table_query_submit_response = cls(
            table_query_id=table_query_id,
            status=status,
            created_at=created_at,
        )


        table_query_submit_response.additional_properties = d
        return table_query_submit_response

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
