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






T = TypeVar("T", bound="FileRequest")



@_attrs_define
class FileRequest:
    """ 
        Attributes:
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
            dataset (None | Unset | UUID):
            meta (Any | Unset):
     """

    hash_: str
    name: str
    size: int
    content_type: ContentTypeEnum
    blob_id: str
    dataset: None | Unset | UUID = UNSET
    meta: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        hash_ = self.hash_

        name = self.name

        size = self.size

        content_type = self.content_type.value

        blob_id = self.blob_id

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
            "hash": hash_,
            "name": name,
            "size": size,
            "content_type": content_type,
            "blob_id": blob_id,
        })
        if dataset is not UNSET:
            field_dict["dataset"] = dataset
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("hash", (None, str(self.hash_).encode(), "text/plain")))



        files.append(("name", (None, str(self.name).encode(), "text/plain")))



        files.append(("size", (None, str(self.size).encode(), "text/plain")))



        files.append(("content_type",  (None, str(self.content_type.value).encode(), "text/plain")))



        files.append(("blob_id", (None, str(self.blob_id).encode(), "text/plain")))



        if not isinstance(self.dataset, Unset):
            if isinstance(self.dataset, UUID):

                files.append(("dataset", (None, str(self.dataset), "text/plain")))
            else:
                files.append(("dataset", (None, str(self.dataset).encode(), "text/plain")))


        if not isinstance(self.meta, Unset):
            files.append(("meta", (None, str(self.meta).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        hash_ = d.pop("hash")

        name = d.pop("name")

        size = d.pop("size")

        content_type = ContentTypeEnum(d.pop("content_type"))




        blob_id = d.pop("blob_id")

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

        file_request = cls(
            hash_=hash_,
            name=name,
            size=size,
            content_type=content_type,
            blob_id=blob_id,
            dataset=dataset,
            meta=meta,
        )


        file_request.additional_properties = d
        return file_request

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
