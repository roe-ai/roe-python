from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.relevance_enum import RelevanceEnum
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="DraftRef")



@_attrs_define
class DraftRef:
    """ A single ref in a selection (names-only projection from atlas).

        Attributes:
            typology_id (str):
            typology_name (str | Unset):
            relevance (RelevanceEnum | Unset): * `core` - core
                * `watch` - watch
                * `edge` - edge Default: RelevanceEnum.WATCH.
            rationale (str | Unset):
            tactic_ids (list[str] | None | Unset):
            tactic_names (list[str] | None | Unset):
     """

    typology_id: str
    typology_name: str | Unset = UNSET
    relevance: RelevanceEnum | Unset = RelevanceEnum.WATCH
    rationale: str | Unset = UNSET
    tactic_ids: list[str] | None | Unset = UNSET
    tactic_names: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        typology_id = self.typology_id

        typology_name = self.typology_name

        relevance: str | Unset = UNSET
        if not isinstance(self.relevance, Unset):
            relevance = self.relevance.value


        rationale = self.rationale

        tactic_ids: list[str] | None | Unset
        if isinstance(self.tactic_ids, Unset):
            tactic_ids = UNSET
        elif isinstance(self.tactic_ids, list):
            tactic_ids = self.tactic_ids


        else:
            tactic_ids = self.tactic_ids

        tactic_names: list[str] | None | Unset
        if isinstance(self.tactic_names, Unset):
            tactic_names = UNSET
        elif isinstance(self.tactic_names, list):
            tactic_names = self.tactic_names


        else:
            tactic_names = self.tactic_names


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "typologyId": typology_id,
        })
        if typology_name is not UNSET:
            field_dict["typologyName"] = typology_name
        if relevance is not UNSET:
            field_dict["relevance"] = relevance
        if rationale is not UNSET:
            field_dict["rationale"] = rationale
        if tactic_ids is not UNSET:
            field_dict["tacticIds"] = tactic_ids
        if tactic_names is not UNSET:
            field_dict["tacticNames"] = tactic_names

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        typology_id = d.pop("typologyId")

        typology_name = d.pop("typologyName", UNSET)

        _relevance = d.pop("relevance", UNSET)
        relevance: RelevanceEnum | Unset
        if isinstance(_relevance,  Unset):
            relevance = UNSET
        else:
            relevance = RelevanceEnum(_relevance)




        rationale = d.pop("rationale", UNSET)

        def _parse_tactic_ids(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tactic_ids_type_0 = cast(list[str], data)

                return tactic_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tactic_ids = _parse_tactic_ids(d.pop("tacticIds", UNSET))


        def _parse_tactic_names(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tactic_names_type_0 = cast(list[str], data)

                return tactic_names_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        tactic_names = _parse_tactic_names(d.pop("tacticNames", UNSET))


        draft_ref = cls(
            typology_id=typology_id,
            typology_name=typology_name,
            relevance=relevance,
            rationale=rationale,
            tactic_ids=tactic_ids,
            tactic_names=tactic_names,
        )


        draft_ref.additional_properties = d
        return draft_ref

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
