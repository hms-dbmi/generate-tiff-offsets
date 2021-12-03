# generate-tiff-offsets

A python cli (and web-application) for generating an Image File Directory (IFD)
index for TIFFs. Read [our paper](https://osf.io/wd2gu/) or watch
[this video](https://www.youtube.com/watch?v=cGB2TsSnfbo) to learn more about
how our strategy improves random chunk access speeds for OME-TIFF in
[Viv](https://github.com/hms-dbmi/viv).

## TIFF IFD Index specification

The content of an TIFF IFD Index should match the given description here.

### Version 0

Prototype spec for the structure required for TIFF IFD Index (JSON):

```
[IFD_offset_0, IFD_offset_1, IFD_offset_2, IFD_offset_3, ..., IFD_offset_N]
```

where `IFD_offset_n` corresponds to the _nth_ byte-offset for the corresponding
Image File Directory in the linear TIFF series.

> **Note**: For OME-TIFF, the ordering of IFDs is determined by the `DimensionOrder`
> attribute in the OME-XML metadata. Each combination of `C`, `Z`, and `T`
> corresponds to **one IFD**, meaning the total number of IFDs is the product
> of these dimensions (`T x C x Z`) and _independent_ of the number of pyramidal
> resolutions in the OME-TIFF.

## 🐍 Python CLI

```bash
  pip install generate-tiff-offsets
  generate_tiff_offsets --input_file <my_file>.ome.tiff
```

This command writes the Version 0 Index to the local file system, adjacent to the
input TIFF with the file name `<my_file>.offsets.json`.

> **Note**: ⚠️ Our OME-TIFF web-viewer, [Avivator](http://avivator.gehlenborglab.org) expects
> this naming convension and folder structure in order for the Index
> OME-TIFF to be recognized.

## 🌎 Web application

Our website requires no installation and can be used to generate the Version 0 Index
directly in the browser. See our [video tutorial](https://www.youtube.com/watch?v=cGB2TsSnfbo)
for usage instructions.
