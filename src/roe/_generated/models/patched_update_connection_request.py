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

if TYPE_CHECKING:
  from ..models.patched_update_connection_request_auth_config import PatchedUpdateConnectionRequestAuthConfig
  from ..models.patched_update_connection_request_config import PatchedUpdateConnectionRequestConfig





T = TypeVar("T", bound="PatchedUpdateConnectionRequest")



@_attrs_define
class PatchedUpdateConnectionRequest:
    """ Serializer for updating connections.

        Attributes:
            name (str | Unset):
            description (str | Unset):
            config (PatchedUpdateConnectionRequestConfig | Unset):
            auth_config (PatchedUpdateConnectionRequestAuthConfig | Unset):
     """

    name: str | Unset = UNSET
    description: str | Unset = UNSET
    config: PatchedUpdateConnectionRequestConfig | Unset = UNSET
    auth_config: PatchedUpdateConnectionRequestAuthConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.patched_update_connection_request_auth_config import PatchedUpdateConnectionRequestAuthConfig
        from ..models.patched_update_connection_request_config import PatchedUpdateConnectionRequestConfig
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


    def to_multipart(self) -> types.RequestFiles:
        from ..models.patched_update_connection_request_auth_config import PatchedUpdateConnectionRequestAuthConfig
        from ..models.patched_update_connection_request_config import PatchedUpdateConnectionRequestConfig
        files: types.RequestFiles = []

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))



        if not isinstance(self.description, Unset):
            files.append(("description", (None, str(self.description).encode(), "text/plain")))



        if not isinstance(self.config, Unset):
            files.append(("config", (None, json.dumps( self.config.to_dict()).encode(), "application/json")))



        if not isinstance(self.auth_config, Unset):
            files.append(("auth_config", (None, json.dumps( self.auth_config.to_dict()).encode(), "application/json")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patched_update_connection_request_auth_config import PatchedUpdateConnectionRequestAuthConfig
        from ..models.patched_update_connection_request_config import PatchedUpdateConnectionRequestConfig
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _config = d.pop("config", UNSET)
        config: PatchedUpdateConnectionRequestConfig | Unset
        if isinstance(_config,  Unset):
            config = UNSET
        else:
            config = PatchedUpdateConnectionRequestConfig.from_dict(_config)




        _auth_config = d.pop("auth_config", UNSET)
        auth_config: PatchedUpdateConnectionRequestAuthConfig | Unset
        if isinstance(_auth_config,  Unset):
            auth_config = UNSET
        else:
            auth_config = PatchedUpdateConnectionRequestAuthConfig.from_dict(_auth_config)




        patched_update_connection_request = cls(
            name=name,
            description=description,
            config=config,
            auth_config=auth_config,
        )


        patched_update_connection_request.additional_properties = d
        return patched_update_connection_request

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
