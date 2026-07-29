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
  from ..models.agent_tag import AgentTag
  from ..models.user_info import UserInfo





T = TypeVar("T", bound="BaseAgent")



@_attrs_define
class BaseAgent:
    """ Serializer for BaseAgent (agent config)

        Attributes:
            id (UUID):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            name (str):
            disable_cache (bool): Whether to disable job cache fetching for this agent.
            cache_failed_jobs (bool): Whether to cache failed jobs for this agent.
            organization_id (UUID): Organization ID that owns this agent.
            engine_class_id (str):
            current_version_id (UUID): UUID of the current agent version.
            job_count (int | None): Served job count: cached baseline + live delta, annotated by the views
                as ``job_count``. ``None`` when stats weren't fetched (the list can be
                requested with ``include_job_stats=false``; use /agents/job-stats/).
            most_recent_job (datetime.datetime | None):
            engine_name (str): Engine Display Name
            tags (list[AgentTag]):
            creator (None | Unset | UserInfo):
     """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: str
    disable_cache: bool
    cache_failed_jobs: bool
    organization_id: UUID
    engine_class_id: str
    current_version_id: UUID
    job_count: int | None
    most_recent_job: datetime.datetime | None
    engine_name: str
    tags: list[AgentTag]
    creator: None | Unset | UserInfo = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_tag import AgentTag
        from ..models.user_info import UserInfo
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name = self.name

        disable_cache = self.disable_cache

        cache_failed_jobs = self.cache_failed_jobs

        organization_id = str(self.organization_id)

        engine_class_id = self.engine_class_id

        current_version_id = str(self.current_version_id)

        job_count: int | None
        job_count = self.job_count

        most_recent_job: None | str
        if isinstance(self.most_recent_job, datetime.datetime):
            most_recent_job = self.most_recent_job.isoformat()
        else:
            most_recent_job = self.most_recent_job

        engine_name = self.engine_name

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)



        creator: dict[str, Any] | None | Unset
        if isinstance(self.creator, Unset):
            creator = UNSET
        elif isinstance(self.creator, UserInfo):
            creator = self.creator.to_dict()
        else:
            creator = self.creator


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "created_at": created_at,
            "updated_at": updated_at,
            "name": name,
            "disable_cache": disable_cache,
            "cache_failed_jobs": cache_failed_jobs,
            "organization_id": organization_id,
            "engine_class_id": engine_class_id,
            "current_version_id": current_version_id,
            "job_count": job_count,
            "most_recent_job": most_recent_job,
            "engine_name": engine_name,
            "tags": tags,
        })
        if creator is not UNSET:
            field_dict["creator"] = creator

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_tag import AgentTag
        from ..models.user_info import UserInfo
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        name = d.pop("name")

        disable_cache = d.pop("disable_cache")

        cache_failed_jobs = d.pop("cache_failed_jobs")

        organization_id = UUID(d.pop("organization_id"))




        engine_class_id = d.pop("engine_class_id")

        current_version_id = UUID(d.pop("current_version_id"))




        def _parse_job_count(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        job_count = _parse_job_count(d.pop("job_count"))


        def _parse_most_recent_job(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                most_recent_job_type_0 = isoparse(data)



                return most_recent_job_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        most_recent_job = _parse_most_recent_job(d.pop("most_recent_job"))


        engine_name = d.pop("engine_name")

        tags = []
        _tags = d.pop("tags")
        for tags_item_data in (_tags):
            tags_item = AgentTag.from_dict(tags_item_data)



            tags.append(tags_item)


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


        base_agent = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            disable_cache=disable_cache,
            cache_failed_jobs=cache_failed_jobs,
            organization_id=organization_id,
            engine_class_id=engine_class_id,
            current_version_id=current_version_id,
            job_count=job_count,
            most_recent_job=most_recent_job,
            engine_name=engine_name,
            tags=tags,
            creator=creator,
        )


        base_agent.additional_properties = d
        return base_agent

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
