from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="SkillSetGenerationRun")



@_attrs_define
class SkillSetGenerationRun:
    """ A generation already in flight, so a page can reattach to it.

        Attributes:
            workflow_id (str): Temporal workflow ID for tracking the process
            sse_endpoint (str): SSE endpoint URL for real-time status updates
            id (UUID):
            status (str): building, succeeded, or failed.
            started_at (datetime.datetime): When the run started — the UI shows elapsed time from this.
     """

    workflow_id: str
    sse_endpoint: str
    id: UUID
    status: str
    started_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        workflow_id = self.workflow_id

        sse_endpoint = self.sse_endpoint

        id = str(self.id)

        status = self.status

        started_at = self.started_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "workflow_id": workflow_id,
            "sse_endpoint": sse_endpoint,
            "id": id,
            "status": status,
            "started_at": started_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        workflow_id = d.pop("workflow_id")

        sse_endpoint = d.pop("sse_endpoint")

        id = UUID(d.pop("id"))




        status = d.pop("status")

        started_at = isoparse(d.pop("started_at"))




        skill_set_generation_run = cls(
            workflow_id=workflow_id,
            sse_endpoint=sse_endpoint,
            id=id,
            status=status,
            started_at=started_at,
        )


        skill_set_generation_run.additional_properties = d
        return skill_set_generation_run

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
