from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="ConnectorMetadata")



@_attrs_define
class ConnectorMetadata:
    """ Serializer for connector metadata.

        Attributes:
            id (str):
            display_name (str):
            description (str):
            icon (str):
            category (str):
            config_schema (Any):
            auth_schema (Any):
            supports_delivery (bool):
            delivery_config_schema (Any | None):
     """

    id: str
    display_name: str
    description: str
    icon: str
    category: str
    config_schema: Any
    auth_schema: Any
    supports_delivery: bool
    delivery_config_schema: Any | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        description = self.description

        icon = self.icon

        category = self.category

        config_schema = self.config_schema

        auth_schema = self.auth_schema

        supports_delivery = self.supports_delivery

        delivery_config_schema: Any | None
        delivery_config_schema = self.delivery_config_schema


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "display_name": display_name,
            "description": description,
            "icon": icon,
            "category": category,
            "config_schema": config_schema,
            "auth_schema": auth_schema,
            "supports_delivery": supports_delivery,
            "delivery_config_schema": delivery_config_schema,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        display_name = d.pop("display_name")

        description = d.pop("description")

        icon = d.pop("icon")

        category = d.pop("category")

        config_schema = d.pop("config_schema")

        auth_schema = d.pop("auth_schema")

        supports_delivery = d.pop("supports_delivery")

        def _parse_delivery_config_schema(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        delivery_config_schema = _parse_delivery_config_schema(d.pop("delivery_config_schema"))


        connector_metadata = cls(
            id=id,
            display_name=display_name,
            description=description,
            icon=icon,
            category=category,
            config_schema=config_schema,
            auth_schema=auth_schema,
            supports_delivery=supports_delivery,
            delivery_config_schema=delivery_config_schema,
        )


        connector_metadata.additional_properties = d
        return connector_metadata

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
