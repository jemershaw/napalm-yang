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


class state(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/ipv4-internal-reachability/prefixes/prefixes/default-metric/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters for default-metric.
  """
    __slots__ = ("_path_helper", "_extmethods", "__flags", "__default_metric")

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__flags = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={"INTERNAL": {}},
            ),
            is_leaf=True,
            yang_name="flags",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="enumeration",
            is_config=False,
        )
        self.__default_metric = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..63"]},
            ),
            is_leaf=True,
            yang_name="default-metric",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-isis-types:narrow-metric",
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
                "ipv4-internal-reachability",
                "prefixes",
                "prefixes",
                "default-metric",
                "state",
            ]

    def _get_flags(self):
        """
    Getter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/default_metric/state/flags (enumeration)

    YANG Description: ISIS Default-Metric Flags.
    """
        return self.__flags

    def _set_flags(self, v, load=False):
        """
    Setter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/default_metric/state/flags (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flags() directly.

    YANG Description: ISIS Default-Metric Flags.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=six.text_type,
                    restriction_type="dict_key",
                    restriction_arg={"INTERNAL": {}},
                ),
                is_leaf=True,
                yang_name="flags",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="enumeration",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """flags must be of a type compatible with enumeration""",
                    "defined-type": "openconfig-network-instance:enumeration",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'INTERNAL': {}},), is_leaf=True, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
                }
            )

        self.__flags = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_flags(self):
        self.__flags = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={"INTERNAL": {}},
            ),
            is_leaf=True,
            yang_name="flags",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="enumeration",
            is_config=False,
        )

    def _get_default_metric(self):
        """
    Getter method for default_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/default_metric/state/default_metric (oc-isis-types:narrow-metric)

    YANG Description: ISIS default metric value. This is a metric understood by every
Intermediate system in the domain. Each circuit shall have a
positive  integral value assigned for this metric. The value may be
associated with any  objective function of the circuit, but by
convention is intended to measure the capacity of the circuit for
handling traffic, for example, its throughput in  bits-per-second.
Higher values indicate a lower capacity.
    """
        return self.__default_metric

    def _set_default_metric(self, v, load=False):
        """
    Setter method for default_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/default_metric/state/default_metric (oc-isis-types:narrow-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_metric() directly.

    YANG Description: ISIS default metric value. This is a metric understood by every
Intermediate system in the domain. Each circuit shall have a
positive  integral value assigned for this metric. The value may be
associated with any  objective function of the circuit, but by
convention is intended to measure the capacity of the circuit for
handling traffic, for example, its throughput in  bits-per-second.
Higher values indicate a lower capacity.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=RestrictedClassType(
                        base_type=int,
                        restriction_dict={"range": ["0..255"]},
                        int_size=8,
                    ),
                    restriction_dict={"range": ["1..63"]},
                ),
                is_leaf=True,
                yang_name="default-metric",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="oc-isis-types:narrow-metric",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """default_metric must be of a type compatible with oc-isis-types:narrow-metric""",
                    "defined-type": "oc-isis-types:narrow-metric",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..63']}), is_leaf=True, yang_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:narrow-metric', is_config=False)""",
                }
            )

        self.__default_metric = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_default_metric(self):
        self.__default_metric = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..63"]},
            ),
            is_leaf=True,
            yang_name="default-metric",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-isis-types:narrow-metric",
            is_config=False,
        )

    flags = __builtin__.property(_get_flags)
    default_metric = __builtin__.property(_get_default_metric)

    _pyangbind_elements = OrderedDict(
        [("flags", flags), ("default_metric", default_metric)]
    )


class state(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/protocols/protocol/isis/levels/level/link-state-database/lsp/tlvs/tlv/ipv4-internal-reachability/prefixes/prefixes/default-metric/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: State parameters for default-metric.
  """
    __slots__ = ("_path_helper", "_extmethods", "__flags", "__default_metric")

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__flags = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={"INTERNAL": {}},
            ),
            is_leaf=True,
            yang_name="flags",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="enumeration",
            is_config=False,
        )
        self.__default_metric = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..63"]},
            ),
            is_leaf=True,
            yang_name="default-metric",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-isis-types:narrow-metric",
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
                "ipv4-internal-reachability",
                "prefixes",
                "prefixes",
                "default-metric",
                "state",
            ]

    def _get_flags(self):
        """
    Getter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/default_metric/state/flags (enumeration)

    YANG Description: ISIS Default-Metric Flags.
    """
        return self.__flags

    def _set_flags(self, v, load=False):
        """
    Setter method for flags, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/default_metric/state/flags (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flags() directly.

    YANG Description: ISIS Default-Metric Flags.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=six.text_type,
                    restriction_type="dict_key",
                    restriction_arg={"INTERNAL": {}},
                ),
                is_leaf=True,
                yang_name="flags",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="enumeration",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """flags must be of a type compatible with enumeration""",
                    "defined-type": "openconfig-network-instance:enumeration",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=six.text_type,                                     restriction_type="dict_key",                                     restriction_arg={'INTERNAL': {}},), is_leaf=True, yang_name="flags", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='enumeration', is_config=False)""",
                }
            )

        self.__flags = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_flags(self):
        self.__flags = YANGDynClass(
            base=RestrictedClassType(
                base_type=six.text_type,
                restriction_type="dict_key",
                restriction_arg={"INTERNAL": {}},
            ),
            is_leaf=True,
            yang_name="flags",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="enumeration",
            is_config=False,
        )

    def _get_default_metric(self):
        """
    Getter method for default_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/default_metric/state/default_metric (oc-isis-types:narrow-metric)

    YANG Description: ISIS default metric value. This is a metric understood by every
Intermediate system in the domain. Each circuit shall have a
positive  integral value assigned for this metric. The value may be
associated with any  objective function of the circuit, but by
convention is intended to measure the capacity of the circuit for
handling traffic, for example, its throughput in  bits-per-second.
Higher values indicate a lower capacity.
    """
        return self.__default_metric

    def _set_default_metric(self, v, load=False):
        """
    Setter method for default_metric, mapped from YANG variable /network_instances/network_instance/protocols/protocol/isis/levels/level/link_state_database/lsp/tlvs/tlv/ipv4_internal_reachability/prefixes/prefixes/default_metric/state/default_metric (oc-isis-types:narrow-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_metric is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_metric() directly.

    YANG Description: ISIS default metric value. This is a metric understood by every
Intermediate system in the domain. Each circuit shall have a
positive  integral value assigned for this metric. The value may be
associated with any  objective function of the circuit, but by
convention is intended to measure the capacity of the circuit for
handling traffic, for example, its throughput in  bits-per-second.
Higher values indicate a lower capacity.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=RestrictedClassType(
                    base_type=RestrictedClassType(
                        base_type=int,
                        restriction_dict={"range": ["0..255"]},
                        int_size=8,
                    ),
                    restriction_dict={"range": ["1..63"]},
                ),
                is_leaf=True,
                yang_name="default-metric",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="oc-isis-types:narrow-metric",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """default_metric must be of a type compatible with oc-isis-types:narrow-metric""",
                    "defined-type": "oc-isis-types:narrow-metric",
                    "generated-type": """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': ['1..63']}), is_leaf=True, yang_name="default-metric", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='oc-isis-types:narrow-metric', is_config=False)""",
                }
            )

        self.__default_metric = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_default_metric(self):
        self.__default_metric = YANGDynClass(
            base=RestrictedClassType(
                base_type=RestrictedClassType(
                    base_type=int, restriction_dict={"range": ["0..255"]}, int_size=8
                ),
                restriction_dict={"range": ["1..63"]},
            ),
            is_leaf=True,
            yang_name="default-metric",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="oc-isis-types:narrow-metric",
            is_config=False,
        )

    flags = __builtin__.property(_get_flags)
    default_metric = __builtin__.property(_get_default_metric)

    _pyangbind_elements = OrderedDict(
        [("flags", flags), ("default_metric", default_metric)]
    )
