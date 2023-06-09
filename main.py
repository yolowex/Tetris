import traceback
import re
import sys

try:

    from core.common.names import *
    try:
        def version():
            v = pg.version
            return f"SDL version: {v.SDL}, pygame version: {v.ver}, python version: {sys.version}"

        print("[CHECKPOINT: Version] :", version())
    except Exception as e:
        print("[CHECKPOINT: Version] : Could not print Pygame's version",e)

    import core.common.resources as cr

    import gui.common.resources as guiCr

    from core.event_holder import EventHolder


    from gui.menu import Menu as guiMenu


    from gui.drawables.page import Page

    pg.init()
    scale = 50
    aspect_ratio = Vector2(9, 18)


    guiCr.screen = cr.screen = pg.display.set_mode(
        (aspect_ratio.x * scale, aspect_ratio.y * scale), SCALED | FULLSCREEN
    )


    guiCr.event_holder = cr.event_holder = EventHolder()
    cr.event_holder.should_render_debug = True

    rect = Rect(0, 0, 35, 35)
    edges = [rect.copy() for i in range(4)]

    edges[1].x = cr.screen.get_width() - edges[1].w
    edges[2].x = cr.screen.get_width() - edges[2].w
    edges[2].y = cr.screen.get_height() - edges[2].h
    edges[3].y = cr.screen.get_height() - edges[3].h


    menu = guiMenu(cr.screen,cr.event_holder)

    font = pg.font.SysFont("monospace",30)

    rect = cr.screen.get_rect()
    rect.x += rect.w * 0.1
    rect.y += rect.h * 0.1
    rect.w -= rect.w * 0.1 * 2
    rect.h -= rect.h * 0.1 * 2

    texts = [
        ["0;Play Game"],
        ["1;Settings"],
        ["2;Leaderboards"],
        ["3;Stats"],
        ["4;Quit"]
    ]

    page = Page(rect,texts,font)

    menu.add_page(page)
    menu.set_active(0)


    while not cr.event_holder.should_quit:
        cr.screen.fill("gray")
        cr.event_holder.get_events()


        if cr.event_holder.should_render_debug:
            for rect in edges:
                pg.draw.rect(cr.screen,"black",rect,width=2)

        menu.check_events()
        menu.render()

        pg.display.update()

except Exception as e:
    error_message = re.sub(r'\s+', ' ', traceback.format_exc())
    print("[Checkpoint:Error]", error_message.strip())
