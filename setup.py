from setuptools import find_packages, setup

setup(
    name="transformutils",
    version="1.1",
    license="MIT",
    description="Useful conversion tools for rospy",
    author="Yasunori Hirakawa",
    url="https://github.com/amslabtech/rospy_transform_utils.git",
    packages=["transformutils"],
    install_requires=["numpy", "rospy", "tf_conversions"]
)
