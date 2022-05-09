def rgb(r, g, b):
    hex = '0123456789ABCDEF'
    r = min(255, max(0, r))
    g = min(255, max(0, g))
    b = min(255, max(0, b))
    return hex[r//16] + hex[r%16] + hex[g//16] + hex[g%16] + hex[b//16] + hex[b%16]