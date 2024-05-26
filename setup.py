# Use: python setup.py build_ext --inplace

from setuptools import setup, Extension
from Cython.Build import cythonize


extensions = [
    Extension(
        name="modules.loop",
        sources=["modules/loop.py"],
    ),
    Extension(
        name="modules.time_counter",
        sources=["modules/time_counter.py"],
    ),
]


setup(
    name="modules",
    ext_modules=cythonize(extensions),
    compiler_directives={"language_level": "3"},
    annotate=True,
)
