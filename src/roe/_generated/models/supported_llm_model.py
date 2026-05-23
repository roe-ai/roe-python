from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="SupportedLLMModel")



@_attrs_define
class SupportedLLMModel:
    """ Serializer for tenant-agnostic supported LLM metadata.

        Attributes:
            id (str): Model identifier accepted in engine_config.model
            providers (list[str]): Non-customer-specific providers registered for this model
            capabilities (list[str]): Input capabilities supported by this model
            context_window (int): Largest context window across global providers
            max_output_tokens (int): Largest max output token limit across global providers
            supports_system_message (bool):
            supports_temperature (bool):
            supports_reasoning_effort (bool):
            supports_json_output (bool):
            supports_json_schema (bool):
     """

    id: str
    providers: list[str]
    capabilities: list[str]
    context_window: int
    max_output_tokens: int
    supports_system_message: bool
    supports_temperature: bool
    supports_reasoning_effort: bool
    supports_json_output: bool
    supports_json_schema: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        providers = self.providers



        capabilities = self.capabilities



        context_window = self.context_window

        max_output_tokens = self.max_output_tokens

        supports_system_message = self.supports_system_message

        supports_temperature = self.supports_temperature

        supports_reasoning_effort = self.supports_reasoning_effort

        supports_json_output = self.supports_json_output

        supports_json_schema = self.supports_json_schema


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "providers": providers,
            "capabilities": capabilities,
            "context_window": context_window,
            "max_output_tokens": max_output_tokens,
            "supports_system_message": supports_system_message,
            "supports_temperature": supports_temperature,
            "supports_reasoning_effort": supports_reasoning_effort,
            "supports_json_output": supports_json_output,
            "supports_json_schema": supports_json_schema,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        providers = cast(list[str], d.pop("providers"))


        capabilities = cast(list[str], d.pop("capabilities"))


        context_window = d.pop("context_window")

        max_output_tokens = d.pop("max_output_tokens")

        supports_system_message = d.pop("supports_system_message")

        supports_temperature = d.pop("supports_temperature")

        supports_reasoning_effort = d.pop("supports_reasoning_effort")

        supports_json_output = d.pop("supports_json_output")

        supports_json_schema = d.pop("supports_json_schema")

        supported_llm_model = cls(
            id=id,
            providers=providers,
            capabilities=capabilities,
            context_window=context_window,
            max_output_tokens=max_output_tokens,
            supports_system_message=supports_system_message,
            supports_temperature=supports_temperature,
            supports_reasoning_effort=supports_reasoning_effort,
            supports_json_output=supports_json_output,
            supports_json_schema=supports_json_schema,
        )


        supported_llm_model.additional_properties = d
        return supported_llm_model

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
