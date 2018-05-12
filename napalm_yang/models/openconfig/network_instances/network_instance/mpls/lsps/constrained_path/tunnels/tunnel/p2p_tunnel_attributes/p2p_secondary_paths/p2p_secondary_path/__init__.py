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

from . import config
from . import state
from . import admin_groups


class p2p_secondary_path(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-secondary-paths/p2p-secondary-path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of p2p primary paths for a tunnel
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__name", "__config", "__state", "__admin_groups"
    )

    _yang_name = "p2p-secondary-path"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__name = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            is_keyval=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="leafref",
            is_config=True,
        )
        self.__config = YANGDynClass(
            base=config.config,
            is_container="container",
            yang_name="config",
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
        self.__admin_groups = YANGDynClass(
            base=admin_groups.admin_groups,
            is_container="container",
            yang_name="admin-groups",
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
                "lsps",
                "constrained-path",
                "tunnels",
                "tunnel",
                "p2p-tunnel-attributes",
                "p2p-secondary-paths",
                "p2p-secondary-path",
            ]

    def _get_name(self):
        """
    Getter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/name (leafref)

    YANG Description: Path name
    """
        return self.__name

    def _set_name(self, v, load=False):
        """
    Setter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Path name
    """
        parent = getattr(self, "_parent", None)
        if parent is not None and load is False:
            raise AttributeError(
                "Cannot set keys directly when" + " within an instantiated list"
            )

        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=six.text_type,
                is_leaf=True,
                yang_name="name",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                is_keyval=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="leafref",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """name must be of a type compatible with leafref""",
                    "defined-type": "leafref",
                    "generated-type": """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
                }
            )

        self.__name = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_name(self):
        self.__name = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            is_keyval=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="leafref",
            is_config=True,
        )

    def _get_config(self):
        """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/config (container)

    YANG Description: Configuration parameters related to paths
    """
        return self.__config

    def _set_config(self, v, load=False):
        """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters related to paths
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=config.config,
                is_container="container",
                yang_name="config",
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
                    "error-string": """config must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__config = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_config(self):
        self.__config = YANGDynClass(
            base=config.config,
            is_container="container",
            yang_name="config",
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
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/state (container)

    YANG Description: State parameters related to paths
    """
        return self.__state

    def _set_state(self, v, load=False):
        """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters related to paths
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

    def _get_admin_groups(self):
        """
    Getter method for admin_groups, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/admin_groups (container)

    YANG Description: Top-level container for include/exclude constraints for
link affinities
    """
        return self.__admin_groups

    def _set_admin_groups(self, v, load=False):
        """
    Setter method for admin_groups, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/admin_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_admin_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_admin_groups() directly.

    YANG Description: Top-level container for include/exclude constraints for
link affinities
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=admin_groups.admin_groups,
                is_container="container",
                yang_name="admin-groups",
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
                    "error-string": """admin_groups must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=admin_groups.admin_groups, is_container='container', yang_name="admin-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__admin_groups = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_admin_groups(self):
        self.__admin_groups = YANGDynClass(
            base=admin_groups.admin_groups,
            is_container="container",
            yang_name="admin-groups",
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

    name = __builtin__.property(_get_name, _set_name)
    config = __builtin__.property(_get_config, _set_config)
    state = __builtin__.property(_get_state, _set_state)
    admin_groups = __builtin__.property(_get_admin_groups, _set_admin_groups)

    _pyangbind_elements = OrderedDict(
        [
            ("name", name),
            ("config", config),
            ("state", state),
            ("admin_groups", admin_groups),
        ]
    )


from . import config
from . import state
from . import admin_groups


class p2p_secondary_path(PybindBase):
    """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module openconfig-network-instance-l2 - based on the path /network-instances/network-instance/mpls/lsps/constrained-path/tunnels/tunnel/p2p-tunnel-attributes/p2p-secondary-paths/p2p-secondary-path. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: List of p2p primary paths for a tunnel
  """
    __slots__ = (
        "_path_helper", "_extmethods", "__name", "__config", "__state", "__admin_groups"
    )

    _yang_name = "p2p-secondary-path"

    _pybind_generated_by = "container"

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__name = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            is_keyval=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="leafref",
            is_config=True,
        )
        self.__config = YANGDynClass(
            base=config.config,
            is_container="container",
            yang_name="config",
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
        self.__admin_groups = YANGDynClass(
            base=admin_groups.admin_groups,
            is_container="container",
            yang_name="admin-groups",
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
                "lsps",
                "constrained-path",
                "tunnels",
                "tunnel",
                "p2p-tunnel-attributes",
                "p2p-secondary-paths",
                "p2p-secondary-path",
            ]

    def _get_name(self):
        """
    Getter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/name (leafref)

    YANG Description: Path name
    """
        return self.__name

    def _set_name(self, v, load=False):
        """
    Setter method for name, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/name (leafref)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: Path name
    """
        parent = getattr(self, "_parent", None)
        if parent is not None and load is False:
            raise AttributeError(
                "Cannot set keys directly when" + " within an instantiated list"
            )

        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=six.text_type,
                is_leaf=True,
                yang_name="name",
                parent=self,
                path_helper=self._path_helper,
                extmethods=self._extmethods,
                register_paths=True,
                is_keyval=True,
                namespace="http://openconfig.net/yang/network-instance",
                defining_module="openconfig-network-instance",
                yang_type="leafref",
                is_config=True,
            )
        except (TypeError, ValueError):
            raise ValueError(
                {
                    "error-string": """name must be of a type compatible with leafref""",
                    "defined-type": "leafref",
                    "generated-type": """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='leafref', is_config=True)""",
                }
            )

        self.__name = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_name(self):
        self.__name = YANGDynClass(
            base=six.text_type,
            is_leaf=True,
            yang_name="name",
            parent=self,
            path_helper=self._path_helper,
            extmethods=self._extmethods,
            register_paths=True,
            is_keyval=True,
            namespace="http://openconfig.net/yang/network-instance",
            defining_module="openconfig-network-instance",
            yang_type="leafref",
            is_config=True,
        )

    def _get_config(self):
        """
    Getter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/config (container)

    YANG Description: Configuration parameters related to paths
    """
        return self.__config

    def _set_config(self, v, load=False):
        """
    Setter method for config, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_config() directly.

    YANG Description: Configuration parameters related to paths
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=config.config,
                is_container="container",
                yang_name="config",
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
                    "error-string": """config must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=config.config, is_container='container', yang_name="config", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__config = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_config(self):
        self.__config = YANGDynClass(
            base=config.config,
            is_container="container",
            yang_name="config",
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
    Getter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/state (container)

    YANG Description: State parameters related to paths
    """
        return self.__state

    def _set_state(self, v, load=False):
        """
    Setter method for state, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/state (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_state() directly.

    YANG Description: State parameters related to paths
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

    def _get_admin_groups(self):
        """
    Getter method for admin_groups, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/admin_groups (container)

    YANG Description: Top-level container for include/exclude constraints for
link affinities
    """
        return self.__admin_groups

    def _set_admin_groups(self, v, load=False):
        """
    Setter method for admin_groups, mapped from YANG variable /network_instances/network_instance/mpls/lsps/constrained_path/tunnels/tunnel/p2p_tunnel_attributes/p2p_secondary_paths/p2p_secondary_path/admin_groups (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_admin_groups is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_admin_groups() directly.

    YANG Description: Top-level container for include/exclude constraints for
link affinities
    """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(
                v,
                base=admin_groups.admin_groups,
                is_container="container",
                yang_name="admin-groups",
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
                    "error-string": """admin_groups must be of a type compatible with container""",
                    "defined-type": "container",
                    "generated-type": """YANGDynClass(base=admin_groups.admin_groups, is_container='container', yang_name="admin-groups", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://openconfig.net/yang/network-instance', defining_module='openconfig-network-instance', yang_type='container', is_config=True)""",
                }
            )

        self.__admin_groups = t
        if hasattr(self, "_set"):
            self._set()

    def _unset_admin_groups(self):
        self.__admin_groups = YANGDynClass(
            base=admin_groups.admin_groups,
            is_container="container",
            yang_name="admin-groups",
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

    name = __builtin__.property(_get_name, _set_name)
    config = __builtin__.property(_get_config, _set_config)
    state = __builtin__.property(_get_state, _set_state)
    admin_groups = __builtin__.property(_get_admin_groups, _set_admin_groups)

    _pyangbind_elements = OrderedDict(
        [
            ("name", name),
            ("config", config),
            ("state", state),
            ("admin_groups", admin_groups),
        ]
    )
