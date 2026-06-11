from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.agent_execution_request_metadata_type_0 import AgentExecutionRequestMetadataType0





T = TypeVar("T", bound="AgentExecutionRequest")



@_attrs_define
class AgentExecutionRequest:
    """ Agent execution request. In addition to `metadata`, every key of the agent's input definitions is accepted as a
    property (text value or file upload).

        Attributes:
            metadata (AgentExecutionRequestMetadataType0 | None | Unset): Optional metadata stored as-is on the created
                agent job. A JSON-encoded object string is also accepted; null is treated the same as omitting the field (empty
                metadata). Only honored by the single-run endpoints — when this object is an item of the run-async-many `inputs`
                list, `metadata` is ignored.
     """

    metadata: AgentExecutionRequestMetadataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_execution_request_metadata_type_0 import AgentExecutionRequestMetadataType0
        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, AgentExecutionRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_execution_request_metadata_type_0 import AgentExecutionRequestMetadataType0
        d = dict(src_dict)
        def _parse_metadata(data: object) -> AgentExecutionRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = AgentExecutionRequestMetadataType0.from_dict(data)



                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentExecutionRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))


        agent_execution_request = cls(
            metadata=metadata,
        )


        agent_execution_request.additional_properties = d
        return agent_execution_request

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
