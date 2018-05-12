# -*- coding: utf-8 -*-
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from collections import OrderedDict
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
    import builtins as __builtin__

    long = int
elif six.PY2:
    import __builtin__

from . import state
from . import neighbors


class mt_isn(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isn. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines list of ISIS multi-topology
neighbors.
  """
    __slots__ = ("_path_helper", "_extmethods", "__state", "__neighbors")

    _yang_name = "mt-isn"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )
        self.__neighbors = YANGDynClass(
            base=neighbors.neighbors,
            is_container="container",
            yang_name="neighbors",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

        load = kwargs.pop("load", None)
        if args:
            if len(args) > 1:
                raise TypeError("cannot create a YANG container with >1 argument")
            all_attr = True
            for e in self._pyangbind_elements:
                if not hasattr(args[0], e):
                    all_attr = False
                    break
            if not all_attr:
                raise ValueError("Supplied object did not have the correct attributes")
            for e in self._pyangbind_elements:
                nobj = getattr(args[0], e)
                if nobj._changed() is False:
                    continue
                setmethod = getattr(self, "_set_%s" % e)
                if load is None:
                    setmethod(getattr(args[0], e))
                else:
                    setmethod(getattr(args[0], e), load=load)

    def _path(self):
        if hasattr(self, "_parent"):
            return self._parent._path() + [self._yang_name]
        else:
            return [
                "network-instances",
                "network-instance",
                "protocols",
                "protocol",
                "isis",
                "levels",
                "level",
                "link-state-database",
                "lsp",
                "tlvs",
                "tlv",
                "mt-isn",
            ]

    def _get_state(self):
        """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/state (container)

    YANG Description: This container describes IS MT-ISN state.
    """
        return self.__state

    def _set_state(self, v, load=False):
        """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: This container describes IS MT-ISN state.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=state.state,
                is_container="container",
                yang_name="state",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """state must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__state = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_state(self):
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

    def _get_neighbors(self):
        """
    Getter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors (container)

    YANG Description: This container describes IS neighbors.
    """
        return self.__neighbors

    def _set_neighbors(self, v, load=False):
        """
    Setter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbors() directly.

    YANG Description: This container describes IS neighbors.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=neighbors.neighbors,
                is_container="container",
                yang_name="neighbors",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """neighbors must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__neighbors = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_neighbors(self):
        self.__neighbors = YANGDynClass(
            base=neighbors.neighbors,
            is_container="container",
            yang_name="neighbors",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

    state = __builtin__.property(_get_state)
    neighbors = __builtin__.property(_get_neighbors)

    _pyangbind_elements = OrderedDict([("state", state), ("neighbors", neighbors)])


from . import state
from . import neighbors


class mt_isn(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/mt-isn. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines list of ISIS multi-topology
neighbors.
  """
    __slots__ = ("_path_helper", "_extmethods", "__state", "__neighbors")

    _yang_name = "mt-isn"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )
        self.__neighbors = YANGDynClass(
            base=neighbors.neighbors,
            is_container="container",
            yang_name="neighbors",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

        load = kwargs.pop("load", None)
        if args:
            if len(args) > 1:
                raise TypeError("cannot create a YANG container with >1 argument")
            all_attr = True
            for e in self._pyangbind_elements:
                if not hasattr(args[0], e):
                    all_attr = False
                    break
            if not all_attr:
                raise ValueError("Supplied object did not have the correct attributes")
            for e in self._pyangbind_elements:
                nobj = getattr(args[0], e)
                if nobj._changed() is False:
                    continue
                setmethod = getattr(self, "_set_%s" % e)
                if load is None:
                    setmethod(getattr(args[0], e))
                else:
                    setmethod(getattr(args[0], e), load=load)

    def _path(self):
        if hasattr(self, "_parent"):
            return self._parent._path() + [self._yang_name]
        else:
            return [
                "network-instances",
                "network-instance",
                "protocols",
                "protocol",
                "isis",
                "levels",
                "level",
                "link-state-database",
                "lsp",
                "tlvs",
                "tlv",
                "mt-isn",
            ]

    def _get_state(self):
        """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/state (container)

    YANG Description: This container describes IS MT-ISN state.
    """
        return self.__state

    def _set_state(self, v, load=False):
        """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: This container describes IS MT-ISN state.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=state.state,
                is_container="container",
                yang_name="state",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """state must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__state = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_state(self):
        self.__state = YANGDynClass(
            base=state.state,
            is_container="container",
            yang_name="state",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

    def _get_neighbors(self):
        """
    Getter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors (container)

    YANG Description: This container describes IS neighbors.
    """
        return self.__neighbors

    def _set_neighbors(self, v, load=False):
        """
    Setter method for neighbors, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/mt_isn/neighbors (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbors is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbors() directly.

    YANG Description: This container describes IS neighbors.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=neighbors.neighbors,
                is_container="container",
                yang_name="neighbors",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """neighbors must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=neighbors.neighbors, is_container='container', yang_name="neighbors", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__neighbors = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_neighbors(self):
        self.__neighbors = YANGDynClass(
            base=neighbors.neighbors,
            is_container="container",
            yang_name="neighbors",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=False,
        )

    state = __builtin__.property(_get_state)
    neighbors = __builtin__.property(_get_neighbors)

    _pyangbind_elements = OrderedDict([("state", state), ("neighbors", neighbors)])
