# maubot - A plugin-based Matrix bot system.
# Copyright (C) 2018 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from typing import TypeVar, Type, Dict
from abc import ABC, abstractmethod

from ..plugin_base import Plugin

PluginClass = TypeVar("PluginClass", bound=Plugin)


class IDConflictError(Exception):
    pass


class PluginLoader(ABC):
    id_cache: Dict[str, 'PluginLoader'] = {}

    id: str
    version: str

    @property
    @abstractmethod
    def source(self) -> str:
        pass

    @abstractmethod
    def load(self) -> Type[PluginClass]:
        pass

    @abstractmethod
    def reload(self) -> Type[PluginClass]:
        pass

    @abstractmethod
    def unload(self) -> None:
        pass
