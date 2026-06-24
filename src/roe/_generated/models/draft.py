from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.draft_status_enum import DraftStatusEnum
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.draft_ref import DraftRef
  from ..models.pending_proposal import PendingProposal





T = TypeVar("T", bound="Draft")



@_attrs_define
class Draft:
    """ Projected atlas draft returned from poll/regenerate/resolve endpoints.

        Attributes:
            id (str):
            status (DraftStatusEnum): * `generating` - generating
                * `ready` - ready
                * `error` - error
            company (str):
            suggested_name (str):
            product_summary (str):
            iteration_count (int):
            refs (list[DraftRef]):
            error (None | str | Unset):
            product_name (None | str | Unset):
            pending_proposal (None | PendingProposal | Unset):
            created_at (None | str | Unset):
            updated_at (None | str | Unset):
     """

    id: str
    status: DraftStatusEnum
    company: str
    suggested_name: str
    product_summary: str
    iteration_count: int
    refs: list[DraftRef]
    error: None | str | Unset = UNSET
    product_name: None | str | Unset = UNSET
    pending_proposal: None | PendingProposal | Unset = UNSET
    created_at: None | str | Unset = UNSET
    updated_at: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.draft_ref import DraftRef
        from ..models.pending_proposal import PendingProposal
        id = self.id

        status = self.status.value

        company = self.company

        suggested_name = self.suggested_name

        product_summary = self.product_summary

        iteration_count = self.iteration_count

        refs = []
        for refs_item_data in self.refs:
            refs_item = refs_item_data.to_dict()
            refs.append(refs_item)



        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        product_name: None | str | Unset
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        pending_proposal: dict[str, Any] | None | Unset
        if isinstance(self.pending_proposal, Unset):
            pending_proposal = UNSET
        elif isinstance(self.pending_proposal, PendingProposal):
            pending_proposal = self.pending_proposal.to_dict()
        else:
            pending_proposal = self.pending_proposal

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        else:
            created_at = self.created_at

        updated_at: None | str | Unset
        if isinstance(self.updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "status": status,
            "company": company,
            "suggestedName": suggested_name,
            "productSummary": product_summary,
            "iterationCount": iteration_count,
            "refs": refs,
        })
        if error is not UNSET:
            field_dict["error"] = error
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if pending_proposal is not UNSET:
            field_dict["pendingProposal"] = pending_proposal
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.draft_ref import DraftRef
        from ..models.pending_proposal import PendingProposal
        d = dict(src_dict)
        id = d.pop("id")

        status = DraftStatusEnum(d.pop("status"))




        company = d.pop("company")

        suggested_name = d.pop("suggestedName")

        product_summary = d.pop("productSummary")

        iteration_count = d.pop("iterationCount")

        refs = []
        _refs = d.pop("refs")
        for refs_item_data in (_refs):
            refs_item = DraftRef.from_dict(refs_item_data)



            refs.append(refs_item)


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        def _parse_product_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        product_name = _parse_product_name(d.pop("productName", UNSET))


        def _parse_pending_proposal(data: object) -> None | PendingProposal | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pending_proposal_type_0 = PendingProposal.from_dict(data)



                return pending_proposal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PendingProposal | Unset, data)

        pending_proposal = _parse_pending_proposal(d.pop("pendingProposal", UNSET))


        def _parse_created_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))


        def _parse_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        updated_at = _parse_updated_at(d.pop("updatedAt", UNSET))


        draft = cls(
            id=id,
            status=status,
            company=company,
            suggested_name=suggested_name,
            product_summary=product_summary,
            iteration_count=iteration_count,
            refs=refs,
            error=error,
            product_name=product_name,
            pending_proposal=pending_proposal,
            created_at=created_at,
            updated_at=updated_at,
        )


        draft.additional_properties = d
        return draft

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
