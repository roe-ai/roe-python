from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connector_type_enum import ConnectorTypeEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.create_connection_request_auth_config import CreateConnectionRequestAuthConfig
  from ..models.create_connection_request_config import CreateConnectionRequestConfig





T = TypeVar("T", bound="CreateConnectionRequest")



@_attrs_define
class CreateConnectionRequest:
    """ Serializer for creating connections.
    Accepts full config, splits into config (DB) and auth (Secrets Manager).

        Attributes:
            connector_type (ConnectorTypeEnum): * `snowflake` - SNOWFLAKE
                * `s3` - S3
                * `sharepoint` - SHAREPOINT
                * `zendesk` - ZENDESK
                * `google_drive` - GOOGLE_DRIVE
                * `salesforce` - SALESFORCE
                * `web_application` - WEB_APPLICATION
                * `custom_api` - CUSTOM_API
                * `lexis_nexis` - LEXIS_NEXIS
                * `sardine` - SARDINE
                * `intercom` - INTERCOM
                * `stripe` - STRIPE
                * `plaid` - PLAID
                * `checkout_com` - CHECKOUT_COM
                * `socure` - SOCURE
                * `custom_mcp` - CUSTOM_MCP
            name (str):
            config (CreateConnectionRequestConfig):
            description (str | Unset):
            auth_config (CreateConnectionRequestAuthConfig | Unset):
            organization_id (None | Unset | UUID):
     """

    connector_type: ConnectorTypeEnum
    name: str
    config: CreateConnectionRequestConfig
    description: str | Unset = UNSET
    auth_config: CreateConnectionRequestAuthConfig | Unset = UNSET
    organization_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_connection_request_auth_config import CreateConnectionRequestAuthConfig
        from ..models.create_connection_request_config import CreateConnectionRequestConfig
        connector_type = self.connector_type.value

        name = self.name

        config = self.config.to_dict()

        description = self.description

        auth_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_config, Unset):
            auth_config = self.auth_config.to_dict()

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "connector_type": connector_type,
            "name": name,
            "config": config,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if auth_config is not UNSET:
            field_dict["auth_config"] = auth_config
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_connection_request_auth_config import CreateConnectionRequestAuthConfig
        from ..models.create_connection_request_config import CreateConnectionRequestConfig
        d = dict(src_dict)
        connector_type = ConnectorTypeEnum(d.pop("connector_type"))




        name = d.pop("name")

        config = CreateConnectionRequestConfig.from_dict(d.pop("config"))




        description = d.pop("description", UNSET)

        _auth_config = d.pop("auth_config", UNSET)
        auth_config: CreateConnectionRequestAuthConfig | Unset
        if isinstance(_auth_config,  Unset):
            auth_config = UNSET
        else:
            auth_config = CreateConnectionRequestAuthConfig.from_dict(_auth_config)




        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)



                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))


        create_connection_request = cls(
            connector_type=connector_type,
            name=name,
            config=config,
            description=description,
            auth_config=auth_config,
            organization_id=organization_id,
        )


        create_connection_request.additional_properties = d
        return create_connection_request

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
