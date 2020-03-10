import errno
from setuptools import setup, find_packages
from setuptools.command.install import install
from subprocess import check_call

def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()

setup(name='pulumi_drone',
      version='${VERSION}',
      description='A Pulumi package to safely setup drone in Pulumi.',
      long_description=readme(),
      long_description_content_type='text/markdown',
      keywords='pulumi drone',
      url='https://pulumi.io',
      project_urls={
          'Repository': 'https://github.com/exfi/pulumi-drone'
      },
      license='Apache-2.0',
      packages=find_packages(),
      package_data={
			'pulumi_drone': [
				'py.typed'
			]
		},
      install_requires=[
          'parver>=0.2.1',
          'pulumi>=1.0.0,<2.0.0',
          'semver>=2.8.1'
      ],
      zip_safe=False)