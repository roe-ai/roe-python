from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.step_run_delivery_enum import StepRunDeliveryEnum
from ..models.step_run_status_enum import StepRunStatusEnum
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="StepRun")



@_attrs_define
class StepRun:
    """ 
        Attributes:
            step_id (str):
            execution_path (Any):
            status (StepRunStatusEnum): * `succeeded` - succeeded
                * `failed` - failed
                * `skipped` - skipped
                * `cancelled` - cancelled
            child_job_id (None | UUID):
            cached (bool | Unset):
            input_ (Any | None | Unset):
            output (Any | None | Unset):
            error (None | str | Unset):
            delivery (None | StepRunDeliveryEnum | Unset): For a step that sends: sending, sent, or unknown when Roe
                couldn't tell whether the send went through.

                * `sending` - Sending
                * `sent` - Sent
                * `unknown` - Unknown
            started_at (datetime.datetime | None | Unset):
            finished_at (datetime.datetime | None | Unset):
     """

    step_id: str
    execution_path: Any
    status: StepRunStatusEnum
    child_job_id: None | UUID
    cached: bool | Unset = UNSET
    input_: Any | None | Unset = UNSET
    output: Any | None | Unset = UNSET
    error: None | str | Unset = UNSET
    delivery: None | StepRunDeliveryEnum | Unset = UNSET
    started_at: datetime.datetime | None | Unset = UNSET
    finished_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        step_id = self.step_id

        execution_path = self.execution_path

        status = self.status.value

        child_job_id: None | str
        if isinstance(self.child_job_id, UUID):
            child_job_id = str(self.child_job_id)
        else:
            child_job_id = self.child_job_id

        cached = self.cached

        input_: Any | None | Unset
        if isinstance(self.input_, Unset):
            input_ = UNSET
        else:
            input_ = self.input_

        output: Any | None | Unset
        if isinstance(self.output, Unset):
            output = UNSET
        else:
            output = self.output

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        delivery: None | str | Unset
        if isinstance(self.delivery, Unset):
            delivery = UNSET
        elif isinstance(self.delivery, StepRunDeliveryEnum):
            delivery = self.delivery.value
        else:
            delivery = self.delivery

        started_at: None | str | Unset
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        finished_at: None | str | Unset
        if isinstance(self.finished_at, Unset):
            finished_at = UNSET
        elif isinstance(self.finished_at, datetime.datetime):
            finished_at = self.finished_at.isoformat()
        else:
            finished_at = self.finished_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "step_id": step_id,
            "execution_path": execution_path,
            "status": status,
            "child_job_id": child_job_id,
        })
        if cached is not UNSET:
            field_dict["cached"] = cached
        if input_ is not UNSET:
            field_dict["input"] = input_
        if output is not UNSET:
            field_dict["output"] = output
        if error is not UNSET:
            field_dict["error"] = error
        if delivery is not UNSET:
            field_dict["delivery"] = delivery
        if started_at is not UNSET:
            field_dict["started_at"] = started_at
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        step_id = d.pop("step_id")

        execution_path = d.pop("execution_path")

        status = StepRunStatusEnum(d.pop("status"))




        def _parse_child_job_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                child_job_id_type_0 = UUID(data)



                return child_job_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        child_job_id = _parse_child_job_id(d.pop("child_job_id"))


        cached = d.pop("cached", UNSET)

        def _parse_input_(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        input_ = _parse_input_(d.pop("input", UNSET))


        def _parse_output(data: object) -> Any | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Any | None | Unset, data)

        output = _parse_output(d.pop("output", UNSET))


        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))


        def _parse_delivery(data: object) -> None | StepRunDeliveryEnum | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivery_type_0 = StepRunDeliveryEnum(data)



                return delivery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StepRunDeliveryEnum | Unset, data)

        delivery = _parse_delivery(d.pop("delivery", UNSET))


        def _parse_started_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)



                return started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        started_at = _parse_started_at(d.pop("started_at", UNSET))


        def _parse_finished_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finished_at_type_0 = isoparse(data)



                return finished_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        finished_at = _parse_finished_at(d.pop("finished_at", UNSET))


        step_run = cls(
            step_id=step_id,
            execution_path=execution_path,
            status=status,
            child_job_id=child_job_id,
            cached=cached,
            input_=input_,
            output=output,
            error=error,
            delivery=delivery,
            started_at=started_at,
            finished_at=finished_at,
        )


        step_run.additional_properties = d
        return step_run

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
