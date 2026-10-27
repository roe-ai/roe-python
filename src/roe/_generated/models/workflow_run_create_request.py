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
  from ..models.workflow_run_create_request_inputs import WorkflowRunCreateRequestInputs
  from ..models.workflow_run_create_request_metadata import WorkflowRunCreateRequestMetadata





T = TypeVar("T", bound="WorkflowRunCreateRequest")



@_attrs_define
class WorkflowRunCreateRequest:
    """ 
        Attributes:
            inputs (WorkflowRunCreateRequestInputs | Unset): Values for the workflow's inputs, keyed by input. A file input
                takes a file id or URL, or the file itself in a multipart request.
            version_id (UUID | Unset): The version to run. Defaults to the current one.
            metadata (WorkflowRunCreateRequestMetadata | Unset):
            wait (bool | Unset): Wait up to 60 seconds for the run to finish, then return it as it stands. Default: False.
     """

    inputs: WorkflowRunCreateRequestInputs | Unset = UNSET
    version_id: UUID | Unset = UNSET
    metadata: WorkflowRunCreateRequestMetadata | Unset = UNSET
    wait: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.workflow_run_create_request_inputs import WorkflowRunCreateRequestInputs
        from ..models.workflow_run_create_request_metadata import WorkflowRunCreateRequestMetadata
        inputs: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = self.inputs.to_dict()

        version_id: str | Unset = UNSET
        if not isinstance(self.version_id, Unset):
            version_id = str(self.version_id)

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        wait = self.wait


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if version_id is not UNSET:
            field_dict["version_id"] = version_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if wait is not UNSET:
            field_dict["wait"] = wait

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_run_create_request_inputs import WorkflowRunCreateRequestInputs
        from ..models.workflow_run_create_request_metadata import WorkflowRunCreateRequestMetadata
        d = dict(src_dict)
        _inputs = d.pop("inputs", UNSET)
        inputs: WorkflowRunCreateRequestInputs | Unset
        if isinstance(_inputs,  Unset):
            inputs = UNSET
        else:
            inputs = WorkflowRunCreateRequestInputs.from_dict(_inputs)




        _version_id = d.pop("version_id", UNSET)
        version_id: UUID | Unset
        if isinstance(_version_id,  Unset):
            version_id = UNSET
        else:
            version_id = UUID(_version_id)




        _metadata = d.pop("metadata", UNSET)
        metadata: WorkflowRunCreateRequestMetadata | Unset
        if isinstance(_metadata,  Unset):
            metadata = UNSET
        else:
            metadata = WorkflowRunCreateRequestMetadata.from_dict(_metadata)




        wait = d.pop("wait", UNSET)

        workflow_run_create_request = cls(
            inputs=inputs,
            version_id=version_id,
            metadata=metadata,
            wait=wait,
        )


        workflow_run_create_request.additional_properties = d
        return workflow_run_create_request

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
