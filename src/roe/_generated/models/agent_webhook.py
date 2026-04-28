from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="AgentWebhook")



@_attrs_define
class AgentWebhook:
    """ Agent-specific webhook subscription serializer.
    Provides agent_id and agent_name fields.

        Attributes:
            id (UUID):
            webhook_id (UUID):
            name (str):
            delivery_type (str):
            url (str):
            connection_id (None | UUID):
            connector_type (None | str):
            connection_name (None | str):
            destination_config (Any):
            agent_id (UUID):
            agent_name (None | str):
            is_active (bool):
            failure_count (int):
            last_triggered_at (datetime.datetime | None | Unset):
            last_success_at (datetime.datetime | None | Unset):
            last_failure_at (datetime.datetime | None | Unset):
     """

    id: UUID
    webhook_id: UUID
    name: str
    delivery_type: str
    url: str
    connection_id: None | UUID
    connector_type: None | str
    connection_name: None | str
    destination_config: Any
    agent_id: UUID
    agent_name: None | str
    is_active: bool
    failure_count: int
    last_triggered_at: datetime.datetime | None | Unset = UNSET
    last_success_at: datetime.datetime | None | Unset = UNSET
    last_failure_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        webhook_id = str(self.webhook_id)

        name = self.name

        delivery_type = self.delivery_type

        url = self.url

        connection_id: None | str
        if isinstance(self.connection_id, UUID):
            connection_id = str(self.connection_id)
        else:
            connection_id = self.connection_id

        connector_type: None | str
        connector_type = self.connector_type

        connection_name: None | str
        connection_name = self.connection_name

        destination_config = self.destination_config

        agent_id = str(self.agent_id)

        agent_name: None | str
        agent_name = self.agent_name

        is_active = self.is_active

        failure_count = self.failure_count

        last_triggered_at: None | str | Unset
        if isinstance(self.last_triggered_at, Unset):
            last_triggered_at = UNSET
        elif isinstance(self.last_triggered_at, datetime.datetime):
            last_triggered_at = self.last_triggered_at.isoformat()
        else:
            last_triggered_at = self.last_triggered_at

        last_success_at: None | str | Unset
        if isinstance(self.last_success_at, Unset):
            last_success_at = UNSET
        elif isinstance(self.last_success_at, datetime.datetime):
            last_success_at = self.last_success_at.isoformat()
        else:
            last_success_at = self.last_success_at

        last_failure_at: None | str | Unset
        if isinstance(self.last_failure_at, Unset):
            last_failure_at = UNSET
        elif isinstance(self.last_failure_at, datetime.datetime):
            last_failure_at = self.last_failure_at.isoformat()
        else:
            last_failure_at = self.last_failure_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "webhook_id": webhook_id,
            "name": name,
            "delivery_type": delivery_type,
            "url": url,
            "connection_id": connection_id,
            "connector_type": connector_type,
            "connection_name": connection_name,
            "destination_config": destination_config,
            "agent_id": agent_id,
            "agent_name": agent_name,
            "is_active": is_active,
            "failure_count": failure_count,
        })
        if last_triggered_at is not UNSET:
            field_dict["last_triggered_at"] = last_triggered_at
        if last_success_at is not UNSET:
            field_dict["last_success_at"] = last_success_at
        if last_failure_at is not UNSET:
            field_dict["last_failure_at"] = last_failure_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        webhook_id = UUID(d.pop("webhook_id"))




        name = d.pop("name")

        delivery_type = d.pop("delivery_type")

        url = d.pop("url")

        def _parse_connection_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                connection_id_type_0 = UUID(data)



                return connection_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        connection_id = _parse_connection_id(d.pop("connection_id"))


        def _parse_connector_type(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        connector_type = _parse_connector_type(d.pop("connector_type"))


        def _parse_connection_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        connection_name = _parse_connection_name(d.pop("connection_name"))


        destination_config = d.pop("destination_config")

        agent_id = UUID(d.pop("agent_id"))




        def _parse_agent_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_name = _parse_agent_name(d.pop("agent_name"))


        is_active = d.pop("is_active")

        failure_count = d.pop("failure_count")

        def _parse_last_triggered_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_triggered_at_type_0 = isoparse(data)



                return last_triggered_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_triggered_at = _parse_last_triggered_at(d.pop("last_triggered_at", UNSET))


        def _parse_last_success_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_success_at_type_0 = isoparse(data)



                return last_success_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_success_at = _parse_last_success_at(d.pop("last_success_at", UNSET))


        def _parse_last_failure_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_failure_at_type_0 = isoparse(data)



                return last_failure_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_failure_at = _parse_last_failure_at(d.pop("last_failure_at", UNSET))


        agent_webhook = cls(
            id=id,
            webhook_id=webhook_id,
            name=name,
            delivery_type=delivery_type,
            url=url,
            connection_id=connection_id,
            connector_type=connector_type,
            connection_name=connection_name,
            destination_config=destination_config,
            agent_id=agent_id,
            agent_name=agent_name,
            is_active=is_active,
            failure_count=failure_count,
            last_triggered_at=last_triggered_at,
            last_success_at=last_success_at,
            last_failure_at=last_failure_at,
        )


        agent_webhook.additional_properties = d
        return agent_webhook

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
