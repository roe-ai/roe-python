from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.skill_set_generation_run import SkillSetGenerationRun





T = TypeVar("T", bound="PublicSkillSetGeneration")



@_attrs_define
class PublicSkillSetGeneration:
    """ 
        Attributes:
            generation (None | SkillSetGenerationRun):
     """

    generation: None | SkillSetGenerationRun
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.skill_set_generation_run import SkillSetGenerationRun
        generation: dict[str, Any] | None
        if isinstance(self.generation, SkillSetGenerationRun):
            generation = self.generation.to_dict()
        else:
            generation = self.generation


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "generation": generation,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.skill_set_generation_run import SkillSetGenerationRun
        d = dict(src_dict)
        def _parse_generation(data: object) -> None | SkillSetGenerationRun:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                generation_type_0 = SkillSetGenerationRun.from_dict(data)



                return generation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SkillSetGenerationRun, data)

        generation = _parse_generation(d.pop("generation"))


        public_skill_set_generation = cls(
            generation=generation,
        )


        public_skill_set_generation.additional_properties = d
        return public_skill_set_generation

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
