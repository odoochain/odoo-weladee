# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: odoo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import service as _service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import weladee_pb2 as weladee__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='odoo.proto',
  package='grpc.weladee.com',
  syntax='proto3',
  serialized_pb=_b('\n\nodoo.proto\x12\x10grpc.weladee.com\x1a\rweladee.proto\"5\n\x11\x41ttendanceRequest\x12\x0c\n\x04\x46rom\x18\x02 \x01(\x03\x12\x12\n\nEmployeeID\x18\x03 \x01(\x03\"_\n\x0bHolidayOdoo\x12*\n\x07Holiday\x18\x01 \x01(\x0b\x32\x19.grpc.weladee.com.Holiday\x12$\n\x04odoo\x18\x02 \x01(\x0b\x32\x16.grpc.weladee.com.odoo\"V\n\x0cLogEventOdoo\x12,\n\x08logevent\x18\x02 \x01(\x0b\x32\x1a.grpc.weladee.com.LogEvent\x12\x18\n\x10\x65mployee_odoo_id\x18\x03 \x01(\x03\"S\n\x0bOdooRequest\x12\x10\n\x02ID\x18\x01 \x01(\x03H\x00R\x02id\x12\x1a\n\x07odoo_id\x18\x02 \x01(\x03H\x00R\x07odoo_id\x12\r\n\x05\x46orce\x18\x03 \x01(\x08\x42\x07\n\x05query\"\x87\x01\n\x0c\x45mployeeOdoo\x12$\n\x04odoo\x18\x01 \x01(\x0b\x32\x16.grpc.weladee.com.odoo\x12,\n\x08\x65mployee\x18\x02 \x01(\x0b\x32\x1a.grpc.weladee.com.Employee\x12\r\n\x05\x42\x61\x64ge\x18\x03 \x01(\t\x12\x14\n\x0c\x44\x65partmentID\x18\x04 \x01(\x03\"h\n\x0e\x44\x65partmentOdoo\x12$\n\x04odoo\x18\x01 \x01(\x0b\x32\x16.grpc.weladee.com.odoo\x12\x30\n\ndepartment\x18\x02 \x01(\x0b\x32\x1c.grpc.weladee.com.Department\"r\n\x0cPositionOdoo\x12*\n\x04odoo\x18\x01 \x01(\x0b\x32\x16.grpc.weladee.com.odooR\x04odoo\x12\x36\n\x08position\x18\x02 \x01(\x0b\x32\x1a.grpc.weladee.com.PositionR\x08position\"\x90\x01\n\x04odoo\x12\x18\n\x07odoo_id\x18\x01 \x01(\x03R\x07odoo_id\x12(\n\x0fodoo_created_on\x18\x02 \x01(\x03R\x0fodoo_created_on\x12&\n\x0eodoo_synced_on\x18\x03 \x01(\x03R\x0eodoo_synced_on\x12\x1c\n\todoo_note\x18\x04 \x01(\tR\todoo_note2\xce\x08\n\x04Odoo\x12I\n\x0eUpdateEmployee\x12\x1e.grpc.weladee.com.EmployeeOdoo\x1a\x17.grpc.weladee.com.Empty\x12O\n\x0cGetEmployees\x12\x1d.grpc.weladee.com.OdooRequest\x1a\x1e.grpc.weladee.com.EmployeeOdoo0\x01\x12J\n\x0b\x41\x64\x64\x45mployee\x12\x1e.grpc.weladee.com.EmployeeOdoo\x1a\x1b.grpc.weladee.com.AddResult\x12U\n\x13GetEmployeeHolidays\x12\x1d.grpc.weladee.com.OdooRequest\x1a\x1d.grpc.weladee.com.HolidayOdoo0\x01\x12G\n\x0bGetHolidays\x12\x17.grpc.weladee.com.Empty\x1a\x1d.grpc.weladee.com.HolidayOdoo0\x01\x12H\n\nAddHoliday\x12\x1d.grpc.weladee.com.HolidayOdoo\x1a\x1b.grpc.weladee.com.AddResult\x12\x45\n\x0b\x44ropHoliday\x12\x1d.grpc.weladee.com.OdooRequest\x1a\x17.grpc.weladee.com.Empty\x12G\n\rUpdateHoliday\x12\x1d.grpc.weladee.com.HolidayOdoo\x1a\x17.grpc.weladee.com.Empty\x12S\n\x0eGetDepartments\x12\x1d.grpc.weladee.com.OdooRequest\x1a .grpc.weladee.com.DepartmentOdoo0\x01\x12N\n\rAddDepartment\x12 .grpc.weladee.com.DepartmentOdoo\x1a\x1b.grpc.weladee.com.AddResult\x12M\n\x10UpdateDepartment\x12 .grpc.weladee.com.DepartmentOdoo\x1a\x17.grpc.weladee.com.Empty\x12Y\n\x10GetNewAttendance\x12#.grpc.weladee.com.AttendanceRequest\x1a\x1e.grpc.weladee.com.LogEventOdoo0\x01\x12I\n\x0cGetPositions\x12\x17.grpc.weladee.com.Empty\x1a\x1e.grpc.weladee.com.PositionOdoo0\x01\x12J\n\x0b\x41\x64\x64Position\x12\x1e.grpc.weladee.com.PositionOdoo\x1a\x1b.grpc.weladee.com.AddResultB0\n\x1a\x63om.frontware.weladee_odooB\x0bWeladeeGRPCH\x03P\x01\x90\x01\x01\x62\x06proto3')
  ,
  dependencies=[weladee__pb2.DESCRIPTOR,])




_ATTENDANCEREQUEST = _descriptor.Descriptor(
  name='AttendanceRequest',
  full_name='grpc.weladee.com.AttendanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='From', full_name='grpc.weladee.com.AttendanceRequest.From', index=0,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='EmployeeID', full_name='grpc.weladee.com.AttendanceRequest.EmployeeID', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=100,
)


_HOLIDAYODOO = _descriptor.Descriptor(
  name='HolidayOdoo',
  full_name='grpc.weladee.com.HolidayOdoo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Holiday', full_name='grpc.weladee.com.HolidayOdoo.Holiday', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='odoo', full_name='grpc.weladee.com.HolidayOdoo.odoo', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=197,
)


_LOGEVENTODOO = _descriptor.Descriptor(
  name='LogEventOdoo',
  full_name='grpc.weladee.com.LogEventOdoo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='logevent', full_name='grpc.weladee.com.LogEventOdoo.logevent', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='employee_odoo_id', full_name='grpc.weladee.com.LogEventOdoo.employee_odoo_id', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=285,
)


_ODOOREQUEST = _descriptor.Descriptor(
  name='OdooRequest',
  full_name='grpc.weladee.com.OdooRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='grpc.weladee.com.OdooRequest.ID', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='id'),
    _descriptor.FieldDescriptor(
      name='odoo_id', full_name='grpc.weladee.com.OdooRequest.odoo_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='odoo_id'),
    _descriptor.FieldDescriptor(
      name='Force', full_name='grpc.weladee.com.OdooRequest.Force', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='query', full_name='grpc.weladee.com.OdooRequest.query',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=287,
  serialized_end=370,
)


_EMPLOYEEODOO = _descriptor.Descriptor(
  name='EmployeeOdoo',
  full_name='grpc.weladee.com.EmployeeOdoo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='odoo', full_name='grpc.weladee.com.EmployeeOdoo.odoo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='employee', full_name='grpc.weladee.com.EmployeeOdoo.employee', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Badge', full_name='grpc.weladee.com.EmployeeOdoo.Badge', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DepartmentID', full_name='grpc.weladee.com.EmployeeOdoo.DepartmentID', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=508,
)


_DEPARTMENTODOO = _descriptor.Descriptor(
  name='DepartmentOdoo',
  full_name='grpc.weladee.com.DepartmentOdoo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='odoo', full_name='grpc.weladee.com.DepartmentOdoo.odoo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='department', full_name='grpc.weladee.com.DepartmentOdoo.department', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=510,
  serialized_end=614,
)


_POSITIONODOO = _descriptor.Descriptor(
  name='PositionOdoo',
  full_name='grpc.weladee.com.PositionOdoo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='odoo', full_name='grpc.weladee.com.PositionOdoo.odoo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='odoo'),
    _descriptor.FieldDescriptor(
      name='position', full_name='grpc.weladee.com.PositionOdoo.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='position'),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=616,
  serialized_end=730,
)


_ODOO = _descriptor.Descriptor(
  name='odoo',
  full_name='grpc.weladee.com.odoo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='odoo_id', full_name='grpc.weladee.com.odoo.odoo_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='odoo_id'),
    _descriptor.FieldDescriptor(
      name='odoo_created_on', full_name='grpc.weladee.com.odoo.odoo_created_on', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='odoo_created_on'),
    _descriptor.FieldDescriptor(
      name='odoo_synced_on', full_name='grpc.weladee.com.odoo.odoo_synced_on', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='odoo_synced_on'),
    _descriptor.FieldDescriptor(
      name='odoo_note', full_name='grpc.weladee.com.odoo.odoo_note', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, json_name='odoo_note'),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=733,
  serialized_end=877,
)

_HOLIDAYODOO.fields_by_name['Holiday'].message_type = weladee__pb2._HOLIDAY
_HOLIDAYODOO.fields_by_name['odoo'].message_type = _ODOO
_LOGEVENTODOO.fields_by_name['logevent'].message_type = weladee__pb2._LOGEVENT
_ODOOREQUEST.oneofs_by_name['query'].fields.append(
  _ODOOREQUEST.fields_by_name['ID'])
_ODOOREQUEST.fields_by_name['ID'].containing_oneof = _ODOOREQUEST.oneofs_by_name['query']
_ODOOREQUEST.oneofs_by_name['query'].fields.append(
  _ODOOREQUEST.fields_by_name['odoo_id'])
_ODOOREQUEST.fields_by_name['odoo_id'].containing_oneof = _ODOOREQUEST.oneofs_by_name['query']
_EMPLOYEEODOO.fields_by_name['odoo'].message_type = _ODOO
_EMPLOYEEODOO.fields_by_name['employee'].message_type = weladee__pb2._EMPLOYEE
_DEPARTMENTODOO.fields_by_name['odoo'].message_type = _ODOO
_DEPARTMENTODOO.fields_by_name['department'].message_type = weladee__pb2._DEPARTMENT
_POSITIONODOO.fields_by_name['odoo'].message_type = _ODOO
_POSITIONODOO.fields_by_name['position'].message_type = weladee__pb2._POSITION
DESCRIPTOR.message_types_by_name['AttendanceRequest'] = _ATTENDANCEREQUEST
DESCRIPTOR.message_types_by_name['HolidayOdoo'] = _HOLIDAYODOO
DESCRIPTOR.message_types_by_name['LogEventOdoo'] = _LOGEVENTODOO
DESCRIPTOR.message_types_by_name['OdooRequest'] = _ODOOREQUEST
DESCRIPTOR.message_types_by_name['EmployeeOdoo'] = _EMPLOYEEODOO
DESCRIPTOR.message_types_by_name['DepartmentOdoo'] = _DEPARTMENTODOO
DESCRIPTOR.message_types_by_name['PositionOdoo'] = _POSITIONODOO
DESCRIPTOR.message_types_by_name['odoo'] = _ODOO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AttendanceRequest = _reflection.GeneratedProtocolMessageType('AttendanceRequest', (_message.Message,), dict(
  DESCRIPTOR = _ATTENDANCEREQUEST,
  __module__ = 'odoo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.AttendanceRequest)
  ))
_sym_db.RegisterMessage(AttendanceRequest)

HolidayOdoo = _reflection.GeneratedProtocolMessageType('HolidayOdoo', (_message.Message,), dict(
  DESCRIPTOR = _HOLIDAYODOO,
  __module__ = 'odoo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.HolidayOdoo)
  ))
_sym_db.RegisterMessage(HolidayOdoo)

LogEventOdoo = _reflection.GeneratedProtocolMessageType('LogEventOdoo', (_message.Message,), dict(
  DESCRIPTOR = _LOGEVENTODOO,
  __module__ = 'odoo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.LogEventOdoo)
  ))
_sym_db.RegisterMessage(LogEventOdoo)

OdooRequest = _reflection.GeneratedProtocolMessageType('OdooRequest', (_message.Message,), dict(
  DESCRIPTOR = _ODOOREQUEST,
  __module__ = 'odoo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.OdooRequest)
  ))
_sym_db.RegisterMessage(OdooRequest)

EmployeeOdoo = _reflection.GeneratedProtocolMessageType('EmployeeOdoo', (_message.Message,), dict(
  DESCRIPTOR = _EMPLOYEEODOO,
  __module__ = 'odoo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.EmployeeOdoo)
  ))
_sym_db.RegisterMessage(EmployeeOdoo)

DepartmentOdoo = _reflection.GeneratedProtocolMessageType('DepartmentOdoo', (_message.Message,), dict(
  DESCRIPTOR = _DEPARTMENTODOO,
  __module__ = 'odoo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.DepartmentOdoo)
  ))
_sym_db.RegisterMessage(DepartmentOdoo)

PositionOdoo = _reflection.GeneratedProtocolMessageType('PositionOdoo', (_message.Message,), dict(
  DESCRIPTOR = _POSITIONODOO,
  __module__ = 'odoo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.PositionOdoo)
  ))
_sym_db.RegisterMessage(PositionOdoo)

odoo = _reflection.GeneratedProtocolMessageType('odoo', (_message.Message,), dict(
  DESCRIPTOR = _ODOO,
  __module__ = 'odoo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.odoo)
  ))
_sym_db.RegisterMessage(odoo)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032com.frontware.weladee_odooB\013WeladeeGRPCH\003P\001\220\001\001'))

_ODOO = _descriptor.ServiceDescriptor(
  name='Odoo',
  full_name='grpc.weladee.com.Odoo',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=880,
  serialized_end=1982,
  methods=[
  _descriptor.MethodDescriptor(
    name='UpdateEmployee',
    full_name='grpc.weladee.com.Odoo.UpdateEmployee',
    index=0,
    containing_service=None,
    input_type=_EMPLOYEEODOO,
    output_type=weladee__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetEmployees',
    full_name='grpc.weladee.com.Odoo.GetEmployees',
    index=1,
    containing_service=None,
    input_type=_ODOOREQUEST,
    output_type=_EMPLOYEEODOO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddEmployee',
    full_name='grpc.weladee.com.Odoo.AddEmployee',
    index=2,
    containing_service=None,
    input_type=_EMPLOYEEODOO,
    output_type=weladee__pb2._ADDRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetEmployeeHolidays',
    full_name='grpc.weladee.com.Odoo.GetEmployeeHolidays',
    index=3,
    containing_service=None,
    input_type=_ODOOREQUEST,
    output_type=_HOLIDAYODOO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetHolidays',
    full_name='grpc.weladee.com.Odoo.GetHolidays',
    index=4,
    containing_service=None,
    input_type=weladee__pb2._EMPTY,
    output_type=_HOLIDAYODOO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddHoliday',
    full_name='grpc.weladee.com.Odoo.AddHoliday',
    index=5,
    containing_service=None,
    input_type=_HOLIDAYODOO,
    output_type=weladee__pb2._ADDRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DropHoliday',
    full_name='grpc.weladee.com.Odoo.DropHoliday',
    index=6,
    containing_service=None,
    input_type=_ODOOREQUEST,
    output_type=weladee__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateHoliday',
    full_name='grpc.weladee.com.Odoo.UpdateHoliday',
    index=7,
    containing_service=None,
    input_type=_HOLIDAYODOO,
    output_type=weladee__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDepartments',
    full_name='grpc.weladee.com.Odoo.GetDepartments',
    index=8,
    containing_service=None,
    input_type=_ODOOREQUEST,
    output_type=_DEPARTMENTODOO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddDepartment',
    full_name='grpc.weladee.com.Odoo.AddDepartment',
    index=9,
    containing_service=None,
    input_type=_DEPARTMENTODOO,
    output_type=weladee__pb2._ADDRESULT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateDepartment',
    full_name='grpc.weladee.com.Odoo.UpdateDepartment',
    index=10,
    containing_service=None,
    input_type=_DEPARTMENTODOO,
    output_type=weladee__pb2._EMPTY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetNewAttendance',
    full_name='grpc.weladee.com.Odoo.GetNewAttendance',
    index=11,
    containing_service=None,
    input_type=_ATTENDANCEREQUEST,
    output_type=_LOGEVENTODOO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPositions',
    full_name='grpc.weladee.com.Odoo.GetPositions',
    index=12,
    containing_service=None,
    input_type=weladee__pb2._EMPTY,
    output_type=_POSITIONODOO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddPosition',
    full_name='grpc.weladee.com.Odoo.AddPosition',
    index=13,
    containing_service=None,
    input_type=_POSITIONODOO,
    output_type=weladee__pb2._ADDRESULT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ODOO)

DESCRIPTOR.services_by_name['Odoo'] = _ODOO

Odoo = service_reflection.GeneratedServiceType('Odoo', (_service.Service,), dict(
  DESCRIPTOR = _ODOO,
  __module__ = 'odoo_pb2'
  ))

Odoo_Stub = service_reflection.GeneratedServiceStubType('Odoo_Stub', (Odoo,), dict(
  DESCRIPTOR = _ODOO,
  __module__ = 'odoo_pb2'
  ))


# @@protoc_insertion_point(module_scope)
