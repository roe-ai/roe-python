from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.workflow_run_status_enum import WorkflowRunStatusEnum
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.step_run import StepRun





T = TypeVar("T", bound="WorkflowRunDetail")



@_attrs_define
class WorkflowRunDetail:
    """ 
        Attributes:
            id (UUID):
            workflow_id (UUID):
            version_id (None | UUID):
            status (WorkflowRunStatusEnum): * `pending` - pending
                * `running` - running
                * `succeeded` - succeeded
                * `failed` - failed
                * `cancelled` - cancelled
            error_message (None | str):
            created_at (datetime.datetime):
            inputs (Any):
            outputs (list[Any] | None): The result step's output, once the run has finished.
            steps (list[StepRun]):
     """

    id: UUID
    workflow_id: UUID
    version_id: None | UUID
    status: WorkflowRunStatusEnum
    error_message: None | str
    created_at: datetime.datetime
    inputs: Any
    outputs: list[Any] | None
    steps: list[StepRun]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.step_run import StepRun
        id = str(self.id)

        workflow_id = str(self.workflow_id)

        version_id: None | str
        if isinstance(self.version_id, UUID):
            version_id = str(self.version_id)
        else:
            version_id = self.version_id

        status = self.status.value

        error_message: None | str
        error_message = self.error_message

        created_at = self.created_at.isoformat()

        inputs = self.inputs

        outputs: list[Any] | None
        if isinstance(self.outputs, list):
            outputs = self.outputs


        else:
            outputs = self.outputs

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "workflow_id": workflow_id,
            "version_id": version_id,
            "status": status,
            "error_message": error_message,
            "created_at": created_at,
            "inputs": inputs,
            "outputs": outputs,
            "steps": steps,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_run import StepRun
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        workflow_id = UUID(d.pop("workflow_id"))




        def _parse_version_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                version_id_type_0 = UUID(data)



                return version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        version_id = _parse_version_id(d.pop("version_id"))


        status = WorkflowRunStatusEnum(d.pop("status"))




        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("error_message"))


        created_at = isoparse(d.pop("created_at"))




        inputs = d.pop("inputs")

        def _parse_outputs(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                outputs_type_0 = cast(list[Any], data)

                return outputs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        outputs = _parse_outputs(d.pop("outputs"))


        steps = []
        _steps = d.pop("steps")
        for steps_item_data in (_steps):
            steps_item = StepRun.from_dict(steps_item_data)



            steps.append(steps_item)


        workflow_run_detail = cls(
            id=id,
            workflow_id=workflow_id,
            version_id=version_id,
            status=status,
            error_message=error_message,
            created_at=created_at,
            inputs=inputs,
            outputs=outputs,
            steps=steps,
        )


        workflow_run_detail.additional_properties = d
        return workflow_run_detail

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
