A cli tool for generating IFD offsets within a tiff file, useful for optimizing load times of remote tiff files in viewers like viv.  An `offsets.json` file is written out adjacent to the input file in the folder from which the original file comes.

```
pip install generate-tiff-offsets
generate_tiff_offsets --input-file my_file.ome.tiff
```
