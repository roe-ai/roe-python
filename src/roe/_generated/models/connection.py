from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.health_enum import HealthEnum
from ..models.lifecycle_enum import LifecycleEnum
from ..models.status_enum import StatusEnum
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.connection_auth_config import ConnectionAuthConfig
  from ..models.connection_dynamic_inputs import ConnectionDynamicInputs





T = TypeVar("T", bound="Connection")



@_attrs_define
class Connection:
    """ Serializer for Connection model.
    Returns:
    - config: Non-sensitive config from DB
    - auth_config: Manual credentials, or safe metadata for managed Zendesk OAuth

        Attributes:
            id (UUID):
            user (int | None):
            organization (UUID):
            connector_type (str):
            connector_display_name (str): Get the display name for the connector type.
            name (str):
            credentials_configured (bool):
            dynamic_inputs (ConnectionDynamicInputs):
            dynamic_input_test_disabled_reason (None | str):
            auth_config (ConnectionAuthConfig):
            browser_session_expires_at (datetime.datetime | None):
            health (HealthEnum): * `connecting` - Connecting
                * `expired` - Expired
                * `needs_attention` - Needs attention
                * `failed` - Failed
                * `connected` - Connected
                * `unknown` - Unknown
            last_verified_at (datetime.datetime | None):
            credentials_expire_at (datetime.datetime | None):
            account_label (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            description (str | Unset):
            config (Any | Unset):
            status (StatusEnum | Unset): * `active` - Active
                * `error` - Error
            lifecycle (LifecycleEnum | Unset): * `active` - Active
                * `archived` - Archived
                * `disconnected` - Disconnected
     """

    id: UUID
    user: int | None
    organization: UUID
    connector_type: str
    connector_display_name: str
    name: str
    credentials_configured: bool
    dynamic_inputs: ConnectionDynamicInputs
    dynamic_input_test_disabled_reason: None | str
    auth_config: ConnectionAuthConfig
    browser_session_expires_at: datetime.datetime | None
    health: HealthEnum
    last_verified_at: datetime.datetime | None
    credentials_expire_at: datetime.datetime | None
    account_label: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: str | Unset = UNSET
    config: Any | Unset = UNSET
    status: StatusEnum | Unset = UNSET
    lifecycle: LifecycleEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_auth_config import ConnectionAuthConfig
        from ..models.connection_dynamic_inputs import ConnectionDynamicInputs
        id = str(self.id)

        user: int | None
        user = self.user

        organization = str(self.organization)

        connector_type = self.connector_type

        connector_display_name = self.connector_display_name

        name = self.name

        credentials_configured = self.credentials_configured

        dynamic_inputs = self.dynamic_inputs.to_dict()

        dynamic_input_test_disabled_reason: None | str
        dynamic_input_test_disabled_reason = self.dynamic_input_test_disabled_reason

        auth_config = self.auth_config.to_dict()

        browser_session_expires_at: None | str
        if isinstance(self.browser_session_expires_at, datetime.datetime):
            browser_session_expires_at = self.browser_session_expires_at.isoformat()
        else:
            browser_session_expires_at = self.browser_session_expires_at

        health = self.health.value

        last_verified_at: None | str
        if isinstance(self.last_verified_at, datetime.datetime):
            last_verified_at = self.last_verified_at.isoformat()
        else:
            last_verified_at = self.last_verified_at

        credentials_expire_at: None | str
        if isinstance(self.credentials_expire_at, datetime.datetime):
            credentials_expire_at = self.credentials_expire_at.isoformat()
        else:
            credentials_expire_at = self.credentials_expire_at

        account_label = self.account_label

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description

        config = self.config

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        lifecycle: str | Unset = UNSET
        if not isinstance(self.lifecycle, Unset):
            lifecycle = self.lifecycle.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "user": user,
            "organization": organization,
            "connector_type": connector_type,
            "connector_display_name": connector_display_name,
            "name": name,
            "credentials_configured": credentials_configured,
            "dynamic_inputs": dynamic_inputs,
            "dynamic_input_test_disabled_reason": dynamic_input_test_disabled_reason,
            "auth_config": auth_config,
            "browser_session_expires_at": browser_session_expires_at,
            "health": health,
            "last_verified_at": last_verified_at,
            "credentials_expire_at": credentials_expire_at,
            "account_label": account_label,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if config is not UNSET:
            field_dict["config"] = config
        if status is not UNSET:
            field_dict["status"] = status
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_auth_config import ConnectionAuthConfig
        from ..models.connection_dynamic_inputs import ConnectionDynamicInputs
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

        credentials_configured = d.pop("credentials_configured")

        dynamic_inputs = ConnectionDynamicInputs.from_dict(d.pop("dynamic_inputs"))




        def _parse_dynamic_input_test_disabled_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        dynamic_input_test_disabled_reason = _parse_dynamic_input_test_disabled_reason(d.pop("dynamic_input_test_disabled_reason"))


        auth_config = ConnectionAuthConfig.from_dict(d.pop("auth_config"))




        def _parse_browser_session_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                browser_session_expires_at_type_0 = isoparse(data)



                return browser_session_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        browser_session_expires_at = _parse_browser_session_expires_at(d.pop("browser_session_expires_at"))


        health = HealthEnum(d.pop("health"))




        def _parse_last_verified_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_verified_at_type_0 = isoparse(data)



                return last_verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_verified_at = _parse_last_verified_at(d.pop("last_verified_at"))


        def _parse_credentials_expire_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                credentials_expire_at_type_0 = isoparse(data)



                return credentials_expire_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        credentials_expire_at = _parse_credentials_expire_at(d.pop("credentials_expire_at"))


        account_label = d.pop("account_label")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        description = d.pop("description", UNSET)

        config = d.pop("config", UNSET)

        _status = d.pop("status", UNSET)
        status: StatusEnum | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = StatusEnum(_status)




        _lifecycle = d.pop("lifecycle", UNSET)
        lifecycle: LifecycleEnum | Unset
        if isinstance(_lifecycle,  Unset):
            lifecycle = UNSET
        else:
            lifecycle = LifecycleEnum(_lifecycle)




        connection = cls(
            id=id,
            user=user,
            organization=organization,
            connector_type=connector_type,
            connector_display_name=connector_display_name,
            name=name,
            credentials_configured=credentials_configured,
            dynamic_inputs=dynamic_inputs,
            dynamic_input_test_disabled_reason=dynamic_input_test_disabled_reason,
            auth_config=auth_config,
            browser_session_expires_at=browser_session_expires_at,
            health=health,
            last_verified_at=last_verified_at,
            credentials_expire_at=credentials_expire_at,
            account_label=account_label,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
            config=config,
            status=status,
            lifecycle=lifecycle,
        )


        connection.additional_properties = d
        return connection

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
