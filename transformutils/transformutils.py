"""
This module contains utility functions for calculating coordinates and poses,
which are useful when writing ROS scripts in Python.

TODO: Update to use tf2 and PyKDL instead of tf_conversions
"""

from typing import List, Union

import numpy as np
import tf_conversions
from geometry_msgs.msg import Pose, Quaternion


def get_msg_from_translation_and_quaternion(translation: Union[np.ndarray, list], quaternion: Union[np.ndarray, list]) -> Pose:
    """Convert translation and quaternion to a Pose message.

    Args:
        translation: Translation represented as an array
        quaternion: Quaternion represented as an array

    Returns:
        Pose message
    """

    pose = Pose()
    pose.position.x = translation[0]
    pose.position.y = translation[1]
    pose.position.z = translation[2]
    pose.orientation.x = quaternion[0]
    pose.orientation.y = quaternion[1]
    pose.orientation.z = quaternion[2]
    pose.orientation.w = quaternion[3]

    return pose


def calc_homogeneous_matrix(pose: Pose) -> np.ndarray:
    """Convert a Pose message to a homogeneous matrix.

    Args:
        pose: Pose message

    Returns:
        Homogeneous matrix as a numpy array
    """

    angles = tf_conversions.transformations.euler_from_quaternion([
        pose.orientation.x,
        pose.orientation.y,
        pose.orientation.z,
        pose.orientation.w
    ])
    translate = [pose.position.x, pose.position.y, pose.position.z]
    homogeneous_matrix = tf_conversions.transformations.compose_matrix(
        angles=angles, translate=translate)

    return homogeneous_matrix


def get_msg_from_homogeneous_matrix(homogeneous_matrix: np.ndarray) -> Pose:
    """Convert a homogeneous matrix to a Pose message.

    Args:
        homogeneous_matrix: Homogeneous matrix as a numpy array

    Returns:
        Pose message
    """

    quaternion = tf_conversions.transformations.quaternion_from_matrix(
        homogeneous_matrix)
    translation = tf_conversions.transformations.translation_from_matrix(
        homogeneous_matrix)

    return get_msg_from_translation_and_quaternion(translation, quaternion)


def calc_transformed_pose(pose_from: Pose, pose_diff: Pose) -> Pose:
    """Calculate the pose of a coordinate system after a transformation.

    Args:
        pose_from: Pose of the coordinate system before the transformation
        pose_diff: Pose of the transformation in the coordinate system of the pose_from

    Returns:
        Pose of the coordinate system after the transformation
    """

    converted_matrix = (
        calc_homogeneous_matrix(pose_from) @ calc_homogeneous_matrix(pose_diff))

    return get_msg_from_homogeneous_matrix(converted_matrix)


def calc_relative_pose(pose_from: Pose, pose_to: Pose) -> Pose:
    """Calculate the pose of a coordinate system relative to another coordinate system.

    Args:
        pose_from: Pose of the coordinate system to which the relative pose is calculated
        pose_to: Pose of the coordinate system relative to the pose_from

    Returns:
        Pose of the coordinate system relative to the pose_from
    """

    converted_matrix = (
        tf_conversions.transformations.inverse_matrix(calc_homogeneous_matrix(pose_from)) @ calc_homogeneous_matrix(pose_to))

    return get_msg_from_homogeneous_matrix(converted_matrix)


def get_msg_from_array_2d(array_2d: Union[np.ndarray, list]) -> Pose:
    """Convert an array of 2D coordinates to a Pose message.

    Args:
        array_2d: Array of 2D coordinates

    Returns:
        Pose message
    """

    pose = Pose()
    quaternion = Quaternion(
        *tf_conversions.transformations.quaternion_from_euler(0, 0, array_2d[2]))
    pose.position.x = array_2d[0]
    pose.position.y = array_2d[1]
    pose.position.z = 0
    pose.orientation = quaternion

    return pose


def get_array_2d_from_msg(pose: Pose) -> List[float]:
    """Convert a Pose message to an array of 2D coordinates.

    Args:
        pose: Pose message

    Returns:
        Array of 2D coordinates
    """

    array_2d = [
        pose.position.x,
        pose.position.y,
        tf_conversions.transformations.euler_from_quaternion([
            pose.orientation.x,
            pose.orientation.y,
            pose.orientation.z,
            pose.orientation.w
        ])[2]
    ]
    return array_2d
