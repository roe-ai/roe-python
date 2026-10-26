from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.workflow_run import WorkflowRun





T = TypeVar("T", bound="WorkflowRunBatch")



@_attrs_define
class WorkflowRunBatch:
    """ 
        Attributes:
            runs (list[WorkflowRun]):
     """

    runs: list[WorkflowRun]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_run import WorkflowRun
        runs = []
        for runs_item_data in self.runs:
            runs_item = runs_item_data.to_dict()
            runs.append(runs_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "runs": runs,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_run import WorkflowRun
        d = dict(src_dict)
        runs = []
        _runs = d.pop("runs")
        for runs_item_data in (_runs):
            runs_item = WorkflowRun.from_dict(runs_item_data)



            runs.append(runs_item)


        workflow_run_batch = cls(
            runs=runs,
        )


        workflow_run_batch.additional_properties = d
        return workflow_run_batch

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
