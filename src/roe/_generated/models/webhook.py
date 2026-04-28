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

if TYPE_CHECKING:
  from ..models.webhook_headers import WebhookHeaders





T = TypeVar("T", bound="Webhook")



@_attrs_define
class Webhook:
    """ Serializer for Webhook model

        Attributes:
            id (UUID):
            name (str): User-friendly name for this webhook
            url (str): Webhook endpoint URL
            alerts (list[str]): Alert IDs
            failure_count (int): Number of consecutive failures
            created_by (int):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            secret (str | Unset):
            headers (WebhookHeaders | Unset): Custom headers to include in webhook requests (key-value pairs)
            events (list[str] | Unset): List of events to trigger this webhook (e.g., ['triggered'])
            is_active (bool | Unset):
            last_triggered_at (datetime.datetime | Unset):
            last_success_at (datetime.datetime | Unset):
            last_failure_at (datetime.datetime | Unset):
     """

    id: UUID
    name: str
    url: str
    alerts: list[str]
    failure_count: int
    created_by: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    secret: str | Unset = UNSET
    headers: WebhookHeaders | Unset = UNSET
    events: list[str] | Unset = UNSET
    is_active: bool | Unset = UNSET
    last_triggered_at: datetime.datetime | Unset = UNSET
    last_success_at: datetime.datetime | Unset = UNSET
    last_failure_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_headers import WebhookHeaders
        id = str(self.id)

        name = self.name

        url = self.url

        alerts = self.alerts



        failure_count = self.failure_count

        created_by = self.created_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        secret = self.secret

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events



        is_active = self.is_active

        last_triggered_at: str | Unset = UNSET
        if not isinstance(self.last_triggered_at, Unset):
            last_triggered_at = self.last_triggered_at.isoformat()

        last_success_at: str | Unset = UNSET
        if not isinstance(self.last_success_at, Unset):
            last_success_at = self.last_success_at.isoformat()

        last_failure_at: str | Unset = UNSET
        if not isinstance(self.last_failure_at, Unset):
            last_failure_at = self.last_failure_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "url": url,
            "alerts": alerts,
            "failure_count": failure_count,
            "created_by": created_by,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if secret is not UNSET:
            field_dict["secret"] = secret
        if headers is not UNSET:
            field_dict["headers"] = headers
        if events is not UNSET:
            field_dict["events"] = events
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if last_triggered_at is not UNSET:
            field_dict["last_triggered_at"] = last_triggered_at
        if last_success_at is not UNSET:
            field_dict["last_success_at"] = last_success_at
        if last_failure_at is not UNSET:
            field_dict["last_failure_at"] = last_failure_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_headers import WebhookHeaders
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        name = d.pop("name")

        url = d.pop("url")

        alerts = cast(list[str], d.pop("alerts"))


        failure_count = d.pop("failure_count")

        created_by = d.pop("created_by")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        secret = d.pop("secret", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: WebhookHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = WebhookHeaders.from_dict(_headers)




        events = cast(list[str], d.pop("events", UNSET))


        is_active = d.pop("is_active", UNSET)

        _last_triggered_at = d.pop("last_triggered_at", UNSET)
        last_triggered_at: datetime.datetime | Unset
        if isinstance(_last_triggered_at,  Unset):
            last_triggered_at = UNSET
        else:
            last_triggered_at = isoparse(_last_triggered_at)




        _last_success_at = d.pop("last_success_at", UNSET)
        last_success_at: datetime.datetime | Unset
        if isinstance(_last_success_at,  Unset):
            last_success_at = UNSET
        else:
            last_success_at = isoparse(_last_success_at)




        _last_failure_at = d.pop("last_failure_at", UNSET)
        last_failure_at: datetime.datetime | Unset
        if isinstance(_last_failure_at,  Unset):
            last_failure_at = UNSET
        else:
            last_failure_at = isoparse(_last_failure_at)




        webhook = cls(
            id=id,
            name=name,
            url=url,
            alerts=alerts,
            failure_count=failure_count,
            created_by=created_by,
            created_at=created_at,
            updated_at=updated_at,
            secret=secret,
            headers=headers,
            events=events,
            is_active=is_active,
            last_triggered_at=last_triggered_at,
            last_success_at=last_success_at,
            last_failure_at=last_failure_at,
        )


        webhook.additional_properties = d
        return webhook

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
