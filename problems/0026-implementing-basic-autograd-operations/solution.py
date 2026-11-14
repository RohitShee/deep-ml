class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
    def __repr__(self):
        def fmt(x):
            return int(x) if float(x).is_integer() else round(x, 4)
        return f"Value(data={fmt(self.data)}, grad={fmt(self.grad)})"

    def __add__(self, other):
        return Value(self.data+other.data,{self,other},'+')

    def __mul__(self, other):
        return Value(self.data*other.data,{self,other},'*')


    def relu(self):
        return Value(max(0,self.data),{self},'ReLU')


    def backward(self):
        topo,visited = [],set()

        def build(v) :
            if v not in visited:
                visited.add(v)
                for c in v._prev:
                    build(c)
                topo.append(v)
        build(self)
        self.grad=1
        for v in reversed(topo):
            if v._op == '+':
                for c in v._prev:
                    c.grad += v.grad
            elif v._op == '*':
                a, b = v._prev
                a.grad += b.data * v.grad
                b.grad += a.data * v.grad
            elif v._op == 'ReLU':
                (c,) = v._prev
                c.grad += (v.data > 0) * v.grad
        