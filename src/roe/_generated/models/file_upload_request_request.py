from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO






T = TypeVar("T", bound="FileUploadRequestRequest")



@_attrs_define
class FileUploadRequestRequest:
    """ 
        Attributes:
            file (File): File to upload.
            organization_id (str | Unset): Organization ID. If not provided, file will be uploaded to personal dataset.
            metadata (Any | Unset): Optional metadata for the file in JSON format.
     """

    file: File
    organization_id: str | Unset = UNSET
    metadata: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()


        organization_id = self.organization_id

        metadata = self.metadata


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file": file,
        })
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))



        if not isinstance(self.organization_id, Unset):
            files.append(("organization_id", (None, str(self.organization_id).encode(), "text/plain")))



        if not isinstance(self.metadata, Unset):
            files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(
             payload = BytesIO(d.pop("file"))
        )




        organization_id = d.pop("organization_id", UNSET)

        metadata = d.pop("metadata", UNSET)

        file_upload_request_request = cls(
            file=file,
            organization_id=organization_id,
            metadata=metadata,
        )


        file_upload_request_request.additional_properties = d
        return file_upload_request_request

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
