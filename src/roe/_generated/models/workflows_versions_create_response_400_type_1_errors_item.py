from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="WorkflowsVersionsCreateResponse400Type1ErrorsItem")



@_attrs_define
class WorkflowsVersionsCreateResponse400Type1ErrorsItem:
    """ 
        Attributes:
            step_id (None | str):
            message (str):
     """

    step_id: None | str
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        step_id: None | str
        step_id = self.step_id

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "step_id": step_id,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_step_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        step_id = _parse_step_id(d.pop("step_id"))


        message = d.pop("message")

        workflows_versions_create_response_400_type_1_errors_item = cls(
            step_id=step_id,
            message=message,
        )


        workflows_versions_create_response_400_type_1_errors_item.additional_properties = d
        return workflows_versions_create_response_400_type_1_errors_item

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
