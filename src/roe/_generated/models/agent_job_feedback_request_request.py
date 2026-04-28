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






T = TypeVar("T", bound="AgentJobFeedbackRequestRequest")



@_attrs_define
class AgentJobFeedbackRequestRequest:
    """ Serializer for submitting agent job feedback.

        Attributes:
            matches_ground_truth (bool): True=agree with agent output (YES), False=disagree (NO)
            human_feedback (None | str | Unset): Optional feedback text explaining the decision
            corrected_verdict (None | str | Unset): When disagreeing, the human-selected correct verdict from policy
                dispositions
     """

    matches_ground_truth: bool
    human_feedback: None | str | Unset = UNSET
    corrected_verdict: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        matches_ground_truth = self.matches_ground_truth

        human_feedback: None | str | Unset
        if isinstance(self.human_feedback, Unset):
            human_feedback = UNSET
        else:
            human_feedback = self.human_feedback

        corrected_verdict: None | str | Unset
        if isinstance(self.corrected_verdict, Unset):
            corrected_verdict = UNSET
        else:
            corrected_verdict = self.corrected_verdict


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "matches_ground_truth": matches_ground_truth,
        })
        if human_feedback is not UNSET:
            field_dict["human_feedback"] = human_feedback
        if corrected_verdict is not UNSET:
            field_dict["corrected_verdict"] = corrected_verdict

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("matches_ground_truth", (None, str(self.matches_ground_truth).encode(), "text/plain")))



        if not isinstance(self.human_feedback, Unset):
            if isinstance(self.human_feedback, str):

                files.append(("human_feedback", (None, str(self.human_feedback).encode(), "text/plain")))
            else:
                files.append(("human_feedback", (None, str(self.human_feedback).encode(), "text/plain")))


        if not isinstance(self.corrected_verdict, Unset):
            if isinstance(self.corrected_verdict, str):

                files.append(("corrected_verdict", (None, str(self.corrected_verdict).encode(), "text/plain")))
            else:
                files.append(("corrected_verdict", (None, str(self.corrected_verdict).encode(), "text/plain")))



        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        matches_ground_truth = d.pop("matches_ground_truth")

        def _parse_human_feedback(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        human_feedback = _parse_human_feedback(d.pop("human_feedback", UNSET))


        def _parse_corrected_verdict(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        corrected_verdict = _parse_corrected_verdict(d.pop("corrected_verdict", UNSET))


        agent_job_feedback_request_request = cls(
            matches_ground_truth=matches_ground_truth,
            human_feedback=human_feedback,
            corrected_verdict=corrected_verdict,
        )


        agent_job_feedback_request_request.additional_properties = d
        return agent_job_feedback_request_request

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
