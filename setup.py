from distutils.core import setup

setup(
    name='dosart',
    version='1.0d',
    packages=[''],
    url='',
    license='MIT',
    package=['app'],
    Include_package_data=True,
    author='Liew',
    author_email='pandawarrior91@gmail.com',
    include_package_data=True,
    description='Denial of Service Attack and Reporting Tool (DoSART)',
    install_requires=[
        "flask",
        "pygal",
        "Pillow",
        ],
)
