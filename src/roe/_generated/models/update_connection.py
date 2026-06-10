from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_connection_auth_config import UpdateConnectionAuthConfig
  from ..models.update_connection_config import UpdateConnectionConfig





T = TypeVar("T", bound="UpdateConnection")



@_attrs_define
class UpdateConnection:
    """ Serializer for updating connections.

    Cross-state Pydantic validation (config + auth) lives in the view's
    ``update()`` method now -- see ``connections.views.
    ConnectionRetrieveUpdateDestroyView.update``. That path is the single
    source of truth for canonical validation + write, mirrors the create
    path's ``service.create_connection_with_secrets``, AND correctly
    handles the SM-fetch-failure case for the unchanged-auth branch
    (returns 502 / opportunistic backfill instead of silently corrupting
    the fingerprint by hashing ``{}``). Re-running the same validation
    here would (a) double the work, (b) bypass the SM-failure semantics,
    and (c) leak Pydantic field/value details through DRF's generic 400
    handler. The serializer only does shape checks.

        Attributes:
            name (str | Unset):
            description (str | Unset):
            config (UpdateConnectionConfig | Unset):
            auth_config (UpdateConnectionAuthConfig | Unset):
     """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    config: UpdateConnectionConfig | Unset = UNSET
    auth_config: UpdateConnectionAuthConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_connection_auth_config import UpdateConnectionAuthConfig
        from ..models.update_connection_config import UpdateConnectionConfig
        name = self.name

        description = self.description

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        auth_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth_config, Unset):
            auth_config = self.auth_config.to_dict()


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

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_connection_auth_config import UpdateConnectionAuthConfig
        from ..models.update_connection_config import UpdateConnectionConfig
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _config = d.pop("config", UNSET)
        config: UpdateConnectionConfig | Unset
        if isinstance(_config,  Unset):
            config = UNSET
        else:
            config = UpdateConnectionConfig.from_dict(_config)




        _auth_config = d.pop("auth_config", UNSET)
        auth_config: UpdateConnectionAuthConfig | Unset
        if isinstance(_auth_config,  Unset):
            auth_config = UNSET
        else:
            auth_config = UpdateConnectionAuthConfig.from_dict(_auth_config)




        update_connection = cls(
            name=name,
            description=description,
            config=config,
            auth_config=auth_config,
        )


        update_connection.additional_properties = d
        return update_connection

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
