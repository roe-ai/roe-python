from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="ImportRoeDatasetRequest")



@_attrs_define
class ImportRoeDatasetRequest:
    """ 
        Attributes:
            table_name (str):
            dataset_id (UUID):
            sync_dataset (bool | Unset):  Default: False.
            organization_id (None | Unset | UUID):
     """

    table_name: str
    dataset_id: UUID
    sync_dataset: bool | Unset = False
    organization_id: None | Unset | UUID = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        table_name = self.table_name

        dataset_id = str(self.dataset_id)

        sync_dataset = self.sync_dataset

        organization_id: None | str | Unset
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        elif isinstance(self.organization_id, UUID):
            organization_id = str(self.organization_id)
        else:
            organization_id = self.organization_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "table_name": table_name,
            "dataset_id": dataset_id,
        })
        if sync_dataset is not UNSET:
            field_dict["sync_dataset"] = sync_dataset
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        table_name = d.pop("table_name")

        dataset_id = UUID(d.pop("dataset_id"))




        sync_dataset = d.pop("sync_dataset", UNSET)

        def _parse_organization_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                organization_id_type_0 = UUID(data)



                return organization_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))


        import_roe_dataset_request = cls(
            table_name=table_name,
            dataset_id=dataset_id,
            sync_dataset=sync_dataset,
            organization_id=organization_id,
        )


        import_roe_dataset_request.additional_properties = d
        return import_roe_dataset_request

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
