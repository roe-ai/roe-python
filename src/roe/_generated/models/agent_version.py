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
  from ..models.agent_input_definition import AgentInputDefinition
  from ..models.base_agent import BaseAgent
  from ..models.user_info import UserInfo





T = TypeVar("T", bound="AgentVersion")



@_attrs_define
class AgentVersion:
    """ Serializer for Agent (version) model

        Attributes:
            id (UUID):
            name (str):
            version_name (str): Version name for the agent version. Defaults to 'unnamed version' if not provided.
            created_at (datetime.datetime):
            engine_class_id (str): Get engine_class_id from base_agent.
            engine_name (str): Engine Display Name
            input_definitions (list[AgentInputDefinition]): List of input definitions for this agent version.
            engine_config (Any): Engine configuration.
            organization_id (UUID): Organization ID from base_agent.
            readonly (bool):
            base_agent (BaseAgent): Serializer for BaseAgent (agent config)
            creator (None | Unset | UserInfo):
            description (str | Unset): Description of the agent version.
     """

    id: UUID
    name: str
    version_name: str
    created_at: datetime.datetime
    engine_class_id: str
    engine_name: str
    input_definitions: list[AgentInputDefinition]
    engine_config: Any
    organization_id: UUID
    readonly: bool
    base_agent: BaseAgent
    creator: None | Unset | UserInfo = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_input_definition import AgentInputDefinition
        from ..models.base_agent import BaseAgent
        from ..models.user_info import UserInfo
        id = str(self.id)

        name = self.name

        version_name = self.version_name

        created_at = self.created_at.isoformat()

        engine_class_id = self.engine_class_id

        engine_name = self.engine_name

        input_definitions = []
        for input_definitions_item_data in self.input_definitions:
            input_definitions_item = input_definitions_item_data.to_dict()
            input_definitions.append(input_definitions_item)



        engine_config = self.engine_config

        organization_id = str(self.organization_id)

        readonly = self.readonly

        base_agent = self.base_agent.to_dict()

        creator: dict[str, Any] | None | Unset
        if isinstance(self.creator, Unset):
            creator = UNSET
        elif isinstance(self.creator, UserInfo):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "version_name": version_name,
            "created_at": created_at,
            "engine_class_id": engine_class_id,
            "engine_name": engine_name,
            "input_definitions": input_definitions,
            "engine_config": engine_config,
            "organization_id": organization_id,
            "readonly": readonly,
            "base_agent": base_agent,
        })
        if creator is not UNSET:
            field_dict["creator"] = creator
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_input_definition import AgentInputDefinition
        from ..models.base_agent import BaseAgent
        from ..models.user_info import UserInfo
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        name = d.pop("name")

        version_name = d.pop("version_name")

        created_at = isoparse(d.pop("created_at"))




        engine_class_id = d.pop("engine_class_id")

        engine_name = d.pop("engine_name")

        input_definitions = []
        _input_definitions = d.pop("input_definitions")
        for input_definitions_item_data in (_input_definitions):
            input_definitions_item = AgentInputDefinition.from_dict(input_definitions_item_data)



            input_definitions.append(input_definitions_item)


        engine_config = d.pop("engine_config")

        organization_id = UUID(d.pop("organization_id"))




        readonly = d.pop("readonly")

        base_agent = BaseAgent.from_dict(d.pop("base_agent"))




        def _parse_creator(data: object) -> None | Unset | UserInfo:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                creator_type_0 = UserInfo.from_dict(data)



                return creator_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserInfo, data)

        creator = _parse_creator(d.pop("creator", UNSET))


        description = d.pop("description", UNSET)

        agent_version = cls(
            id=id,
            name=name,
            version_name=version_name,
            created_at=created_at,
            engine_class_id=engine_class_id,
            engine_name=engine_name,
            input_definitions=input_definitions,
            engine_config=engine_config,
            organization_id=organization_id,
            readonly=readonly,
            base_agent=base_agent,
            creator=creator,
            description=description,
        )


        agent_version.additional_properties = d
        return agent_version

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
