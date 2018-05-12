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


class received(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Counters for BGP messages received from the neighbor
  """
    __slots__ = ("_path_helper", "_extmethods", "__UPDATE", "__NOTIFICATION")

    _yang_name = "received"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__UPDATE = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="UPDATE",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
            is_config=False,
        )
        self.__NOTIFICATION = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="NOTIFICATION",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
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
                "bgp",
                "neighbors",
                "neighbor",
                "state",
                "messages",
                "received",
            ]

    def _get_UPDATE(self):
        """
    Getter method for UPDATE, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/UPDATE (uint64)

    YANG Description: Number of BGP UPDATE messages announcing, withdrawing
or modifying paths exchanged.
    """
        return self.__UPDATE

    def _set_UPDATE(self, v, load=False):
        """
    Setter method for UPDATE, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/UPDATE (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_UPDATE is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_UPDATE() directly.

    YANG Description: Number of BGP UPDATE messages announcing, withdrawing
or modifying paths exchanged.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..18446744073709551615"]},
                    int_size=64,
                ),
                is_leaf=True,
                yang_name="UPDATE",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint64",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """UPDATE must be of a type compatible with uint64""",
                    "defined-type": "uint64",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="UPDATE", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
                }
            )

        self.__UPDATE = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_UPDATE(self):
        self.__UPDATE = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="UPDATE",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
            is_config=False,
        )

    def _get_NOTIFICATION(self):
        """
    Getter method for NOTIFICATION, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/NOTIFICATION (uint64)

    YANG Description: Number of BGP NOTIFICATION messages indicating an
error condition has occurred exchanged.
    """
        return self.__NOTIFICATION

    def _set_NOTIFICATION(self, v, load=False):
        """
    Setter method for NOTIFICATION, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/NOTIFICATION (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_NOTIFICATION is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_NOTIFICATION() directly.

    YANG Description: Number of BGP NOTIFICATION messages indicating an
error condition has occurred exchanged.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..18446744073709551615"]},
                    int_size=64,
                ),
                is_leaf=True,
                yang_name="NOTIFICATION",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint64",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """NOTIFICATION must be of a type compatible with uint64""",
                    "defined-type": "uint64",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="NOTIFICATION", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
                }
            )

        self.__NOTIFICATION = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_NOTIFICATION(self):
        self.__NOTIFICATION = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="NOTIFICATION",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
            is_config=False,
        )

    UPDATE = __builtin__.property(_get_UPDATE)
    NOTIFICATION = __builtin__.property(_get_NOTIFICATION)

    _pyangbind_elements = OrderedDict(
        [("UPDATE", UPDATE), ("NOTIFICATION", NOTIFICATION)]
    )


class received(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Counters for BGP messages received from the neighbor
  """
    __slots__ = ("_path_helper", "_extmethods", "__UPDATE", "__NOTIFICATION")

    _yang_name = "received"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__UPDATE = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="UPDATE",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
            is_config=False,
        )
        self.__NOTIFICATION = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="NOTIFICATION",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
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
                "bgp",
                "neighbors",
                "neighbor",
                "state",
                "messages",
                "received",
            ]

    def _get_UPDATE(self):
        """
    Getter method for UPDATE, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/UPDATE (uint64)

    YANG Description: Number of BGP UPDATE messages announcing, withdrawing
or modifying paths exchanged.
    """
        return self.__UPDATE

    def _set_UPDATE(self, v, load=False):
        """
    Setter method for UPDATE, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/UPDATE (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_UPDATE is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_UPDATE() directly.

    YANG Description: Number of BGP UPDATE messages announcing, withdrawing
or modifying paths exchanged.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..18446744073709551615"]},
                    int_size=64,
                ),
                is_leaf=True,
                yang_name="UPDATE",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint64",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """UPDATE must be of a type compatible with uint64""",
                    "defined-type": "uint64",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="UPDATE", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
                }
            )

        self.__UPDATE = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_UPDATE(self):
        self.__UPDATE = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="UPDATE",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
            is_config=False,
        )

    def _get_NOTIFICATION(self):
        """
    Getter method for NOTIFICATION, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/NOTIFICATION (uint64)

    YANG Description: Number of BGP NOTIFICATION messages indicating an
error condition has occurred exchanged.
    """
        return self.__NOTIFICATION

    def _set_NOTIFICATION(self, v, load=False):
        """
    Setter method for NOTIFICATION, mapped from YANG variable /network_instances/network_instance/protocols/protocol/bgp/neighbors/neighbor/state/messages/received/NOTIFICATION (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_NOTIFICATION is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_NOTIFICATION() directly.

    YANG Description: Number of BGP NOTIFICATION messages indicating an
error condition has occurred exchanged.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=long,
                    restriction_dict={"range": ["0..18446744073709551615"]},
                    int_size=64,
                ),
                is_leaf=True,
                yang_name="NOTIFICATION",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="uint64",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """NOTIFICATION must be of a type compatible with uint64""",
                    "defined-type": "uint64",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="NOTIFICATION", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='uint64', is_config=False)""",
                }
            )

        self.__NOTIFICATION = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_NOTIFICATION(self):
        self.__NOTIFICATION = YANGDynClass(
            base=RestrictedClassType(
                base_type=long,
                restriction_dict={"range": ["0..18446744073709551615"]},
                int_size=64,
            ),
            is_leaf=True,
            yang_name="NOTIFICATION",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="uint64",
            is_config=False,
        )

    UPDATE = __builtin__.property(_get_UPDATE)
    NOTIFICATION = __builtin__.property(_get_NOTIFICATION)

    _pyangbind_elements = OrderedDict(
        [("UPDATE", UPDATE), ("NOTIFICATION", NOTIFICATION)]
    )
