from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FinalizeRequest")



@_attrs_define
class FinalizeRequest:
    """ Body for POST /knowledge-base/<id>/finalize/.

        Attributes:
            name (str | Unset):
            mcp_enabled (bool | Unset):  Default: True.
            public (bool | Unset):  Default: True.
     """

    name: str | Unset = UNSET
    mcp_enabled: bool | Unset = True
    public: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        mcp_enabled = self.mcp_enabled

        public = self.public


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if mcp_enabled is not UNSET:
            field_dict["mcp_enabled"] = mcp_enabled
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        mcp_enabled = d.pop("mcp_enabled", UNSET)

        public = d.pop("public", UNSET)

        finalize_request = cls(
            name=name,
            mcp_enabled=mcp_enabled,
            public=public,
        )


        finalize_request.additional_properties = d
        return finalize_request

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
