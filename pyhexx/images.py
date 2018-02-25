
# This is the 256-color palette used by HEXX. Colors are in in 0xRRGGBB format.
thumbnail_palette = [
    0x000000, 0x220607, 0x2F070B, 0x3C0F13, 0x4E1616, 0x5A1E1E, 0x662B26, 0x773132,
    0x83403A, 0x904C42, 0xA1584E, 0xAD645A, 0xBD7466, 0xCA8272, 0xD6927F, 0xE6A38F,
    0x835EFF, 0x8663FF, 0x8E6FFF, 0x947AFF, 0x9B84FF, 0x9F88FF, 0xA692FF, 0xAD9CFF,
    0xB0A0FF, 0xB8AAFF, 0xBFB3FF, 0xC7BDFF, 0xCBC1FF, 0xD2CAFF, 0xDAD3FF, 0xE1DCFF,
    0x001600, 0x002300, 0x003400, 0x004600, 0x005700, 0x006800, 0x007900, 0x008B00,
    0x009C00, 0x00A800, 0x00B900, 0x00CA00, 0x00DC00, 0x00ED00, 0x00FE00, 0x00FF00,
    0x170015, 0x240021, 0x350032, 0x480043, 0x590054, 0x6A0064, 0x7C0074, 0x8E0086,
    0x9F0096, 0xAC00A2, 0xBD00B3, 0xCE00C3, 0xE000D4, 0xF100E5, 0xFF15F5, 0xFF38FF,
    0x020015, 0x020022, 0x060032, 0x0D0044, 0x120054, 0x180065, 0x200075, 0x280087,
    0x310097, 0x3800A3, 0x4100B4, 0x4C14C4, 0x5928D6, 0x6437E6, 0x7045F6, 0x7F58FF,
    0x141502, 0x1F2105, 0x2F3205, 0x3F4304, 0x4F5403, 0x5F6400, 0x6E7500, 0x7F8600,
    0x8E9700, 0x9AA300, 0xAAB400, 0xB9C400, 0xCAD600, 0xD9E600, 0xE9F700, 0xF9FF00,
    0x170000, 0x230000, 0x340000, 0x460000, 0x570000, 0x680000, 0x790000, 0x8B0000,
    0x9C0000, 0xA90000, 0xBA0000, 0xCB0000, 0xDD0000, 0xEE0000, 0xFF0000, 0xFF0000,
    0x220F07, 0x2E170A, 0x3F230C, 0x502A14, 0x5C3717, 0x6D441E, 0x7D5025, 0x8A6127,
    0x9A6D2E, 0xAA7D37, 0xB58F3D, 0xC69F44, 0xD6B04B, 0xE1C152, 0xF0D258, 0xFFE764,
    0x001602, 0x002206, 0x022F0D, 0x003B0F, 0x044917, 0x165523, 0x1D622B, 0x2B6E37,
    0x3A7A45, 0x468751, 0x599361, 0x659F6E, 0x78AB7F, 0x8FB694, 0xA0C1A4, 0xB6CDB9,
    0x220607, 0x2B080B, 0x371013, 0x45171B, 0x521F23, 0x5E272B, 0x662F33, 0x723D40,
    0x7E494C, 0x8C5558, 0x976568, 0x9F7274, 0xAB8385, 0xB69496, 0xC2A4A6, 0xCEB9BA,
    0x170115, 0x230221, 0x30072D, 0x3D073A, 0x4B0E47, 0x571D53, 0x64245F, 0x70316B,
    0x7C3F77, 0x8A4B84, 0x955D90, 0xA1699C, 0xAD7BA8, 0xB891B4, 0xC3A2BF, 0xCFB7CC,
    0x011514, 0x022120, 0x062D2C, 0x063A38, 0x0D4745, 0x1B5351, 0x235F5D, 0x306B6A,
    0x3E7776, 0x4A8483, 0x5C908F, 0x689C9B, 0x7BA8A7, 0x91B4B2, 0xA2BFBE, 0xB7CCCB,
    0x050215, 0x0A0521, 0x130B2E, 0x180E3A, 0x201647, 0x2C2253, 0x342A60, 0x40366C,
    0x4D4478, 0x585085, 0x686191, 0x746D9D, 0x847EA9, 0x9893B4, 0xA8A4C0, 0xBBB8CC,
    0x230000, 0x380000, 0x4F0000, 0x640000, 0x7D0000, 0x930000, 0xA80200, 0xC11E00,
    0xC93F00, 0xD15D00, 0xD77900, 0xE29500, 0xE7B000, 0xECD000, 0xF0EA00, 0xF9FF00,
    0x220600, 0x2F0800, 0x400F01, 0x511C00, 0x5E2403, 0x6E300A, 0x7F3D12, 0x8B4E19,
    0x9C5A27, 0xAC6B33, 0xB87B45, 0xC98D51, 0xD99D61, 0xE3B276, 0xF3C38C, 0xFFD7A0,
    0x101010, 0x1C1C1C, 0x2C2C2C, 0x3C3C3C, 0x494949, 0x595959, 0x696969, 0x757575,
    0x868686, 0x969696, 0xA2A2A2, 0xB2B2B2, 0xC3C3C3, 0xCFCFCF, 0xDFDFDF, 0xEFEFEF,
]
thumbnail_palette = zip(
    ((rgb & 0xFF0000) >> 16 for rgb in thumbnail_palette),
    ((rgb & 0x00FF00) >> 8 for rgb in thumbnail_palette),
    ((rgb & 0x0000FF) >> 0 for rgb in thumbnail_palette),
)
assert len(thumbnail_palette) == 256

def rgb_distance(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

def thumbnail_palette_closest(rgb):
    def key(p):
        return rgb_distance(rgb, thumbnail_palette[p])
    return sorted(range(256), key=key)[0]

def hexx_thumbnail_from_file(png_fname, w, h):
    try:
        from PIL import Image
    except ImportError:
        assert False, "Run 'pip install pillow' to install the PIL module"
    input_image = Image.open(png_fname).convert('RGB').resize((w, h), Image.LANCZOS)
    assert input_image.size == (w, h)
    input_data = [
        [input_image.getpixel((x, y)) for x in range(w)] for y in range(h)
    ]
    output_data = [None] * (w * h)
    for y in range(h):
        for x in range(w):
            rgb = input_data[y][x]
            p = thumbnail_palette_closest(rgb)
            output_data[y*w+x] = p
            error = map(operator.div, map(operator.sub, thumbnail_palette[p], rgb), [16.0]*3)
            if (x+1 < w):
                input_data[y][x+1] = tuple(map(operator.add, input_data[y][x+1], map(operator.mul, error, [7]*3)))
            if (y+1 < h):
                if (0 <= x-1):
                    input_data[y+1][x-1] = tuple(map(operator.add, input_data[y+1][x-1], map(operator.mul, error, [3]*3)))
                input_data[y+1][x] = tuple(map(operator.add, input_data[y+1][x], map(operator.mul, error, [5]*3)))
                if (x+1 < w):
                    input_data[y+1][x+1] = tuple(map(operator.add, input_data[y+1][x+1], map(operator.mul, error, [1]*3)))
    return ''.join(map(chr, output_data))

def dump_hexx_thumbnail(png_fname, content, w):
    try:
        from PIL import Image
    except ImportError:
        assert False, "Run 'pip install pillow' to install the PIL module"
    h = (len(content) + w - 1) / w
    content = content.ljust(w * h, '\0')
    output_image = Image.new('RGB', (w, h))
    for y in range(h):
        for x in range(w):
            p = ord(content[y*w+x])
            output_image.putpixel((x, y), thumbnail_palette[p])
    output_image.save(png_fname, 'PNG')