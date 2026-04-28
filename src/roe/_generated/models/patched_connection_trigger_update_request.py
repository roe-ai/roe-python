from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="PatchedConnectionTriggerUpdateRequest")



@_attrs_define
class PatchedConnectionTriggerUpdateRequest:
    """ Write serializer for updating a connection trigger (enable/disable).

        Attributes:
            enabled (bool | Unset):
            input_key (str | Unset):
     """

    enabled: bool | Unset = UNSET
    input_key: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        input_key = self.input_key


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if input_key is not UNSET:
            field_dict["input_key"] = input_key

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.enabled, Unset):
            files.append(("enabled", (None, str(self.enabled).encode(), "text/plain")))



        if not isinstance(self.input_key, Unset):
            files.append(("input_key", (None, str(self.input_key).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        input_key = d.pop("input_key", UNSET)

        patched_connection_trigger_update_request = cls(
            enabled=enabled,
            input_key=input_key,
        )


        patched_connection_trigger_update_request.additional_properties = d
        return patched_connection_trigger_update_request

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
