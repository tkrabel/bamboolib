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

echo "Install/upgrade npm"

npm install -g npm

# Quick review of program versions
npm --version
python --version
pip --version

echo "Install components using python and pip"

# Install python packages for jupyter lab
python -m pip install pandas matplotlib

pip install 'bamboolib>=1.6.2'
jupyter nbextension install --py qgrid --sys-prefix
jupyter nbextension enable --py qgrid --sys-prefix 
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter nbextension install --py bamboolib --sys-prefix
jupyter nbextension enable --py bamboolib --sys-prefix