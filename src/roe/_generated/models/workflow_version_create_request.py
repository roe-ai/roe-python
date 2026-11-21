from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.workflow_definition_request import WorkflowDefinitionRequest





T = TypeVar("T", bound="WorkflowVersionCreateRequest")



@_attrs_define
class WorkflowVersionCreateRequest:
    """ 
        Attributes:
            definition (WorkflowDefinitionRequest):
            version_name (str | Unset):
            description (str | Unset):
            base_version_id (None | Unset | UUID): The version this definition was made from. When given, the save is
                refused if another version has become current since, so an older definition doesn't replace newer changes.
     """

    definition: WorkflowDefinitionRequest
    version_name: str | Unset = UNSET
    description: str | Unset = UNSET
    base_version_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_definition_request import WorkflowDefinitionRequest
        definition = self.definition.to_dict()

        version_name = self.version_name

        description = self.description

        base_version_id: None | str | Unset
        if isinstance(self.base_version_id, Unset):
            base_version_id = UNSET
        elif isinstance(self.base_version_id, UUID):
            base_version_id = str(self.base_version_id)
        else:
            base_version_id = self.base_version_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "definition": definition,
        })
        if version_name is not UNSET:
            field_dict["version_name"] = version_name
        if description is not UNSET:
            field_dict["description"] = description
        if base_version_id is not UNSET:
            field_dict["base_version_id"] = base_version_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_definition_request import WorkflowDefinitionRequest
        d = dict(src_dict)
        definition = WorkflowDefinitionRequest.from_dict(d.pop("definition"))




        version_name = d.pop("version_name", UNSET)

        description = d.pop("description", UNSET)

        def _parse_base_version_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                base_version_id_type_0 = UUID(data)



                return base_version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        base_version_id = _parse_base_version_id(d.pop("base_version_id", UNSET))


        workflow_version_create_request = cls(
            definition=definition,
            version_name=version_name,
            description=description,
            base_version_id=base_version_id,
        )


        workflow_version_create_request.additional_properties = d
        return workflow_version_create_request

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
