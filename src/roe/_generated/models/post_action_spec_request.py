from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.post_action_spec_request_param_mappings import PostActionSpecRequestParamMappings





T = TypeVar("T", bound="PostActionSpecRequest")



@_attrs_define
class PostActionSpecRequest:
    """ Schema mirror of PostActionSpec (agents/services/post_actions.py);
    generated clients import this component instead of hand-writing it.

        Attributes:
            name (str):
            connection_id (UUID):
            operation (str):
            trigger_on (list[int]):
            param_mappings (PostActionSpecRequestParamMappings):
     """

    name: str
    connection_id: UUID
    operation: str
    trigger_on: list[int]
    param_mappings: PostActionSpecRequestParamMappings
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.post_action_spec_request_param_mappings import PostActionSpecRequestParamMappings
        name = self.name

        connection_id = str(self.connection_id)

        operation = self.operation

        trigger_on = self.trigger_on



        param_mappings = self.param_mappings.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "connection_id": connection_id,
            "operation": operation,
            "trigger_on": trigger_on,
            "param_mappings": param_mappings,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_action_spec_request_param_mappings import PostActionSpecRequestParamMappings
        d = dict(src_dict)
        name = d.pop("name")

        connection_id = UUID(d.pop("connection_id"))




        operation = d.pop("operation")

        trigger_on = cast(list[int], d.pop("trigger_on"))


        param_mappings = PostActionSpecRequestParamMappings.from_dict(d.pop("param_mappings"))




        post_action_spec_request = cls(
            name=name,
            connection_id=connection_id,
            operation=operation,
            trigger_on=trigger_on,
            param_mappings=param_mappings,
        )


        post_action_spec_request.additional_properties = d
        return post_action_spec_request

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
