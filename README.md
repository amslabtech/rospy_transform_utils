# rospy_transform_utils

## Overview

This module contains utility functions for calculating coordinates and poses, which are useful when writing ROS scripts in Python.

|Functions|
|:-|
|get_msg_from_translation_and_quaternion|
|calc_homogeneous_matrix|
|get_msg_from_homogeneous_matrix|
|calc_transformed_pose|
|calc_relative_pose|
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
pip3 install https://github.com/amslabtech/rospy_transform_utils/archive/master.zip
```

## Usage

You can import this module for example:

```python
import transformutils
```
