# Copyright 2016 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'variables': {
    'mojo_cpp_bindings_sources': [
      'public/cpp/bindings/array.h',
      'public/cpp/bindings/array_data_view.h',
      'public/cpp/bindings/array_traits.h',
      'public/cpp/bindings/array_traits_carray.h',
      'public/cpp/bindings/array_traits_standard.h',
      'public/cpp/bindings/array_traits_stl.h',
      'public/cpp/bindings/associated_binding.h',
      'public/cpp/bindings/associated_group.h',
      'public/cpp/bindings/associated_group_controller.h',
      'public/cpp/bindings/associated_interface_ptr.h',
      'public/cpp/bindings/associated_interface_ptr_info.h',
      'public/cpp/bindings/associated_interface_request.h',
      'public/cpp/bindings/binding.h',
      'public/cpp/bindings/binding_set.h',
      'public/cpp/bindings/connector.h',
      'public/cpp/bindings/enum_traits.h',
      'public/cpp/bindings/interface_endpoint_client.h',
      'public/cpp/bindings/interface_endpoint_controller.h',
      'public/cpp/bindings/interface_id.h',
      'public/cpp/bindings/interface_ptr.h',
      'public/cpp/bindings/interface_ptr_set.h',
      'public/cpp/bindings/interface_request.h',
      'public/cpp/bindings/lib/array_internal.cc',
      'public/cpp/bindings/lib/array_internal.h',
      'public/cpp/bindings/lib/array_serialization.h',
      'public/cpp/bindings/lib/associated_group.cc',
      'public/cpp/bindings/lib/associated_group_controller.cc',
      'public/cpp/bindings/lib/associated_interface_ptr_state.h',
      'public/cpp/bindings/lib/binding_state.h',
      'public/cpp/bindings/lib/bindings_internal.cc',
      'public/cpp/bindings/lib/bindings_internal.h',
      'public/cpp/bindings/lib/buffer.h',
      'public/cpp/bindings/lib/clone_equals_util.h',
      'public/cpp/bindings/lib/connector.cc',
      'public/cpp/bindings/lib/control_message_handler.cc',
      'public/cpp/bindings/lib/control_message_handler.h',
      'public/cpp/bindings/lib/control_message_proxy.cc',
      'public/cpp/bindings/lib/control_message_proxy.h',
      'public/cpp/bindings/lib/filter_chain.cc',
      'public/cpp/bindings/lib/filter_chain.h',
      'public/cpp/bindings/lib/fixed_buffer.cc',
      'public/cpp/bindings/lib/fixed_buffer.h',
      'public/cpp/bindings/lib/handle_interface_serialization.h',
      'public/cpp/bindings/lib/interface_endpoint_client.cc',
      'public/cpp/bindings/lib/interface_ptr_state.h',
      'public/cpp/bindings/lib/map_data_internal.h',
      'public/cpp/bindings/lib/map_serialization.h',
      'public/cpp/bindings/lib/message.cc',
      'public/cpp/bindings/lib/message_buffer.cc',
      'public/cpp/bindings/lib/message_buffer.h',
      'public/cpp/bindings/lib/message_builder.cc',
      'public/cpp/bindings/lib/message_builder.h',
      'public/cpp/bindings/lib/message_filter.cc',
      'public/cpp/bindings/lib/message_header_validator.cc',
      'public/cpp/bindings/lib/message_internal.h',
      'public/cpp/bindings/lib/multiplex_router.cc',
      'public/cpp/bindings/lib/multiplex_router.h',
      'public/cpp/bindings/lib/native_enum_data.h',
      'public/cpp/bindings/lib/native_enum_serialization.h',
      'public/cpp/bindings/lib/native_struct.cc',
      'public/cpp/bindings/lib/native_struct_data.cc',
      'public/cpp/bindings/lib/native_struct_data.h',
      'public/cpp/bindings/lib/native_struct_serialization.cc',
      'public/cpp/bindings/lib/native_struct_serialization.h',
      'public/cpp/bindings/lib/no_interface.cc',
      'public/cpp/bindings/lib/pipe_control_message_handler.cc',
      'public/cpp/bindings/lib/pipe_control_message_proxy.cc',
      'public/cpp/bindings/lib/router.cc',
      'public/cpp/bindings/lib/router.h',
      'public/cpp/bindings/lib/scoped_interface_endpoint_handle.cc',
      'public/cpp/bindings/lib/serialization.h',
      'public/cpp/bindings/lib/serialization_context.cc',
      'public/cpp/bindings/lib/serialization_context.h',
      'public/cpp/bindings/lib/serialization_forward.h',
      'public/cpp/bindings/lib/serialization_forward.h',
      'public/cpp/bindings/lib/serialization_util.h',
      'public/cpp/bindings/lib/string_serialization.h',
      'public/cpp/bindings/lib/string_traits_string16.cc',
      'public/cpp/bindings/lib/sync_call_restrictions.cc',
      'public/cpp/bindings/lib/sync_handle_registry.cc',
      'public/cpp/bindings/lib/sync_handle_watcher.cc',
      'public/cpp/bindings/lib/template_util.h',
      'public/cpp/bindings/lib/validate_params.h',
      'public/cpp/bindings/lib/validation_context.cc',
      'public/cpp/bindings/lib/validation_context.h',
      'public/cpp/bindings/lib/validation_errors.cc',
      'public/cpp/bindings/lib/validation_errors.h',
      'public/cpp/bindings/lib/validation_util.cc',
      'public/cpp/bindings/lib/validation_util.h',
      'public/cpp/bindings/map_data_view.h',
      'public/cpp/bindings/map_traits.h',
      'public/cpp/bindings/map_traits_standard.h',
      'public/cpp/bindings/map_traits_stl.h',
      'public/cpp/bindings/message.h',
      'public/cpp/bindings/message_filter.h',
      'public/cpp/bindings/message_header_validator.h',
      'public/cpp/bindings/native_enum.h',
      'public/cpp/bindings/native_struct.h',
      'public/cpp/bindings/native_struct_data_view.h',
      'public/cpp/bindings/no_interface.h',
      'public/cpp/bindings/pipe_control_message_handler.h',
      'public/cpp/bindings/pipe_control_message_handler_delegate.h',
      'public/cpp/bindings/pipe_control_message_proxy.h',
      'public/cpp/bindings/scoped_interface_endpoint_handle.h',
      'public/cpp/bindings/stl_converters.h',
      'public/cpp/bindings/string.h',
      'public/cpp/bindings/string_data_view.h',
      'public/cpp/bindings/string_traits.h',
      'public/cpp/bindings/string_traits_standard.h',
      'public/cpp/bindings/string_traits_stl.h',
      'public/cpp/bindings/string_traits_string16.h',
      'public/cpp/bindings/string_traits_string_piece.h',
      'public/cpp/bindings/strong_binding.h',
      'public/cpp/bindings/struct_ptr.h',
      'public/cpp/bindings/struct_traits.h',
      'public/cpp/bindings/sync_call_restrictions.h',
      'public/cpp/bindings/sync_handle_registry.h',
      'public/cpp/bindings/sync_handle_watcher.h',
      'public/cpp/bindings/type_converter.h',
    ],
    'mojo_cpp_system_sources': [
      'public/cpp/system/buffer.cc',
      'public/cpp/system/buffer.h',
      'public/cpp/system/core.h',
      'public/cpp/system/data_pipe.h',
      'public/cpp/system/functions.h',
      'public/cpp/system/handle.h',
      'public/cpp/system/message.h',
      'public/cpp/system/message_pipe.h',
      'public/cpp/system/platform_handle.cc',
      'public/cpp/system/platform_handle.h',
      'public/cpp/system/watcher.cc',
      'public/cpp/system/watcher.h',
    ],
    'mojo_public_system_sources': [
      'public/c/system/buffer.h',
      'public/c/system/core.h',
      'public/c/system/data_pipe.h',
      'public/c/system/functions.h',
      'public/c/system/macros.h',
      'public/c/system/message_pipe.h',
      'public/c/system/platform_handle.h',
      'public/c/system/system_export.h',
      'public/c/system/thunks.cc',
      'public/c/system/thunks.h',
      'public/c/system/types.h',
      'public/c/system/wait_set.h',
    ],
  },
}
