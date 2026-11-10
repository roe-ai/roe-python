from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.lifecycle_enum import LifecycleEnum
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_connection_request_auth_config import UpdateConnectionRequestAuthConfig
  from ..models.update_connection_request_config import UpdateConnectionRequestConfig
  from ..models.update_connection_request_dynamic_inputs import UpdateConnectionRequestDynamicInputs





T = TypeVar("T", bound="UpdateConnectionRequest")



@_attrs_define
class UpdateConnectionRequest:
    """ Serializer for updating connections.

    Cross-state Pydantic validation (config + auth) lives in
    ``connections.services.connection.update_connection_with_secrets``. That
    path is the single source of truth for canonical validation + write,
    mirrors the create path's ``create_connection_with_secrets``, AND correctly
    handles the SM-fetch-failure case for the unchanged-auth branch
    (returns 502 / opportunistic backfill instead of silently corrupting
    the fingerprint by hashing ``{}``). Re-running the same validation
    here would (a) double the work, (b) bypass the SM-failure semantics,
    and (c) leak Pydantic field/value details through DRF's generic 400
    handler. The serializer only does shape checks.

        Attributes:
            name (str | Unset):
            description (str | Unset):
            config (UpdateConnectionRequestConfig | Unset):
            auth_config (UpdateConnectionRequestAuthConfig | Unset):
            dynamic_inputs (UpdateConnectionRequestDynamicInputs | Unset):
            lifecycle (LifecycleEnum | Unset): * `active` - Active
                * `archived` - Archived
                * `disconnected` - Disconnected
            confirm_in_use (bool | Unset): Save a config change that alters calls for agents or webhooks that already use
                the connection.
     """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    config: UpdateConnectionRequestConfig | Unset = UNSET
    auth_config: UpdateConnectionRequestAuthConfig | Unset = UNSET
    dynamic_inputs: UpdateConnectionRequestDynamicInputs | Unset = UNSET
    lifecycle: LifecycleEnum | Unset = UNSET
    confirm_in_use: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_connection_request_auth_config import UpdateConnectionRequestAuthConfig
        from ..models.update_connection_request_config import UpdateConnectionRequestConfig
        from ..models.update_connection_request_dynamic_inputs import UpdateConnectionRequestDynamicInputs
        name = self.name

        description = self.description

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        auth_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_config, Unset):
            auth_config = self.auth_config.to_dict()

        dynamic_inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic_inputs, Unset):
            dynamic_inputs = self.dynamic_inputs.to_dict()

        lifecycle: str | Unset = UNSET
        if not isinstance(self.lifecycle, Unset):
            lifecycle = self.lifecycle.value


        confirm_in_use = self.confirm_in_use


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if config is not UNSET:
            field_dict["config"] = config
        if auth_config is not UNSET:
            field_dict["auth_config"] = auth_config
        if dynamic_inputs is not UNSET:
            field_dict["dynamic_inputs"] = dynamic_inputs
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if confirm_in_use is not UNSET:
            field_dict["confirm_in_use"] = confirm_in_use

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_connection_request_auth_config import UpdateConnectionRequestAuthConfig
        from ..models.update_connection_request_config import UpdateConnectionRequestConfig
        from ..models.update_connection_request_dynamic_inputs import UpdateConnectionRequestDynamicInputs
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _config = d.pop("config", UNSET)
        config: UpdateConnectionRequestConfig | Unset
        if isinstance(_config,  Unset):
            config = UNSET
        else:
            config = UpdateConnectionRequestConfig.from_dict(_config)




        _auth_config = d.pop("auth_config", UNSET)
        auth_config: UpdateConnectionRequestAuthConfig | Unset
        if isinstance(_auth_config,  Unset):
            auth_config = UNSET
        else:
            auth_config = UpdateConnectionRequestAuthConfig.from_dict(_auth_config)




        _dynamic_inputs = d.pop("dynamic_inputs", UNSET)
        dynamic_inputs: UpdateConnectionRequestDynamicInputs | Unset
        if isinstance(_dynamic_inputs,  Unset):
            dynamic_inputs = UNSET
        else:
            dynamic_inputs = UpdateConnectionRequestDynamicInputs.from_dict(_dynamic_inputs)




        _lifecycle = d.pop("lifecycle", UNSET)
        lifecycle: LifecycleEnum | Unset
        if isinstance(_lifecycle,  Unset):
            lifecycle = UNSET
        else:
            lifecycle = LifecycleEnum(_lifecycle)




        confirm_in_use = d.pop("confirm_in_use", UNSET)

        update_connection_request = cls(
            name=name,
            description=description,
            config=config,
            auth_config=auth_config,
            dynamic_inputs=dynamic_inputs,
            lifecycle=lifecycle,
            confirm_in_use=confirm_in_use,
        )


        update_connection_request.additional_properties = d
        return update_connection_request

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
