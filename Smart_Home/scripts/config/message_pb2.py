# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\"i\n\x07Request\x12\x14\n\x07\x61\x64\x64ress\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04port\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x14\n\x07request\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\n\n\x08_addressB\x07\n\x05_portB\n\n\x08_request\".\n\x08Response\x12\x15\n\x08response\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\x0b\n\t_response2\x82\x01\n\x04Grpc\x12%\n\x0cServerClient\x12\x08.Request\x1a\t.Response0\x01\x12%\n\x0c\x43lientServer\x12\x08.Request\x1a\t.Response(\x01\x12,\n\x11InteractingStream\x12\x08.Request\x1a\t.Response(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=17
  _REQUEST._serialized_end=122
  _RESPONSE._serialized_start=124
  _RESPONSE._serialized_end=170
  _GRPC._serialized_start=173
  _GRPC._serialized_end=303
# @@protoc_insertion_point(module_scope)
