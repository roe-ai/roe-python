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
  from ..models.skill_file import SkillFile
  from ..models.skill_set import SkillSet
  from ..models.skill_set_version_created_by import SkillSetVersionCreatedBy





T = TypeVar("T", bound="SkillSetVersion")



@_attrs_define
class SkillSetVersion:
    """ Full skill set version (nested set + files) for read responses.

        Attributes:
            id (UUID):
            version_name (str):
            created_at (datetime.datetime):
            updated_at (datetime.datetime):
            skill_set (SkillSet): Skill set metadata (read).
            created_by (SkillSetVersionCreatedBy): Minimal user serializer for audit metadata on skill set versions.
            base_version_id (None | UUID):
            files (list[SkillFile]):
            summary (str | Unset):
            file_changes (Any | Unset):
     """

    id: UUID
    version_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    skill_set: SkillSet
    created_by: SkillSetVersionCreatedBy
    base_version_id: None | UUID
    files: list[SkillFile]
    summary: str | Unset = UNSET
    file_changes: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.skill_file import SkillFile
        from ..models.skill_set import SkillSet
        from ..models.skill_set_version_created_by import SkillSetVersionCreatedBy
        id = str(self.id)

        version_name = self.version_name

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        skill_set = self.skill_set.to_dict()

        created_by = self.created_by.to_dict()

        base_version_id: None | str
        if isinstance(self.base_version_id, UUID):
            base_version_id = str(self.base_version_id)
        else:
            base_version_id = self.base_version_id

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)



        summary = self.summary

        file_changes = self.file_changes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "version_name": version_name,
            "created_at": created_at,
            "updated_at": updated_at,
            "skill_set": skill_set,
            "created_by": created_by,
            "base_version_id": base_version_id,
            "files": files,
        })
        if summary is not UNSET:
            field_dict["summary"] = summary
        if file_changes is not UNSET:
            field_dict["file_changes"] = file_changes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.skill_file import SkillFile
        from ..models.skill_set import SkillSet
        from ..models.skill_set_version_created_by import SkillSetVersionCreatedBy
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        version_name = d.pop("version_name")

        created_at = isoparse(d.pop("created_at"))




        updated_at = isoparse(d.pop("updated_at"))




        skill_set = SkillSet.from_dict(d.pop("skill_set"))




        created_by = SkillSetVersionCreatedBy.from_dict(d.pop("created_by"))




        def _parse_base_version_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                base_version_id_type_0 = UUID(data)



                return base_version_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        base_version_id = _parse_base_version_id(d.pop("base_version_id"))


        files = []
        _files = d.pop("files")
        for files_item_data in (_files):
            files_item = SkillFile.from_dict(files_item_data)



            files.append(files_item)


        summary = d.pop("summary", UNSET)

        file_changes = d.pop("file_changes", UNSET)

        skill_set_version = cls(
            id=id,
            version_name=version_name,
            created_at=created_at,
            updated_at=updated_at,
            skill_set=skill_set,
            created_by=created_by,
            base_version_id=base_version_id,
            files=files,
            summary=summary,
            file_changes=file_changes,
        )


        skill_set_version.additional_properties = d
        return skill_set_version

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
