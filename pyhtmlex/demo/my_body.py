# -*- coding: UTF-8 -*-
from utils import *


def style_factory():
    style = Style()

    width = [200, 800]
    r_margin = 20
    l = width[0]
    r = width[1] - r_margin
    w = width[0] + width[1]
    h = 1000
    navi_h = 30
    navi_item_h = navi_h - 2
    style.add_tag("body", margin=0, font_size=12, font_family="微软雅黑")
    style.add_tag("p", text_indent=25)
    style.add_tag("pre", font_size=14, font_family="Consolas")
    style.add_tag("script", font_size=14, font_family="Consolas")
    style.add_class("topbox", width="100%", height=20, background="#aaa")
    style.add_class("top", width=w, height=20, background="#aaa", margin_left="auto", margin_right="auto")
    style.add_class("topleft", width=300, height=20, float="left")
    style.add_class("topright", width=300, height=20, float="right", text_align="right")
    style.add_class("center",  width=w, height="auto", margin="auto", clear="both")
    style.add_class("logo", width=w, height=100, background="#9cf")
    style.add_class("navi", width=w, height=navi_h, color="#6cc")
    style.add_class("navi_item", width=100, height=navi_item_h, float="left",
                    margin_right=10, border="1px solid", text_align="center", line_height=navi_h)
    style.add_class("crumbs", width=w, height=20, background="#6c9")
    style.add_class("main", width=w, height="auto")
    style.add_class("left",  width=l, height=h, background="#cff", float="left")
    style.add_class("right", width=r, height="auto", float="left",
                    padding_left=r_margin/2, padding_right=r_margin/2, font_size=20)
    style.add_class("bottombox", width="100%", height=100, float="left", background="#9cf")

    return style


topbox = Div("topbox")
top = Div("top")
topbox.push_back(top)
topleft = Div("topleft")
topleft.inner_html = "welcome"
topright = Div("topright")
topright.inner_html = "add to fav"
top.push_back(topleft)
top.push_back(topright)

bottombox = Div("bottombox")

logo = Logo("logo", "/static/img/logo.jpg", "/")
navi = Navigate("navi", "navi_item", [
        # ("/books/1/", "BOOK"),
        ("/blog/lenovo", "LCTC"),
        ("/blog/python", "PYTHON"),
        ("/blog/openstack", "OPENSTACK")])


def body_factory(bread):
    body = Body()

    body.push_back(topbox)

    center = Div("center")
    body.push_back(center)
    body.push_back(bottombox)

    center.push_back(logo)
    center.push_back(navi)
    center.push_back(Breadcrumbs("crumbs", bread))

    main = Div("main")

    left = Div("left")
    main.push_back(left)
    right = Div("right")
    main.push_back(right)

    center.push_back(main)

    return body, [style_factory()], left, right
