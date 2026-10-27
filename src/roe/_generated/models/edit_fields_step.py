from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.edit_fields_step_fields import EditFieldsStepFields





T = TypeVar("T", bound="EditFieldsStep")



@_attrs_define
class EditFieldsStep:
    """ 
        Attributes:
            id (str):
            kind (Literal['edit_fields']):  Default: 'edit_fields'.
            fields (EditFieldsStepFields):
     """

    id: str
    fields: EditFieldsStepFields
    kind: Literal['edit_fields'] = 'edit_fields'





    def to_dict(self) -> dict[str, Any]:
        from ..models.edit_fields_step_fields import EditFieldsStepFields
        id = self.id

        kind = self.kind

        fields = self.fields.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "kind": kind,
            "fields": fields,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_fields_step_fields import EditFieldsStepFields
        d = dict(src_dict)
        id = d.pop("id")

        kind = cast(Literal['edit_fields'] , d.pop("kind"))
        if kind != 'edit_fields':
            raise ValueError(f"kind must match const 'edit_fields', got '{kind}'")

        fields = EditFieldsStepFields.from_dict(d.pop("fields"))




        edit_fields_step = cls(
            id=id,
            kind=kind,
            fields=fields,
        )

        return edit_fields_step

