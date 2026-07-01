from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.draft_ref import DraftRef





T = TypeVar("T", bound="PendingProposal")



@_attrs_define
class PendingProposal:
    """ A staged regeneration awaiting reviewer approval (names-only).

        Attributes:
            refs (list[DraftRef]):
            base_selection (list[DraftRef]):
            feedback (None | str | Unset):
            suggested_name (str | Unset):
            product_summary (str | Unset):
            created_at (None | str | Unset):
     """

    refs: list[DraftRef]
    base_selection: list[DraftRef]
    feedback: None | str | Unset = UNSET
    suggested_name: str | Unset = UNSET
    product_summary: str | Unset = UNSET
    created_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.draft_ref import DraftRef
        refs = []
        for refs_item_data in self.refs:
            refs_item = refs_item_data.to_dict()
            refs.append(refs_item)



        base_selection = []
        for base_selection_item_data in self.base_selection:
            base_selection_item = base_selection_item_data.to_dict()
            base_selection.append(base_selection_item)



        feedback: None | str | Unset
        if isinstance(self.feedback, Unset):
            feedback = UNSET
        else:
            feedback = self.feedback

        suggested_name = self.suggested_name

        product_summary = self.product_summary

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "refs": refs,
            "baseSelection": base_selection,
        })
        if feedback is not UNSET:
            field_dict["feedback"] = feedback
        if suggested_name is not UNSET:
            field_dict["suggestedName"] = suggested_name
        if product_summary is not UNSET:
            field_dict["productSummary"] = product_summary
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.draft_ref import DraftRef
        d = dict(src_dict)
        refs = []
        _refs = d.pop("refs")
        for refs_item_data in (_refs):
            refs_item = DraftRef.from_dict(refs_item_data)



            refs.append(refs_item)


        base_selection = []
        _base_selection = d.pop("baseSelection")
        for base_selection_item_data in (_base_selection):
            base_selection_item = DraftRef.from_dict(base_selection_item_data)



            base_selection.append(base_selection_item)


        def _parse_feedback(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        feedback = _parse_feedback(d.pop("feedback", UNSET))


        suggested_name = d.pop("suggestedName", UNSET)

        product_summary = d.pop("productSummary", UNSET)

        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        pending_proposal = cls(
            refs=refs,
            base_selection=base_selection,
            feedback=feedback,
            suggested_name=suggested_name,
            product_summary=product_summary,
            created_at=created_at,
        )


        pending_proposal.additional_properties = d
        return pending_proposal

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
