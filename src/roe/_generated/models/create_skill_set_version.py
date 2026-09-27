from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID

if TYPE_CHECKING:
  from ..models.create_skill_set_version_file_changes_item import CreateSkillSetVersionFileChangesItem
  from ..models.skill_file import SkillFile





T = TypeVar("T", bound="CreateSkillSetVersion")



@_attrs_define
class CreateSkillSetVersion:
    """ Create a new (full) version of an existing skill set.

        Attributes:
            id (UUID):
            files (list[SkillFile]): The complete file set for this new version.
            version_name (str | Unset): Version name (auto-generated if not provided).
            summary (str | Unset): What this version changed and why, in plain language. Default: ''.
            file_changes (list[CreateSkillSetVersionFileChangesItem] | Unset): Per-file walkthrough: [{path, status, note,
                added_lines, removed_lines}]. status is created, edited, or untouched.
     """

    id: UUID
    files: list[SkillFile]
    version_name: str | Unset = UNSET
    summary: str | Unset = ''
    file_changes: list[CreateSkillSetVersionFileChangesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_skill_set_version_file_changes_item import CreateSkillSetVersionFileChangesItem
        from ..models.skill_file import SkillFile
        id = str(self.id)

        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)



        version_name = self.version_name

        summary = self.summary

        file_changes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.file_changes, Unset):
            file_changes = []
            for file_changes_item_data in self.file_changes:
                file_changes_item = file_changes_item_data.to_dict()
                file_changes.append(file_changes_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "files": files,
        })
        if version_name is not UNSET:
            field_dict["version_name"] = version_name
        if summary is not UNSET:
            field_dict["summary"] = summary
        if file_changes is not UNSET:
            field_dict["file_changes"] = file_changes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_skill_set_version_file_changes_item import CreateSkillSetVersionFileChangesItem
        from ..models.skill_file import SkillFile
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        files = []
        _files = d.pop("files")
        for files_item_data in (_files):
            files_item = SkillFile.from_dict(files_item_data)



            files.append(files_item)


        version_name = d.pop("version_name", UNSET)

        summary = d.pop("summary", UNSET)

        _file_changes = d.pop("file_changes", UNSET)
        file_changes: list[CreateSkillSetVersionFileChangesItem] | Unset = UNSET
        if _file_changes is not UNSET:
            file_changes = []
            for file_changes_item_data in _file_changes:
                file_changes_item = CreateSkillSetVersionFileChangesItem.from_dict(file_changes_item_data)



                file_changes.append(file_changes_item)


        create_skill_set_version = cls(
            id=id,
            files=files,
            version_name=version_name,
            summary=summary,
            file_changes=file_changes,
        )


        create_skill_set_version.additional_properties = d
        return create_skill_set_version

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
