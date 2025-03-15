# setup.py
import os
import re
import sys
import subprocess
from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from distutils.version import LooseVersion

class CMakeExtension(Extension):
    def __init__(self, name, source_dir=''):
        super().__init__(name, sources=[])
        self.source_dir = os.path.abspath(source_dir)

class CMakeBuild(build_ext):
    def run(self):
        self._validate_environment()
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
        cmake_args = [
            f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={extdir}',
            f'-DPYTHON_EXECUTABLE={sys.executable}',
            f'-DCMAKE_BUILD_TYPE={"Debug" if self.debug else "Release"}'
        ]

        self._configure_and_build(str(ext.source_dir), cmake_args)

    def _configure_and_build(self, source_dir, cmake_args):
        os.makedirs(self.build_temp, exist_ok=True)
        self.spawn(['cmake', '-S', source_dir, '-B', self.build_temp] + cmake_args)
        self.spawn(['cmake', '--build', self.build_temp, '--config', "Debug" if self.debug else "Release"])

    def _validate_environment(self):
        cmake = self._get_cmake_version()
        if LooseVersion(cmake) < LooseVersion('3.18'):
            raise RuntimeError("CMake >= 3.18 required")

    def _get_cmake_version(self):
        try:
            # Check system CMake instead of Python module
            output = subprocess.check_output(['cmake', '--version'])
            return re.search(r'version\s+([\d.]+)', output.decode()).group(1)
        except (subprocess.CalledProcessError, FileNotFoundError):
            raise RuntimeError("CMake executable not found in PATH")

setup(
    name='py-cuda-study',  # python package name (used to do pip uninstall)
    version='0.1',
    packages=find_packages(),
    ext_modules=[CMakeExtension('random-name-with-no-importance', source_dir='pybind11_bindings')],
    cmdclass={'build_ext': CMakeBuild},
    zip_safe=False,
    python_requires='>=3.8',
)
