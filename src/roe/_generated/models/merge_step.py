from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.mode_enum import ModeEnum
from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast






T = TypeVar("T", bound="MergeStep")



@_attrs_define
class MergeStep:
    """ One value from several steps' outputs, leaving out any that didn't run,
    such as the side of an If that wasn't taken.

        Attributes:
            id (str):
            kind (Literal['merge']):  Default: 'merge'.
            sources (list[str]):
            mode (ModeEnum | Unset):  Default: ModeEnum.APPEND.
     """

    id: str
    sources: list[str]
    kind: Literal['merge'] = 'merge'
    mode: ModeEnum | Unset = ModeEnum.APPEND





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind

        sources = self.sources



        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "kind": kind,
            "sources": sources,
        })
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        kind = cast(Literal['merge'] , d.pop("kind"))
        if kind != 'merge':
            raise ValueError(f"kind must match const 'merge', got '{kind}'")

        sources = cast(list[str], d.pop("sources"))


        _mode = d.pop("mode", UNSET)
        mode: ModeEnum | Unset
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = ModeEnum(_mode)




        merge_step = cls(
            id=id,
            kind=kind,
            sources=sources,
            mode=mode,
        )

        return merge_step

