=====================
generate-tiff-offsets
=====================


.. image:: https://img.shields.io/pypi/v/generate_tiff_offsets.svg
        :target: https://pypi.python.org/pypi/generate_tiff_offsets

.. image:: https://img.shields.io/travis/ilan-gold/generate_tiff_offsets.svg
        :target: https://travis-ci.com/ilan-gold/generate_tiff_offsets

.. image:: https://readthedocs.org/projects/generate-tiff-offsets/badge/?version=latest
        :target: https://generate-tiff-offsets.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




A cli tool for generating IFD offsets within a tiff file, useful for optimizing load times of remote tiff files in viewers like viv.  An `offsets.json` file is written out adjacent to the input file in the folder from which the original file comes.

```
pip install generate-tiff-offsets
generate-tiff-offsets --input-file my_file.ome.tiff
```
