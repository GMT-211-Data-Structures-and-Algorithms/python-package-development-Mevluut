# Geometry_Package

A Python package for working with 2D Points and Lines.

## Project Structure
python-package-development-Mevluut/
├── docs/
│   ├── conf.py
│   ├── index.rst
│   └── _build/html/        ← generated documentation
├── geometry.py
├── point1.txt
├── points2.txt
├── line1.txt
├── line2.txt
└── README.md

## Classes

### `point(x, y, name="")`
Represents a point in 2D space.
- `get_enlem()` → returns x coordinate
- `get_boylam()` → returns y coordinate

### `line(points, name="")`
Represents a line consisting of multiple points.
- `get_points()` → returns list of points

## Functions

- `read_points(filename)` → reads points from a text file
- `read_lines(filename)` → reads lines from a text file

## Documentation

Built with [Sphinx](https://www.sphinx-doc.org/) using the Alabaster theme.

To regenerate the docs:
```bash
cd docs
.\make.bat html
```

## Author

Mevlüt Can Çınar — Hacettepe University, Geomatics Engineering
