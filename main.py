mySprite = sprites.create(assets.image("""
        Hover_Bike_Right_1
        """),
    SpriteKind.player)
mySprite2 = sprites.create(assets.image("""
        Hover_Bike_Right _2
        """),
    SpriteKind.player)
mySprite3 = sprites.create(assets.image("""
        Hover_Bike_Left_1
        """),
    SpriteKind.player)
mySprite4 = sprites.create(assets.image("""
        Hoover_Bike_Left_2
        """),
    SpriteKind.player)
rd = assets.image("""
    HWY_Tile
    """)
MWall = img("""
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
        1 c c c c c c c c c c c c c c 8
        1 c b b b b b b b b b b b b c 8
        1 c b f f f f f f f f f f b c 8
        1 c b f 8 8 8 8 8 8 8 8 f b c 8
        1 c b f 8 c c c c c c 8 f b c 8
        1 c b f 8 c f f f f c 8 f b c 8
        1 c b f 8 c f 1 1 f c 8 f b c 8
        1 c b f 8 c f 1 1 f c 8 f b c 8
        1 c b f 8 c f f f f c 8 f b c 8
        1 c b f 8 c c c c c c 8 f b c 8
        1 c b f 8 8 8 8 8 8 8 8 f b c 8
        1 c b f f f f f f f f f f b c 8
        1 c b b b b b b b b b b b b c 8
        1 c c c c c c c c c c c c c c 8
        8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8
    """)

ckka = img("""
    f f f f f f f f f f f f f f f f
    f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f
    f 5 f f f f f f f f f f f f 5 f
    f 5 f 4 4 4 4 4 4 4 4 4 4 f 5 f
    f 5 f 4 5 5 5 5 5 5 5 5 4 f 5 f
    f 5 f 4 5 1 1 5 5 1 1 5 4 f 5 f
    f 5 f 4 5 1 1 5 5 1 1 5 4 f 5 f
    f 5 f 4 5 5 5 1 1 5 5 5 4 f 5 f
    f 5 f 4 5 5 5 1 1 5 5 5 4 f 5 f
    f 5 f 4 5 1 1 1 1 1 1 5 4 f 5 f
    f 5 f 4 5 1 1 1 1 1 1 5 4 f 5 f
    f 5 f 4 5 5 5 5 5 5 5 5 4 f 5 f
    f 5 f 4 4 4 4 4 4 4 4 4 4 f 5 f
    f 5 f f f f f f f f f f f f 5 f
    f 5 5 5 5 5 5 5 5 5 5 5 5 5 5 f
    f f f f f f f f f f f f f f f f
""")
chkb = img("""
    f f f f f f f f f f f f f f f f
    f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f
    f 2 f f f f f f f f f f f f 2 f
    f 2 f 2 2 2 2 2 2 2 2 2 2 f 2 f
    f 2 f 2 1 1 1 1 1 1 1 1 2 f 2 f
    f 2 f 2 1 2 2 1 1 2 2 1 2 f 2 f
    f 2 f 2 1 2 2 1 1 2 2 1 2 f 2 f
    f 2 f 2 1 1 1 2 2 1 1 1 2 f 2 f
    f 2 f 2 1 1 2 2 2 2 1 1 2 f 2 f
    f 2 f 2 1 2 1 2 2 1 2 1 2 f 2 f
    f 2 f 2 1 2 1 1 1 1 2 1 2 f 2 f
    f 2 f 2 1 1 1 1 1 1 1 1 2 f 2 f
    f 2 f 2 2 2 2 2 2 2 2 2 2 f 2 f
    f 2 f f f f f f f f f f f f 2 f
    f 2 2 2 2 2 2 2 2 2 2 2 2 2 2 f
    f f f f f f f f f f f f f f f f
""")
chkc = img("""
    f f f f f f f f f f f f f f f f
    f 8 9 9 9 9 9 9 9 9 9 9 9 9 8 f
    f 9 8 8 8 8 8 8 8 8 8 8 8 8 9 f
    f 9 8 9 9 9 9 9 9 9 9 9 9 8 9 f
    f 9 8 9 1 1 1 1 1 1 1 1 9 8 9 f
    f 9 8 9 1 8 8 9 9 8 8 1 9 8 9 f
    f 9 8 9 1 8 9 1 1 9 8 1 9 8 9 f
    f 9 8 9 1 9 1 1 1 1 9 1 9 8 9 f
    f 9 8 9 1 9 1 1 1 1 9 1 9 8 9 f
    f 9 8 9 1 8 9 1 1 9 8 1 9 8 9 f
    f 9 8 9 1 8 8 9 9 8 8 1 9 8 9 f
    f 9 8 9 1 1 1 1 1 1 1 1 9 8 9 f
    f 9 8 9 9 9 9 9 9 9 9 9 9 8 9 f
    f 9 8 8 8 8 8 8 8 8 8 8 8 8 9 f
    f 8 9 9 9 9 9 9 9 9 9 9 9 9 8 f
    f f f f f f f f f f f f f f f f
""")
chkd = img("""
    f f f f f f f f f f f f f f f f
    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f
    f 7 f f f f f f f f f f f f 7 f
    f 7 f 7 6 7 6 7 6 7 6 7 6 f 7 f
    f 7 f 6 1 6 1 6 1 6 1 6 1 f 7 f
    f 7 f 7 6 7 6 7 6 7 6 7 6 f 7 f
    f 7 f 6 1 6 1 1 1 1 6 1 6 f 7 f
    f 7 f 7 6 7 1 6 6 1 7 6 7 f 7 f
    f 7 f 6 1 6 1 6 6 1 6 1 6 f 7 f
    f 7 f 7 6 7 6 1 1 6 7 6 7 f 7 f
    f 7 f 6 1 6 1 6 1 6 1 6 1 f 7 f
    f 7 f 7 6 7 6 7 6 7 6 7 6 f 7 f
    f 7 f 6 7 6 7 6 7 6 7 6 7 f 7 f
    f 7 f f f f f f f f f f f f 7 f
    f 7 7 7 7 7 7 7 7 7 7 7 7 7 7 f
    f f f f f f f f f f f f f f f f
""")
chke = img("""
    f f f f f f f f f f f f f f f f
    f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f
    f 4 f f f f f f f f f f f f 4 f
    f 4 f 4 5 4 5 4 5 4 5 4 5 f 4 f
    f 4 f 5 2 2 2 2 2 2 2 2 5 f 4 f
    f 4 f 4 2 4 4 4 4 4 4 2 4 f 4 f
    f 4 f 5 2 4 5 5 5 5 4 2 5 f 4 f
    f 4 f 4 2 4 5 1 1 5 4 2 4 f 4 f
    f 4 f 5 2 4 5 1 1 5 4 2 5 f 4 f
    f 4 f 4 2 4 5 5 5 5 4 2 4 f 4 f
    f 4 f 5 2 4 4 4 4 4 4 2 5 f 4 f
    f 4 f 4 2 2 2 2 2 2 2 2 4 f 4 f
    f 4 f 5 4 5 4 5 4 5 4 5 4 f 4 f
    f 4 f f f f f f f f f f f f 4 f
    f 4 4 4 4 4 4 4 4 4 4 4 4 4 4 f
    f f f f f f f f f f f f f f f f
""")
chkf = img("""
    f f f f f f f f f f f f f f f f
    f 1 9 8 1 9 8 1 1 8 9 1 8 9 1 f
    f 9 1 1 9 8 9 b b 9 8 9 1 1 9 f
    f 8 1 b b b b 9 9 b b b b 1 8 f
    f 1 9 b 9 9 9 1 1 9 9 9 b 9 1 f
    f 9 8 b 9 1 1 8 8 1 1 9 b 8 9 f
    f 8 9 b 9 1 8 b b 8 1 9 b 9 8 f
    f 1 b b 1 8 b 1 1 b 8 1 b b 1 f
    f 1 b b 1 8 b 1 1 b 8 1 b b 1 f
    f 8 9 b 9 1 8 b b 8 1 9 b 9 8 f
    f 9 8 b 9 1 1 8 8 1 1 9 b 8 9 f
    f 1 9 b 9 9 9 1 1 9 9 9 b 9 1 f
    f 8 1 b b b b 9 9 b b b b 1 8 f
    f 9 1 1 9 8 9 b b 9 8 9 1 1 9 f
    f 1 9 8 1 9 8 1 1 8 9 1 8 9 1 f
    f f f f f f f f f f f f f f f f
""")
chkg = img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    """)