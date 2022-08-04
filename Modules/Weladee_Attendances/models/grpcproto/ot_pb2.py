# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ot.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import weladee_pb2 as weladee__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08ot.proto\x12\x10grpc.weladee.com\x1a\rweladee.proto\"\xa7\x04\n\tOTRequest\x12\x0e\n\x02ID\x18\x01 \x01(\x03R\x02id\x12\x12\n\x04\x44\x61te\x18\x02 \x01(\x05R\x04\x64\x61te\x12 \n\x0b\x44\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x16\n\x06Reason\x18\x04 \x01(\tR\x06reason\x12\x1e\n\nEmployeeID\x18\x05 \x01(\x03R\nemployeeid\x12\x12\n\x04\x46rom\x18\x14 \x01(\tR\x04\x66rom\x12\x0e\n\x02To\x18\x15 \x01(\tR\x02to\x12\x1a\n\x08\x44uration\x18\x16 \x01(\x05R\x08\x64uration\x12\x16\n\x06TypeID\x18\x19 \x01(\x03R\x06typeid\x12\x39\n\x06Status\x18\x06 \x01(\x0e\x32!.grpc.weladee.com.OTRequestStatusR\x06status\x12\x1d\n\tTreatedBy\x18\x07 \x01(\x03R\ntreated_by\x12\x1d\n\tTreatedOn\x18\x08 \x01(\x03R\ntreated_on\x12\x12\n\x04\x43ode\x18\x1e \x01(\tR\x04\x63ode\x12#\n\x0c\x45mployeeName\x18\x1f \x01(\tR\remployee_name\x12&\n\rTreatedByName\x18  \x01(\tR\x0ftreated_by_name\x12#\n\x0c\x45mployeeCode\x18! \x01(\tR\remployee_code\x12\x14\n\x05Photo\x18\" \x01(\tR\x05photo\x12\x1b\n\x08TypeName\x18# \x01(\tR\ttype_name\x12\x12\n\x04\x43ost\x18( \x01(\x03R\x04\x63ost\"\xbe\x01\n\x07OTQuery\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x0e\n\x06TypeID\x18\x19 \x01(\x03\x12\x31\n\x06Status\x18\x06 \x01(\x0e\x32!.grpc.weladee.com.OTRequestStatus\x12\x12\n\nEmployeeID\x18\x05 \x01(\x03\x12\x0e\n\x06TeamID\x18\x08 \x01(\x03\x12\x14\n\x0c\x44\x65partmentID\x18\t \x01(\x03\x12\x0c\n\x04\x46rom\x18\n \x01(\x03\x12\n\n\x02To\x18\x0b \x01(\x03\x12\x10\n\x03XLS\x18\x13 \x01(\x08R\x03xls\"\xc0\x01\n\x06OTType\x12\x0e\n\x02ID\x18\x01 \x01(\x03R\x02id\x12!\n\x0bNameEnglish\x18\x03 \x01(\tR\x0cname_english\x12\x1b\n\x08NameThai\x18\x04 \x01(\tR\tname_thai\x12\x16\n\x06\x61\x63tive\x18\x05 \x01(\x08R\x06\x61\x63tive\x12\x12\n\x04\x43ode\x18\x08 \x01(\tR\x04\x63ode\x12\x12\n\x04Note\x18\x06 \x01(\tR\x04note\x12&\n\rHourlyRatePct\x18\x14 \x01(\rR\x0fhourly_rate_pct\"b\n\rOTTypeRequest\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x0c\n\x04Name\x18\x03 \x01(\t\x12)\n\x06\x61\x63tive\x18\x05 \x01(\x0e\x32\x19.grpc.weladee.com.Trinary\x12\x0c\n\x04\x43ode\x18\x08 \x01(\t\"\xe2\x03\n\rOTPreferences\x12,\n\x10\x41pproveByManager\x18\x01 \x01(\x08R\x12\x61pprove_by_manager\x12\x35\n\x14\x41pproveByTeamManager\x18\x02 \x01(\x08R\x17\x61pprove_by_team_manager\x12\x31\n\x12\x41pproveByHRManager\x18\x03 \x01(\x08R\x15\x61pprove_by_hr_manager\x12\x35\n\x14\x41pproveByDeptManager\x18\x06 \x01(\x08R\x17\x61pprove_by_dept_manager\x12*\n\x0fMustDefineRange\x18\x04 \x01(\x08R\x11must_define_range\x12\x36\n\x15MustDefineDescription\x18\x05 \x01(\x08R\x17must_define_description\x12\x1d\n\tDateAfter\x18\x1e \x01(\rR\ndate_after\x12\x1f\n\nDateBefore\x18( \x01(\rR\x0b\x64\x61te_before\x12\x31\n\x13InstructionsEnglish\x18\x14 \x01(\tR\x14instructions_english\x12+\n\x10InstructionsThai\x18\x15 \x01(\tR\x11instructions_thai*M\n\x0fOTRequestStatus\x12\x0f\n\x0bOTStatusNew\x10\x00\x12\x14\n\x10OTStatusApproved\x10\x01\x12\x13\n\x0fOTStatusRefused\x10\x02\x42+\n\x18\x63om.frontware.weladee_otB\x0bWeladeeGRPCH\x03P\x00\x62\x06proto3')

_OTREQUESTSTATUS = DESCRIPTOR.enum_types_by_name['OTRequestStatus']
OTRequestStatus = enum_type_wrapper.EnumTypeWrapper(_OTREQUESTSTATUS)
OTStatusNew = 0
OTStatusApproved = 1
OTStatusRefused = 2


_OTREQUEST = DESCRIPTOR.message_types_by_name['OTRequest']
_OTQUERY = DESCRIPTOR.message_types_by_name['OTQuery']
_OTTYPE = DESCRIPTOR.message_types_by_name['OTType']
_OTTYPEREQUEST = DESCRIPTOR.message_types_by_name['OTTypeRequest']
_OTPREFERENCES = DESCRIPTOR.message_types_by_name['OTPreferences']
OTRequest = _reflection.GeneratedProtocolMessageType('OTRequest', (_message.Message,), {
  'DESCRIPTOR' : _OTREQUEST,
  '__module__' : 'ot_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.OTRequest)
  })
_sym_db.RegisterMessage(OTRequest)

OTQuery = _reflection.GeneratedProtocolMessageType('OTQuery', (_message.Message,), {
  'DESCRIPTOR' : _OTQUERY,
  '__module__' : 'ot_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.OTQuery)
  })
_sym_db.RegisterMessage(OTQuery)

OTType = _reflection.GeneratedProtocolMessageType('OTType', (_message.Message,), {
  'DESCRIPTOR' : _OTTYPE,
  '__module__' : 'ot_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.OTType)
  })
_sym_db.RegisterMessage(OTType)

OTTypeRequest = _reflection.GeneratedProtocolMessageType('OTTypeRequest', (_message.Message,), {
  'DESCRIPTOR' : _OTTYPEREQUEST,
  '__module__' : 'ot_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.OTTypeRequest)
  })
_sym_db.RegisterMessage(OTTypeRequest)

OTPreferences = _reflection.GeneratedProtocolMessageType('OTPreferences', (_message.Message,), {
  'DESCRIPTOR' : _OTPREFERENCES,
  '__module__' : 'ot_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.OTPreferences)
  })
_sym_db.RegisterMessage(OTPreferences)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.frontware.weladee_otB\013WeladeeGRPCH\003P\000'
  _OTREQUESTSTATUS._serialized_start=1572
  _OTREQUESTSTATUS._serialized_end=1649
  _OTREQUEST._serialized_start=46
  _OTREQUEST._serialized_end=597
  _OTQUERY._serialized_start=600
  _OTQUERY._serialized_end=790
  _OTTYPE._serialized_start=793
  _OTTYPE._serialized_end=985
  _OTTYPEREQUEST._serialized_start=987
  _OTTYPEREQUEST._serialized_end=1085
  _OTPREFERENCES._serialized_start=1088
  _OTPREFERENCES._serialized_end=1570
# @@protoc_insertion_point(module_scope)
