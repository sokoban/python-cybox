# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import entities
from mixbox import fields

import cybox.bindings.cybox_common as common_binding
from cybox.common import String


class EnvironmentVariable(entities.Entity):
    _namespace = 'http://cybox.mitre.org/common-2'
    _binding = common_binding
    _binding_class = _binding.EnvironmentVariableType

    name = fields.TypedField("name", String)
    value = fields.TypedField("value", String)


class EnvironmentVariableList(entities.EntityList):
    _binding_class = common_binding.EnvironmentVariableListType
    _binding_var = "Environment_Variable"
    _contained_type = EnvironmentVariable
    _namespace = 'http://cybox.mitre.org/common-2'
