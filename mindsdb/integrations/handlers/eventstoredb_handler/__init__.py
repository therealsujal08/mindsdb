from mindsdb.integrations.libs.const import HANDLER_TYPE

from .eventstoredb_handler import EventStoreDB as Handler
from .__about__ import __version__ as version

title = 'EventStoreDB'
name = 'eventstoredb'
type = HANDLER_TYPE.DATA

__all__ = [
    'Handler', 'version', 'name', 'type', 'title'
]
