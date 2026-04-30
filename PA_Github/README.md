# PA Package — Geometri

2D line ve point nesneleri için basit bir Python paketi.

## Dosya Yapısı

```
pa_package/
├── geometry/
│   ├── points_lines.py       
│   ├── test_points_lines.py 
│   ├── point1.txt            
│   ├── points2.txt           
│   ├── line1.txt             
│   └── line2.txt             
├── README.md
└── requirements.txt
```

## Sınıflar

### `point(x, y, name="")`
- `get_enlem()` → x koordinatı
- `get_boylam()` → y koordinatı

### `line(points, name="")`
- `get_points()` → nokta listesi

## Testleri Çalıştırma

```bash
cd geometry
pytest test_points_lines.py -v
```
