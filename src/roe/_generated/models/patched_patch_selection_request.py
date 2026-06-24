from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.patched_patch_selection_request_refs_item import PatchedPatchSelectionRequestRefsItem





T = TypeVar("T", bound="PatchedPatchSelectionRequest")



@_attrs_define
class PatchedPatchSelectionRequest:
    """ Body for PATCH /knowledge-base/<id>/selection/.

        Attributes:
            refs (list[PatchedPatchSelectionRequestRefsItem] | Unset):
            suggested_name (str | Unset):
     """

    refs: list[PatchedPatchSelectionRequestRefsItem] | Unset = UNSET
    suggested_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.patched_patch_selection_request_refs_item import PatchedPatchSelectionRequestRefsItem
        refs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.refs, Unset):
            refs = []
            for refs_item_data in self.refs:
                refs_item = refs_item_data.to_dict()
                refs.append(refs_item)



        suggested_name = self.suggested_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if refs is not UNSET:
            field_dict["refs"] = refs
        if suggested_name is not UNSET:
            field_dict["suggested_name"] = suggested_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patched_patch_selection_request_refs_item import PatchedPatchSelectionRequestRefsItem
        d = dict(src_dict)
        _refs = d.pop("refs", UNSET)
        refs: list[PatchedPatchSelectionRequestRefsItem] | Unset = UNSET
        if _refs is not UNSET:
            refs = []
            for refs_item_data in _refs:
                refs_item = PatchedPatchSelectionRequestRefsItem.from_dict(refs_item_data)



                refs.append(refs_item)


        suggested_name = d.pop("suggested_name", UNSET)

        patched_patch_selection_request = cls(
            refs=refs,
            suggested_name=suggested_name,
        )


        patched_patch_selection_request.additional_properties = d
        return patched_patch_selection_request

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
