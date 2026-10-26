from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.workflow_definition import WorkflowDefinition





T = TypeVar("T", bound="WorkflowVersionDetail")



@_attrs_define
class WorkflowVersionDetail:
    """ 
        Attributes:
            id (UUID):
            workflow_id (UUID):
            is_current (bool):
            read_only (bool): Saved in the old graph format: it still runs, but can only be edited by saving a new version.
            definition (None | WorkflowDefinition): The steps, in the block format. Null for a read-only version.
            conversion_reasons (list[str]): Why a read-only version couldn't be converted to the block format.
            version_name (None | str | Unset):
            description (None | str | Unset):
            format_version (int | Unset):
            created_at (datetime.datetime | Unset):
            input_definitions (Any | Unset):
     """

    id: UUID
    workflow_id: UUID
    is_current: bool
    read_only: bool
    definition: None | WorkflowDefinition
    conversion_reasons: list[str]
    version_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    format_version: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    input_definitions: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_definition import WorkflowDefinition
        id = str(self.id)

        workflow_id = str(self.workflow_id)

        is_current = self.is_current

        read_only = self.read_only

        definition: dict[str, Any] | None
        if isinstance(self.definition, WorkflowDefinition):
            definition = self.definition.to_dict()
        else:
            definition = self.definition

        conversion_reasons = self.conversion_reasons



        version_name: None | str | Unset
        if isinstance(self.version_name, Unset):
            version_name = UNSET
        else:
            version_name = self.version_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        format_version = self.format_version

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        input_definitions = self.input_definitions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "workflow_id": workflow_id,
            "is_current": is_current,
            "read_only": read_only,
            "definition": definition,
            "conversion_reasons": conversion_reasons,
        })
        if version_name is not UNSET:
            field_dict["version_name"] = version_name
        if description is not UNSET:
            field_dict["description"] = description
        if format_version is not UNSET:
            field_dict["format_version"] = format_version
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if input_definitions is not UNSET:
            field_dict["input_definitions"] = input_definitions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_definition import WorkflowDefinition
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        workflow_id = UUID(d.pop("workflow_id"))




        is_current = d.pop("is_current")

        read_only = d.pop("read_only")

        def _parse_definition(data: object) -> None | WorkflowDefinition:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                definition_type_0 = WorkflowDefinition.from_dict(data)



                return definition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | WorkflowDefinition, data)

        definition = _parse_definition(d.pop("definition"))


        conversion_reasons = cast(list[str], d.pop("conversion_reasons"))


        def _parse_version_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version_name = _parse_version_name(d.pop("version_name", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        format_version = d.pop("format_version", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        input_definitions = d.pop("input_definitions", UNSET)

        workflow_version_detail = cls(
            id=id,
            workflow_id=workflow_id,
            is_current=is_current,
            read_only=read_only,
            definition=definition,
            conversion_reasons=conversion_reasons,
            version_name=version_name,
            description=description,
            format_version=format_version,
            created_at=created_at,
            input_definitions=input_definitions,
        )


        workflow_version_detail.additional_properties = d
        return workflow_version_detail

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
