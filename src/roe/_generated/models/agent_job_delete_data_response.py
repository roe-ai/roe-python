from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AgentJobDeleteDataResponse")



@_attrs_define
class AgentJobDeleteDataResponse:
    """ 
        Attributes:
            status (str): Overall status: 'success' or 'partial_success'
            deleted_count (int): Number of input files successfully deleted
            failed_count (int): Number of input files that failed to delete
            blob_sanitized (bool): Whether blob data (outputs, steps, logs, trace) was successfully sanitized
            artifacts_deleted_count (int): Number of workflow artifacts successfully deleted
            artifacts_failed_count (int): Number of workflow artifacts that failed to delete
            errors (list[Any] | Unset): List of errors encountered during deletion
     """

    status: str
    deleted_count: int
    failed_count: int
    blob_sanitized: bool
    artifacts_deleted_count: int
    artifacts_failed_count: int
    errors: list[Any] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status = self.status

        deleted_count = self.deleted_count

        failed_count = self.failed_count

        blob_sanitized = self.blob_sanitized

        artifacts_deleted_count = self.artifacts_deleted_count

        artifacts_failed_count = self.artifacts_failed_count

        errors: list[Any] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "deleted_count": deleted_count,
            "failed_count": failed_count,
            "blob_sanitized": blob_sanitized,
            "artifacts_deleted_count": artifacts_deleted_count,
            "artifacts_failed_count": artifacts_failed_count,
        })
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = d.pop("status")

        deleted_count = d.pop("deleted_count")

        failed_count = d.pop("failed_count")

        blob_sanitized = d.pop("blob_sanitized")

        artifacts_deleted_count = d.pop("artifacts_deleted_count")

        artifacts_failed_count = d.pop("artifacts_failed_count")

        errors = cast(list[Any], d.pop("errors", UNSET))


        agent_job_delete_data_response = cls(
            status=status,
            deleted_count=deleted_count,
            failed_count=failed_count,
            blob_sanitized=blob_sanitized,
            artifacts_deleted_count=artifacts_deleted_count,
            artifacts_failed_count=artifacts_failed_count,
            errors=errors,
        )


        agent_job_delete_data_response.additional_properties = d
        return agent_job_delete_data_response

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
