// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef MOJO_PUBLIC_BINDINGS_LIB_MESSAGE_INTERNAL_H_
#define MOJO_PUBLIC_BINDINGS_LIB_MESSAGE_INTERNAL_H_

#include "mojo/public/bindings/lib/bindings_internal.h"

namespace mojo {
namespace internal {

#pragma pack(push, 1)

enum {
  kMessageExpectsResponse = 1 << 0,
  kMessageIsResponse      = 1 << 1
};

struct MessageHeader : internal::StructHeader {
  uint32_t name;
  uint32_t flags;
};
MOJO_COMPILE_ASSERT(sizeof(MessageHeader) == 16, bad_sizeof_MessageHeader);

struct MessageHeaderWithRequestID : MessageHeader {
  uint64_t request_id;
};
MOJO_COMPILE_ASSERT(sizeof(MessageHeaderWithRequestID) == 24,
                    bad_sizeof_MessageHeaderWithRequestID);

struct MessageData {
  MessageHeader header;
  uint8_t payload[1];
};
MOJO_COMPILE_ASSERT(sizeof(MessageData) == 17, bad_sizeof_MessageData);

struct MessageDataWithRequestID {
  MessageHeaderWithRequestID header;
  uint8_t payload[1];
};
MOJO_COMPILE_ASSERT(sizeof(MessageDataWithRequestID) == 25,
                    bad_sizeof_MessageDataWithRequestID);

#pragma pack(pop)

}  // namespace internal
}  // namespace mojo

#endif  // MOJO_PUBLIC_BINDINGS_LIB_MESSAGE_INTERNAL_H_
