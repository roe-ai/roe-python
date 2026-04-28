from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.agent_job_evaluation_item_request import AgentJobEvaluationItemRequest





T = TypeVar("T", bound="BulkAgentJobEvaluationRequest")



@_attrs_define
class BulkAgentJobEvaluationRequest:
    """ Serializer for bulk agent job evaluation operations.

        Attributes:
            evaluations (list[AgentJobEvaluationItemRequest]):
            failed_job_ids (list[UUID] | Unset):
     """

    evaluations: list[AgentJobEvaluationItemRequest]
    failed_job_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_job_evaluation_item_request import AgentJobEvaluationItemRequest
        evaluations = []
        for evaluations_item_data in self.evaluations:
            evaluations_item = evaluations_item_data.to_dict()
            evaluations.append(evaluations_item)



        failed_job_ids: list[str] | Unset = UNSET
        if not isinstance(self.failed_job_ids, Unset):
            failed_job_ids = []
            for failed_job_ids_item_data in self.failed_job_ids:
                failed_job_ids_item = str(failed_job_ids_item_data)
                failed_job_ids.append(failed_job_ids_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "evaluations": evaluations,
        })
        if failed_job_ids is not UNSET:
            field_dict["failed_job_ids"] = failed_job_ids

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        from ..models.agent_job_evaluation_item_request import AgentJobEvaluationItemRequest
        files: types.RequestFiles = []

        for evaluations_item_element in self.evaluations:
            files.append(("evaluations", (None, json.dumps( evaluations_item_element.to_dict()).encode(), "application/json")))




        if not isinstance(self.failed_job_ids, Unset):
            for failed_job_ids_item_element in self.failed_job_ids:
                files.append(("failed_job_ids", (None, str(failed_job_ids_item_element), "text/plain")))





        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_job_evaluation_item_request import AgentJobEvaluationItemRequest
        d = dict(src_dict)
        evaluations = []
        _evaluations = d.pop("evaluations")
        for evaluations_item_data in (_evaluations):
            evaluations_item = AgentJobEvaluationItemRequest.from_dict(evaluations_item_data)



            evaluations.append(evaluations_item)


        _failed_job_ids = d.pop("failed_job_ids", UNSET)
        failed_job_ids: list[UUID] | Unset = UNSET
        if _failed_job_ids is not UNSET:
            failed_job_ids = []
            for failed_job_ids_item_data in _failed_job_ids:
                failed_job_ids_item = UUID(failed_job_ids_item_data)



                failed_job_ids.append(failed_job_ids_item)


        bulk_agent_job_evaluation_request = cls(
            evaluations=evaluations,
            failed_job_ids=failed_job_ids,
        )


        bulk_agent_job_evaluation_request.additional_properties = d
        return bulk_agent_job_evaluation_request

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
