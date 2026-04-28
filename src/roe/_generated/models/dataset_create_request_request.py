from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from uuid import UUID






T = TypeVar("T", bound="DatasetCreateRequestRequest")



@_attrs_define
class DatasetCreateRequestRequest:
    """ 
        Attributes:
            name (str): Name of the dataset.
            organization (UUID | Unset): ID of the organization to associate the dataset with.
     """

    name: str
    organization: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        organization: str | Unset = UNSET
        if not isinstance(self.organization, Unset):
            organization = str(self.organization)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if organization is not UNSET:
            field_dict["organization"] = organization

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))



        if not isinstance(self.organization, Unset):
            files.append(("organization", (None, str(self.organization), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _organization = d.pop("organization", UNSET)
        organization: UUID | Unset
        if isinstance(_organization,  Unset):
            organization = UNSET
        else:
            organization = UUID(_organization)




        dataset_create_request_request = cls(
            name=name,
            organization=organization,
        )


        dataset_create_request_request.additional_properties = d
        return dataset_create_request_request

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
