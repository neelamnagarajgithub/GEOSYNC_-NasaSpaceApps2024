import sys
import json

def safe_divide(numerator, denominator):
    return numerator / denominator if denominator != 0 else 0

def ndvi(NIR, Red):
    return safe_divide(NIR - Red, NIR + Red)

def evi(NIR, Red, Blue, G=2.5, C1=6, C2=7.5, L=1):
    return G * safe_divide(NIR - Red, NIR + C1 * Red - C2 * Blue + L)

def savi(NIR, Red, L=0.5):
    return safe_divide(NIR - Red, NIR + Red + L) * (1 + L)

def ndwi(NIR, SWIR):
    return safe_divide(NIR - SWIR, NIR + SWIR)

def gndvi(NIR, Green):
    return safe_divide(NIR - Green, NIR + Green)

def ndre(NIR, RedEdge):
    return safe_divide(NIR - RedEdge, NIR + RedEdge)

def rvi(NIR, Red):
    return safe_divide(NIR, Red)

def tsavi(NIR, Red, a=0.5, X=0.08):
    return a * safe_divide(NIR - a * Red - X, Red + a * NIR + X)

def arvi(NIR, Red, Blue):
    return safe_divide(NIR - (2 * Red - Blue), NIR + (2 * Red - Blue))

def dvi(NIR, Red):
    return NIR - Red

def wdrvi(NIR, Red, a=0.1):
    return safe_divide(a * NIR - Red, a * NIR + Red)

def main(NIR, Red, Blue, SWIR, Green, RedEdge):
    results = {
        "NDVI": ndvi(NIR, Red),
        "EVI": evi(NIR, Red, Blue),
        "SAVI": savi(NIR, Red),
        "NDWI": ndwi(NIR, SWIR),
        "GNDVI": gndvi(NIR, Green),
        "NDRE": ndre(NIR, RedEdge),
        "RVI": rvi(NIR, Red),
        "TSAVI": tsavi(NIR, Red),
        "ARVI": arvi(NIR, Red, Blue),
        "DVI": dvi(NIR, Red),
        "WDRVI": wdrvi(NIR, Red)
    }

    print(json.dumps(results, indent=4))

if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: python v_Indices.py <NIR> <Red> <Blue> <SWIR> <Green> <RedEdge>")
        sys.exit(1)

    NIR = int(sys.argv[1])
    Red = int(sys.argv[2])
    Blue = int(sys.argv[3])
    SWIR = int(sys.argv[4])
    Green = int(sys.argv[5])
    RedEdge = int(sys.argv[6])
    main(NIR, Red, Blue, SWIR, Green, RedEdge)