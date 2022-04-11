# rospy_transform_utils

## Overview

This module contains utility functions for calculating coordinates and poses, which are useful when writing ROS scripts in Python.

|Functions|
|:-|
|calc_homogeneous_matrix|
|calc_relative_pose|
|calc_global_pose_from_relative_pose|
|get_msg_from_translation_and_quaternion|
|get_msg_from_array_2d|
|get_array_2d_from_msg|

## Requirements

- numpy
- rospy
- tf_conversions


## Install

You can install this module with the following command if you are using pip3.

The requirements will be automatically installed by pip3.

```sh
pip3 install git+https://github.com/amslabtech/rospy_transform_utils.git
```

## Usage

You can import this module for example:

```python
import transformutils
```
