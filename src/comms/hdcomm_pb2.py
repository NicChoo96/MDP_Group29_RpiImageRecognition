# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hdcomm.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hdcomm.proto',
  package='hdcomm',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0chdcomm.proto\x12\x06hdcomm\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/duration.proto\"7\n\x0bMoveRequest\x12\x16\n\x0eradius_indexed\x18\x01 \x01(\x05\x12\x10\n\x08\x64istance\x18\x02 \x01(\x01\"@\n\x0cMoveResponse\x12\x30\n\rtime_required\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\"#\n\x0cPingResponse\x12\x13\n\x0b\x64\x65vice_time\x18\x01 \x01(\x01\"\x1e\n\rRadiiResponse\x12\r\n\x05radii\x18\x01 \x03(\x01\"7\n\x0fHeadingResponse\x12\x13\n\x0b\x64\x65vice_time\x18\x01 \x01(\x01\x12\x0f\n\x07heading\x18\x02 \x01(\x01\"]\n\x15\x46rontDistanceResponse\x12\x19\n\x11\x64\x65vice_time_start\x18\x01 \x01(\x01\x12\x17\n\x0f\x64\x65vice_time_end\x18\x02 \x01(\x01\x12\x10\n\x08\x64istance\x18\x03 \x01(\x01\x32\xf4\x02\n\x06HdComm\x12\x31\n\x04Move\x12\x13.hdcomm.MoveRequest\x1a\x14.hdcomm.MoveResponse\x12<\n\nMoveCancel\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\x12\x34\n\x04Ping\x12\x16.google.protobuf.Empty\x1a\x14.hdcomm.PingResponse\x12\x39\n\x08GetRadii\x12\x16.google.protobuf.Empty\x1a\x15.hdcomm.RadiiResponse\x12=\n\nGetHeading\x12\x16.google.protobuf.Empty\x1a\x17.hdcomm.HeadingResponse\x12I\n\x10GetFrontDistance\x12\x16.google.protobuf.Empty\x1a\x1d.hdcomm.FrontDistanceResponseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])




_MOVEREQUEST = _descriptor.Descriptor(
  name='MoveRequest',
  full_name='hdcomm.MoveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='radius_indexed', full_name='hdcomm.MoveRequest.radius_indexed', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distance', full_name='hdcomm.MoveRequest.distance', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=140,
)


_MOVERESPONSE = _descriptor.Descriptor(
  name='MoveResponse',
  full_name='hdcomm.MoveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_required', full_name='hdcomm.MoveResponse.time_required', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=206,
)


_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='hdcomm.PingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_time', full_name='hdcomm.PingResponse.device_time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=208,
  serialized_end=243,
)


_RADIIRESPONSE = _descriptor.Descriptor(
  name='RadiiResponse',
  full_name='hdcomm.RadiiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='radii', full_name='hdcomm.RadiiResponse.radii', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=275,
)


_HEADINGRESPONSE = _descriptor.Descriptor(
  name='HeadingResponse',
  full_name='hdcomm.HeadingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_time', full_name='hdcomm.HeadingResponse.device_time', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heading', full_name='hdcomm.HeadingResponse.heading', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=332,
)


_FRONTDISTANCERESPONSE = _descriptor.Descriptor(
  name='FrontDistanceResponse',
  full_name='hdcomm.FrontDistanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_time_start', full_name='hdcomm.FrontDistanceResponse.device_time_start', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_time_end', full_name='hdcomm.FrontDistanceResponse.device_time_end', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='distance', full_name='hdcomm.FrontDistanceResponse.distance', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=427,
)

_MOVERESPONSE.fields_by_name['time_required'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
DESCRIPTOR.message_types_by_name['MoveRequest'] = _MOVEREQUEST
DESCRIPTOR.message_types_by_name['MoveResponse'] = _MOVERESPONSE
DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
DESCRIPTOR.message_types_by_name['RadiiResponse'] = _RADIIRESPONSE
DESCRIPTOR.message_types_by_name['HeadingResponse'] = _HEADINGRESPONSE
DESCRIPTOR.message_types_by_name['FrontDistanceResponse'] = _FRONTDISTANCERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MoveRequest = _reflection.GeneratedProtocolMessageType('MoveRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOVEREQUEST,
  '__module__' : 'hdcomm_pb2'
  # @@protoc_insertion_point(class_scope:hdcomm.MoveRequest)
  })
_sym_db.RegisterMessage(MoveRequest)

MoveResponse = _reflection.GeneratedProtocolMessageType('MoveResponse', (_message.Message,), {
  'DESCRIPTOR' : _MOVERESPONSE,
  '__module__' : 'hdcomm_pb2'
  # @@protoc_insertion_point(class_scope:hdcomm.MoveResponse)
  })
_sym_db.RegisterMessage(MoveResponse)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), {
  'DESCRIPTOR' : _PINGRESPONSE,
  '__module__' : 'hdcomm_pb2'
  # @@protoc_insertion_point(class_scope:hdcomm.PingResponse)
  })
_sym_db.RegisterMessage(PingResponse)

RadiiResponse = _reflection.GeneratedProtocolMessageType('RadiiResponse', (_message.Message,), {
  'DESCRIPTOR' : _RADIIRESPONSE,
  '__module__' : 'hdcomm_pb2'
  # @@protoc_insertion_point(class_scope:hdcomm.RadiiResponse)
  })
_sym_db.RegisterMessage(RadiiResponse)

HeadingResponse = _reflection.GeneratedProtocolMessageType('HeadingResponse', (_message.Message,), {
  'DESCRIPTOR' : _HEADINGRESPONSE,
  '__module__' : 'hdcomm_pb2'
  # @@protoc_insertion_point(class_scope:hdcomm.HeadingResponse)
  })
_sym_db.RegisterMessage(HeadingResponse)

FrontDistanceResponse = _reflection.GeneratedProtocolMessageType('FrontDistanceResponse', (_message.Message,), {
  'DESCRIPTOR' : _FRONTDISTANCERESPONSE,
  '__module__' : 'hdcomm_pb2'
  # @@protoc_insertion_point(class_scope:hdcomm.FrontDistanceResponse)
  })
_sym_db.RegisterMessage(FrontDistanceResponse)



_HDCOMM = _descriptor.ServiceDescriptor(
  name='HdComm',
  full_name='hdcomm.HdComm',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=430,
  serialized_end=802,
  methods=[
  _descriptor.MethodDescriptor(
    name='Move',
    full_name='hdcomm.HdComm.Move',
    index=0,
    containing_service=None,
    input_type=_MOVEREQUEST,
    output_type=_MOVERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MoveCancel',
    full_name='hdcomm.HdComm.MoveCancel',
    index=1,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='hdcomm.HdComm.Ping',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_PINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetRadii',
    full_name='hdcomm.HdComm.GetRadii',
    index=3,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_RADIIRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetHeading',
    full_name='hdcomm.HdComm.GetHeading',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_HEADINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetFrontDistance',
    full_name='hdcomm.HdComm.GetFrontDistance',
    index=5,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_FRONTDISTANCERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_HDCOMM)

DESCRIPTOR.services_by_name['HdComm'] = _HDCOMM

# @@protoc_insertion_point(module_scope)