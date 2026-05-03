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






T = TypeVar("T", bound="UpdatePolicy")



@_attrs_define
class UpdatePolicy:
    """ Serializer for updating policy metadata (name, description)

        Attributes:
            id (UUID):
            name (str):
            organization_id (UUID):
            current_version_id (None | UUID):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            description (str | Unset):
     """

    id: UUID
    name: str
    organization_id: UUID
    current_version_id: None | UUID
    created_at: datetime.datetime
    updated_at: datetime.datetime
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        organization_id = str(self.organization_id)

        current_version_id: None | str
        if isinstance(self.current_version_id, UUID):
            current_version_id = str(self.current_version_id)
        else:
            current_version_id = self.current_version_id

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "organization_id": organization_id,
            "current_version_id": current_version_id,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        name = d.pop("name")

        organization_id = UUID(d.pop("organization_id"))




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


        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        description = d.pop("description", UNSET)

        update_policy = cls(
            id=id,
            name=name,
            organization_id=organization_id,
            current_version_id=current_version_id,
            created_at=created_at,
            updated_at=updated_at,
            description=description,
        )


        update_policy.additional_properties = d
        return update_policy

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
