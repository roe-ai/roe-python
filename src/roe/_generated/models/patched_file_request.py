from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..models.content_type_enum import ContentTypeEnum
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="PatchedFileRequest")



@_attrs_define
class PatchedFileRequest:
    """ 
        Attributes:
            dataset (None | Unset | UUID):
            hash_ (str | Unset):
            name (str | Unset):
            size (int | Unset):
            content_type (ContentTypeEnum | Unset): * `application/pdf` - APPLICATION_PDF
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
            blob_id (str | Unset):
            meta (Any | Unset):
     """

    dataset: None | Unset | UUID = UNSET
    hash_: str | Unset = UNSET
    name: str | Unset = UNSET
    size: int | Unset = UNSET
    content_type: ContentTypeEnum | Unset = UNSET
    blob_id: str | Unset = UNSET
    meta: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        dataset: None | str | Unset
        if isinstance(self.dataset, Unset):
            dataset = UNSET
        elif isinstance(self.dataset, UUID):
            dataset = str(self.dataset)
        else:
            dataset = self.dataset

        hash_ = self.hash_

        name = self.name

        size = self.size

        content_type: str | Unset = UNSET
        if not isinstance(self.content_type, Unset):
            content_type = self.content_type.value


        blob_id = self.blob_id

        meta = self.meta


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if content_type is not UNSET:
            field_dict["content_type"] = content_type
        if blob_id is not UNSET:
            field_dict["blob_id"] = blob_id
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.dataset, Unset):
            if isinstance(self.dataset, UUID):

                files.append(("dataset", (None, str(self.dataset), "text/plain")))
            else:
                files.append(("dataset", (None, str(self.dataset).encode(), "text/plain")))


        if not isinstance(self.hash_, Unset):
            files.append(("hash", (None, str(self.hash_).encode(), "text/plain")))



        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))



        if not isinstance(self.size, Unset):
            files.append(("size", (None, str(self.size).encode(), "text/plain")))



        if not isinstance(self.content_type, Unset):
            files.append(("content_type",  (None, str(self.content_type.value).encode(), "text/plain")))



        if not isinstance(self.blob_id, Unset):
            files.append(("blob_id", (None, str(self.blob_id).encode(), "text/plain")))



        if not isinstance(self.meta, Unset):
            files.append(("meta", (None, str(self.meta).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
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


        hash_ = d.pop("hash", UNSET)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        _content_type = d.pop("content_type", UNSET)
        content_type: ContentTypeEnum | Unset
        if isinstance(_content_type,  Unset):
            content_type = UNSET
        else:
            content_type = ContentTypeEnum(_content_type)




        blob_id = d.pop("blob_id", UNSET)

        meta = d.pop("meta", UNSET)

        patched_file_request = cls(
            dataset=dataset,
            hash_=hash_,
            name=name,
            size=size,
            content_type=content_type,
            blob_id=blob_id,
            meta=meta,
        )


        patched_file_request.additional_properties = d
        return patched_file_request

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
