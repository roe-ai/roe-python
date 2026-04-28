from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="ConnectionTriggerCreateRequest")



@_attrs_define
class ConnectionTriggerCreateRequest:
    """ Write serializer for creating a connection trigger.

        Attributes:
            connection_id (UUID):
            agent_id (UUID):
            input_key (str):
            drive_id (str):
            drive_name (str):
     """

    connection_id: UUID
    agent_id: UUID
    input_key: str
    drive_id: str
    drive_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        connection_id = str(self.connection_id)

        agent_id = str(self.agent_id)

        input_key = self.input_key

        drive_id = self.drive_id

        drive_name = self.drive_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "connection_id": connection_id,
            "agent_id": agent_id,
            "input_key": input_key,
            "drive_id": drive_id,
            "drive_name": drive_name,
        })

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("connection_id", (None, str(self.connection_id), "text/plain")))



        files.append(("agent_id", (None, str(self.agent_id), "text/plain")))



        files.append(("input_key", (None, str(self.input_key).encode(), "text/plain")))



        files.append(("drive_id", (None, str(self.drive_id).encode(), "text/plain")))



        files.append(("drive_name", (None, str(self.drive_name).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connection_id = UUID(d.pop("connection_id"))




        agent_id = UUID(d.pop("agent_id"))




        input_key = d.pop("input_key")

        drive_id = d.pop("drive_id")

        drive_name = d.pop("drive_name")

        connection_trigger_create_request = cls(
            connection_id=connection_id,
            agent_id=agent_id,
            input_key=input_key,
            drive_id=drive_id,
            drive_name=drive_name,
        )


        connection_trigger_create_request.additional_properties = d
        return connection_trigger_create_request

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
