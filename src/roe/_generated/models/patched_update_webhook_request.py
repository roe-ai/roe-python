from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.patched_update_webhook_request_headers import PatchedUpdateWebhookRequestHeaders





T = TypeVar("T", bound="PatchedUpdateWebhookRequest")



@_attrs_define
class PatchedUpdateWebhookRequest:
    """ Serializer for updating webhooks

        Attributes:
            name (str | Unset): User-friendly name for this webhook
            url (str | Unset): Webhook endpoint URL
            secret (str | Unset):
            headers (PatchedUpdateWebhookRequestHeaders | Unset): Custom headers to include in webhook requests (key-value
                pairs)
            events (list[str] | Unset): List of events to trigger this webhook (e.g., ['triggered'])
            is_active (bool | Unset):
            alerts (list[UUID] | Unset):
     """

    name: str | Unset = UNSET
    url: str | Unset = UNSET
    secret: str | Unset = UNSET
    headers: PatchedUpdateWebhookRequestHeaders | Unset = UNSET
    events: list[str] | Unset = UNSET
    is_active: bool | Unset = UNSET
    alerts: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.patched_update_webhook_request_headers import PatchedUpdateWebhookRequestHeaders
        name = self.name

        url = self.url

        secret = self.secret

        headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.headers, Unset):
            headers = self.headers.to_dict()

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events



        is_active = self.is_active

        alerts: list[str] | Unset = UNSET
        if not isinstance(self.alerts, Unset):
            alerts = []
            for alerts_item_data in self.alerts:
                alerts_item = str(alerts_item_data)
                alerts.append(alerts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if url is not UNSET:
            field_dict["url"] = url
        if secret is not UNSET:
            field_dict["secret"] = secret
        if headers is not UNSET:
            field_dict["headers"] = headers
        if events is not UNSET:
            field_dict["events"] = events
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if alerts is not UNSET:
            field_dict["alerts"] = alerts

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        from ..models.patched_update_webhook_request_headers import PatchedUpdateWebhookRequestHeaders
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))



        if not isinstance(self.url, Unset):
            files.append(("url", (None, str(self.url).encode(), "text/plain")))



        if not isinstance(self.secret, Unset):
            files.append(("secret", (None, str(self.secret).encode(), "text/plain")))



        if not isinstance(self.headers, Unset):
            files.append(("headers", (None, json.dumps( self.headers.to_dict()).encode(), "application/json")))



        if not isinstance(self.events, Unset):
            for events_item_element in self.events:
                files.append(("events", (None, str(events_item_element).encode(), "text/plain")))




        if not isinstance(self.is_active, Unset):
            files.append(("is_active", (None, str(self.is_active).encode(), "text/plain")))



        if not isinstance(self.alerts, Unset):
            for alerts_item_element in self.alerts:
                files.append(("alerts", (None, str(alerts_item_element), "text/plain")))





        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patched_update_webhook_request_headers import PatchedUpdateWebhookRequestHeaders
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        url = d.pop("url", UNSET)

        secret = d.pop("secret", UNSET)

        _headers = d.pop("headers", UNSET)
        headers: PatchedUpdateWebhookRequestHeaders | Unset
        if isinstance(_headers,  Unset):
            headers = UNSET
        else:
            headers = PatchedUpdateWebhookRequestHeaders.from_dict(_headers)




        events = cast(list[str], d.pop("events", UNSET))


        is_active = d.pop("is_active", UNSET)

        _alerts = d.pop("alerts", UNSET)
        alerts: list[UUID] | Unset = UNSET
        if _alerts is not UNSET:
            alerts = []
            for alerts_item_data in _alerts:
                alerts_item = UUID(alerts_item_data)



                alerts.append(alerts_item)


        patched_update_webhook_request = cls(
            name=name,
            url=url,
            secret=secret,
            headers=headers,
            events=events,
            is_active=is_active,
            alerts=alerts,
        )


        patched_update_webhook_request.additional_properties = d
        return patched_update_webhook_request

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
