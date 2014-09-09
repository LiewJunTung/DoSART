from setuptools import setup

setup(
    name='DoS Launcher with Reporting and Suggestion Tool',
    version='2.2',
    url='http://kaibuku.com',
    packages=["app"],
    license='MIT',
    author='Liew',
    author_email='pandawarrior91@gmail.com',
    include_package_data=True,
    description='To provide penetration tester the tool to test Dos Attacks against their own web server',
    long_description=open("README.txt").read(),
    install_requires=[
        "flask",
        "pygal",
        "requests",
        ],
    )