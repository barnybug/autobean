# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

import datetime
from typing import Iterable, Mapping, Optional, Type, TypeVar, final
from .. import base, internal, meta_item_internal
from ..account import Account
from ..block_comment import BlockComment
from ..date import Date
from ..escaped_string import EscapedString
from ..inline_comment import InlineComment
from ..meta_item import MetaItem
from ..meta_value import MetaRawValue, MetaValue
from ..punctuation import Eol
from ..spacing import Newline, Whitespace

_Self = TypeVar('_Self', bound='Note')


@internal.token_model
class NoteLabel(internal.SimpleDefaultRawTokenModel):
    RULE = 'NOTE'
    DEFAULT = 'note'


@internal.tree_model
class Note(internal.SurroundingCommentsMixin, base.RawTreeModel, internal.SpacingAccessorsMixin):
    RULE = 'note'

    _date = internal.required_field[Date]()
    _label = internal.required_field[NoteLabel]()
    _account = internal.required_field[Account]()
    _comment = internal.required_field[EscapedString]()
    _inline_comment = internal.optional_left_field[InlineComment](separators=(Whitespace.from_default(),))
    _eol = internal.required_field[Eol]()
    _meta = internal.repeated_field[MetaItem](separators=(Newline.from_default(),), default_indent='    ')

    raw_leading_comment = internal.optional_node_property(internal.SurroundingCommentsMixin._leading_comment)
    raw_date = internal.required_node_property(_date)
    raw_account = internal.required_node_property(_account)
    raw_comment = internal.required_node_property(_comment)
    raw_inline_comment = internal.optional_node_property(_inline_comment)
    raw_meta = meta_item_internal.repeated_raw_meta_item_property(_meta)
    raw_trailing_comment = internal.optional_node_property(internal.SurroundingCommentsMixin._trailing_comment)

    leading_comment = internal.optional_string_property(raw_leading_comment, BlockComment)
    date = internal.required_value_property(raw_date)
    account = internal.required_value_property(raw_account)
    comment = internal.required_value_property(raw_comment)
    inline_comment = internal.optional_string_property(raw_inline_comment, InlineComment)
    meta = meta_item_internal.repeated_meta_item_property(_meta)
    trailing_comment = internal.optional_string_property(raw_trailing_comment, BlockComment)

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            leading_comment: internal.Maybe[BlockComment],
            date: Date,
            label: NoteLabel,
            account: Account,
            comment: EscapedString,
            inline_comment: internal.Maybe[InlineComment],
            eol: Eol,
            meta: internal.Repeated[MetaItem],
            trailing_comment: internal.Maybe[BlockComment],
    ):
        super().__init__(token_store)
        self._leading_comment = leading_comment
        self._date = date
        self._label = label
        self._account = account
        self._comment = comment
        self._inline_comment = inline_comment
        self._eol = eol
        self._meta = meta
        self._trailing_comment = trailing_comment

    @property
    def first_token(self) -> base.RawTokenModel:
        return self._leading_comment.first_token

    @property
    def last_token(self) -> base.RawTokenModel:
        return self._trailing_comment.last_token

    def clone(self: _Self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> _Self:
        return type(self)(
            token_store,
            self._leading_comment.clone(token_store, token_transformer),
            self._date.clone(token_store, token_transformer),
            self._label.clone(token_store, token_transformer),
            self._account.clone(token_store, token_transformer),
            self._comment.clone(token_store, token_transformer),
            self._inline_comment.clone(token_store, token_transformer),
            self._eol.clone(token_store, token_transformer),
            self._meta.clone(token_store, token_transformer),
            self._trailing_comment.clone(token_store, token_transformer),
        )

    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._leading_comment = self._leading_comment.reattach(token_store, token_transformer)
        self._date = self._date.reattach(token_store, token_transformer)
        self._label = self._label.reattach(token_store, token_transformer)
        self._account = self._account.reattach(token_store, token_transformer)
        self._comment = self._comment.reattach(token_store, token_transformer)
        self._inline_comment = self._inline_comment.reattach(token_store, token_transformer)
        self._eol = self._eol.reattach(token_store, token_transformer)
        self._meta = self._meta.reattach(token_store, token_transformer)
        self._trailing_comment = self._trailing_comment.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, Note)
            and self._leading_comment == other._leading_comment
            and self._date == other._date
            and self._label == other._label
            and self._account == other._account
            and self._comment == other._comment
            and self._inline_comment == other._inline_comment
            and self._eol == other._eol
            and self._meta == other._meta
            and self._trailing_comment == other._trailing_comment
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            date: Date,
            account: Account,
            comment: EscapedString,
            *,
            leading_comment: Optional[BlockComment] = None,
            inline_comment: Optional[InlineComment] = None,
            meta: Iterable[MetaItem] = (),
            trailing_comment: Optional[BlockComment] = None,
    ) -> _Self:
        maybe_leading_comment = cls._leading_comment.create_maybe(leading_comment)
        label = NoteLabel.from_default()
        maybe_inline_comment = cls._inline_comment.create_maybe(inline_comment)
        eol = Eol.from_default()
        repeated_meta = cls._meta.create_repeated(meta)
        maybe_trailing_comment = cls._trailing_comment.create_maybe(trailing_comment)
        tokens = [
            *maybe_leading_comment.detach(),
            *date.detach(),
            Whitespace.from_default(),
            *label.detach(),
            Whitespace.from_default(),
            *account.detach(),
            Whitespace.from_default(),
            *comment.detach(),
            *maybe_inline_comment.detach(),
            *eol.detach(),
            *repeated_meta.detach(),
            *maybe_trailing_comment.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        maybe_leading_comment.reattach(token_store)
        date.reattach(token_store)
        label.reattach(token_store)
        account.reattach(token_store)
        comment.reattach(token_store)
        maybe_inline_comment.reattach(token_store)
        eol.reattach(token_store)
        repeated_meta.reattach(token_store)
        maybe_trailing_comment.reattach(token_store)
        return cls(token_store, maybe_leading_comment, date, label, account, comment, maybe_inline_comment, eol, repeated_meta, maybe_trailing_comment)

    @classmethod
    def from_value(
            cls: Type[_Self],
            date: datetime.date,
            account: str,
            comment: str,
            *,
            leading_comment: Optional[str] = None,
            inline_comment: Optional[str] = None,
            meta: Optional[Mapping[str, MetaValue | MetaRawValue]] = None,
            trailing_comment: Optional[str] = None,
    ) -> _Self:
        return cls.from_children(
            leading_comment=BlockComment.from_value(leading_comment) if leading_comment is not None else None,
            date=Date.from_value(date),
            account=Account.from_value(account),
            comment=EscapedString.from_value(comment),
            inline_comment=InlineComment.from_value(inline_comment) if inline_comment is not None else None,
            meta=meta_item_internal.from_mapping(meta) if meta is not None else (),
            trailing_comment=BlockComment.from_value(trailing_comment) if trailing_comment is not None else None,
        )
