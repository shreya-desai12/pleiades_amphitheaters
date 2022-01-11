# pleiades_amphitheaters

Code for collating Sebastian Heath's Roman Amphitheaters dataset with the Pleiades gazetteer of ancient places.


Install development packages including setup "requires" packages using:

```bash
pip install -r requirements_dev.txt
```

## tests

We are using the [nose2 unittest framework](https://docs.nose2.io/en/latest/). Relevant packages are included in the `requirements_dev.txt` file. Our tests are stored in the `tests` subdirectory. Configuration is in `nose2.cfg`. We use the `coverage` plugin as well to see how complete our tests are. Configuration details for the coverage plugin are found in `.coveragerc`. 

Here's how to run tests from the top package directory:

```bash
nose2
```

The resulting coverage report (in HTML) is written to `index.html` in the `htmlcov` subdirectory.

