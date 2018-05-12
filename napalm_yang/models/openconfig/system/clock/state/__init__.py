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
  from YANG module openconfig-system - based on the path /system/clock/state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Operational state data for system clock
  """
    __slots__ = ("_path_helper", "_extmethods", "__timezone_name")

    _yang_name = "state"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__timezone_name = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="timezone-name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="timezone-name-type",
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
            return ["system", "clock", "state"]

    def _get_timezone_name(self):
        """
    Getter method for timezone_name, mapped from YANG variable /system/clock/state/timezone_name (timezone-name-type)

    YANG Description: The TZ database name to use for the system, such
as 'Europe/Stockholm'.
    """
        return self.__timezone_name

    def _set_timezone_name(self, v, load=False):
        """
    Setter method for timezone_name, mapped from YANG variable /system/clock/state/timezone_name (timezone-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timezone_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timezone_name() directly.

    YANG Description: The TZ database name to use for the system, such
as 'Europe/Stockholm'.
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=six.text_type,
                is_leaf=True,
                yang_name="timezone-name",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                namespace="http://openconfig.net/yang/system",
                defining_module="openconfig-system",
                yang_type="timezone-name-type",
                is_config=False,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """timezone_name must be of a type compatible with timezone-name-type""",
                    "defined-type": "openconfig-system:timezone-name-type",
                    "generated-type": """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="timezone-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://openconfig.net/yang/system', defining_module='openconfig-system', yang_type='timezone-name-type', is_config=False)""",
                }
            )

        self.__timezone_name = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_timezone_name(self):
        self.__timezone_name = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="timezone-name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            namespace="http://openconfig.net/yang/system",
            defining_module="openconfig-system",
            yang_type="timezone-name-type",
            is_config=False,
        )

    timezone_name = __builtin__.property(_get_timezone_name)

    _pyangbind_elements = OrderedDict([("timezone_name", timezone_name)])
