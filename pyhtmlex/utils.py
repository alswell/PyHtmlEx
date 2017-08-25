# -*- coding: UTF-8 -*-
import copy
from base.head import *
from base.body import *


def lazy_head(title, styles):
    head = Head()
    meta = Meta()
    meta.set_attributes(http_equiv="Content-Type", content="text/html; charset=utf-8")
    head.push_back(meta)
    # head.push_back(Css("static/css/test.css"))
    for style in styles:
        head.push_back(style)
    head.push_back(Title(title))
    return head


class Logo(Div):
    def __init__(self, cls_name, pic_path, link):
        super(Logo, self).__init__(cls_name)
        a = A(link)
        a.push_back(Img(pic_path))
        self.children.append(a)


class Navigate(Div):
    def __init__(self, cls_name, sub_cls_name, name_links):
        super(Navigate, self).__init__(cls_name)
        for name_link in name_links:
            div = Div(sub_cls_name)
            a = A(*name_link)
            div.push_back(a)
            self.children.append(div)


class Breadcrumbs(Div):
    def __init__(self, cls_name, name_links):
        super(Breadcrumbs, self).__init__(cls_name)
        for name_link in name_links:
            a = A(*name_link)
            self.children.append(a)
            txt = Text(">>")
            self.children.append(txt)
        self.children.pop()


class ColorTable(Table):
    def __init__(self, r, c, w=120, color=['#fff', '#0ac']):
        if r < 2:
            r = 2
        if c < 2:
            c = 2
        margin = 0
        total_width = 0
        if isinstance(w, list):
            if len(w) < c:
                for i in range(len(w), c):
                    w.append(120)
            for i in range(c):
                total_width += w[i] + margin * 2
        else:
            w = [w] * c
            total_width = c * (w + margin * 2)

        self.style = Style()
        self.style.add_class('x_table', width=total_width, float='left',
                             text_align='center', word_wrap='break-word', word_break='break-all')
        self.style.add_class('x_cell_top', width=total_width, float='left', background=color[1],
                             margin=margin, border_top='5px double', border_bottom='2px dashed')
        self.style.add_class('x_cell_bottom', width=total_width, float='left', background=color[r % 2],
                             margin=margin, border_bottom='5px double')
        self.style.add_class('x_cell_1', width=total_width, float='left', background=color[0],
                             margin=margin)
        self.style.add_class('x_cell_2', width=total_width, float='left', background=color[1],
                             margin=margin)
        super(ColorTable, self).__init__('x_table')

        row_top = Tr('x_cell_top')
        for i in range(c):
            row_top.push_back(Th(w[i]))
        self.children.append(row_top)

        row_1 = Tr('x_cell_1')
        for i in range(c):
            row_1.push_back(Td(w[i]))
        row_2 = Tr('x_cell_2')
        for i in range(c):
            row_2.push_back(Td(w[i]))
        for i in range(r-2):
            if i % 2 == 0:
                self.children.append(copy.deepcopy(row_1))
            else:
                self.children.append(copy.deepcopy(row_2))

        row_bottom = Tr('x_cell_bottom')
        for i in range(c):
            row_bottom.push_back(Td(w[i]))
        self.children.append(row_bottom)

    def __call__(self, r, c=None):
        if c is None:
            return self.children[r]
        return self.children[r].children[c]


python_key = [
    'False', 'class', 'finally', 'is', 'return',
    'None', 'continue', 'for', 'lambda', 'try',
    'True', 'def', 'from', 'nonlocal', 'while',
    'and', 'del', 'global', 'not', 'with',
    'as', 'elif', 'if', 'or', 'yield',
    'assert', 'else', 'import', 'pass',
    'break', 'except', 'in', 'raise', 'print']


def get_words(line):
    words = []
    i = 0
    while i < len(line):
        start1 = line.find("'", i)
        start2 = line.find('"', i)
        if start1 == start2 == -1:
            words.extend([(word + ' ') for word in line[i:].strip('\n').split(' ')])
            words[-1] = words[-1].strip()
            return words
        if start1 == -1:
            start1 = start2 + 1
        if start2 == -1:
            start2 = start1 + 1

        if start1 < start2:
            end = line.find("'", start1 + 1)
            # print line[start1:end + 1]
            words.extend([(word + ' ') for word in line[i:start1].strip('\n').split(' ')])
            words[-1] = words[-1].strip()
            words.append(line[start1:end + 1])
        else:
            end = line.find('"', start2 + 1)
            # print line[start2:end + 1]
            words.extend([(word + ' ') for word in line[i:start2].strip('\n').split(' ')])
            words[-1] = words[-1].strip()
            words.append(line[start2:end + 1])
        i = end + 1


class Code(Div):
    style = Style()
    style.add_class("code", margin=0, display='block', overflow='auto')
    style.add_class("code_line1", background="#ccc")
    style.add_class("code_line2", background="#aca")
    style.add_class("code_key", color="#00a", font_weight="bold")
    style.add_class("code_interpreter", color="#aaa", font_weight="bold")
    style.add_class("code_comment", color="#0a0", font_weight="bold")
    style.add_class("code_plain", color="#000")
    style.add_class("code_str", color="#900")

    def __init__(self, lines):
        super(Code, self).__init__('code')

        pre = Pre()
        pre.set_attributes(style='display:inline-block; *display:inline; *zoom:1;')
        ol = Ol()
        pre.push_back(ol)
        i = 0
        cls_name = ['code_line1', 'code_line2']
        for line in lines:
            i = (i + 1) % 2
            li = Li(cls_name=cls_name[i])
            raw_line = line.strip()
            if len(raw_line) > 1 and raw_line[:2] == '#!':
                li.push_back(Span(line, 'code_interpreter'))
            elif len(raw_line) > 0 and raw_line[0] == '#':
                li.push_back(Span(line, 'code_comment'))
            else:
                # words = line.strip('\n').split(' ')
                words = get_words(line)
                for word in words:
                    if len(word) > 0 and (word[0] == '"' or word[0] == "'"):
                        li.push_back(Span(word, 'code_str'))
                    elif word.strip() in python_key:
                        li.push_back(Span(word, 'code_key'))
                    else:
                        li.push_back(Span(word, 'code_plain'))
            ol.push_back(li)
        self.children.append(pre)


class Console(Div):
    style = Style()
    style.add_class("console", margin=0, color='#0a0', background='#000', display='block', overflow='auto')

    def __init__(self, lines):
        super(Console, self).__init__('console')

        pre = Pre()
        ul = Ul()
        pre.push_back(ul)
        ul.set_attributes(style="list-style-type:none")
        for line in lines:
            script = Script(line)
            script.set_attributes(type='text/html', style="display:block")
            li = Li()
            li.push_back(script)
            ul.push_back(li)
        self.children.append(pre)
