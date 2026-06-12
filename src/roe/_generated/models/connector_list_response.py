from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.connector_metadata import ConnectorMetadata





T = TypeVar("T", bound="ConnectorListResponse")



@_attrs_define
class ConnectorListResponse:
    """ 
        Attributes:
            connectors (list[ConnectorMetadata]):
     """

    connectors: list[ConnectorMetadata]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.connector_metadata import ConnectorMetadata
        connectors = []
        for connectors_item_data in self.connectors:
            connectors_item = connectors_item_data.to_dict()
            connectors.append(connectors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "connectors": connectors,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_metadata import ConnectorMetadata
        d = dict(src_dict)
        connectors = []
        _connectors = d.pop("connectors")
        for connectors_item_data in (_connectors):
            connectors_item = ConnectorMetadata.from_dict(connectors_item_data)



            connectors.append(connectors_item)


        connector_list_response = cls(
            connectors=connectors,
        )


        connector_list_response.additional_properties = d
        return connector_list_response

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
