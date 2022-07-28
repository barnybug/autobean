# DO NOT EDIT
# This file is automatically generated by autobean.refactor.modelgen.

from typing import Type, TypeVar, final
from .. import base
from .. import internal
from ..date import Date
from ..escaped_string import EscapedString
from ..punctuation import Whitespace

_Self = TypeVar('_Self', bound='Event')


class EventLabel(internal.SimpleDefaultRawTokenModel):
    RULE = 'EVENT'
    DEFAULT = 'event'


class Event(base.RawTreeModel):
    RULE = 'event'

    _date = internal.required_field[Date]()
    _label = internal.required_field[EventLabel]()
    _type = internal.required_field[EscapedString]()
    _description = internal.required_field[EscapedString]()

    raw_date = internal.required_node_property(_date)
    raw_type = internal.required_node_property(_type)
    raw_description = internal.required_node_property(_description)

    @final
    def __init__(
            self,
            token_store: base.TokenStore,
            date: Date,
            label: EventLabel,
            type: EscapedString,
            description: EscapedString,
    ):
        super().__init__(token_store)
        self._date = date
        self._label = label
        self._type = type
        self._description = description

    @property
    def first_token(self) -> base.RawTokenModel:
        return self._date.first_token

    @property
    def last_token(self) -> base.RawTokenModel:
        return self._description.last_token

    def clone(self: _Self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> _Self:
        return type(self)(
            token_store,
            self._date.clone(token_store, token_transformer),
            self._label.clone(token_store, token_transformer),
            self._type.clone(token_store, token_transformer),
            self._description.clone(token_store, token_transformer),
        )
    
    def _reattach(self, token_store: base.TokenStore, token_transformer: base.TokenTransformer) -> None:
        self._token_store = token_store
        self._date = self._date.reattach(token_store, token_transformer)
        self._label = self._label.reattach(token_store, token_transformer)
        self._type = self._type.reattach(token_store, token_transformer)
        self._description = self._description.reattach(token_store, token_transformer)

    def _eq(self, other: base.RawTreeModel) -> bool:
        return (
            isinstance(other, Event)
            and self._date == other._date
            and self._label == other._label
            and self._type == other._type
            and self._description == other._description
        )

    @classmethod
    def from_children(
            cls: Type[_Self],
            date: Date,
            type: EscapedString,
            description: EscapedString,
    ) -> _Self:
        label = EventLabel.from_default()
        tokens = [
            *date.detach(),
            Whitespace.from_default(),
            *label.detach(),
            Whitespace.from_default(),
            *type.detach(),
            Whitespace.from_default(),
            *description.detach(),
        ]
        token_store = base.TokenStore.from_tokens(tokens)
        date.reattach(token_store)
        label.reattach(token_store)
        type.reattach(token_store)
        description.reattach(token_store)
        return cls(token_store, date, label, type, description)
