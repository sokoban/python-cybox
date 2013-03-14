#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#
# Generated Tue Nov 06 14:02:22 2012 by generateDS.py version 2.7c.
#

import sys
import getopt
import re as re_

import cybox_common_types_1_0
import disk_partition_object_1_3

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    if Verbose_import_:
        print('Error: LXML version 2.3+ required for parsing files')

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

    class GeneratedsSuper(object):
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_validate_integer(self, input_data, node, input_name=''):
            return input_data
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_integer_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of integers')
            return input_data
        def gds_format_float(self, input_data, input_name=''):
            return '%f' % input_data
        def gds_validate_float(self, input_data, node, input_name=''):
            return input_data
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_float_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of floats')
            return input_data
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_validate_double(self, input_data, node, input_name=''):
            return input_data
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_double_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    fvalue = float(value)
                except (TypeError, ValueError), exp:
                    raise_parse_error(node, 'Requires sequence of doubles')
            return input_data
        def gds_format_boolean(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean(self, input_data, node, input_name=''):
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % input_data
        def gds_validate_boolean_list(self, input_data, node, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in ('true', '1', 'false', '0', ):
                    raise_parse_error(node, 'Requires sequence of booleans ("true", "1", "false", "0")')
            return input_data
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'utf-8'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1

def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip(): 
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (self.name, self.value, self.name))
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n' % \
                (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container

def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

class PartitionListType(GeneratedsSuper):
    """The PartionListType type specifies a list of partitions."""
    subclass = None
    superclass = None
    def __init__(self, Partition=None):
        if Partition is None:
            self.Partition = []
        else:
            self.Partition = Partition
    def factory(*args_, **kwargs_):
        if PartitionListType.subclass:
            return PartitionListType.subclass(*args_, **kwargs_)
        else:
            return PartitionListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Partition(self): return self.Partition
    def set_Partition(self, Partition): self.Partition = Partition
    def add_Partition(self, value): self.Partition.append(value)
    def insert_Partition(self, index, value): self.Partition[index] = value
    def export(self, outfile, level, namespace_='DiskObj:', name_='PartitionListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='PartitionListType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='DiskObj:', name_='PartitionListType'):
        pass
    def exportChildren(self, outfile, level, namespace_='DiskObj:', name_='PartitionListType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Partition_ in self.Partition:
            Partition_.export(outfile, level, 'DiskObj:', name_='Partition', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Partition
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='PartitionListType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Partition=[\n')
        level += 1
        for Partition_ in self.Partition:
            showIndent(outfile, level)
            outfile.write('model_.disk_partition_object_1_3.DiskPartitionObjectType(\n')
            Partition_.exportLiteral(outfile, level, name_='disk_partition_object_1_3.DiskPartitionObjectType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Partition':
            obj_ = disk_partition_object_1_3.DiskPartitionObjectType.factory()
            obj_.build(child_)
            self.Partition.append(obj_)
# end class PartitionListType

class DiskType(cybox_common_types_1_0.BaseObjectAttributeType):
    """DiskType specifies disk types, via a union of the DiskTypeEnum type
    and the atomic xs:string type. Its base type is the CybOX Core
    cybox_common_types_1_0.BaseObjectAttributeType, for permitting complex (i.e. regular-
    expression based) specifications.This attribute is optional and
    specifies the expected type for the value of the specified
    element."""
    subclass = None
    superclass = cybox_common_types_1_0.BaseObjectAttributeType
    def __init__(self, end_range=None, pattern_type=None, has_changed=None, value_set=None, datatype='String', refanging_transform=None, refanging_transform_type=None, appears_random=None, trend=None, defanging_algorithm_ref=None, is_obfuscated=None, regex_syntax=None, obfuscation_algorithm_ref=None, start_range=None, idref=None, is_defanged=None, id=None, condition=None, valueOf_=None):
        super(DiskType, self).__init__(end_range, pattern_type, has_changed, value_set, datatype, refanging_transform, refanging_transform_type, appears_random, trend, defanging_algorithm_ref, is_obfuscated, regex_syntax, obfuscation_algorithm_ref, start_range, idref, is_defanged, id, condition, valueOf_, )
        self.datatype = _cast(None, datatype)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if DiskType.subclass:
            return DiskType.subclass(*args_, **kwargs_)
        else:
            return DiskType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_datatype(self): return self.datatype
    def set_datatype(self, datatype): self.datatype = datatype
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def export(self, outfile, level, namespace_='DiskObj:', name_='DiskType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DiskType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(str(self.valueOf_).encode(ExternalEncoding))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='DiskObj:', name_='DiskType'):
        super(DiskType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DiskType')
        if self.datatype is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            outfile.write(' datatype=%s' % (quote_attrib(self.datatype), ))
    def exportChildren(self, outfile, level, namespace_='DiskObj:', name_='DiskType', fromsubclass_=False, pretty_print=True):
        super(DiskType, self).exportChildren(outfile, level, 'DiskObj:', name_, True, pretty_print=pretty_print)
        pass
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(DiskType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DiskType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.datatype is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            showIndent(outfile, level)
            outfile.write('datatype = %s,\n' % (self.datatype,))
        super(DiskType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(DiskType, self).exportLiteralChildren(outfile, level, name_)
        pass
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('datatype', node)
        if value is not None and 'datatype' not in already_processed:
            already_processed.append('datatype')
            self.datatype = value
        super(DiskType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DiskType

class DiskObjectType(cybox_common_types_1_0.DefinedObjectType):
    """The DiskObjectType type is intended to characterize disk drives."""
    subclass = None
    superclass = cybox_common_types_1_0.DefinedObjectType
    def __init__(self, object_reference=None, Disk_Name=None, Disk_Size=None, Free_Space=None, Partition_List=None, Type=None):
        super(DiskObjectType, self).__init__(object_reference, )
        self.Disk_Name = Disk_Name
        self.Disk_Size = Disk_Size
        self.Free_Space = Free_Space
        self.Partition_List = Partition_List
        self.Type = Type
    def factory(*args_, **kwargs_):
        if DiskObjectType.subclass:
            return DiskObjectType.subclass(*args_, **kwargs_)
        else:
            return DiskObjectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Disk_Name(self): return self.Disk_Name
    def set_Disk_Name(self, Disk_Name): self.Disk_Name = Disk_Name
    def validate_StringObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.StringObjectAttributeType, a restriction on None.
        pass
    def get_Disk_Size(self): return self.Disk_Size
    def set_Disk_Size(self, Disk_Size): self.Disk_Size = Disk_Size
    def validate_UnsignedLongObjectAttributeType(self, value):
        # Validate type cybox_common_types_1_0.UnsignedLongObjectAttributeType, a restriction on None.
        pass
    def get_Free_Space(self): return self.Free_Space
    def set_Free_Space(self, Free_Space): self.Free_Space = Free_Space
    def get_Partition_List(self): return self.Partition_List
    def set_Partition_List(self, Partition_List): self.Partition_List = Partition_List
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def validate_DiskType(self, value):
        # Validate type DiskType, a restriction on None.
        pass
    def export(self, outfile, level, namespace_='DiskObj:', name_='DiskObjectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespace_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = []
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='DiskObjectType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespace_, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespace_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_='DiskObj:', name_='DiskObjectType'):
        super(DiskObjectType, self).exportAttributes(outfile, level, already_processed, namespace_, name_='DiskObjectType')
    def exportChildren(self, outfile, level, namespace_='DiskObj:', name_='DiskObjectType', fromsubclass_=False, pretty_print=True):
        super(DiskObjectType, self).exportChildren(outfile, level, 'DiskObj:', name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Disk_Name is not None:
            self.Disk_Name.export(outfile, level, 'DiskObj:', name_='Disk_Name', pretty_print=pretty_print)
        if self.Disk_Size is not None:
            self.Disk_Size.export(outfile, level, 'DiskObj:', name_='Disk_Size', pretty_print=pretty_print)
        if self.Free_Space is not None:
            self.Free_Space.export(outfile, level, 'DiskObj:', name_='Free_Space', pretty_print=pretty_print)
        if self.Partition_List is not None:
            self.Partition_List.export(outfile, level, 'DiskObj:', name_='Partition_List', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(outfile, level, 'DiskObj:', name_='Type', pretty_print=pretty_print)
    def hasContent_(self):
        if (
            self.Disk_Name is not None or
            self.Disk_Size is not None or
            self.Free_Space is not None or
            self.Partition_List is not None or
            self.Type is not None or
            super(DiskObjectType, self).hasContent_()
            ):
            return True
        else:
            return False
    def exportLiteral(self, outfile, level, name_='DiskObjectType'):
        level += 1
        self.exportLiteralAttributes(outfile, level, [], name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(DiskObjectType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(DiskObjectType, self).exportLiteralChildren(outfile, level, name_)
        if self.Disk_Name is not None:
            showIndent(outfile, level)
            outfile.write('Disk_Name=model_.cybox_common_types_1_0.StringObjectAttributeType(\n')
            self.Disk_Name.exportLiteral(outfile, level, name_='Disk_Name')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Disk_Size is not None:
            showIndent(outfile, level)
            outfile.write('Disk_Size=model_.cybox_common_types_1_0.UnsignedLongObjectAttributeType(\n')
            self.Disk_Size.exportLiteral(outfile, level, name_='Disk_Size')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Free_Space is not None:
            showIndent(outfile, level)
            outfile.write('Free_Space=model_.cybox_common_types_1_0.UnsignedLongObjectAttributeType(\n')
            self.Free_Space.exportLiteral(outfile, level, name_='Free_Space')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Partition_List is not None:
            showIndent(outfile, level)
            outfile.write('Partition_List=model_.PartitionListType(\n')
            self.Partition_List.exportLiteral(outfile, level, name_='Partition_List')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.Type is not None:
            showIndent(outfile, level)
            outfile.write('Type=model_.DiskType(\n')
            self.Type.exportLiteral(outfile, level, name_='Type')
            showIndent(outfile, level)
            outfile.write('),\n')
    def build(self, node):
        self.buildAttributes(node, node.attrib, [])
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DiskObjectType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Disk_Name':
            obj_ = cybox_common_types_1_0.StringObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Disk_Name(obj_)
        elif nodeName_ == 'Disk_Size':
            obj_ = cybox_common_types_1_0.UnsignedLongObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Disk_Size(obj_)
        elif nodeName_ == 'Free_Space':
            obj_ = cybox_common_types_1_0.UnsignedLongObjectAttributeType.factory()
            obj_.build(child_)
            self.set_Free_Space(obj_)
        elif nodeName_ == 'Partition_List':
            obj_ = PartitionListType.factory()
            obj_.build(child_)
            self.set_Partition_List(obj_)
        elif nodeName_ == 'Type':
            obj_ = DiskType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        super(DiskObjectType, self).buildChildren(child_, node, nodeName_, True)
# end class DiskObjectType

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print(USAGE_TEXT)
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Disk'
        rootClass = DiskObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Disk'
        rootClass = DiskObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="Disk",
        namespacedef_='')
    return rootObj

def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Disk'
        rootClass = DiskObjectType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from temp import *\n\n')
    sys.stdout.write('import temp as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "DiskObjectType",
    "PartitionListType",
    "DiskType"
    ]