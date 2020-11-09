import json
import re
from pathlib import Path

from tifffile import tifffile

def get_offsets(tiff_filepath):
    with tifffile.TiffFile(tiff_filepath) as tif:
        offsets = [page.offset for page in tif.pages]
    return offsets

def generate_tiff_offsets(input_file):

  # Get list of offsets.
  offsets = get_offsets(str(input_file))

  # Get output path for OME.TIFF.
  output_dir = Path(input_file).parent

  # Set output filename for JSON file and dump to disk.
  output_path = re.sub(r'((\.ome)?\.tiff?)', '.offsets.json', str(input_file))
  with open(output_path, 'w+') as f:
      f.write(json.dumps(offsets))