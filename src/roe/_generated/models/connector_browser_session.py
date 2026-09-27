from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.connector_browser_session_required_config import ConnectorBrowserSessionRequiredConfig





T = TypeVar("T", bound="ConnectorBrowserSession")



@_attrs_define
class ConnectorBrowserSession:
    """ 
        Attributes:
            field (str): Auth field the capture button sits beside.
            required_config (ConnectorBrowserSessionRequiredConfig): Config values required before signing in.
     """

    field: str
    required_config: ConnectorBrowserSessionRequiredConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.connector_browser_session_required_config import ConnectorBrowserSessionRequiredConfig
        field = self.field

        required_config = self.required_config.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "field": field,
            "required_config": required_config,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_browser_session_required_config import ConnectorBrowserSessionRequiredConfig
        d = dict(src_dict)
        field = d.pop("field")

        required_config = ConnectorBrowserSessionRequiredConfig.from_dict(d.pop("required_config"))




        connector_browser_session = cls(
            field=field,
            required_config=required_config,
        )


        connector_browser_session.additional_properties = d
        return connector_browser_session

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
