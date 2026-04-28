from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime

if TYPE_CHECKING:
  from ..models.roe_database import RoeDatabase





T = TypeVar("T", bound="SearchIndex")



@_attrs_define
class SearchIndex:
    """ 
        Attributes:
            id (UUID):
            name (str):
            database (RoeDatabase):
            table_name (str):
            id_column_name (str):
            column_names (list[str]):
            status (None | str):
            created_at (datetime.datetime):
            search_index_config (Any):
            display_name (None | str | Unset):
     """

    id: UUID
    name: str
    database: RoeDatabase
    table_name: str
    id_column_name: str
    column_names: list[str]
    status: None | str
    created_at: datetime.datetime
    search_index_config: Any
    display_name: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.roe_database import RoeDatabase
        id = str(self.id)

        name = self.name

        database = self.database.to_dict()

        table_name = self.table_name

        id_column_name = self.id_column_name

        column_names = self.column_names



        status: None | str
        status = self.status

        created_at = self.created_at.isoformat()

        search_index_config = self.search_index_config

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "database": database,
            "table_name": table_name,
            "id_column_name": id_column_name,
            "column_names": column_names,
            "status": status,
            "created_at": created_at,
            "search_index_config": search_index_config,
        })
        if display_name is not UNSET:
            field_dict["display_name"] = display_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.roe_database import RoeDatabase
        d = dict(src_dict)
        id = UUID(d.pop("id"))




        name = d.pop("name")

        database = RoeDatabase.from_dict(d.pop("database"))




        table_name = d.pop("table_name")

        id_column_name = d.pop("id_column_name")

        column_names = cast(list[str], d.pop("column_names"))


        def _parse_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        status = _parse_status(d.pop("status"))


        created_at = isoparse(d.pop("created_at"))




        search_index_config = d.pop("search_index_config")

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))


        search_index = cls(
            id=id,
            name=name,
            database=database,
            table_name=table_name,
            id_column_name=id_column_name,
            column_names=column_names,
            status=status,
            created_at=created_at,
            search_index_config=search_index_config,
            display_name=display_name,
        )


        search_index.additional_properties = d
        return search_index

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
