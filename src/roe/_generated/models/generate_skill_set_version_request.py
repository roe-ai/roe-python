from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from uuid import UUID






T = TypeVar("T", bound="GenerateSkillSetVersionRequest")



@_attrs_define
class GenerateSkillSetVersionRequest:
    """ Request to author the next version of a skill set with an agent.

    ``base_version_id`` is the version the draft is derived from; omit it to
    start from the set's current version. By default nothing here writes a
    version — the generated file set comes back for review and is saved
    through the normal version-create path. With ``auto_commit`` the workflow
    saves it itself on success, through that same path. At least one table name
    or attachment is required; a use case or policy alone is not a data source.

        Attributes:
            use_case (str): What the company does and what this agent decides: the decision scope, the labels it may apply,
                and anything it must always do.
            base_version_id (UUID | Unset): Version to start from. Defaults to the set's current version.
            auto_commit (bool | Unset): Save the generated draft as the set's next version automatically when the run
                succeeds, skipping draft review. Agents following the set pick the new version up the moment it lands. Default:
                False.
            table_names (list[str] | Unset): Roe table names the agent may profile to learn the data shape.
            attachments (list[str] | Unset): File IDs (file_<uuid>) of CSVs or documents to read.
            policy_id (UUID | Unset): Policy whose dispositions the generated skill must use as its label list. Omit to let
                the agent choose labels from the use case.
            policy_version_id (UUID | Unset): Requires policy_id. Which version of that policy to read. Defaults to the
                policy's current version. An agent may be pinned to an older one.
     """

    use_case: str
    base_version_id: UUID | Unset = UNSET
    auto_commit: bool | Unset = False
    table_names: list[str] | Unset = UNSET
    attachments: list[str] | Unset = UNSET
    policy_id: UUID | Unset = UNSET
    policy_version_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        use_case = self.use_case

        base_version_id: str | Unset = UNSET
        if not isinstance(self.base_version_id, Unset):
            base_version_id = str(self.base_version_id)

        auto_commit = self.auto_commit

        table_names: list[str] | Unset = UNSET
        if not isinstance(self.table_names, Unset):
            table_names = self.table_names



        attachments: list[str] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = self.attachments



        policy_id: str | Unset = UNSET
        if not isinstance(self.policy_id, Unset):
            policy_id = str(self.policy_id)

        policy_version_id: str | Unset = UNSET
        if not isinstance(self.policy_version_id, Unset):
            policy_version_id = str(self.policy_version_id)


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "use_case": use_case,
        })
        if base_version_id is not UNSET:
            field_dict["base_version_id"] = base_version_id
        if auto_commit is not UNSET:
            field_dict["auto_commit"] = auto_commit
        if table_names is not UNSET:
            field_dict["table_names"] = table_names
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id
        if policy_version_id is not UNSET:
            field_dict["policy_version_id"] = policy_version_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        use_case = d.pop("use_case")

        _base_version_id = d.pop("base_version_id", UNSET)
        base_version_id: UUID | Unset
        if isinstance(_base_version_id,  Unset):
            base_version_id = UNSET
        else:
            base_version_id = UUID(_base_version_id)




        auto_commit = d.pop("auto_commit", UNSET)

        table_names = cast(list[str], d.pop("table_names", UNSET))


        attachments = cast(list[str], d.pop("attachments", UNSET))


        _policy_id = d.pop("policy_id", UNSET)
        policy_id: UUID | Unset
        if isinstance(_policy_id,  Unset):
            policy_id = UNSET
        else:
            policy_id = UUID(_policy_id)




        _policy_version_id = d.pop("policy_version_id", UNSET)
        policy_version_id: UUID | Unset
        if isinstance(_policy_version_id,  Unset):
            policy_version_id = UNSET
        else:
            policy_version_id = UUID(_policy_version_id)




        generate_skill_set_version_request = cls(
            use_case=use_case,
            base_version_id=base_version_id,
            auto_commit=auto_commit,
            table_names=table_names,
            attachments=attachments,
            policy_id=policy_id,
            policy_version_id=policy_version_id,
        )


        generate_skill_set_version_request.additional_properties = d
        return generate_skill_set_version_request

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
