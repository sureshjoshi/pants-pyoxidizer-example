python_sources(name="libhellofib", sources=["**/*.py"])

python_distribution(
    name="hellofib-dist",
    dependencies=[":libhellofib"],
    wheel=True,
    sdist=False,
    provides=setup_py(
        name="hellofib-dist",
        version="0.0.1",
        description="A distribution for the hello fib library.",
    ),
)

pyoxidizer_binary(
    name="hellofib-bin",
    entry_point="hellofib.main",
    dependencies=[":hellofib-dist"],
)
