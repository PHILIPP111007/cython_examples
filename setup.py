# Use: python setup.py build_ext --inplace

from setuptools import setup, Extension
from Cython.Build import cythonize

cython_directives = {
    "boundscheck": False,
    "cdivision": True,
    "wraparound": False,
    "language_level": 3,
}

# Options.default_options['language_level'] = '3'


# Options.docstrings = False
# Options.language_level = 2



extensions = [
    Extension(
        "modules.loop",
        sources=["modules/loop.py"],
        language="c",
    ),
    Extension(
        "modules.time_counter",
        sources=["modules/time_counter.py"],
        language="c",
    ),
]

setup(
    name="modules",
    ext_modules=cythonize(
        extensions,
    ),
)
