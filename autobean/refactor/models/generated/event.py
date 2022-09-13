# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

import datetime
from typing import Iterable, Mapping, Optional, Type, TypeVar, final
from .. import base, internal, meta_item_internal
from ..block_comment import BlockComment
from ..date import Date
from ..escaped_string import EscapedString
from ..inline_comment import InlineComment
from ..meta_item import MetaItem
from ..meta_value import MetaRawValue, MetaValue
from ..punctuation import DedentMark, Eol, IndentMark
from ..spacing import Newline, Whitespace

_Self = TypeVar('_Self', bound='Event')


@internal.token_model
class EventLabel(internal.SimpleDefaultRawTokenModel):
    RULE = 'EVENT'
    DEFAULT = 'event'


@internal.tree_model
class Event(internal.SurroundingCommentsMixin, base.RawTreeModel, internal.SpacingAccessorsMixin):
    RULE = 'event'

    _date = internal.required_field[Date]()
    _label = internal.required_field[EventLabel]()
    _type = internal.required_field[EscapedString]()
    _description = internal.required_field[EscapedString]()
    _inline_comment = internal.optional_left_field[InlineComment](separators=(Whitespace.from_default(),))
    _eol = internal.required_field[Eol]()
    _indent_mark = internal.optional_left_field[IndentMark](separators=())
    _meta = internal.repeated_field[MetaItem | BlockComment](separators=(Newline.from_default(),), default_indent='    ')
    _dedent_mark = internal.optional_left_field[DedentMark](separators=())

    raw_leading_comment = internal.optional_node_property(internal.SurroundingCommentsMixin._leading_comment)
    raw_date = internal.required_node_property(_date)
    raw_type = internal.required_node_property(_type)
    raw_description = internal.required_node_property(_description)
    raw_inline_comment = internal.optional_node_property(_inline_comment)
    raw_meta_with_comments = internal.repeated_node_with_interleaving_comments_property(_meta)
    raw_meta = meta_item_internal.repeated_raw_meta_item_property(raw_meta_with_comments)
    raw_trailing_comment = internal.optional_node_property(internal.SurroundingCommentsMixin._trailing_comment)

    leading_comment = internal.optional_string_property(raw_leading_comment, BlockComment)
    date = internal.required_value_property(raw_date)
    type = internal.required_value_property(raw_type)
    description = internal.required_value_property(raw_description)
    inline_comment = internal.optional_string_property(raw_inline_comment, InlineComment)
    meta = meta_item_internal.repeated_meta_item_property(raw_meta_with_comments)
    trailing_comment = internal.optional_string_property(raw_trailing_comment, BlockComment)

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            leading_comment: internal.Maybe[BlockComment],
            date: Date,
            label: EventLabel,
            type: EscapedString,
            description: EscapedString,
            inline_comment: internal.Maybe[InlineComment],
            eol: Eol,
            indent_mark: internal.Maybe[IndentMark],
            meta: internal.Repeated[MetaItem | BlockComment],
            dedent_mark: internal.Maybe[DedentMark],
            trailing_comment: internal.Maybe[BlockComment],
    ):
        super().__init__(token_store)
        self._leading_comment = leading_comment
        self._date = date
        self._label = label
        self._type = type
        self._description = description
        self._inline_comment = inline_comment
        self._eol = eol
        self._indent_mark = indent_mark
        self._meta = meta
        self._dedent_mark = dedent_mark
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
            self._type.clone(token_store, token_transformer),
            self._description.clone(token_store, token_transformer),
            self._inline_comment.clone(token_store, token_transformer),
            self._eol.clone(token_store, token_transformer),
            self._indent_mark.clone(token_store, token_transformer),
            self._meta.clone(token_store, token_transformer),
            self._dedent_mark.clone(token_store, token_transformer),
            self._trailing_comment.clone(token_store, token_transformer),
        )

    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._leading_comment = self._leading_comment.reattach(token_store, token_transformer)
        self._date = self._date.reattach(token_store, token_transformer)
        self._label = self._label.reattach(token_store, token_transformer)
        self._type = self._type.reattach(token_store, token_transformer)
        self._description = self._description.reattach(token_store, token_transformer)
        self._inline_comment = self._inline_comment.reattach(token_store, token_transformer)
        self._eol = self._eol.reattach(token_store, token_transformer)
        self._indent_mark = self._indent_mark.reattach(token_store, token_transformer)
        self._meta = self._meta.reattach(token_store, token_transformer)
        self._dedent_mark = self._dedent_mark.reattach(token_store, token_transformer)
        self._trailing_comment = self._trailing_comment.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, Event)
            and self._leading_comment == other._leading_comment
            and self._date == other._date
            and self._label == other._label
            and self._type == other._type
            and self._description == other._description
            and self._inline_comment == other._inline_comment
            and self._eol == other._eol
            and self._indent_mark == other._indent_mark
            and self._meta == other._meta
            and self._dedent_mark == other._dedent_mark
            and self._trailing_comment == other._trailing_comment
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            date: Date,
            type: EscapedString,
            description: EscapedString,
            *,
            leading_comment: Optional[BlockComment] = None,
            inline_comment: Optional[InlineComment] = None,
            meta: Iterable[MetaItem | BlockComment] = (),
            trailing_comment: Optional[BlockComment] = None,
    ) -> _Self:
        maybe_leading_comment = cls._leading_comment.create_maybe(leading_comment)
        label = EventLabel.from_default()
        maybe_inline_comment = cls._inline_comment.create_maybe(inline_comment)
        eol = Eol.from_default()
        maybe_indent_mark = cls._indent_mark.create_maybe(None)
        repeated_meta = cls._meta.create_repeated(meta)
        maybe_dedent_mark = cls._dedent_mark.create_maybe(None)
        maybe_trailing_comment = cls._trailing_comment.create_maybe(trailing_comment)
        tokens = [
            *maybe_leading_comment.detach(),
            *date.detach(),
            Whitespace.from_default(),
            *label.detach(),
            Whitespace.from_default(),
            *type.detach(),
            Whitespace.from_default(),
            *description.detach(),
            *maybe_inline_comment.detach(),
            *eol.detach(),
            *maybe_indent_mark.detach(),
            *repeated_meta.detach(),
            *maybe_dedent_mark.detach(),
            *maybe_trailing_comment.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        maybe_leading_comment.reattach(token_store)
        date.reattach(token_store)
        label.reattach(token_store)
        type.reattach(token_store)
        description.reattach(token_store)
        maybe_inline_comment.reattach(token_store)
        eol.reattach(token_store)
        maybe_indent_mark.reattach(token_store)
        repeated_meta.reattach(token_store)
        maybe_dedent_mark.reattach(token_store)
        maybe_trailing_comment.reattach(token_store)
        return cls(token_store, maybe_leading_comment, date, label, type, description, maybe_inline_comment, eol, maybe_indent_mark, repeated_meta, maybe_dedent_mark, maybe_trailing_comment)

    @classmethod
    def from_value(
            cls: Type[_Self],
            date: datetime.date,
            type: str,
            description: str,
            *,
            leading_comment: Optional[str] = None,
            inline_comment: Optional[str] = None,
            meta: Optional[Mapping[str, MetaValue | MetaRawValue]] = None,
            trailing_comment: Optional[str] = None,
    ) -> _Self:
        return cls.from_children(
            leading_comment=BlockComment.from_value(leading_comment) if leading_comment is not None else None,
            date=Date.from_value(date),
            type=EscapedString.from_value(type),
            description=EscapedString.from_value(description),
            inline_comment=InlineComment.from_value(inline_comment) if inline_comment is not None else None,
            meta=meta_item_internal.from_mapping(meta) if meta is not None else (),
            trailing_comment=BlockComment.from_value(trailing_comment) if trailing_comment is not None else None,
        )

    def auto_claim_comments(self) -> None:
        self.claim_leading_comment(ignore_if_already_claimed=True)
        self.claim_trailing_comment(ignore_if_already_claimed=True)
        self._trailing_comment.auto_claim_comments()
        self.raw_meta_with_comments.auto_claim_comments()
        self._inline_comment.auto_claim_comments()
        self._description.auto_claim_comments()
        self._type.auto_claim_comments()
        self._date.auto_claim_comments()
        self._leading_comment.auto_claim_comments()
