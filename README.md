markdown# Geometry_Package

A Python package for working with 2D Points and Lines.

## Project Structure
python-package-development-Mevluut/
├── docs/
│   ├── conf.py
│   ├── index.rst
│   ├── point_page.rst
│   ├── line_page.rst
│   └── _build/html/     
├── Point.py
├── Line.py
├── point1.txt
├── points2.txt
├── line1.txt
├── line2.txt
└── README.md

## Classes

### `point(x, y, name="")` — Point.py
Represents a point in 2D space.
- `get_enlem()` → returns x coordinate (latitude)
- `get_boylam()` → returns y coordinate (longitude)

### `line(points, name="")` — Line.py
Represents a line consisting of multiple points.
- `get_points()` → returns list of points

## Functions

- `read_points(filename)` → reads points from a text file
- `read_lines(filename)` → reads lines from a text file

## Documentation

Built with [Sphinx](https://www.sphinx-doc.org/) using the Alabaster theme.  
Point and Line modules are documented separately with source code viewer enabled.

To regenerate the docs:
```bash
cd docs
.\make.bat html
```

## Author

Mevlüt Can Çınar — Hacettepe University, Geomatic Engineering
