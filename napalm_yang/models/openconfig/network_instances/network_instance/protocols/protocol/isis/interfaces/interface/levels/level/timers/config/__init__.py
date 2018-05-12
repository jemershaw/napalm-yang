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


class config(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/timers/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS interface hello-timers configuration.
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__hello_interval", "__hello_multiplier"
    )

    _yang_name = "config"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__hello_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..4294967295"]},
                int_size=32,
            ),
            is_leaf=True,
            yang_name="hello-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint32",
            is_config=True,
        )
        self.__hello_multiplier = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="hello-multiplier",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=True,
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
                "interfaces",
                "interface",
                "levels",
                "level",
                "timers",
                "config",
            ]

    def _get_hello_interval(self):
        """
    Getter method for hello_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/timers/config/hello_interval (uint32)

    YANG Description: ISIS hello-interval value.
    """
        return self.__hello_interval

    def _set_hello_interval(self, v, load=False):
        """
    Setter method for hello_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/timers/config/hello_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_interval() directly.

    YANG Description: ISIS hello-interval value.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..4294967295"]},
                    int_size=32,
                ),
                is_leaf=True,
                yang_name="hello-interval",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint32",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """hello_interval must be of a type compatible with uint32""",
                    "defined-type": "uint32",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
                }
            )

        self.__hello_interval = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_hello_interval(self):
        self.__hello_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..4294967295"]},
                int_size=32,
            ),
            is_leaf=True,
            yang_name="hello-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint32",
            is_config=True,
        )

    def _get_hello_multiplier(self):
        """
    Getter method for hello_multiplier, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/timers/config/hello_multiplier (uint8)

    YANG Description: ISIS hello-multiplier value.
    """
        return self.__hello_multiplier

    def _set_hello_multiplier(self, v, load=False):
        """
    Setter method for hello_multiplier, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/timers/config/hello_multiplier (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_multiplier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_multiplier() directly.

    YANG Description: ISIS hello-multiplier value.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                is_leaf=True,
                yang_name="hello-multiplier",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint8",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """hello_multiplier must be of a type compatible with uint8""",
                    "defined-type": "uint8",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="hello-multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)""",
                }
            )

        self.__hello_multiplier = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_hello_multiplier(self):
        self.__hello_multiplier = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="hello-multiplier",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=True,
        )

    hello_interval = __builtin__.property(_get_hello_interval, _set_hello_interval)
    hello_multiplier = __builtin__.property(
        _get_hello_multiplier, _set_hello_multiplier
    )

    _pyangbind_elements = OrderedDict(
        [("hello_interval", hello_interval), ("hello_multiplier", hello_multiplier)]
    )


class config(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/interfaces/interface/levels/level/timers/config. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This container defines ISIS interface hello-timers configuration.
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__hello_interval", "__hello_multiplier"
    )

    _yang_name = "config"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__hello_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..4294967295"]},
                int_size=32,
            ),
            is_leaf=True,
            yang_name="hello-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint32",
            is_config=True,
        )
        self.__hello_multiplier = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="hello-multiplier",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=True,
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
                "interfaces",
                "interface",
                "levels",
                "level",
                "timers",
                "config",
            ]

    def _get_hello_interval(self):
        """
    Getter method for hello_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/timers/config/hello_interval (uint32)

    YANG Description: ISIS hello-interval value.
    """
        return self.__hello_interval

    def _set_hello_interval(self, v, load=False):
        """
    Setter method for hello_interval, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/timers/config/hello_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_interval() directly.

    YANG Description: ISIS hello-interval value.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..4294967295"]},
                    int_size=32,
                ),
                is_leaf=True,
                yang_name="hello-interval",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint32",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """hello_interval must be of a type compatible with uint32""",
                    "defined-type": "uint32",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint32', is_config=True)""",
                }
            )

        self.__hello_interval = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_hello_interval(self):
        self.__hello_interval = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..4294967295"]},
                int_size=32,
            ),
            is_leaf=True,
            yang_name="hello-interval",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint32",
            is_config=True,
        )

    def _get_hello_multiplier(self):
        """
    Getter method for hello_multiplier, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/timers/config/hello_multiplier (uint8)

    YANG Description: ISIS hello-multiplier value.
    """
        return self.__hello_multiplier

    def _set_hello_multiplier(self, v, load=False):
        """
    Setter method for hello_multiplier, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/interfaces/interface/levels/level/timers/config/hello_multiplier (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_multiplier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_multiplier() directly.

    YANG Description: ISIS hello-multiplier value.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                is_leaf=True,
                yang_name="hello-multiplier",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint8",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """hello_multiplier must be of a type compatible with uint8""",
                    "defined-type": "uint8",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="hello-multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint8', is_config=True)""",
                }
            )

        self.__hello_multiplier = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_hello_multiplier(self):
        self.__hello_multiplier = YANGDynClass(
            base=RestrictedClassType(
                base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
            ),
            is_leaf=True,
            yang_name="hello-multiplier",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint8",
            is_config=True,
        )

    hello_interval = __builtin__.property(_get_hello_interval, _set_hello_interval)
    hello_multiplier = __builtin__.property(
        _get_hello_multiplier, _set_hello_multiplier
    )

    _pyangbind_elements = OrderedDict(
        [("hello_interval", hello_interval), ("hello_multiplier", hello_multiplier)]
    )
