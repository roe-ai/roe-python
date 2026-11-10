from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.duplicate_connection_existing import DuplicateConnectionExisting





T = TypeVar("T", bound="ConnectionUpdateConflictResponse")



@_attrs_define
class ConnectionUpdateConflictResponse:
    """ Body of a 409 from update/replace; which fields are set depends on the cause.

        Attributes:
            error (str):
            existing_connection (DuplicateConnectionExisting | Unset): Identifying summary of the existing connection that
                triggered a 409.
            in_use (bool | Unset): True when agents or webhooks use the settings being changed; resend with confirm_in_use
                to save anyway.
     """

    error: str
    existing_connection: DuplicateConnectionExisting | Unset = UNSET
    in_use: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.duplicate_connection_existing import DuplicateConnectionExisting
        error = self.error

        existing_connection: dict[str, Any] | Unset = UNSET
        if not isinstance(self.existing_connection, Unset):
            existing_connection = self.existing_connection.to_dict()

        in_use = self.in_use


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "error": error,
        })
        if existing_connection is not UNSET:
            field_dict["existing_connection"] = existing_connection
        if in_use is not UNSET:
            field_dict["in_use"] = in_use

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.duplicate_connection_existing import DuplicateConnectionExisting
        d = dict(src_dict)
        error = d.pop("error")

        _existing_connection = d.pop("existing_connection", UNSET)
        existing_connection: DuplicateConnectionExisting | Unset
        if isinstance(_existing_connection,  Unset):
            existing_connection = UNSET
        else:
            existing_connection = DuplicateConnectionExisting.from_dict(_existing_connection)




        in_use = d.pop("in_use", UNSET)

        connection_update_conflict_response = cls(
            error=error,
            existing_connection=existing_connection,
            in_use=in_use,
        )


        connection_update_conflict_response.additional_properties = d
        return connection_update_conflict_response

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
