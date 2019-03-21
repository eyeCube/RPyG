#engine.py

#   TO MAINTAIN ORDER:
#Nothing in this file should EVER have references to other game files.
#This is just a resource of functions, classes, etc. to be used by the
#game file. The game files reference this file, never the other way around.

#   Naming convention:
#-All constants begin with a capitalized letter and use underscores
#-All class names capitalize each word and are as terse as possible.
#-All function names use underscores, no capitalization at all.

#   todo:
#

import pygame
import math
import queue
from dataclasses import dataclass, field
from typing import Any


#Prioritized Item
#Used for priority queues when you don't want to compare the items,
#just the priority values (int).
@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
    

#Point
    #Pixel point on the game window where (0,0) is the top-left corner
    #and y increases going downward.
@dataclass
class Point:
    x: int
    y: int
    
#Cube
class Cube:
    def __init__(self,x,y,z):
        self._x=x
        self._y=y
        self._z=z
    @property
    def x(self): return self._x
    @property
    def y(self): return self._y
    @property
    def z(self): return self._z
    def __add__(self,cube):
        x = self.x + cube.x
        y = self.y + cube.y
        z = self.z + cube.z
        return Cube(x, y, z)
    def __sub__(self,cube):
        x = self.x - cube.x
        y = self.y - cube.y
        z = self.z - cube.z
        return Cube(x, y, z)
    def __mul__(self, k): #scalar multiplication
        return Cube(self.x * k, self.y * k, self.z * k)
Cube_directions=[ #neighbors, ccw starting @ 0 degs. (0,60,120,180,240,300)
    Cube( 1, -1, 0), Cube( 1, 0, -1), Cube( 0, 1, -1),
    Cube(-1, 1, 0), Cube(-1, 0, 1), Cube( 0, -1, 1),
    ]

#Hex
class Hex:
    def __init__(self,q=0,r=0):
        self._q=q #column
        self._r=r #row
    @property
    def q(self): return self._q
    @property
    def r(self): return self._r
    def __hash__(self): #hash as a tuple (q,r)
        return hash((self._q, self._r,))
    def __add__(self,_hex):
        q = self.q + _hex.q
        r = self.r + _hex.r
        return Hex(q, r)
    def __sub__(self,_hex):
        q = self.q - _hex.q
        r = self.r - _hex.r
        return Hex(q, r)
    def __eq__(self,other):
        if not isinstance(other, Hex):
            return False
        if self.q == other.q and self.r == other.r:
            return True
Axial_directions=[ #neighbors, ccw starting @ 0 degs. (0,60,120,180,240,300)
    Hex( 1, 0), Hex( 1,-1), Hex( 0,-1),
    Hex(-1, 0), Hex(-1, 1), Hex( 0, 1),
    ]







#FUNCTIONS


#cube functions
def cube_round(cube): #round the coords of a Cube
    rx = int(round(cube.x))
    ry = int(round(cube.y))
    rz = int(round(cube.z))
    x_diff = abs(rx - cube.x)
    y_diff = abs(ry - cube.y)
    z_diff = abs(rz - cube.z)
    if (x_diff > y_diff and x_diff > z_diff):
        rx = -ry - rz
    elif y_diff > z_diff:
        ry = -rx - rz
    else:
        rz = -rx - ry
    return Cube(rx, ry, rz)
def cube_distance(a, b):
    return (abs(a.x - b.x) + abs(a.y - b.y) + abs(a.z - b.z))//2
def lerp(a, b, t): #lerp for floats
    return a + (b - a) * t
def cube_lerp(a, b, t): #lerp for cubes
    return Cube(lerp(a.x, b.x, t),
                lerp(a.y, b.y, t),
                lerp(a.z, b.z, t))
#def cube_scale(c, k): #not needed, member function __mul__ used instead
#    return Cube(c.x * k, c.y * k, c.z * k)
def cube_direction(direction): #get a Hex direction from an integer 0-5
    return Cube_directions[direction]
def cube_neighbor(cube, direction): #return a neighbor in the given direction
    _dir = cube_direction(direction)
    return Cube(cube.x + _dir.x, cube.y + _dir.y, cube.z + _dir.z)

#Hex / Cube conversion
def cube_to_axial(cube):
    q = cube.x
    r = cube.z
    return Hex(q, r)
def axial_to_cube(_hex):
    x = _hex.q
    z = _hex.r
    y = -x - z
    return Cube(x, y, z)

#Hex functions
def hex_round(_hex): #round the coords of a Hex
    return cube_to_axial(cube_round(axial_to_cube(_hex)))
def hex_vertex(point,size,i): #get the ith vertex of a hexagon
    angle_deg = 60 * i - 30
    angle_rad = math.pi / 180 * angle_deg
    return Point(point.x + size * math.cos(angle_rad),
                 point.y + size * math.sin(angle_rad))
def hex_direction(direction): #get a Hex direction from an integer 0-5
    return Axial_directions[direction]
def hex_neighbor(_hex, direction): #return a neighbor in the given direction
    _dir = hex_direction(direction)
    return Hex(_hex.q + _dir.q, _hex.r + _dir.r)
def hex_neighbors(_hex): #return all 6 neighbor Hexes to the given Hex
    _list = []
    for _hexdir in Axial_directions:
        _list.append(_hex + _hexdir)
    return _list
def hex_distance(a, b): #distance btn. two tiles or Hexes
    return cube_distance(axial_to_cube(a), axial_to_cube(b))
def hex_linedraw(a, b, extend=0): #return a list of tiles between 2 hexes
#extend is how many extra tiles to add into the list after reaching destination
    ac = axial_to_cube(a)
    bc = axial_to_cube(b)
    n = cube_distance(ac, bc)
    if not n:
        results = [a,]
    else:
        results = []
        for i in range(0, n + 1 + extend):
            cube = cube_round(cube_lerp(ac, bc, 1.0/n*i))
            results.append(cube_to_axial(cube))
    return results
def hex_range(center, r): #return the tiles within range r of Hex center
    results = []
    for x in range(-r, r + 1):
        for y in range(max(-r, -x - r), min(r, -x + r) + 1):
            z = -x - y
            results.append(center + cube_to_axial(Cube(x, y, z)))
    return results
def pixel_to_hex(point,size,offsetx,offsety): #get a hex tile from a Point
    point = Point(point.x - offsetx, point.y - offsety)
    q = (math.sqrt(3)/3*point.x - 1/3*point.y)/size
    r = (                         2/3*point.y)/size
    return hex_round(Hex(q, r))
def hex_to_pixel(_hex,size,offsetx,offsety): #get a Point onscreen from a Hex tile location
    x = size*(math.sqrt(3)*_hex.q + math.sqrt(3)/2*_hex.r)
    y = size*(                                 3/2*_hex.r)
    point = Point(x + offsetx, y + offsety)
    return point
def hex_ring(centerHex, radius):
    results = []
    if radius <= 0: return results; #radius must be pos. integer
    center = axial_to_cube(centerHex)
    #scalar multiplication. Argument 4 is arbitrary.
    cube = center + (cube_direction(4)*radius) 
    for i in range(0, 6):
        for j in range(0, radius):
            results.append(cube_to_axial(cube))
            cube = cube_neighbor(cube, i)
    return results



#drawing
def hex_draw(disp,point,size,col): #draw hex polygon fill
    vertices = []
    for i in range(6):
        v = hex_vertex(point,size,i)
        vertices.append((v.x,v.y,))
    pygame.draw.polygon(disp, col, vertices)
def hex_draw_outline(disp,origin,size,col,width=1): #draw hex polygon lines
    vertices = []
    for i in range(6):
        v = hex_vertex(origin,size,i)
        vertices.append((v.x,v.y,))
    pygame.draw.polygon(disp, col, vertices, width)


#pathfinding
def get_path(start, goal, Map, solidHexes=None): # A* algorithm
    frontier = queue.PriorityQueue()
    frontier.put(PrioritizedItem(0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        currentHex = current.item

        if currentHex == goal: #early exit
            break;

        for neighbor in hex_neighbors(currentHex):
            if neighbor not in Map.getMap(): #out of bounds
                continue
            
            #terrain cost
            new_cost = cost_so_far[currentHex] + Map.terrainCost(currentHex, neighbor)
            
            #solid hexes to avoid, such as those occupied by units
            if solidHexes is not None:
                if (neighbor != start and neighbor != goal):
                    if neighbor in solidHexes:
                        new_cost = 999999
                        
            if (neighbor not in cost_so_far
                or new_cost < cost_so_far[neighbor]):
                cost_so_far[neighbor] = new_cost
                #in A*, priority adds heuristic to the actual cost
                heuristic = hex_distance(neighbor, goal)
                priority = new_cost + heuristic #lower is higher priority
                frontier.put(PrioritizedItem(priority, neighbor))
                came_from[neighbor] = currentHex
    current = goal
    path = []
    while not current == start:
        path.append(current)
        current = came_from[current]
    #path.append(start) #optional
    path.reverse() #optional
    
    return path














'''def get_(start, Map):
    frontier = queue.Queue()
    frontier.put(start)
    came_from = {}
    #cost_so_far = {}
    came_from[start] = None
    #cost_so_far[start] = 0
    
    while not frontier.empty():
        currentHex = frontier.get()

        if currentHex: #early exit
            break;

        for neighbor in hex_neighbors(currentHex):
            if neighbor not in Map.getMap():
                continue
            new_cost = cost_so_far[currentHex] + Map.terrainCost(currentHex, neighbor)
            if (neighbor not in cost_so_far
            or new_cost < cost_so_far[neighbor]):
                cost_so_far[neighbor] = new_cost
                #in A*, priority adds heuristic to the actual cost
                priority = new_cost + hex_distance(currentHex, neighbor)
                frontier.put(PrioritizedItem(priority, neighbor))
                came_from[neighbor] = currentHex
    current = goal
    path = []
    while not current == start:
        path.append(current)
        current = came_from[current]
    path.append(start) #optional
    #path.reverse() #optional
    
    return path
    '''


'''
    start = Hex(3,6)
    goal = Hex(14,10)
    for _hex in path:
        drawTile(_hex, COLOURS['red'], COLOURS['deep'])
        pygame.display.update()
'''
'''
def get_path_dijkstra(start, goal, Map): # dijkstra algorithm
    frontier = queue.PriorityQueue()
    frontier.put(PrioritizedItem(0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    i = 0
    while not frontier.empty():
        i += 1
        current = frontier.get()
        currentHex = current.item

        if currentHex == goal: #early exit
            break;

        for neighbor in hex_neighbors(currentHex):
            if neighbor not in Map.getMap():
                continue
            new_cost = cost_so_far[currentHex] + Map.terrainCost(currentHex, neighbor)
            if (neighbor not in cost_so_far
            or new_cost < cost_so_far[neighbor]):
                cost_so_far[neighbor] = new_cost
                #in dijkstra, the cost is not added to any heuristic.
                priority = new_cost
                frontier.put(PrioritizedItem(priority, neighbor))
                came_from[neighbor] = currentHex
    current = goal
    path = []
    while not current == start:
        path.append(current)
        current = came_from[current]
    path.append(start) #optional
    #path.reverse() #optional

    print(i)
    
    return path
    '''


























