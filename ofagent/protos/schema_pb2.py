# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='schema.proto',
  package='schema',
  syntax='proto3',
  serialized_pb=_b('\n\x0cschema.proto\x12\x06schema\x1a\x1cgoogle/api/annotations.proto\"\xcd\x01\n\x06Schema\x12*\n\x06protos\x18\x01 \x03(\x0b\x32\x1a.schema.Schema.ProtosEntry\x12\x34\n\x0b\x64\x65scriptors\x18\x02 \x03(\x0b\x32\x1f.schema.Schema.DescriptorsEntry\x1a-\n\x0bProtosEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x32\n\x10\x44\x65scriptorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\r\n\x0bNullMessage2R\n\rSchemaService\x12\x41\n\tGetSchema\x12\x13.schema.NullMessage\x1a\x0e.schema.Schema\"\x0f\x82\xd3\xe4\x93\x02\t\x12\x07/schemab\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SCHEMA_PROTOSENTRY = _descriptor.Descriptor(
  name='ProtosEntry',
  full_name='schema.Schema.ProtosEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='schema.Schema.ProtosEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='schema.Schema.ProtosEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=163,
  serialized_end=208,
)

_SCHEMA_DESCRIPTORSENTRY = _descriptor.Descriptor(
  name='DescriptorsEntry',
  full_name='schema.Schema.DescriptorsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='schema.Schema.DescriptorsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='schema.Schema.DescriptorsEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=260,
)

_SCHEMA = _descriptor.Descriptor(
  name='Schema',
  full_name='schema.Schema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='protos', full_name='schema.Schema.protos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='descriptors', full_name='schema.Schema.descriptors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_SCHEMA_PROTOSENTRY, _SCHEMA_DESCRIPTORSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=260,
)


_NULLMESSAGE = _descriptor.Descriptor(
  name='NullMessage',
  full_name='schema.NullMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=262,
  serialized_end=275,
)

_SCHEMA_PROTOSENTRY.containing_type = _SCHEMA
_SCHEMA_DESCRIPTORSENTRY.containing_type = _SCHEMA
_SCHEMA.fields_by_name['protos'].message_type = _SCHEMA_PROTOSENTRY
_SCHEMA.fields_by_name['descriptors'].message_type = _SCHEMA_DESCRIPTORSENTRY
DESCRIPTOR.message_types_by_name['Schema'] = _SCHEMA
DESCRIPTOR.message_types_by_name['NullMessage'] = _NULLMESSAGE

Schema = _reflection.GeneratedProtocolMessageType('Schema', (_message.Message,), dict(

  ProtosEntry = _reflection.GeneratedProtocolMessageType('ProtosEntry', (_message.Message,), dict(
    DESCRIPTOR = _SCHEMA_PROTOSENTRY,
    __module__ = 'schema_pb2'
    # @@protoc_insertion_point(class_scope:schema.Schema.ProtosEntry)
    ))
  ,

  DescriptorsEntry = _reflection.GeneratedProtocolMessageType('DescriptorsEntry', (_message.Message,), dict(
    DESCRIPTOR = _SCHEMA_DESCRIPTORSENTRY,
    __module__ = 'schema_pb2'
    # @@protoc_insertion_point(class_scope:schema.Schema.DescriptorsEntry)
    ))
  ,
  DESCRIPTOR = _SCHEMA,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:schema.Schema)
  ))
_sym_db.RegisterMessage(Schema)
_sym_db.RegisterMessage(Schema.ProtosEntry)
_sym_db.RegisterMessage(Schema.DescriptorsEntry)

NullMessage = _reflection.GeneratedProtocolMessageType('NullMessage', (_message.Message,), dict(
  DESCRIPTOR = _NULLMESSAGE,
  __module__ = 'schema_pb2'
  # @@protoc_insertion_point(class_scope:schema.NullMessage)
  ))
_sym_db.RegisterMessage(NullMessage)


_SCHEMA_PROTOSENTRY.has_options = True
_SCHEMA_PROTOSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_SCHEMA_DESCRIPTORSENTRY.has_options = True
_SCHEMA_DESCRIPTORSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class SchemaServiceStub(object):
  """Schema services
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetSchema = channel.unary_unary(
        '/schema.SchemaService/GetSchema',
        request_serializer=NullMessage.SerializeToString,
        response_deserializer=Schema.FromString,
        )


class SchemaServiceServicer(object):
  """Schema services
  """

  def GetSchema(self, request, context):
    """Return active grpc schemas
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SchemaServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetSchema': grpc.unary_unary_rpc_method_handler(
          servicer.GetSchema,
          request_deserializer=NullMessage.FromString,
          response_serializer=Schema.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'schema.SchemaService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaSchemaServiceServicer(object):
  """Schema services
  """
  def GetSchema(self, request, context):
    """Return active grpc schemas
    """
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaSchemaServiceStub(object):
  """Schema services
  """
  def GetSchema(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    """Return active grpc schemas
    """
    raise NotImplementedError()
  GetSchema.future = None


def beta_create_SchemaService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  request_deserializers = {
    ('schema.SchemaService', 'GetSchema'): NullMessage.FromString,
  }
  response_serializers = {
    ('schema.SchemaService', 'GetSchema'): Schema.SerializeToString,
  }
  method_implementations = {
    ('schema.SchemaService', 'GetSchema'): face_utilities.unary_unary_inline(servicer.GetSchema),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_SchemaService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  request_serializers = {
    ('schema.SchemaService', 'GetSchema'): NullMessage.SerializeToString,
  }
  response_deserializers = {
    ('schema.SchemaService', 'GetSchema'): Schema.FromString,
  }
  cardinalities = {
    'GetSchema': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'schema.SchemaService', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
