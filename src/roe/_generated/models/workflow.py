from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.user_info import UserInfo





T = TypeVar("T", bound="Workflow")



@_attrs_define
class Workflow:
    """ 
        Attributes:
            id (UUID):
            name (str):
            agent_id (UUID): The workflow's id as an agent. Calling a workflow by it is deprecated; the agent_id filter
                finds the workflow it belongs to.
            current_version_id (None | UUID):
            creator (None | UserInfo):
            updated_at (datetime.datetime):
            created_at (datetime.datetime | Unset):
     """

    id: UUID
    name: str
    agent_id: UUID
    current_version_id: None | UUID
    creator: None | UserInfo
    updated_at: datetime.datetime
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_info import UserInfo
        id = str(self.id)

        name = self.name

        agent_id = str(self.agent_id)

        current_version_id: None | str
        if isinstance(self.current_version_id, UUID):
            current_version_id = str(self.current_version_id)
        else:
            current_version_id = self.current_version_id

        creator: dict[str, Any] | None
        if isinstance(self.creator, UserInfo):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        updated_at = self.updated_at.isoformat()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "agent_id": agent_id,
            "current_version_id": current_version_id,
            "creator": creator,
            "updated_at": updated_at,
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_info import UserInfo
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        name = d.pop("name")

        agent_id = UUID(d.pop("agent_id"))




        def _parse_current_version_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                current_version_id_type_0 = UUID(data)



                return current_version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        current_version_id = _parse_current_version_id(d.pop("current_version_id"))


        def _parse_creator(data: object) -> None | UserInfo:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                creator_type_0 = UserInfo.from_dict(data)



                return creator_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserInfo, data)

        creator = _parse_creator(d.pop("creator"))


        updated_at = isoparse(d.pop("updated_at"))




        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        workflow = cls(
            id=id,
            name=name,
            agent_id=agent_id,
            current_version_id=current_version_id,
            creator=creator,
            updated_at=updated_at,
            created_at=created_at,
        )


        workflow.additional_properties = d
        return workflow

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
