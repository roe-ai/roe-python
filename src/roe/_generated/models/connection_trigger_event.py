from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connection_trigger_event_status_enum import ConnectionTriggerEventStatusEnum
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="ConnectionTriggerEvent")



@_attrs_define
class ConnectionTriggerEvent:
    """ Read-only serializer for trigger events.

        Attributes:
            id (UUID):
            external_file_id (str):
            file_name (str):
            agent_job (None | UUID):
            status (ConnectionTriggerEventStatusEnum): * `detected` - Detected
                * `processing` - Processing
                * `completed` - Completed
                * `failed` - Failed
            error_message (str):
            created_at (datetime.datetime):
     """

    id: UUID
    external_file_id: str
    file_name: str
    agent_job: None | UUID
    status: ConnectionTriggerEventStatusEnum
    error_message: str
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        external_file_id = self.external_file_id

        file_name = self.file_name

        agent_job: None | str
        if isinstance(self.agent_job, UUID):
            agent_job = str(self.agent_job)
        else:
            agent_job = self.agent_job

        status = self.status.value

        error_message = self.error_message

        created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "external_file_id": external_file_id,
            "file_name": file_name,
            "agent_job": agent_job,
            "status": status,
            "error_message": error_message,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        external_file_id = d.pop("external_file_id")

        file_name = d.pop("file_name")

        def _parse_agent_job(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                agent_job_type_0 = UUID(data)



                return agent_job_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        agent_job = _parse_agent_job(d.pop("agent_job"))


        status = ConnectionTriggerEventStatusEnum(d.pop("status"))




        error_message = d.pop("error_message")

        created_at = isoparse(d.pop("created_at"))




        connection_trigger_event = cls(
            id=id,
            external_file_id=external_file_id,
            file_name=file_name,
            agent_job=agent_job,
            status=status,
            error_message=error_message,
            created_at=created_at,
        )


        connection_trigger_event.additional_properties = d
        return connection_trigger_event

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
