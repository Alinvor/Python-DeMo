# -*- coding:utf-8 -*-
"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/Alinvor/Python-DeMo
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import os
import sys


def read_text(file_name):
    ''' the read describe readme files content. '''
    content = ''
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if sys.version_info.major > 2:
                content += str(line)
            else:
                content += str(line).encode('utf-8')
    # print(content)
    return content


PROJECT_PREFIX = '/Users/dovsnier/Documents/Work_Space_Python/Python-DeMo/'
project = PROJECT_PREFIX
print(project)
PROJECT_DIRECTORY = 'git'  # project directory
PROJECT_README_FILE = 'README.md'  # project readme file
README_ROOT_DIRECTORY = os.path.join(project, 'doc/description')
README_PROJECT_DIRECTORY = os.path.join(README_ROOT_DIRECTORY, PROJECT_DIRECTORY)
PROJECT_DESCRIPTION = os.path.join(README_PROJECT_DIRECTORY, PROJECT_README_FILE)
#
# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.
#
# |  序列  |                 字段                  |   数据类型   |  选项  |  描述                 | 备注 |
# | :---: | :-----------------------------------: | :---------: | :---: | -------------------- | ---- |
# |   1   |             DVSNIER_NAME              |   string    |   Y   | 包名称                |      |
# |   2   |            DVSNIER_VERSION            |   string    |   Y   | 包版本                |      |
# |   3   |          DVSNIER_DESCRIPTOIN          |   string    |       | 包简单描述             |      |
# |   4   |       DVSNIER_LONG_DESCRIPTOIN        |    file     |       | 较长文档描述           |      |
# |   5   | DVSNIER_LONG_DESCRIPTION_CONTENT_TYPE |   string    |       | 长文本类型描述          |      |
# |   6   |              DVSNIER_URL              |    http     |       | 项目主页               |      |
# |   7   |            DVSNIER_AUTHOR             |   string    |       | 项目作者               |      |
# |   8   |         DVSNIER_AUTHOR_EMAIL          |    email    |       | 项目作者邮箱           |      |
# |   9   |         DVSNIER_LICENSE               |    许可证    |       | 许可证                |      |
# |  10   |          DVSNIER_CLASSIFIERS          | classifiers |       | 项目分类器             |      |
# |  11   |           DVSNIER_KEYWORDS            |  keywords   |       | 项目关键字             |      |
# |  12   |          DVSNIER_PACKAGE_DIR          |   string    |       | 包目录                |      |
# |  13   |          DVSNIER_PY_MODULES           |   string    |   Y   | 模块名称               |      |
# |  14   |           DVSNIER_PACKAGES            |   string    |   Y   | 包名称                 |      |
# |  15   |        DVSNIER_PYTHON_REQUIRES        |   string    |   Y   | 版本匹配分类器描述符     |      |
# |  16   |       DVSNIER_INSTALL_REQUIRES        |    list     |       | 依赖库                 |      |
# |  17   |        DVSNIER_EXTRAS_REQUIRE         |    dict     |       | 附加/扩展依赖           |      |
# |  18   |         DVSNIER_PACKAGE_DATA          |    dict     |       | 包数据文件              |      |
# |  19   |          DVSNIER_DATA_FILES           |    list     |       | 包外数据文件            |      |
# |  20   |         DVSNIER_ENTRY_POINTS          |    dict     |       | 入口点                 |      |
# |  21   |         DVSNIER_PROJECT_URLS          |    dict     |       | 项目 URL               |      |
# |  22   |                                       |             |       |                       |      |
DVSNIER_NAME = 'com.dvsnier.git'  # Required
DVSNIER_VERSION = '0.0.1.dev1'  # Required
DVSNIER_DESCRIPTOIN = 'this is dvsnier git.'  # Optional
# Get the long description from the README file
DVSNIER_LONG_DESCRIPTOIN = read_text(str(PROJECT_DESCRIPTION))  # Optional
DVSNIER_LONG_DESCRIPTION_CONTENT_TYPE = 'text/markdown'  # Optional
DVSNIER_URL = 'https://github.com/Alinvor/Python-DeMo'  # Optional
DVSNIER_AUTHOR = 'dvsnier'  # Optional
DVSNIER_AUTHOR_EMAIL = 'dovsnier@qq.com'  # Optional
DVSNIER_LICENSE = 'MIT'  # Optional
DVSNIER_CLASSIFIERS = [  # Optional
    #
    # https://pypi.org/classifiers/
    #
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    # 'Intended Audience :: Developers',
    # 'Topic :: Software Development :: Build Tools',
    'Topic :: Software Development :: Libraries',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate you support Python 3. These classifiers are *not*
    # checked by 'pip install'. See instead 'python_requires' below.
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    # 'Programming Language :: Python :: 3 :: Only',
    # 'Operating System :: OS Independent'
]
DVSNIER_KEYWORDS = 'git, development'  # Optional
DVSNIER_PACKAGE_DIR = {'': 'src'}  # Optional
# DVSNIER_PY_MODULES = ["xxx"]  # Required
# DVSNIER_PACKAGES = find_packages(include=['xxx', 'xxx.*'])  # Required
DVSNIER_PACKAGES = find_packages(where='src')  # Required
# DVSNIER_PYTHON_REQUIRES = '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*'
DVSNIER_PYTHON_REQUIRES = '>=2.7, <4'
DVSNIER_INSTALL_REQUIRES = [  # Optional
    # 'discover==0.4.0',
    # 'build==0.4.0',
    # 'pathlib2==2.3.5',
    # 'toml==0.10.2',
    # 'twine==1.15.0',
]
DVSNIER_EXTRAS_REQUIRE = {  # Optional
    'dev': ['check-manifest'],
    'test': ['coverage']
}
DVSNIER_PACKAGE_DATA = {  # Optional
    # 'sample': ['package_data.dat'],
}
DVSNIER_DATA_FILES = [  # Optional
    # ('my_data', ['data/data_file'])
]
DVSNIER_ENTRY_POINTS = {  # Optional
    # 'console_scripts': [
    #     'dvs-dir=dvs:main',
    # ],
}
DVSNIER_PROJECT_URLS = {  # Optional
    'Bug_Tracker': 'https://github.com/Alinvor/Python-DeMo/issues',
    'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
    'Funding': 'https://donate.pypi.org',
    'Wiki': 'https://github.com/Alinvor/Python-DeMo/wiki',
    'Source': 'https://github.com/Alinvor/Python-DeMo'
}

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install com.dvsnier.xxx
    #
    # And where it will live on PyPI: https://pypi.org/project/com.dvsnier.xxx/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name=DVSNIER_NAME,  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    # https://semver.org/lang/zh-CN/
    #
    # 1.2.0.dev1   Development release
    # 1.2.0a1      Alpha Release
    # 1.2.0b1      Beta Release
    # 1.2.0rc1     Release Candidate
    # 1.2.0        Final Release
    # 1.2.0.post1  Post Release
    # 15.10        Date based release
    # 23           Serial release
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=DVSNIER_VERSION,  # Required

    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description=DVSNIER_DESCRIPTOIN,  # Optional

    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=DVSNIER_LONG_DESCRIPTOIN,  # Optional

    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    #
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type=DVSNIER_LONG_DESCRIPTION_CONTENT_TYPE,  # Optional (see note above)

    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url=DVSNIER_URL,  # Optional

    # This should be your name or the name of the organization which owns the project.
    author=DVSNIER_AUTHOR,  # Optional

    # This should be a valid email address corresponding to the author listed above.
    author_email=DVSNIER_AUTHOR_EMAIL,  # Optional

    # The license argument doesn’t have to indicate the license under which your package is being released,
    # although you may optionally do so if you want. If you’re using a standard, well-known license, then
    # your main indication can and should be via the classifiers argument. Classifiers exist for all major
    #  open-source licenses.
    license=DVSNIER_LICENSE,  # Optional

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=DVSNIER_CLASSIFIERS,  # Optional

    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a list of additional keywords, separated
    # by commas, to be used to assist searching for the distribution in a
    # larger catalog.
    keywords=DVSNIER_KEYWORDS,  # Optional

    # When your source code is in a subdirectory under the project root, e.g.
    # `src/`, it is necessary to specify the `package_dir` argument.
    package_dir=DVSNIER_PACKAGE_DIR,  # Optional

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=DVSNIER_PACKAGES,  # Required

    # If your project contains any single-file Python modules that aren’t part of
    # a package, set py_modules to a list of the names of the modules (minus the .py
    # extension) in order to make setuptools aware of them.
    # py_modules=DVSNIER_PY_MODULES,  # Required

    # Specify which Python versions you support. In contrast to the
    # 'Programming Language' classifiers above, 'pip install' will check this
    # and refuse to install the project if the version does not match. See
    # https://packaging.python.org/guides/distributing-packages-using-setuptools/#python-requires
    python_requires=DVSNIER_PYTHON_REQUIRES,

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    install_requires=DVSNIER_INSTALL_REQUIRES,  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing projects.
    extras_require=DVSNIER_EXTRAS_REQUIRE,  # Optional

    # If there are data files included in your packages that need to be
    # installed, specify them here.
    # https://setuptools.readthedocs.io/en/latest/userguide/datafiles.html
    package_data=DVSNIER_PACKAGE_DATA,  # Optional

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/distutils/setupscript.html#installing-additional-files
    # http://docs.python.org/3/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=DVSNIER_DATA_FILES,  # Optional

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `dvsnier` which
    # executes the function `main` from this package when invoked:
    entry_points=DVSNIER_ENTRY_POINTS,  # Optional

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls=DVSNIER_PROJECT_URLS,  # Optional
)
