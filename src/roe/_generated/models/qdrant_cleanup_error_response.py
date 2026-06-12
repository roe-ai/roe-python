from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="QdrantCleanupErrorResponse")



@_attrs_define
class QdrantCleanupErrorResponse:
    """ 500 body when deleting an agent/version fails Qdrant collection cleanup.

        Attributes:
            detail (str): Human-readable error detail
            failed_collections (list[str]): Qdrant collections that could not be deleted
     """

    detail: str
    failed_collections: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        failed_collections = self.failed_collections




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "detail": detail,
            "failed_collections": failed_collections,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detail = d.pop("detail")

        failed_collections = cast(list[str], d.pop("failed_collections"))


        qdrant_cleanup_error_response = cls(
            detail=detail,
            failed_collections=failed_collections,
        )


        qdrant_cleanup_error_response.additional_properties = d
        return qdrant_cleanup_error_response

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
