class Vertex:
    def __init__(self, v):
        self.v = v-1
        self.side_v = []
        self.side_vinstance = []
        self.connection = set()
        self.connection_side = set()
        self.n_side = 0

    def __len__(self):
        return len(self.side_v)

    def v(self):
        return self.v

    def create_side(self, side_id, neibhor, vinstance_list):
        self.side_v.append((side_id, neibhor))
        self.side_vinstance.append(vinstance_list[neibhor])

    def count_neibhor(self):
        return self.side_v, self.side_vinstance

    def count_side_in_connection(self,
                                 connection = None,
                                 connection_side = None,
                                 side_count = 0,
                                 ):
        ### init
        if side_count == 0:
            # print(f"start to side_count of v in connection from {self.v}")
            pass
        else:
            self.connection = connection
            self.connection_side = connection_side

        ### 
        self.connection.add(self.v)
        for (side_id, side_v), side_vi in zip(self.side_v, self.side_vinstance):

            if side_id in self.connection_side:
                pass
            else:
                self.connection_side.add(side_id)
                side_count += 1
                
            #
            if side_v in self.connection:
                continue
            # 
            else:
                neibhor_side_count, neibhor_sides = side_vi.count_side_in_connection(
                    connection=self.connection,
                    connection_side=self.connection_side,
                    side_count=side_count
                )
                side_count = neibhor_side_count
                self.connection_side = self.connection_side | neibhor_sides
                
        self.side_count = side_count
        return side_count, self.connection_side

# initialize
flg = True
n, m = map(int, input().split())
sides = []
for _ in range(m):
    sides.append(tuple(map(int, input().split())))

# create vertex instances
vl = []
for i in range(1, n+1):
    v = Vertex(v=i)
    vl.append(v)

# process for each sides.
for i, (sv, ev) in enumerate(sides):
    vl[sv-1].create_side(i, ev-1, vl)
    if sv != ev:
        vl[ev-1].create_side(i, sv-1, vl)

# count each connection
side_c = []
for v in vl:
    side_c.append(v.count_side_in_connection())
# print(f"num of sides which each v has : {side_c}")

sv = set(range(n))
counted_connection = set()
# print('---')
for i, v in enumerate(vl):

    ### if the v is already connected, skip
    if (v.connection - counted_connection) == set():
        continue

    # print(f"v{i} >>> vertex: {len(v.connection)} side: {len(v.connection_side)}")
    if len(v.connection) != len(v.connection_side):
        flg = False
        break
    # print(f"    before sv:{sv} conn: {v.connection}")
    sv = sv - v.connection

    counted_connection = counted_connection | v.connection
    # print(f"    after sv:{sv}")
    
    # print(f"== len{len(v)}")
    if sv == set():
        continue


if flg:
    print("Yes")
else:
    print("No")
