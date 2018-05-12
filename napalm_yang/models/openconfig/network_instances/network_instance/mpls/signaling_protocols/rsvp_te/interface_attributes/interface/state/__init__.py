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

from . import counters


class state(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-interface RSVP protocol and state information
  """
    __slots__ = ("_path_helper", "_extmethods", "__interface_id", "__counters")

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__interface_id = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="interface-id",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-if:interface-id",
            is_config=False,
        )
        self.__counters = YANGDynClass(
            base=counters.counters,
            is_container="container",
            yang_name="counters",
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
                "mpls",
                "signaling-protocols",
                "rsvp-te",
                "interface-attributes",
                "interface",
                "state",
            ]

    def _get_interface_id(self):
        """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/state/interface_id (oc-if:interface-id)

    YANG Description: Identifier for the interface
    """
        return self.__interface_id

    def _set_interface_id(self, v, load=False):
        """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/state/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Identifier for the interface
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=six.text_type,
                is_leaf=True,
                yang_name="interface-id",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="oc-if:interface-id",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """interface_id must be of a type compatible with oc-if:interface-id""",
                    "defined-type": "oc-if:interface-id",
                    "generated-type": """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=False)""",
                }
            )

        self.__interface_id = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_interface_id(self):
        self.__interface_id = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="interface-id",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-if:interface-id",
            is_config=False,
        )

    def _get_counters(self):
        """
    Getter method for counters, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/state/counters (container)

    YANG Description: Interface specific RSVP statistics and counters
    """
        return self.__counters

    def _set_counters(self, v, load=False):
        """
    Setter method for counters, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/state/counters (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_counters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_counters() directly.

    YANG Description: Interface specific RSVP statistics and counters
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=counters.counters,
                is_container="container",
                yang_name="counters",
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
                    "error-string": """counters must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__counters = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_counters(self):
        self.__counters = YANGDynClass(
            base=counters.counters,
            is_container="container",
            yang_name="counters",
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

    interface_id = __builtin__.property(_get_interface_id)
    counters = __builtin__.property(_get_counters)

    _pyangbind_elements = OrderedDict(
        [("interface_id", interface_id), ("counters", counters)]
    )


from . import counters


class state(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/interface-attributes/interface/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Per-interface RSVP protocol and state information
  """
    __slots__ = ("_path_helper", "_extmethods", "__interface_id", "__counters")

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__interface_id = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="interface-id",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-if:interface-id",
            is_config=False,
        )
        self.__counters = YANGDynClass(
            base=counters.counters,
            is_container="container",
            yang_name="counters",
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
                "mpls",
                "signaling-protocols",
                "rsvp-te",
                "interface-attributes",
                "interface",
                "state",
            ]

    def _get_interface_id(self):
        """
    Getter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/state/interface_id (oc-if:interface-id)

    YANG Description: Identifier for the interface
    """
        return self.__interface_id

    def _set_interface_id(self, v, load=False):
        """
    Setter method for interface_id, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/state/interface_id (oc-if:interface-id)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_id() directly.

    YANG Description: Identifier for the interface
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=six.text_type,
                is_leaf=True,
                yang_name="interface-id",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="oc-if:interface-id",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """interface_id must be of a type compatible with oc-if:interface-id""",
                    "defined-type": "oc-if:interface-id",
                    "generated-type": """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="interface-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-if:interface-id', is_config=False)""",
                }
            )

        self.__interface_id = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_interface_id(self):
        self.__interface_id = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="interface-id",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-if:interface-id",
            is_config=False,
        )

    def _get_counters(self):
        """
    Getter method for counters, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/state/counters (container)

    YANG Description: Interface specific RSVP statistics and counters
    """
        return self.__counters

    def _set_counters(self, v, load=False):
        """
    Setter method for counters, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/interface_attributes/interface/state/counters (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_counters is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_counters() directly.

    YANG Description: Interface specific RSVP statistics and counters
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=counters.counters,
                is_container="container",
                yang_name="counters",
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
                    "error-string": """counters must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=counters.counters, is_container='container', yang_name="counters", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=False)""",
                }
            )

        self.__counters = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_counters(self):
        self.__counters = YANGDynClass(
            base=counters.counters,
            is_container="container",
            yang_name="counters",
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

    interface_id = __builtin__.property(_get_interface_id)
    counters = __builtin__.property(_get_counters)

    _pyangbind_elements = OrderedDict(
        [("interface_id", interface_id), ("counters", counters)]
    )
