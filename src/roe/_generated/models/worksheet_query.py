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
  from ..models.organization_slim import OrganizationSlim
  from ..models.user_info import UserInfo
  from ..models.worksheet import Worksheet





T = TypeVar("T", bound="WorksheetQuery")



@_attrs_define
class WorksheetQuery:
    """ 
        Attributes:
            id (UUID):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            finished_at (datetime.datetime | None):
            query (str):
            query_task_id (None | str):
            query_task_status (None | str):
            error (None | str):
            ai_summary (None | str):
            worksheet (Worksheet | Unset):
            organization (OrganizationSlim | Unset): Simple organization serializer for nested use.
            creator (UserInfo | Unset):
     """

    id: UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    finished_at: datetime.datetime | None
    query: str
    query_task_id: None | str
    query_task_status: None | str
    error: None | str
    ai_summary: None | str
    worksheet: Worksheet | Unset = UNSET
    organization: OrganizationSlim | Unset = UNSET
    creator: UserInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.organization_slim import OrganizationSlim
        from ..models.user_info import UserInfo
        from ..models.worksheet import Worksheet
        id = str(self.id)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        finished_at: None | str
        if isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at

        query = self.query

        query_task_id: None | str
        query_task_id = self.query_task_id

        query_task_status: None | str
        query_task_status = self.query_task_status

        error: None | str
        error = self.error

        ai_summary: None | str
        ai_summary = self.ai_summary

        worksheet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.worksheet, Unset):
            worksheet = self.worksheet.to_dict()

        organization: dict[str, Any] | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = self.organization.to_dict()

        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "created_at": created_at,
            "updated_at": updated_at,
            "finished_at": finished_at,
            "query": query,
            "query_task_id": query_task_id,
            "query_task_status": query_task_status,
            "error": error,
            "ai_summary": ai_summary,
        })
        if worksheet is not UNSET:
            field_dict["worksheet"] = worksheet
        if organization is not UNSET:
            field_dict["organization"] = organization
        if creator is not UNSET:
            field_dict["creator"] = creator

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_slim import OrganizationSlim
        from ..models.user_info import UserInfo
        from ..models.worksheet import Worksheet
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        def _parse_finished_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)



                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        finished_at = _parse_finished_at(d.pop("finished_at"))


        query = d.pop("query")

        def _parse_query_task_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        query_task_id = _parse_query_task_id(d.pop("query_task_id"))


        def _parse_query_task_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        query_task_status = _parse_query_task_status(d.pop("query_task_status"))


        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(d.pop("error"))


        def _parse_ai_summary(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ai_summary = _parse_ai_summary(d.pop("ai_summary"))


        _worksheet = d.pop("worksheet", UNSET)
        worksheet: Worksheet | Unset
        if isinstance(_worksheet,  Unset):
            worksheet = UNSET
        else:
            worksheet = Worksheet.from_dict(_worksheet)




        _organization = d.pop("organization", UNSET)
        organization: OrganizationSlim | Unset
        if isinstance(_organization,  Unset):
            organization = UNSET
        else:
            organization = OrganizationSlim.from_dict(_organization)




        _creator = d.pop("creator", UNSET)
        creator: UserInfo | Unset
        if isinstance(_creator,  Unset):
            creator = UNSET
        else:
            creator = UserInfo.from_dict(_creator)




        worksheet_query = cls(
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            finished_at=finished_at,
            query=query,
            query_task_id=query_task_id,
            query_task_status=query_task_status,
            error=error,
            ai_summary=ai_summary,
            worksheet=worksheet,
            organization=organization,
            creator=creator,
        )


        worksheet_query.additional_properties = d
        return worksheet_query

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
