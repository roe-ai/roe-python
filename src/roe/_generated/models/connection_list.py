from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.status_768_enum import Status768Enum
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="ConnectionList")



@_attrs_define
class ConnectionList:
    """ Lightweight serializer for listing connections.
    Only returns metadata, no auth_config (avoids Secrets Manager calls).

        Attributes:
            id (UUID):
            user (int | None):
            organization (UUID):
            connector_type (str):
            connector_display_name (str): Get the display name for the connector type.
            name (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            description (str | Unset):
            config (Any | Unset):
            status (Status768Enum | Unset): * `active` - Active
                * `error` - Error
     """

    id: UUID
    user: int | None
    organization: UUID
    connector_type: str
    connector_display_name: str
    name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: str | Unset = UNSET
    config: Any | Unset = UNSET
    status: Status768Enum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        user: int | None
        user = self.user

        organization = str(self.organization)

        connector_type = self.connector_type

        connector_display_name = self.connector_display_name

        name = self.name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description

        config = self.config

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "user": user,
            "organization": organization,
            "connector_type": connector_type,
            "connector_display_name": connector_display_name,
            "name": name,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if config is not UNSET:
            field_dict["config"] = config
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        def _parse_user(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        user = _parse_user(d.pop("user"))


        organization = UUID(d.pop("organization"))




        connector_type = d.pop("connector_type")

        connector_display_name = d.pop("connector_display_name")

        name = d.pop("name")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        description = d.pop("description", UNSET)

        config = d.pop("config", UNSET)

        _status = d.pop("status", UNSET)
        status: Status768Enum | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = Status768Enum(_status)




        connection_list = cls(
            id=id,
            user=user,
            organization=organization,
            connector_type=connector_type,
            connector_display_name=connector_display_name,
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            config=config,
            status=status,
        )


        connection_list.additional_properties = d
        return connection_list

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
