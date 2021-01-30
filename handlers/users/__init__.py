from .start import dp
from .update_db import dp
from handlers.users.admin_commands.users import dp
from handlers.users.admin_commands.message import dp
from .menu import dp
from .standart import dp

__all__ = ["dp"]
