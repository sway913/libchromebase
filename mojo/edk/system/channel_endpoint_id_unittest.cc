// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "mojo/edk/system/channel_endpoint_id.h"

#include <sstream>

#include "testing/gtest/include/gtest/gtest.h"

namespace mojo {
namespace system {
namespace {

TEST(ChannelEndpointIdTest, Basic) {
  ChannelEndpointId invalid;
  ChannelEndpointId bootstrap(ChannelEndpointId::GetBootstrap());

  EXPECT_EQ(invalid, invalid);
  EXPECT_EQ(bootstrap, bootstrap);
  EXPECT_FALSE(invalid == bootstrap);

  EXPECT_FALSE(invalid != invalid);
  EXPECT_FALSE(bootstrap != bootstrap);
  EXPECT_NE(invalid, bootstrap);

  EXPECT_FALSE(invalid < invalid);
  EXPECT_LT(invalid, bootstrap);

  EXPECT_FALSE(invalid.is_valid());
  EXPECT_TRUE(bootstrap.is_valid());

  // Test assignment.
  ChannelEndpointId copy;
  copy = bootstrap;
  EXPECT_EQ(copy, bootstrap);
  copy = invalid;
  EXPECT_EQ(copy, invalid);
}

// Tests values of invalid and bootstrap IDs. (This tests implementation
// details.)
TEST(ChannelEndpointIdTest, Value) {
  EXPECT_EQ(0u, ChannelEndpointId().value());
  EXPECT_EQ(1u, ChannelEndpointId::GetBootstrap().value());
}

// Tests ostream output. (This tests implementation details.)
TEST(ChannelEndpointIdTest, Ostream) {
  {
    std::ostringstream stream;
    stream << ChannelEndpointId();
    EXPECT_EQ("0", stream.str());
  }
  {
    std::ostringstream stream;
    stream << ChannelEndpointId::GetBootstrap();
    EXPECT_EQ("1", stream.str());
  }
}

TEST(LocalChannelEndpointIdGeneratorTest, Basic) {
  LocalChannelEndpointIdGenerator gen;

  ChannelEndpointId id1;
  EXPECT_FALSE(id1.is_valid());  // Check sanity.

  id1 = gen.GetNext();
  EXPECT_TRUE(id1.is_valid());

  EXPECT_EQ(id1, ChannelEndpointId::GetBootstrap());

  ChannelEndpointId id2 = gen.GetNext();
  EXPECT_TRUE(id2.is_valid());
  // Technically, nonequality here is an implementation detail, since, e.g.,
  // random generation of IDs would be a valid implementation.
  EXPECT_NE(id2, id1);
  // ... but right now we just increment to generate IDs.
  EXPECT_EQ(2u, id2.value());
}

}  // namespace

// Tests that the generator handles wrap-around correctly. (This tests
// implementation details.) This test isn't in an anonymous namespace, since
// it needs to be friended.
TEST(LocalChannelEndpointIdGeneratorTest, WrapAround) {
  LocalChannelEndpointIdGenerator gen;
  gen.next_channel_endpoint_id_.value_ = static_cast<uint32_t>(-1);

  ChannelEndpointId id = gen.GetNext();
  EXPECT_TRUE(id.is_valid());
  EXPECT_EQ(static_cast<uint32_t>(-1), id.value());

  id = gen.GetNext();
  EXPECT_TRUE(id.is_valid());
  EXPECT_EQ(1u, id.value());
}

}  // namespace system
}  // namespace mojo
