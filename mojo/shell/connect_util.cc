// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "mojo/shell/connect_util.h"

#include <utility>

#include "mojo/shell/application_manager.h"
#include "mojo/shell/capability_filter.h"
#include "mojo/shell/connect_to_application_params.h"

namespace mojo {
namespace shell {

ScopedMessagePipeHandle ConnectToInterfaceByName(
    ApplicationManager* application_manager,
    const Identity& source,
    const GURL& application_url,
    const std::string& interface_name) {
  shell::mojom::InterfaceProviderPtr remote_interfaces;
  scoped_ptr<ConnectToApplicationParams> params(new ConnectToApplicationParams);
  params->set_source(source);
  params->set_target(Identity(application_url, std::string(),
                              GetPermissiveCapabilityFilter()));
  params->set_remote_interfaces(GetProxy(&remote_interfaces));
  application_manager->ConnectToApplication(std::move(params));
  MessagePipe pipe;
  remote_interfaces->GetInterface(interface_name, std::move(pipe.handle1));
  return std::move(pipe.handle0);
}

}  // namespace shell
}  // namespace mojo
