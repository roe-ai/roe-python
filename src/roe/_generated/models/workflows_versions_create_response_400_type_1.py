from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.workflows_versions_create_response_400_type_1_errors_item import WorkflowsVersionsCreateResponse400Type1ErrorsItem





T = TypeVar("T", bound="WorkflowsVersionsCreateResponse400Type1")



@_attrs_define
class WorkflowsVersionsCreateResponse400Type1:
    """ The definition failed its save checks; each error names its step.

        Attributes:
            detail (str):
            errors (list[WorkflowsVersionsCreateResponse400Type1ErrorsItem]):
     """

    detail: str
    errors: list[WorkflowsVersionsCreateResponse400Type1ErrorsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflows_versions_create_response_400_type_1_errors_item import WorkflowsVersionsCreateResponse400Type1ErrorsItem
        detail = self.detail

        errors = []
        for errors_item_data in self.errors:
            errors_item = errors_item_data.to_dict()
            errors.append(errors_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "detail": detail,
            "errors": errors,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflows_versions_create_response_400_type_1_errors_item import WorkflowsVersionsCreateResponse400Type1ErrorsItem
        d = dict(src_dict)
        detail = d.pop("detail")

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in (_errors):
            errors_item = WorkflowsVersionsCreateResponse400Type1ErrorsItem.from_dict(errors_item_data)



            errors.append(errors_item)


        workflows_versions_create_response_400_type_1 = cls(
            detail=detail,
            errors=errors,
        )


        workflows_versions_create_response_400_type_1.additional_properties = d
        return workflows_versions_create_response_400_type_1

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
