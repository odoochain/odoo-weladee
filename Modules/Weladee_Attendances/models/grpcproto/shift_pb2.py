# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shift.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import weladee_pb2 as weladee__pb2
import ot_pb2 as ot__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bshift.proto\x12\x10grpc.weladee.com\x1a\rweladee.proto\x1a\x08ot.proto\"a\n\x0fScheduleRequest\x12\x0e\n\x02ID\x18\x01 \x01(\x03R\x02id\x12\x16\n\x06TeamID\x18\x04 \x01(\x03R\x06teamid\x12\x12\n\x04Year\x18\x05 \x01(\rR\x04year\x12\x12\n\x04Week\x18\x06 \x01(\rR\x04week\"\xe6\x07\n\x08Schedule\x12\x0e\n\x02ID\x18\x01 \x01(\x03R\x02id\x12\x1b\n\x08\x44\x61teFrom\x18\x02 \x01(\x03R\tdate_from\x12\x17\n\x06\x44\x61teTo\x18\x03 \x01(\x03R\x07\x64\x61te_to\x12\x16\n\x06TeamID\x18\x04 \x01(\x03R\x06teamid\x12\x1b\n\x08TeamName\x18\x05 \x01(\tR\tteam_name\x12\x16\n\x06GateID\x18\x08 \x01(\x03R\x06gateid\x12\x1b\n\x08GateName\x18\t \x01(\tR\tgate_name\x12\x12\n\x04Year\x18\n \x01(\rR\x04year\x12\x12\n\x04Week\x18\x0b \x01(\rR\x04week\x12\x1d\n\tTotalTime\x18\x0c \x01(\rR\ntotal_time\x12\x1c\n\tPublished\x18\r \x01(\x08R\tpublished\x12!\n\x0bPublishedBy\x18\x0e \x01(\x03R\x0cpublished_by\x12!\n\x0bPublishedOn\x18\x10 \x01(\x03R\x0cpublished_on\x12\x12\n\x04Note\x18\x0f \x01(\tR\x04note\x12/\n\x06Shifts\x18\x14 \x03(\x0b\x32\x17.grpc.weladee.com.ShiftR\x06shifts\x12X\n\x0e\x44urationPerDay\x18\x1e \x03(\x0b\x32..grpc.weladee.com.Schedule.DurationPerDayEntryR\x10\x64uration_per_day\x12g\n\x13\x44urationPerEmployee\x18\x1f \x03(\x0b\x32\x33.grpc.weladee.com.Schedule.DurationPerEmployeeEntryR\x15\x64uration_per_employee\x12\x46\n\x08OTPerDay\x18  \x03(\x0b\x32(.grpc.weladee.com.Schedule.OTPerDayEntryR\not_per_day\x12U\n\rOTPerEmployee\x18! \x03(\x0b\x32-.grpc.weladee.com.Schedule.OTPerEmployeeEntryR\x0fot_per_employee\x1a\x35\n\x13\x44urationPerDayEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a:\n\x18\x44urationPerEmployeeEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a/\n\rOTPerDayEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x34\n\x12OTPerEmployeeEntry\x12\x0b\n\x03key\x18\x01 \x01(\x03\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\"r\n\x10ShiftPreferences\x12\x31\n\x13InstructionsEnglish\x18\x14 \x01(\tR\x14instructions_english\x12+\n\x10InstructionsThai\x18\x15 \x01(\tR\x11instructions_thai\"\xe9\x02\n\x05Shift\x12\x0e\n\x02ID\x18\x01 \x01(\x03R\x02id\x12\x18\n\x07Weekday\x18\x02 \x01(\rR\x07weekday\x12\x1e\n\nEmployeeID\x18\x03 \x01(\x03R\nemployeeid\x12?\n\x0cWorkinghours\x18\x04 \x03(\x0b\x32\x1a.grpc.weladee.com.OpenhourR\rworking_hours\x12\x1a\n\x08\x44uration\x18\x06 \x01(\rR\x08\x64uration\x12\x1e\n\nScheduleID\x18\x07 \x01(\x03R\nscheduleid\x12\x12\n\x04\x44\x61te\x18\x08 \x01(\x03R\x04\x64\x61te\x12\x33\n\x07Holiday\x18\t \x01(\x0b\x32\x19.grpc.weladee.com.HolidayR\x07holiday\x12\x12\n\x04Note\x18\n \x01(\tR\x04note\x12<\n\nOTApproved\x18\x0b \x01(\x0b\x32\x1b.grpc.weladee.com.OTRequestR\x0bot_approved\"y\n\x10ShiftAndDuration\x12-\n\x05shift\x18\x01 \x01(\x0b\x32\x17.grpc.weladee.com.ShiftR\x05shift\x12\x36\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x1a.grpc.weladee.com.DurationR\x08\x64uration\"Z\n\x08\x44uration\x12!\n\x0b\x44\x61yDuration\x18\x01 \x01(\rR\x0c\x64\x61y_duration\x12+\n\x10\x45mployeeDuration\x18\x02 \x01(\rR\x11\x65mployee_duration\"c\n\x13\x43opyScheduleRequest\x12\'\n\x0eScheduleFromID\x18\x01 \x01(\x03R\x0fschedule_fromid\x12#\n\x0cScheduleToID\x18\x02 \x01(\x03R\rschedule_toidB.\n\x1b\x63om.frontware.weladee_shiftB\x0bWeladeeGRPCH\x03P\x01\x62\x06proto3')



_SCHEDULEREQUEST = DESCRIPTOR.message_types_by_name['ScheduleRequest']
_SCHEDULE = DESCRIPTOR.message_types_by_name['Schedule']
_SCHEDULE_DURATIONPERDAYENTRY = _SCHEDULE.nested_types_by_name['DurationPerDayEntry']
_SCHEDULE_DURATIONPEREMPLOYEEENTRY = _SCHEDULE.nested_types_by_name['DurationPerEmployeeEntry']
_SCHEDULE_OTPERDAYENTRY = _SCHEDULE.nested_types_by_name['OTPerDayEntry']
_SCHEDULE_OTPEREMPLOYEEENTRY = _SCHEDULE.nested_types_by_name['OTPerEmployeeEntry']
_SHIFTPREFERENCES = DESCRIPTOR.message_types_by_name['ShiftPreferences']
_SHIFT = DESCRIPTOR.message_types_by_name['Shift']
_SHIFTANDDURATION = DESCRIPTOR.message_types_by_name['ShiftAndDuration']
_DURATION = DESCRIPTOR.message_types_by_name['Duration']
_COPYSCHEDULEREQUEST = DESCRIPTOR.message_types_by_name['CopyScheduleRequest']
ScheduleRequest = _reflection.GeneratedProtocolMessageType('ScheduleRequest', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULEREQUEST,
  '__module__' : 'shift_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.ScheduleRequest)
  })
_sym_db.RegisterMessage(ScheduleRequest)

Schedule = _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), {

  'DurationPerDayEntry' : _reflection.GeneratedProtocolMessageType('DurationPerDayEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCHEDULE_DURATIONPERDAYENTRY,
    '__module__' : 'shift_pb2'
    # @@protoc_insertion_point(class_scope:grpc.weladee.com.Schedule.DurationPerDayEntry)
    })
  ,

  'DurationPerEmployeeEntry' : _reflection.GeneratedProtocolMessageType('DurationPerEmployeeEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCHEDULE_DURATIONPEREMPLOYEEENTRY,
    '__module__' : 'shift_pb2'
    # @@protoc_insertion_point(class_scope:grpc.weladee.com.Schedule.DurationPerEmployeeEntry)
    })
  ,

  'OTPerDayEntry' : _reflection.GeneratedProtocolMessageType('OTPerDayEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCHEDULE_OTPERDAYENTRY,
    '__module__' : 'shift_pb2'
    # @@protoc_insertion_point(class_scope:grpc.weladee.com.Schedule.OTPerDayEntry)
    })
  ,

  'OTPerEmployeeEntry' : _reflection.GeneratedProtocolMessageType('OTPerEmployeeEntry', (_message.Message,), {
    'DESCRIPTOR' : _SCHEDULE_OTPEREMPLOYEEENTRY,
    '__module__' : 'shift_pb2'
    # @@protoc_insertion_point(class_scope:grpc.weladee.com.Schedule.OTPerEmployeeEntry)
    })
  ,
  'DESCRIPTOR' : _SCHEDULE,
  '__module__' : 'shift_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.Schedule)
  })
_sym_db.RegisterMessage(Schedule)
_sym_db.RegisterMessage(Schedule.DurationPerDayEntry)
_sym_db.RegisterMessage(Schedule.DurationPerEmployeeEntry)
_sym_db.RegisterMessage(Schedule.OTPerDayEntry)
_sym_db.RegisterMessage(Schedule.OTPerEmployeeEntry)

ShiftPreferences = _reflection.GeneratedProtocolMessageType('ShiftPreferences', (_message.Message,), {
  'DESCRIPTOR' : _SHIFTPREFERENCES,
  '__module__' : 'shift_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.ShiftPreferences)
  })
_sym_db.RegisterMessage(ShiftPreferences)

Shift = _reflection.GeneratedProtocolMessageType('Shift', (_message.Message,), {
  'DESCRIPTOR' : _SHIFT,
  '__module__' : 'shift_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.Shift)
  })
_sym_db.RegisterMessage(Shift)

ShiftAndDuration = _reflection.GeneratedProtocolMessageType('ShiftAndDuration', (_message.Message,), {
  'DESCRIPTOR' : _SHIFTANDDURATION,
  '__module__' : 'shift_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.ShiftAndDuration)
  })
_sym_db.RegisterMessage(ShiftAndDuration)

Duration = _reflection.GeneratedProtocolMessageType('Duration', (_message.Message,), {
  'DESCRIPTOR' : _DURATION,
  '__module__' : 'shift_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.Duration)
  })
_sym_db.RegisterMessage(Duration)

CopyScheduleRequest = _reflection.GeneratedProtocolMessageType('CopyScheduleRequest', (_message.Message,), {
  'DESCRIPTOR' : _COPYSCHEDULEREQUEST,
  '__module__' : 'shift_pb2'
  # @@protoc_insertion_point(class_scope:grpc.weladee.com.CopyScheduleRequest)
  })
_sym_db.RegisterMessage(CopyScheduleRequest)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.frontware.weladee_shiftB\013WeladeeGRPCH\003P\001'
  _SCHEDULE_DURATIONPERDAYENTRY._options = None
  _SCHEDULE_DURATIONPERDAYENTRY._serialized_options = b'8\001'
  _SCHEDULE_DURATIONPEREMPLOYEEENTRY._options = None
  _SCHEDULE_DURATIONPEREMPLOYEEENTRY._serialized_options = b'8\001'
  _SCHEDULE_OTPERDAYENTRY._options = None
  _SCHEDULE_OTPERDAYENTRY._serialized_options = b'8\001'
  _SCHEDULE_OTPEREMPLOYEEENTRY._options = None
  _SCHEDULE_OTPEREMPLOYEEENTRY._serialized_options = b'8\001'
  _SCHEDULEREQUEST._serialized_start=58
  _SCHEDULEREQUEST._serialized_end=155
  _SCHEDULE._serialized_start=158
  _SCHEDULE._serialized_end=1156
  _SCHEDULE_DURATIONPERDAYENTRY._serialized_start=940
  _SCHEDULE_DURATIONPERDAYENTRY._serialized_end=993
  _SCHEDULE_DURATIONPEREMPLOYEEENTRY._serialized_start=995
  _SCHEDULE_DURATIONPEREMPLOYEEENTRY._serialized_end=1053
  _SCHEDULE_OTPERDAYENTRY._serialized_start=1055
  _SCHEDULE_OTPERDAYENTRY._serialized_end=1102
  _SCHEDULE_OTPEREMPLOYEEENTRY._serialized_start=1104
  _SCHEDULE_OTPEREMPLOYEEENTRY._serialized_end=1156
  _SHIFTPREFERENCES._serialized_start=1158
  _SHIFTPREFERENCES._serialized_end=1272
  _SHIFT._serialized_start=1275
  _SHIFT._serialized_end=1636
  _SHIFTANDDURATION._serialized_start=1638
  _SHIFTANDDURATION._serialized_end=1759
  _DURATION._serialized_start=1761
  _DURATION._serialized_end=1851
  _COPYSCHEDULEREQUEST._serialized_start=1853
  _COPYSCHEDULEREQUEST._serialized_end=1952
# @@protoc_insertion_point(module_scope)
