#!/bin/bash

#
# Copyright 2019 Mani Sarkar
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

set -e
set -u
set -o pipefail

# Install and update necessary Linux packages

apt-get update && apt-get install -y --fix-missing \
                  wget curl liblapack-dev libswscale-dev pkg-config

apt-get install -y libc-ares2 libuv1 nodejs-doc
apt-get install -y npm

./install-dependencies.sh