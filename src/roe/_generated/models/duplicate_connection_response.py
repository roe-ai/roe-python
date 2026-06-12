from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.duplicate_connection_existing import DuplicateConnectionExisting





T = TypeVar("T", bound="DuplicateConnectionResponse")



@_attrs_define
class DuplicateConnectionResponse:
    """ Body of the 409 response when create/update hits a strict-identity duplicate.

        Attributes:
            error (str):
            existing_connection (DuplicateConnectionExisting): Identifying summary of the existing connection that triggered
                a 409.
     """

    error: str
    existing_connection: DuplicateConnectionExisting
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.duplicate_connection_existing import DuplicateConnectionExisting
        error = self.error

        existing_connection = self.existing_connection.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "error": error,
            "existing_connection": existing_connection,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duplicate_connection_existing import DuplicateConnectionExisting
        d = dict(src_dict)
        error = d.pop("error")

        existing_connection = DuplicateConnectionExisting.from_dict(d.pop("existing_connection"))




        duplicate_connection_response = cls(
            error=error,
            existing_connection=existing_connection,
        )


        duplicate_connection_response.additional_properties = d
        return duplicate_connection_response

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
