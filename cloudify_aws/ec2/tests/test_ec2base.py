# Copyright (c) 2018 Cloudify Platform Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from cloudify_aws.common.tests.test_base import TestServiceBase
from cloudify_aws.ec2 import EC2Base


class TestEC2Base(TestServiceBase):

    def setUp(self):
        super(TestEC2Base, self).setUp()
        self.base = EC2Base("ctx_node", resource_id=True,
                            client=True, logger=None)


if __name__ == '__main__':
    unittest.main()
