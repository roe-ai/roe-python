from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.supported_llm_model import SupportedLLMModel





T = TypeVar("T", bound="SupportedLLMModelList")



@_attrs_define
class SupportedLLMModelList:
    """ Serializer for non-deprecated LLM discovery.

        Attributes:
            models (list[SupportedLLMModel]):
            total_count (int):
            tenant_scope (str): Scope of the model list; this endpoint returns all-tenants models
     """

    models: list[SupportedLLMModel]
    total_count: int
    tenant_scope: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.supported_llm_model import SupportedLLMModel
        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)



        total_count = self.total_count

        tenant_scope = self.tenant_scope


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "models": models,
            "total_count": total_count,
            "tenant_scope": tenant_scope,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.supported_llm_model import SupportedLLMModel
        d = dict(src_dict)
        models = []
        _models = d.pop("models")
        for models_item_data in (_models):
            models_item = SupportedLLMModel.from_dict(models_item_data)



            models.append(models_item)


        total_count = d.pop("total_count")

        tenant_scope = d.pop("tenant_scope")

        supported_llm_model_list = cls(
            models=models,
            total_count=total_count,
            tenant_scope=tenant_scope,
        )


        supported_llm_model_list.additional_properties = d
        return supported_llm_model_list

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
