from pprint import pprint

class Point:
    color = 'red'
    circle = 2

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

pt = Point
val = 46

def introspection_info(obj):
    type_obj = type(obj)
    attr = []
    mtd = []
    for attr_and_mtd in dir(obj):
        if attr_and_mtd[0:2] == '__':
            attr.append(attr_and_mtd)
        else:
            mtd.append(attr_and_mtd)
    if type_obj == int:
        info = {'type': type_obj, 'attributes': attr, 'methods': mtd, 'module': []}

    else:
        name_obj = obj.__name__
        module_obj = obj.__module__
        info = {'name': name_obj, 'type': type_obj, 'attributes': attr, 'methods': mtd, 'module': module_obj}
    pprint(info)


introspection_info(pt)
