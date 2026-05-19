from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TemporalWorkflow")



@_attrs_define
class TemporalWorkflow:
    """ Serializer for Temporal Workflow engine information.

    Matches the shape returned by fetch_all_temporal_workflows() in
    agents/services/temporal_service.py.

        Attributes:
            type_ (str): Engine type discriminator, always 'temporal_workflow'
            class_id (str): Unique class identifier for this workflow
            workflow_type (str): The temporal workflow type identifier
            display_name (str): Human-readable name of the workflow
            description (str): Detailed description of what the workflow does
            summary (str): Brief summary of the workflow's capabilities
            input_schema (Any): Pydantic JSON Schema describing the workflow's input model
            default_values (Any): Default values for the workflow input fields
            category (str): The workflow category
            form_type (str): The form type that determines which frontend create form to render
     """

    type_: str
    class_id: str
    workflow_type: str
    display_name: str
    description: str
    summary: str
    input_schema: Any
    default_values: Any
    category: str
    form_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        class_id = self.class_id

        workflow_type = self.workflow_type

        display_name = self.display_name

        description = self.description

        summary = self.summary

        input_schema = self.input_schema

        default_values = self.default_values

        category = self.category

        form_type = self.form_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
            "class_id": class_id,
            "workflow_type": workflow_type,
            "display_name": display_name,
            "description": description,
            "summary": summary,
            "input_schema": input_schema,
            "default_values": default_values,
            "category": category,
            "form_type": form_type,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        class_id = d.pop("class_id")

        workflow_type = d.pop("workflow_type")

        display_name = d.pop("display_name")

        description = d.pop("description")

        summary = d.pop("summary")

        input_schema = d.pop("input_schema")

        default_values = d.pop("default_values")

        category = d.pop("category")

        form_type = d.pop("form_type")

        temporal_workflow = cls(
            type_=type_,
            class_id=class_id,
            workflow_type=workflow_type,
            display_name=display_name,
            description=description,
            summary=summary,
            input_schema=input_schema,
            default_values=default_values,
            category=category,
            form_type=form_type,
        )


        temporal_workflow.additional_properties = d
        return temporal_workflow

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
