from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.connector_type_enum import ConnectorTypeEnum
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.test_connection_credentials_request_auth_config import TestConnectionCredentialsRequestAuthConfig
  from ..models.test_connection_credentials_request_config import TestConnectionCredentialsRequestConfig
  from ..models.test_connection_credentials_request_dynamic_inputs import TestConnectionCredentialsRequestDynamicInputs





T = TypeVar("T", bound="TestConnectionCredentialsRequest")



@_attrs_define
class TestConnectionCredentialsRequest:
    """ Serializer for testing connector credentials without saving a connection.

        Attributes:
            connector_type (ConnectorTypeEnum): * `snowflake` - SNOWFLAKE
                * `s3` - S3
                * `sharepoint` - SHAREPOINT
                * `zendesk` - ZENDESK
                * `google_drive` - GOOGLE_DRIVE
                * `google_docs` - GOOGLE_DOCS
                * `google_sheets` - GOOGLE_SHEETS
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
            config (TestConnectionCredentialsRequestConfig):
            auth_config (TestConnectionCredentialsRequestAuthConfig | Unset):
            dynamic_inputs (TestConnectionCredentialsRequestDynamicInputs | Unset):
     """

    connector_type: ConnectorTypeEnum
    config: TestConnectionCredentialsRequestConfig
    auth_config: TestConnectionCredentialsRequestAuthConfig | Unset = UNSET
    dynamic_inputs: TestConnectionCredentialsRequestDynamicInputs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.test_connection_credentials_request_auth_config import TestConnectionCredentialsRequestAuthConfig
        from ..models.test_connection_credentials_request_config import TestConnectionCredentialsRequestConfig
        from ..models.test_connection_credentials_request_dynamic_inputs import TestConnectionCredentialsRequestDynamicInputs
        connector_type = self.connector_type.value

        config = self.config.to_dict()

        auth_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_config, Unset):
            auth_config = self.auth_config.to_dict()

        dynamic_inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_inputs, Unset):
            dynamic_inputs = self.dynamic_inputs.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "connector_type": connector_type,
            "config": config,
        })
        if auth_config is not UNSET:
            field_dict["auth_config"] = auth_config
        if dynamic_inputs is not UNSET:
            field_dict["dynamic_inputs"] = dynamic_inputs

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_connection_credentials_request_auth_config import TestConnectionCredentialsRequestAuthConfig
        from ..models.test_connection_credentials_request_config import TestConnectionCredentialsRequestConfig
        from ..models.test_connection_credentials_request_dynamic_inputs import TestConnectionCredentialsRequestDynamicInputs
        d = dict(src_dict)
        connector_type = ConnectorTypeEnum(d.pop("connector_type"))




        config = TestConnectionCredentialsRequestConfig.from_dict(d.pop("config"))




        _auth_config = d.pop("auth_config", UNSET)
        auth_config: TestConnectionCredentialsRequestAuthConfig | Unset
        if isinstance(_auth_config,  Unset):
            auth_config = UNSET
        else:
            auth_config = TestConnectionCredentialsRequestAuthConfig.from_dict(_auth_config)




        _dynamic_inputs = d.pop("dynamic_inputs", UNSET)
        dynamic_inputs: TestConnectionCredentialsRequestDynamicInputs | Unset
        if isinstance(_dynamic_inputs,  Unset):
            dynamic_inputs = UNSET
        else:
            dynamic_inputs = TestConnectionCredentialsRequestDynamicInputs.from_dict(_dynamic_inputs)




        test_connection_credentials_request = cls(
            connector_type=connector_type,
            config=config,
            auth_config=auth_config,
            dynamic_inputs=dynamic_inputs,
        )


        test_connection_credentials_request.additional_properties = d
        return test_connection_credentials_request

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
