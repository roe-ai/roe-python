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






T = TypeVar("T", bound="WorkflowVersion")



@_attrs_define
class WorkflowVersion:
    """ 
        Attributes:
            id (UUID):
            workflow_id (UUID):
            is_current (bool):
            read_only (bool): Saved in the old graph format: it still runs, but can only be edited by saving a new version.
            version_name (None | str | Unset):
            description (None | str | Unset):
            format_version (int | Unset):
            created_at (datetime.datetime | Unset):
     """

    id: UUID
    workflow_id: UUID
    is_current: bool
    read_only: bool
    version_name: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    format_version: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        workflow_id = str(self.workflow_id)

        is_current = self.is_current

        read_only = self.read_only

        version_name: None | str | Unset
        if isinstance(self.version_name, Unset):
            version_name = UNSET
        else:
            version_name = self.version_name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        format_version = self.format_version

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "workflow_id": workflow_id,
            "is_current": is_current,
            "read_only": read_only,
        })
        if version_name is not UNSET:
            field_dict["version_name"] = version_name
        if description is not UNSET:
            field_dict["description"] = description
        if format_version is not UNSET:
            field_dict["format_version"] = format_version
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        workflow_id = UUID(d.pop("workflow_id"))




        is_current = d.pop("is_current")

        read_only = d.pop("read_only")

        def _parse_version_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version_name = _parse_version_name(d.pop("version_name", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        format_version = d.pop("format_version", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)




        workflow_version = cls(
            id=id,
            workflow_id=workflow_id,
            is_current=is_current,
            read_only=read_only,
            version_name=version_name,
            description=description,
            format_version=format_version,
            created_at=created_at,
        )


        workflow_version.additional_properties = d
        return workflow_version

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
