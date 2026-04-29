from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.content_type_enum import ContentTypeEnum
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.file_metadata import FileMetadata
  from ..models.user_info import UserInfo





T = TypeVar("T", bound="File")



@_attrs_define
class File:
    """ 
        Attributes:
            id (UUID):
            hash_ (str):
            name (str):
            size (int):
            content_type (ContentTypeEnum): * `application/pdf` - APPLICATION_PDF
                * `application/json` - APPLICATION_JSON
                * `audio/mpeg` - AUDIO_MPEG
                * `audio/mp3` - AUDIO_MP3
                * `audio/wav` - AUDIO_WAV
                * `audio/x-m4a` - AUDIO_M4A
                * `video/mp4` - VIDEO_MP4
                * `image/jpeg` - IMAGE_JPEG
                * `image/png` - IMAGE_PNG
                * `text/plain` - TEXT_PLAIN
                * `text/html` - TEXT_HTML
                * `text/xml` - TEXT_XML
                * `text/csv` - TEXT_CSV
                * `text/markdown` - TEXT_MARKDOWN
                * `audio/*` - AUDIO
                * `video/*` - VIDEO
                * `image/*` - IMAGE
                * `text/*` - TEXT
                * `*/*` - ANY
            blob_id (str):
            creator (None | UserInfo):
            created_at (datetime.datetime):
            metadata (FileMetadata):
            deleted_at (datetime.datetime | None):
            deleted_by (None | UserInfo):
            dataset (None | Unset | UUID):
            meta (Any | Unset):
     """

    id: UUID
    hash_: str
    name: str
    size: int
    content_type: ContentTypeEnum
    blob_id: str
    creator: None | UserInfo
    created_at: datetime.datetime
    metadata: FileMetadata
    deleted_at: datetime.datetime | None
    deleted_by: None | UserInfo
    dataset: None | Unset | UUID = UNSET
    meta: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_metadata import FileMetadata
        from ..models.user_info import UserInfo
        id = str(self.id)

        hash_ = self.hash_

        name = self.name

        size = self.size

        content_type = self.content_type.value

        blob_id = self.blob_id

        creator: dict[str, Any] | None
        if isinstance(self.creator, UserInfo):
            creator = self.creator.to_dict()
        else:
            creator = self.creator

        created_at = self.created_at.isoformat()

        metadata = self.metadata.to_dict()

        deleted_at: None | str
        if isinstance(self.deleted_at, datetime.datetime):
            deleted_at = self.deleted_at.isoformat()
        else:
            deleted_at = self.deleted_at

        deleted_by: dict[str, Any] | None
        if isinstance(self.deleted_by, UserInfo):
            deleted_by = self.deleted_by.to_dict()
        else:
            deleted_by = self.deleted_by

        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        elif isinstance(self.dataset, UUID):
            dataset = str(self.dataset)
        else:
            dataset = self.dataset

        meta = self.meta


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "hash": hash_,
            "name": name,
            "size": size,
            "content_type": content_type,
            "blob_id": blob_id,
            "creator": creator,
            "created_at": created_at,
            "metadata": metadata,
            "deleted_at": deleted_at,
            "deleted_by": deleted_by,
        })
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_metadata import FileMetadata
        from ..models.user_info import UserInfo
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        hash_ = d.pop("hash")

        name = d.pop("name")

        size = d.pop("size")

        content_type = ContentTypeEnum(d.pop("content_type"))




        blob_id = d.pop("blob_id")

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


        created_at = isoparse(d.pop("created_at"))




        metadata = FileMetadata.from_dict(d.pop("metadata"))




        def _parse_deleted_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                deleted_at_type_0 = isoparse(data)



                return deleted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        deleted_at = _parse_deleted_at(d.pop("deleted_at"))


        def _parse_deleted_by(data: object) -> None | UserInfo:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                deleted_by_type_0 = UserInfo.from_dict(data)



                return deleted_by_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UserInfo, data)

        deleted_by = _parse_deleted_by(d.pop("deleted_by"))


        def _parse_dataset(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                dataset_type_0 = UUID(data)



                return dataset_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        dataset = _parse_dataset(d.pop("dataset", UNSET))


        meta = d.pop("meta", UNSET)

        file = cls(
            id=id,
            hash_=hash_,
            name=name,
            size=size,
            content_type=content_type,
            blob_id=blob_id,
            creator=creator,
            created_at=created_at,
            metadata=metadata,
            deleted_at=deleted_at,
            deleted_by=deleted_by,
            dataset=dataset,
            meta=meta,
        )


        file.additional_properties = d
        return file

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
