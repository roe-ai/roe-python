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
  from ..models.workflow_run_batch_create_request_inputs_item import WorkflowRunBatchCreateRequestInputsItem





T = TypeVar("T", bound="WorkflowRunBatchCreateRequest")



@_attrs_define
class WorkflowRunBatchCreateRequest:
    """ 
        Attributes:
            inputs (list[WorkflowRunBatchCreateRequestInputsItem]): One object of input values per run.
            version_id (UUID | Unset): The version to run. Defaults to the current one.
     """

    inputs: list[WorkflowRunBatchCreateRequestInputsItem]
    version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_run_batch_create_request_inputs_item import WorkflowRunBatchCreateRequestInputsItem
        inputs = []
        for inputs_item_data in self.inputs:
            inputs_item = inputs_item_data.to_dict()
            inputs.append(inputs_item)



        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "inputs": inputs,
        })
        if version_id is not UNSET:
            field_dict["version_id"] = version_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_run_batch_create_request_inputs_item import WorkflowRunBatchCreateRequestInputsItem
        d = dict(src_dict)
        inputs = []
        _inputs = d.pop("inputs")
        for inputs_item_data in (_inputs):
            inputs_item = WorkflowRunBatchCreateRequestInputsItem.from_dict(inputs_item_data)



            inputs.append(inputs_item)


        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id,  Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)




        workflow_run_batch_create_request = cls(
            inputs=inputs,
            version_id=version_id,
        )


        workflow_run_batch_create_request.additional_properties = d
        return workflow_run_batch_create_request

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
