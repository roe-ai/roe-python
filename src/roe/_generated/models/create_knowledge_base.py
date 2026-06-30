from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CreateKnowledgeBase")



@_attrs_define
class CreateKnowledgeBase:
    """ Body for POST /knowledge-base/ — starts a new draft.

        Attributes:
            company (str):
            brief (str):
            name (str | Unset):
            product_name (str | Unset):
            website_url (str | Unset):
     """

    company: str
    brief: str
    name: str | Unset = UNSET
    product_name: str | Unset = UNSET
    website_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        company = self.company

        brief = self.brief

        name = self.name

        product_name = self.product_name

        website_url = self.website_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "company": company,
            "brief": brief,
        })
        if name is not UNSET:
            field_dict["name"] = name
        if product_name is not UNSET:
            field_dict["product_name"] = product_name
        if website_url is not UNSET:
            field_dict["website_url"] = website_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company = d.pop("company")

        brief = d.pop("brief")

        name = d.pop("name", UNSET)

        product_name = d.pop("product_name", UNSET)

        website_url = d.pop("website_url", UNSET)

        create_knowledge_base = cls(
            company=company,
            brief=brief,
            name=name,
            product_name=product_name,
            website_url=website_url,
        )


        create_knowledge_base.additional_properties = d
        return create_knowledge_base

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
