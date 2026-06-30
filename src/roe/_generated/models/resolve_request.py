from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.resolve_request_refs_item import ResolveRequestRefsItem





T = TypeVar("T", bound="ResolveRequest")



@_attrs_define
class ResolveRequest:
    """ Body for POST /knowledge-base/<id>/resolve/.

    discard=True declines the pending proposal. Otherwise refs is the reviewer's
    resolved selection (opaque-handle dicts) and suggested_name / accept_summary
    optionally adopt the proposal's name / summary.

        Attributes:
            refs (list[ResolveRequestRefsItem] | Unset):
            suggested_name (str | Unset):
            accept_summary (bool | Unset):  Default: False.
            discard (bool | Unset):  Default: False.
     """

    refs: list[ResolveRequestRefsItem] | Unset = UNSET
    suggested_name: str | Unset = UNSET
    accept_summary: bool | Unset = False
    discard: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.resolve_request_refs_item import ResolveRequestRefsItem
        refs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.refs, Unset):
            refs = []
            for refs_item_data in self.refs:
                refs_item = refs_item_data.to_dict()
                refs.append(refs_item)



        suggested_name = self.suggested_name

        accept_summary = self.accept_summary

        discard = self.discard


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if refs is not UNSET:
            field_dict["refs"] = refs
        if suggested_name is not UNSET:
            field_dict["suggested_name"] = suggested_name
        if accept_summary is not UNSET:
            field_dict["accept_summary"] = accept_summary
        if discard is not UNSET:
            field_dict["discard"] = discard

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resolve_request_refs_item import ResolveRequestRefsItem
        d = dict(src_dict)
        _refs = d.pop("refs", UNSET)
        refs: list[ResolveRequestRefsItem] | Unset = UNSET
        if _refs is not UNSET:
            refs = []
            for refs_item_data in _refs:
                refs_item = ResolveRequestRefsItem.from_dict(refs_item_data)



                refs.append(refs_item)


        suggested_name = d.pop("suggested_name", UNSET)

        accept_summary = d.pop("accept_summary", UNSET)

        discard = d.pop("discard", UNSET)

        resolve_request = cls(
            refs=refs,
            suggested_name=suggested_name,
            accept_summary=accept_summary,
            discard=discard,
        )


        resolve_request.additional_properties = d
        return resolve_request

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
