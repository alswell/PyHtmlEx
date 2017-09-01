from pyhtmlex.base.head import *
from pyhtmlex.base.body import *


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