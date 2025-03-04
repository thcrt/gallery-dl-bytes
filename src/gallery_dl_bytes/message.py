from dataclasses import dataclass

from gallery_dl.extractor.message import Message

from .extra_types import KWDict, MessageType

type ParsedMessage = VersionMessage | DirectoryMessage | URLMessage | QueueMessage


@dataclass
class VersionMessage:
    protocol_version: int


@dataclass
class DirectoryMessage:
    metadata: KWDict


@dataclass
class URLMessage:
    url: str
    metadata: KWDict


@dataclass
class QueueMessage:
    url: str
    metadata: KWDict


def parse_message(message: MessageType) -> ParsedMessage:
    if message[0] == Message.Version:
        return VersionMessage(message[1])
    elif message[0] == Message.Directory:
        return DirectoryMessage(message[1])
    elif message[0] == Message.Url:
        return URLMessage(message[1], message[2])
    elif message[0] == Message.Queue:
        return QueueMessage(message[1], message[2])
