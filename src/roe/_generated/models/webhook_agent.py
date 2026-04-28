from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID






T = TypeVar("T", bound="WebhookAgent")



@_attrs_define
class WebhookAgent:
    """ Serializer for listing agents linked to a webhook.

        Attributes:
            id (UUID):
            agent_id (UUID):
            agent_name (None | str):
     """

    id: UUID
    agent_id: UUID
    agent_name: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        agent_id = str(self.agent_id)

        agent_name: None | str
        agent_name = self.agent_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "agent_id": agent_id,
            "agent_name": agent_name,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        agent_id = UUID(d.pop("agent_id"))




        def _parse_agent_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        agent_name = _parse_agent_name(d.pop("agent_name"))


        webhook_agent = cls(
            id=id,
            agent_id=agent_id,
            agent_name=agent_name,
        )


        webhook_agent.additional_properties = d
        return webhook_agent

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
