# Copyright 2019 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""
This module py_transforms is implemented basing on Python. It provides common
operations including OneHotOp.
"""

from .validators import check_one_hot_op
from .vision import py_transforms_util as util


class OneHotOp:
    """
    Apply one hot encoding transformation to the input label, make label be more smoothing and continuous.

    Args:
        num_classes (int): Number of classes of objects in dataset. Value must be larger than 0.
        smoothing_rate (float, optional): Adjustable hyperparameter for label smoothing level.
            (Default=0.0 means no smoothing is applied.)
    """

    @check_one_hot_op
    def __init__(self, num_classes, smoothing_rate=0.0):
        self.num_classes = num_classes
        self.smoothing_rate = smoothing_rate

    def __call__(self, label):
        """
        Call method.

        Args:
            label (numpy.ndarray): label to be applied label smoothing.

        Returns:
            label (numpy.ndarray), label after being Smoothed.
        """
        return util.one_hot_encoding(label, self.num_classes, self.smoothing_rate)
