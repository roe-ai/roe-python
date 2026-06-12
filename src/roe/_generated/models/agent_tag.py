from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.color_enum import ColorEnum
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="AgentTag")



@_attrs_define
class AgentTag:
    """ Serializer for AgentTag model

        Attributes:
            id (UUID):
            name (str):
            color (ColorEnum): * `blue` - Blue
                * `green` - Green
                * `purple` - Purple
                * `orange` - Orange
                * `red` - Red
                * `yellow` - Yellow
                * `gray` - Gray
                * `pink` - Pink
            created_at (datetime.datetime):
            creator (int | None):
            usage_count (int): Count of agents using this tag
     """

    id: UUID
    name: str
    color: ColorEnum
    created_at: datetime.datetime
    creator: int | None
    usage_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        color = self.color.value

        created_at = self.created_at.isoformat()

        creator: int | None
        creator = self.creator

        usage_count = self.usage_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "color": color,
            "created_at": created_at,
            "creator": creator,
            "usage_count": usage_count,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        name = d.pop("name")

        color = ColorEnum(d.pop("color"))




        created_at = isoparse(d.pop("created_at"))




        def _parse_creator(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        creator = _parse_creator(d.pop("creator"))


        usage_count = d.pop("usage_count")

        agent_tag = cls(
            id=id,
            name=name,
            color=color,
            created_at=created_at,
            creator=creator,
            usage_count=usage_count,
        )


        agent_tag.additional_properties = d
        return agent_tag

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
