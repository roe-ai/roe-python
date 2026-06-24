from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.knowledge_base_status_enum import KnowledgeBaseStatusEnum
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="KnowledgeBase")



@_attrs_define
class KnowledgeBase:
    """ 
        Attributes:
            id (UUID):
            organization_id (UUID):
            name (str):
            company (str):
            status (KnowledgeBaseStatusEnum): * `drafting` - Drafting
                * `active` - Active
                * `orphaned` - Orphaned
            atlas_draft_id (None | str):
            atlas_lens_id (None | str):
            mcp_url (str):
            lens_snapshot (Any | None):
            last_synced_at (datetime.datetime | None):
            sync_error (None | str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
     """

    id: UUID
    organization_id: UUID
    name: str
    company: str
    status: KnowledgeBaseStatusEnum
    atlas_draft_id: None | str
    atlas_lens_id: None | str
    mcp_url: str
    lens_snapshot: Any | None
    last_synced_at: datetime.datetime | None
    sync_error: None | str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        organization_id = str(self.organization_id)

        name = self.name

        company = self.company

        status = self.status.value

        atlas_draft_id: None | str
        atlas_draft_id = self.atlas_draft_id

        atlas_lens_id: None | str
        atlas_lens_id = self.atlas_lens_id

        mcp_url = self.mcp_url

        lens_snapshot: Any | None
        lens_snapshot = self.lens_snapshot

        last_synced_at: None | str
        if isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        sync_error: None | str
        sync_error = self.sync_error

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "organization_id": organization_id,
            "name": name,
            "company": company,
            "status": status,
            "atlas_draft_id": atlas_draft_id,
            "atlas_lens_id": atlas_lens_id,
            "mcp_url": mcp_url,
            "lens_snapshot": lens_snapshot,
            "last_synced_at": last_synced_at,
            "sync_error": sync_error,
            "created_at": created_at,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        organization_id = UUID(d.pop("organization_id"))




        name = d.pop("name")

        company = d.pop("company")

        status = KnowledgeBaseStatusEnum(d.pop("status"))




        def _parse_atlas_draft_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        atlas_draft_id = _parse_atlas_draft_id(d.pop("atlas_draft_id"))


        def _parse_atlas_lens_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        atlas_lens_id = _parse_atlas_lens_id(d.pop("atlas_lens_id"))


        mcp_url = d.pop("mcp_url")

        def _parse_lens_snapshot(data: object) -> Any | None:
            if data is None:
                return data
            return cast(Any | None, data)

        lens_snapshot = _parse_lens_snapshot(d.pop("lens_snapshot"))


        def _parse_last_synced_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_at_type_0 = isoparse(data)



                return last_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_synced_at = _parse_last_synced_at(d.pop("last_synced_at"))


        def _parse_sync_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        sync_error = _parse_sync_error(d.pop("sync_error"))


        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        knowledge_base = cls(
            id=id,
            organization_id=organization_id,
            name=name,
            company=company,
            status=status,
            atlas_draft_id=atlas_draft_id,
            atlas_lens_id=atlas_lens_id,
            mcp_url=mcp_url,
            lens_snapshot=lens_snapshot,
            last_synced_at=last_synced_at,
            sync_error=sync_error,
            created_at=created_at,
            updated_at=updated_at,
        )


        knowledge_base.additional_properties = d
        return knowledge_base

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
