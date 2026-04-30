# PA Package — Geometry

A basic Python package for 2D Points and Lines

## File Content

```
pa_package/
├── geometry/
│   ├── Geometry.py       
│   ├── point1.txt            
│   ├── points2.txt           
│   ├── line1.txt             
│   └── line2.txt             
├── README.md
└── requirements.txt
```

## Classes

### `point(x, y, name="")`
- `get_enlem()` → x coordinate
- `get_boylam()` → y coordinate

### `line(points, name="")`
- `get_points()` → point list

```bash
cd geometry
pytest test_points_lines.py -v
```
