"""Console script for generate_tiff_offsets."""
import argparse
import sys


def main():
    """Console script for generate_tiff_offsets."""
    parser = argparse.ArgumentParser(
        description='Create a json file for OME-TIFF offsets')
    parser.add_argument(
        '--input_file', required=True, type=Path,
        help='Directory containing ome-tiff files to read')
    args = parser.parse_args()
    main(args.input_file)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
