from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..models.status_768_enum import Status768Enum
from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="ConnectionRequest")



@_attrs_define
class ConnectionRequest:
    """ Serializer for Connection model.
    Returns:
    - config: Non-sensitive config from DB
    - auth_config: Actual auth credentials from Secrets Manager (not the internal reference)

        Attributes:
            organization (UUID):
            connector_type (str):
            name (str):
            description (str | Unset):
            config (Any | Unset):
            status (Status768Enum | Unset): * `active` - Active
                * `error` - Error
     """

    organization: UUID
    connector_type: str
    name: str
    description: str | Unset = UNSET
    config: Any | Unset = UNSET
    status: Status768Enum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        organization = str(self.organization)

        connector_type = self.connector_type

        name = self.name

        description = self.description

        config = self.config

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "organization": organization,
            "connector_type": connector_type,
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if config is not UNSET:
            field_dict["config"] = config
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("organization", (None, str(self.organization), "text/plain")))



        files.append(("connector_type", (None, str(self.connector_type).encode(), "text/plain")))



        files.append(("name", (None, str(self.name).encode(), "text/plain")))



        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))



        if not isinstance(self.config, Unset):
            files.append(("config", (None, str(self.config).encode(), "text/plain")))



        if not isinstance(self.status, Unset):
            files.append(("status",  (None, str(self.status.value).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        organization = UUID(d.pop("organization"))




        connector_type = d.pop("connector_type")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        config = d.pop("config", UNSET)

        _status = d.pop("status", UNSET)
        status: Status768Enum | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = Status768Enum(_status)




        connection_request = cls(
            organization=organization,
            connector_type=connector_type,
            name=name,
            description=description,
            config=config,
            status=status,
        )


        connection_request.additional_properties = d
        return connection_request

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
