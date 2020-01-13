from setuptools import setup, find_packages

setup(
    name='plasma-dpiswitch',
    version='0.1',
    packages=find_packages(),
    scripts=['dpiswitch','dpiswitch-ui'],
    install_requires=open('requirements.txt').read(),

    package_data = {
      'ui': ['ui/*'],
    },
    data_files=[( 'ui' ,['ui/dpiswitch.ui'])]
)
