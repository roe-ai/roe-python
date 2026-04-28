from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="BulkAgentJobEvaluations2Response200")



@_attrs_define
class BulkAgentJobEvaluations2Response200:
    """ 
        Attributes:
            successful_job_ids (list[UUID] | Unset):
            failed_job_ids (list[UUID] | Unset):
     """

    successful_job_ids: list[UUID] | Unset = UNSET
    failed_job_ids: list[UUID] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        successful_job_ids: list[str] | Unset = UNSET
        if not isinstance(self.successful_job_ids, Unset):
            successful_job_ids = []
            for successful_job_ids_item_data in self.successful_job_ids:
                successful_job_ids_item = str(successful_job_ids_item_data)
                successful_job_ids.append(successful_job_ids_item)



        failed_job_ids: list[str] | Unset = UNSET
        if not isinstance(self.failed_job_ids, Unset):
            failed_job_ids = []
            for failed_job_ids_item_data in self.failed_job_ids:
                failed_job_ids_item = str(failed_job_ids_item_data)
                failed_job_ids.append(failed_job_ids_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if successful_job_ids is not UNSET:
            field_dict["successful_job_ids"] = successful_job_ids
        if failed_job_ids is not UNSET:
            field_dict["failed_job_ids"] = failed_job_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _successful_job_ids = d.pop("successful_job_ids", UNSET)
        successful_job_ids: list[UUID] | Unset = UNSET
        if _successful_job_ids is not UNSET:
            successful_job_ids = []
            for successful_job_ids_item_data in _successful_job_ids:
                successful_job_ids_item = UUID(successful_job_ids_item_data)



                successful_job_ids.append(successful_job_ids_item)


        _failed_job_ids = d.pop("failed_job_ids", UNSET)
        failed_job_ids: list[UUID] | Unset = UNSET
        if _failed_job_ids is not UNSET:
            failed_job_ids = []
            for failed_job_ids_item_data in _failed_job_ids:
                failed_job_ids_item = UUID(failed_job_ids_item_data)



                failed_job_ids.append(failed_job_ids_item)


        bulk_agent_job_evaluations_2_response_200 = cls(
            successful_job_ids=successful_job_ids,
            failed_job_ids=failed_job_ids,
        )


        bulk_agent_job_evaluations_2_response_200.additional_properties = d
        return bulk_agent_job_evaluations_2_response_200

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
