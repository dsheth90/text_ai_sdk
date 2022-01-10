# from setuptools import setup, find_packages
import os
import glob
# import re
# import ast
#
#
# def parse_requirements(filehandle):
#     for line in filehandle:
#         line = line.strip()
#         if line == '':
#             continue
#         # Comments are lines that start with # only.
#         elif not line or line.startswith('#'):
#             continue
#         elif (line.startswith('-r') or line.startswith('--requirement') or
#               line.startswith('-f') or line.startswith('--find-links') or
#               line.startswith('-i') or line.startswith('--index-url') or
#               line.startswith('--extra-index-url') or line.startswith('--no-index') or
#               line.startswith('-Z') or line.startswith('--always-unzip')):
#             continue
#         else:
#             yield line
#
#
# _version_re = re.compile(r'__version__\s+=\s+(.*)')
#
# # with open('src/rev_ai/__init__.py', 'rb') as f:
# #     version = str(ast.literal_eval(_version_re.search(
# #         f.read().decode('utf-8')).group(1)))
#
# with open('README.md') as readme_file:
#     readme = readme_file.read()
#
# with open('HISTORY.rst') as history_file:
#     history = history_file.read()
#
# with open('requirements.txt', 'r') as req_file:
#     requirements = list(parse_requirements(req_file))
#
#
# setup(name='text-ai',
#       version='0.0.1',
#       description='Text-ai product initial release',
#       packages=find_packages(),
#       long_description=readme + '\n\n' + history,
#       long_description_content_type='text/markdown',
#       author="Text Ai",
#       package_dir={'': 'src'},
#       include_package_data=True,
#       install_requires=requirements,
#       zip_safe=False,
#       license='MIT license',
#       keywords='text_ai',
#       classifiers=[
#           'License :: OSI Approved :: MIT License',
#           'Intended Audience :: Developers',
#           'License :: OSI Approved :: MIT License',
#           'Natural Language :: English',
#           'Programming Language :: Python :: 3.4',
#           'Programming Language :: Python :: 3.5',
#           'Programming Language :: Python :: 3.6',
#           'Programming Language :: Python :: 3.7',
#           'Programming Language :: Python :: 3.8',
#           'Programming Language :: Python :: 3.8.8',
#       ],
#       )



import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'
PACKAGE_NAME = 'text_ai'
AUTHOR = 'Dhrumil Sheth'
AUTHOR_EMAIL = 'dhrumilsheth90@gmail.com'
URL = 'https://github.com/you/your_package'

LICENSE = 'MIT license'
DESCRIPTION = 'Text-ai product initial release'
LONG_DESCRIPTION = (HERE / "Readme.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'requests',
]

setup(name='text_ai',
      version='0.0.1',
      description='test',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob.glob('src/*.py')]
      )
