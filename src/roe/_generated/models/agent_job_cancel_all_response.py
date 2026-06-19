from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AgentJobCancelAllResponse")



@_attrs_define
class AgentJobCancelAllResponse:
    """ 
        Attributes:
            task_id (None | str):
            targeted_count (int):
            note (str):
     """

    task_id: None | str
    targeted_count: int
    note: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        task_id: None | str
        task_id = self.task_id

        targeted_count = self.targeted_count

        note = self.note


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "task_id": task_id,
            "targeted_count": targeted_count,
            "note": note,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        task_id = _parse_task_id(d.pop("task_id"))


        targeted_count = d.pop("targeted_count")

        note = d.pop("note")

        agent_job_cancel_all_response = cls(
            task_id=task_id,
            targeted_count=targeted_count,
            note=note,
        )


        agent_job_cancel_all_response.additional_properties = d
        return agent_job_cancel_all_response

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
