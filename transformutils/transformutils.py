from typing import List, Union

import numpy as np
import tf_conversions
from geometry_msgs.msg import Pose, Quaternion


def calc_homogeneous_matrix(pose: Pose) -> np.ndarray:

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


def calc_transformed_pose(pose_from: Pose, pose_diff: Pose) -> Pose:

    converted_matrix = (
        calc_homogeneous_matrix(pose_from) @ calc_homogeneous_matrix(pose_diff))
    quaternion = tf_conversions.transformations.quaternion_from_matrix(
        converted_matrix)
    translation = tf_conversions.transformations.translation_from_matrix(
        converted_matrix)

    return get_msg_from_translation_and_quaternion(translation, quaternion)


def calc_relative_pose(pose_from: Pose, pose_to: Pose) -> Pose:

    converted_matrix = (
        tf_conversions.transformations.inverse_matrix(calc_homogeneous_matrix(pose_from)) @ calc_homogeneous_matrix(pose_to))
    quaternion = tf_conversions.transformations.quaternion_from_matrix(
        converted_matrix)
    translation = tf_conversions.transformations.translation_from_matrix(
        converted_matrix)

    return get_msg_from_translation_and_quaternion(translation, quaternion)


def get_msg_from_translation_and_quaternion(translation: Union[np.ndarray, list], quaternion: Union[np.ndarray, list]) -> Pose:

    pose = Pose()
    pose.position.x = translation[0]
    pose.position.y = translation[1]
    pose.position.z = translation[2]
    pose.orientation.x = quaternion[0]
    pose.orientation.y = quaternion[1]
    pose.orientation.z = quaternion[2]
    pose.orientation.w = quaternion[3]

    return pose


def get_msg_from_array_2d(array_2d: Union[np.ndarray, list]) -> Pose:

    pose = Pose()
    quaternion = Quaternion(
        *tf_conversions.transformations.quaternion_from_euler(0, 0, array_2d[2]))
    pose.position.x = array_2d[0]
    pose.position.y = array_2d[1]
    pose.position.z = 0
    pose.orientation = quaternion

    return pose


def get_array_2d_from_msg(pose: Pose) -> List[float]:

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
