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

if TYPE_CHECKING:
  from ..models.connection_trigger_event import ConnectionTriggerEvent





T = TypeVar("T", bound="ConnectionTrigger")



@_attrs_define
class ConnectionTrigger:
    """ Read serializer for connection triggers.

        Attributes:
            id (UUID):
            connection_id (UUID):
            connection_name (str):
            connector_type (str):
            agent_id (UUID):
            agent_name (str):
            enabled (bool):
            input_key (str):
            drive_name (str):
            last_checked_at (datetime.datetime | None):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            recent_events (list[ConnectionTriggerEvent]):
     """

    id: UUID
    connection_id: UUID
    connection_name: str
    connector_type: str
    agent_id: UUID
    agent_name: str
    enabled: bool
    input_key: str
    drive_name: str
    last_checked_at: datetime.datetime | None
    created_at: datetime.datetime
    updated_at: datetime.datetime
    recent_events: list[ConnectionTriggerEvent]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_trigger_event import ConnectionTriggerEvent
        id = str(self.id)

        connection_id = str(self.connection_id)

        connection_name = self.connection_name

        connector_type = self.connector_type

        agent_id = str(self.agent_id)

        agent_name = self.agent_name

        enabled = self.enabled

        input_key = self.input_key

        drive_name = self.drive_name

        last_checked_at: None | str
        if isinstance(self.last_checked_at, datetime.datetime):
            last_checked_at = self.last_checked_at.isoformat()
        else:
            last_checked_at = self.last_checked_at

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        recent_events = []
        for recent_events_item_data in self.recent_events:
            recent_events_item = recent_events_item_data.to_dict()
            recent_events.append(recent_events_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "connection_id": connection_id,
            "connection_name": connection_name,
            "connector_type": connector_type,
            "agent_id": agent_id,
            "agent_name": agent_name,
            "enabled": enabled,
            "input_key": input_key,
            "drive_name": drive_name,
            "last_checked_at": last_checked_at,
            "created_at": created_at,
            "updated_at": updated_at,
            "recent_events": recent_events,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_trigger_event import ConnectionTriggerEvent
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        connection_id = UUID(d.pop("connection_id"))




        connection_name = d.pop("connection_name")

        connector_type = d.pop("connector_type")

        agent_id = UUID(d.pop("agent_id"))




        agent_name = d.pop("agent_name")

        enabled = d.pop("enabled")

        input_key = d.pop("input_key")

        drive_name = d.pop("drive_name")

        def _parse_last_checked_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_checked_at_type_0 = isoparse(data)



                return last_checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_checked_at = _parse_last_checked_at(d.pop("last_checked_at"))


        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        recent_events = []
        _recent_events = d.pop("recent_events")
        for recent_events_item_data in (_recent_events):
            recent_events_item = ConnectionTriggerEvent.from_dict(recent_events_item_data)



            recent_events.append(recent_events_item)


        connection_trigger = cls(
            id=id,
            connection_id=connection_id,
            connection_name=connection_name,
            connector_type=connector_type,
            agent_id=agent_id,
            agent_name=agent_name,
            enabled=enabled,
            input_key=input_key,
            drive_name=drive_name,
            last_checked_at=last_checked_at,
            created_at=created_at,
            updated_at=updated_at,
            recent_events=recent_events,
        )


        connection_trigger.additional_properties = d
        return connection_trigger

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
