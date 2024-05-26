# cython_examples

Create Python env

```sh
micromamba env create -f ./env.yml
```

Compile Cython code

```sh
python setup.py build_ext --inplace
```

And run

```sh
python main.py
```
