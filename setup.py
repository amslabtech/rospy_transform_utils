from setuptools import setup, find_packages

setup(
    name="transformutils",
    version="1.1",
    license="MIT",
    description="Useful conversion tools for rospy",
    author="Yasunori Hirakawa",
    url="https://github.com/amslabtech/rospy_transform_utils.git",
    package=find_packages(),
    install_requires=["numpy", "rospy", "tf_conversions"]
)
