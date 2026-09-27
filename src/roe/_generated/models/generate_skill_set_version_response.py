from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from uuid import UUID






T = TypeVar("T", bound="GenerateSkillSetVersionResponse")



@_attrs_define
class GenerateSkillSetVersionResponse:
    """ Where to stream the generation run's progress and result.

        Attributes:
            workflow_id (str): Temporal workflow ID for tracking the process
            sse_endpoint (str): SSE endpoint URL for real-time status updates
            run_id (UUID): Identifies this run for reattaching to it or cancelling it.
     """

    workflow_id: str
    sse_endpoint: str
    run_id: UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id

        sse_endpoint = self.sse_endpoint

        run_id = str(self.run_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "workflow_id": workflow_id,
            "sse_endpoint": sse_endpoint,
            "run_id": run_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workflow_id = d.pop("workflow_id")

        sse_endpoint = d.pop("sse_endpoint")

        run_id = UUID(d.pop("run_id"))




        generate_skill_set_version_response = cls(
            workflow_id=workflow_id,
            sse_endpoint=sse_endpoint,
            run_id=run_id,
        )


        generate_skill_set_version_response.additional_properties = d
        return generate_skill_set_version_response

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
