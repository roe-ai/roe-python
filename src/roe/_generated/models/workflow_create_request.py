from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_definition_request import WorkflowDefinitionRequest





T = TypeVar("T", bound="WorkflowCreateRequest")



@_attrs_define
class WorkflowCreateRequest:
    """ 
        Attributes:
            name (str):
            definition (WorkflowDefinitionRequest):
            version_name (str | Unset):
            description (str | Unset):
     """

    name: str
    definition: WorkflowDefinitionRequest
    version_name: str | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_definition_request import WorkflowDefinitionRequest
        name = self.name

        definition = self.definition.to_dict()

        version_name = self.version_name

        description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "definition": definition,
        })
        if version_name is not UNSET:
            field_dict["version_name"] = version_name
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_definition_request import WorkflowDefinitionRequest
        d = dict(src_dict)
        name = d.pop("name")

        definition = WorkflowDefinitionRequest.from_dict(d.pop("definition"))




        version_name = d.pop("version_name", UNSET)

        description = d.pop("description", UNSET)

        workflow_create_request = cls(
            name=name,
            definition=definition,
            version_name=version_name,
            description=description,
        )


        workflow_create_request.additional_properties = d
        return workflow_create_request

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
