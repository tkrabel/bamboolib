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

DOCKER_USER_NAME=${DOCKER_USER_NAME:-"neomatrix369"}

IMAGE_NAME=${IMAGE_NAME:-bamboolib}
IMAGE_VERSION=${IMAGE_VERSION:-$(cat version.txt)}
DOCKER_FULL_TAG_NAME="${DOCKER_USER_NAME}/${IMAGE_NAME}"

WORKDIR=/home/jovyan

mkdir -p .local notebooks

if [[ "${DEBUG:-}" = "true" ]]; then
	docker run --rm                         \
	            --interactive --tty         \
		        --volume $(pwd)/notebooks:${WORKDIR}/work  \
	   	        --volume $(pwd)/.local:${WORKDIR}/.local \
	        	-p 8888:8888                \
	        	--workdir ${WORKDIR}        \
	        	--entrypoint /bin/bash      \
	        	${DOCKER_FULL_TAG_NAME}:${IMAGE_VERSION}	
else
	time docker run --rm                        \
		            --interactive --tty         \
	   	         	--volume $(pwd)/notebooks:${WORKDIR}/work  \
	   	         	--volume $(pwd)/.local:${WORKDIR}/.local \
	            	-p 8888:8888                \
	            	--workdir ${WORKDIR}        \
	            	${DOCKER_FULL_TAG_NAME}:${IMAGE_VERSION}
fi