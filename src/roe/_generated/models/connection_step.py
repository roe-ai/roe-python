from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.connection_step_input_mapping import ConnectionStepInputMapping





T = TypeVar("T", bound="ConnectionStep")



@_attrs_define
class ConnectionStep:
    """ Calls one operation of a saved connection, such as an API lookup or a
    Slack message. Credentials stay with the connection.

        Attributes:
            id (str):
            kind (Literal['connection']):  Default: 'connection'.
            connection_id (str):
            operation (str):
            setup_id (None | str | Unset):
            input_mapping (ConnectionStepInputMapping | Unset):
     """

    id: str
    connection_id: str
    operation: str
    kind: Literal['connection'] = 'connection'
    setup_id: None | str | Unset = UNSET
    input_mapping: ConnectionStepInputMapping | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.connection_step_input_mapping import ConnectionStepInputMapping
        id = self.id

        kind = self.kind

        connection_id = self.connection_id

        operation = self.operation

        setup_id: None | str | Unset
        if isinstance(self.setup_id, Unset):
            setup_id = UNSET
        else:
            setup_id = self.setup_id

        input_mapping: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_mapping, Unset):
            input_mapping = self.input_mapping.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "kind": kind,
            "connection_id": connection_id,
            "operation": operation,
        })
        if setup_id is not UNSET:
            field_dict["setup_id"] = setup_id
        if input_mapping is not UNSET:
            field_dict["input_mapping"] = input_mapping

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connection_step_input_mapping import ConnectionStepInputMapping
        d = dict(src_dict)
        id = d.pop("id")

        kind = cast(Literal['connection'] , d.pop("kind"))
        if kind != 'connection':
            raise ValueError(f"kind must match const 'connection', got '{kind}'")

        connection_id = d.pop("connection_id")

        operation = d.pop("operation")

        def _parse_setup_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        setup_id = _parse_setup_id(d.pop("setup_id", UNSET))


        _input_mapping = d.pop("input_mapping", UNSET)
        input_mapping: ConnectionStepInputMapping | Unset
        if isinstance(_input_mapping,  Unset):
            input_mapping = UNSET
        else:
            input_mapping = ConnectionStepInputMapping.from_dict(_input_mapping)




        connection_step = cls(
            id=id,
            kind=kind,
            connection_id=connection_id,
            operation=operation,
            setup_id=setup_id,
            input_mapping=input_mapping,
        )

        return connection_step

