from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID






T = TypeVar("T", bound="BatchCreateAgentWebhookRequest")



@_attrs_define
class BatchCreateAgentWebhookRequest:
    """ Serializer for batch linking multiple agents to a webhook.

        Attributes:
            agent_ids (list[UUID]): List of agent IDs to link to this webhook
     """

    agent_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        agent_ids = []
        for agent_ids_item_data in self.agent_ids:
            agent_ids_item = str(agent_ids_item_data)
            agent_ids.append(agent_ids_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "agent_ids": agent_ids,
        })

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        for agent_ids_item_element in self.agent_ids:
            files.append(("agent_ids", (None, str(agent_ids_item_element), "text/plain")))





        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        agent_ids = []
        _agent_ids = d.pop("agent_ids")
        for agent_ids_item_data in (_agent_ids):
            agent_ids_item = UUID(agent_ids_item_data)



            agent_ids.append(agent_ids_item)


        batch_create_agent_webhook_request = cls(
            agent_ids=agent_ids,
        )


        batch_create_agent_webhook_request.additional_properties = d
        return batch_create_agent_webhook_request

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
