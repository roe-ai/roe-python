from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID






T = TypeVar("T", bound="AgentJobResultManyRequest")



@_attrs_define
class AgentJobResultManyRequest:
    """ Serializer for bulk agent job results request.

        Attributes:
            job_ids (list[UUID]): List of agent job IDs to retrieve results for
     """

    job_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        job_ids = []
        for job_ids_item_data in self.job_ids:
            job_ids_item = str(job_ids_item_data)
            job_ids.append(job_ids_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "job_ids": job_ids,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        job_ids = []
        _job_ids = d.pop("job_ids")
        for job_ids_item_data in (_job_ids):
            job_ids_item = UUID(job_ids_item_data)



            job_ids.append(job_ids_item)


        agent_job_result_many_request = cls(
            job_ids=job_ids,
        )


        agent_job_result_many_request.additional_properties = d
        return agent_job_result_many_request

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
