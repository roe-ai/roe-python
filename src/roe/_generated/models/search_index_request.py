from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SearchIndexRequest")



@_attrs_define
class SearchIndexRequest:
    """ 
        Attributes:
            name (str):
            table_name (str):
            id_column_name (str):
            column_names (list[str]):
            search_index_config (Any):
            display_name (None | str | Unset):
     """

    name: str
    table_name: str
    id_column_name: str
    column_names: list[str]
    search_index_config: Any
    display_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        table_name = self.table_name

        id_column_name = self.id_column_name

        column_names = self.column_names



        search_index_config = self.search_index_config

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "table_name": table_name,
            "id_column_name": id_column_name,
            "column_names": column_names,
            "search_index_config": search_index_config,
        })
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))



        files.append(("table_name", (None, str(self.table_name).encode(), "text/plain")))



        files.append(("id_column_name", (None, str(self.id_column_name).encode(), "text/plain")))



        for column_names_item_element in self.column_names:
            files.append(("column_names", (None, str(column_names_item_element).encode(), "text/plain")))




        files.append(("search_index_config", (None, str(self.search_index_config).encode(), "text/plain")))



        if not isinstance(self.display_name, Unset):
            if isinstance(self.display_name, str):

                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))
            else:
                files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))



        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        table_name = d.pop("table_name")

        id_column_name = d.pop("id_column_name")

        column_names = cast(list[str], d.pop("column_names"))


        search_index_config = d.pop("search_index_config")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))


        search_index_request = cls(
            name=name,
            table_name=table_name,
            id_column_name=id_column_name,
            column_names=column_names,
            search_index_config=search_index_config,
            display_name=display_name,
        )


        search_index_request.additional_properties = d
        return search_index_request

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
