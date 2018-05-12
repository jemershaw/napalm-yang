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

from . import graceful_restart
from . import soft_preemption
from . import hellos
from . import state


class global_(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/global. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Platform wide RSVP configuration and state
  """
    __slots__ = (
        "_path_helper",
        "_extmethods",
        "__graceful_restart",
        "__soft_preemption",
        "__hellos",
        "__state",
    )

    _yang_name = "global"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__graceful_restart = YANGDynClass(
            base=graceful_restart.graceful_restart,
            is_container="container",
            yang_name="graceful-restart",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
        self.__soft_preemption = YANGDynClass(
            base=soft_preemption.soft_preemption,
            is_container="container",
            yang_name="soft-preemption",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
        self.__hellos = YANGDynClass(
            base=hellos.hellos,
            is_container="container",
            yang_name="hellos",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
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
                "mpls",
                "signaling-protocols",
                "rsvp-te",
                "global",
            ]

    def _get_graceful_restart(self):
        """
    Getter method for graceful_restart, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/graceful_restart (container)

    YANG Description: Operational state and configuration parameters relating to
graceful-restart for RSVP
    """
        return self.__graceful_restart

    def _set_graceful_restart(self, v, load=False):
        """
    Setter method for graceful_restart, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/graceful_restart (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_graceful_restart is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_graceful_restart() directly.

    YANG Description: Operational state and configuration parameters relating to
graceful-restart for RSVP
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=graceful_restart.graceful_restart,
                is_container="container",
                yang_name="graceful-restart",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """graceful_restart must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__graceful_restart = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_graceful_restart(self):
        self.__graceful_restart = YANGDynClass(
            base=graceful_restart.graceful_restart,
            is_container="container",
            yang_name="graceful-restart",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_soft_preemption(self):
        """
    Getter method for soft_preemption, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption (container)

    YANG Description: Protocol options relating to RSVP
soft preemption
    """
        return self.__soft_preemption

    def _set_soft_preemption(self, v, load=False):
        """
    Setter method for soft_preemption, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_soft_preemption is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_soft_preemption() directly.

    YANG Description: Protocol options relating to RSVP
soft preemption
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=soft_preemption.soft_preemption,
                is_container="container",
                yang_name="soft-preemption",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """soft_preemption must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=soft_preemption.soft_preemption, is_container='container', yang_name="soft-preemption", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__soft_preemption = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_soft_preemption(self):
        self.__soft_preemption = YANGDynClass(
            base=soft_preemption.soft_preemption,
            is_container="container",
            yang_name="soft-preemption",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_hellos(self):
        """
    Getter method for hellos, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/hellos (container)

    YANG Description: Top level container for RSVP hello parameters
    """
        return self.__hellos

    def _set_hellos(self, v, load=False):
        """
    Setter method for hellos, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/hellos (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hellos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hellos() directly.

    YANG Description: Top level container for RSVP hello parameters
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=hellos.hellos,
                is_container="container",
                yang_name="hellos",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """hellos must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=hellos.hellos, is_container='container', yang_name="hellos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__hellos = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_hellos(self):
        self.__hellos = YANGDynClass(
            base=hellos.hellos,
            is_container="container",
            yang_name="hellos",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_state(self):
        """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/state (container)

    YANG Description: Platform wide RSVP state, including counters
    """
        return self.__state

    def _set_state(self, v, load=False):
        """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Platform wide RSVP state, including counters
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
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """state must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
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
            is_config=True,
        )

    graceful_restart = __builtin__.property(
        _get_graceful_restart, _set_graceful_restart
    )
    soft_preemption = __builtin__.property(_get_soft_preemption, _set_soft_preemption)
    hellos = __builtin__.property(_get_hellos, _set_hellos)
    state = __builtin__.property(_get_state, _set_state)

    _pyangbind_elements = OrderedDict(
        [
            ("graceful_restart", graceful_restart),
            ("soft_preemption", soft_preemption),
            ("hellos", hellos),
            ("state", state),
        ]
    )


from . import graceful_restart
from . import soft_preemption
from . import hellos
from . import state


class global_(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/signaling-protocols/rsvp-te/global. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Platform wide RSVP configuration and state
  """
    __slots__ = (
        "_path_helper",
        "_extmethods",
        "__graceful_restart",
        "__soft_preemption",
        "__hellos",
        "__state",
    )

    _yang_name = "global"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__graceful_restart = YANGDynClass(
            base=graceful_restart.graceful_restart,
            is_container="container",
            yang_name="graceful-restart",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
        self.__soft_preemption = YANGDynClass(
            base=soft_preemption.soft_preemption,
            is_container="container",
            yang_name="soft-preemption",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
        self.__hellos = YANGDynClass(
            base=hellos.hellos,
            is_container="container",
            yang_name="hellos",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )
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
                "mpls",
                "signaling-protocols",
                "rsvp-te",
                "global",
            ]

    def _get_graceful_restart(self):
        """
    Getter method for graceful_restart, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/graceful_restart (container)

    YANG Description: Operational state and configuration parameters relating to
graceful-restart for RSVP
    """
        return self.__graceful_restart

    def _set_graceful_restart(self, v, load=False):
        """
    Setter method for graceful_restart, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/graceful_restart (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_graceful_restart is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_graceful_restart() directly.

    YANG Description: Operational state and configuration parameters relating to
graceful-restart for RSVP
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=graceful_restart.graceful_restart,
                is_container="container",
                yang_name="graceful-restart",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """graceful_restart must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=graceful_restart.graceful_restart, is_container='container', yang_name="graceful-restart", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__graceful_restart = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_graceful_restart(self):
        self.__graceful_restart = YANGDynClass(
            base=graceful_restart.graceful_restart,
            is_container="container",
            yang_name="graceful-restart",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_soft_preemption(self):
        """
    Getter method for soft_preemption, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption (container)

    YANG Description: Protocol options relating to RSVP
soft preemption
    """
        return self.__soft_preemption

    def _set_soft_preemption(self, v, load=False):
        """
    Setter method for soft_preemption, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/soft_preemption (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_soft_preemption is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_soft_preemption() directly.

    YANG Description: Protocol options relating to RSVP
soft preemption
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=soft_preemption.soft_preemption,
                is_container="container",
                yang_name="soft-preemption",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """soft_preemption must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=soft_preemption.soft_preemption, is_container='container', yang_name="soft-preemption", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__soft_preemption = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_soft_preemption(self):
        self.__soft_preemption = YANGDynClass(
            base=soft_preemption.soft_preemption,
            is_container="container",
            yang_name="soft-preemption",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_hellos(self):
        """
    Getter method for hellos, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/hellos (container)

    YANG Description: Top level container for RSVP hello parameters
    """
        return self.__hellos

    def _set_hellos(self, v, load=False):
        """
    Setter method for hellos, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/hellos (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hellos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hellos() directly.

    YANG Description: Top level container for RSVP hello parameters
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=hellos.hellos,
                is_container="container",
                yang_name="hellos",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                extensions=None,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="container",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """hellos must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=hellos.hellos, is_container='container', yang_name="hellos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__hellos = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_hellos(self):
        self.__hellos = YANGDynClass(
            base=hellos.hellos,
            is_container="container",
            yang_name="hellos",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            extensions=None,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="container",
            is_config=True,
        )

    def _get_state(self):
        """
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/state (container)

    YANG Description: Platform wide RSVP state, including counters
    """
        return self.__state

    def _set_state(self, v, load=False):
        """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/signaling_protocols/rsvp_te/global/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: Platform wide RSVP state, including counters
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
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """state must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=state.state, is_container='container', yang_name="state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
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
            is_config=True,
        )

    graceful_restart = __builtin__.property(
        _get_graceful_restart, _set_graceful_restart
    )
    soft_preemption = __builtin__.property(_get_soft_preemption, _set_soft_preemption)
    hellos = __builtin__.property(_get_hellos, _set_hellos)
    state = __builtin__.property(_get_state, _set_state)

    _pyangbind_elements = OrderedDict(
        [
            ("graceful_restart", graceful_restart),
            ("soft_preemption", soft_preemption),
            ("hellos", hellos),
            ("state", state),
        ]
    )
