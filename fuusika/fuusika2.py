import math

def cart2cyl(x, y, z):
    ro = math.sqrt(x**2+y**2)
    theta = (math.atan(y/x))
    z = z
    return ro, theta, z

def cyl2cart(ro, theta, z):
    x = ro*math.cos(theta)
    y = ro*math.sin(theta)
    z = z
    return x, y, z

def cart2sphere(x, y, z):
    r = math.sqrt(x**2+y**2+z**2)
    theta = math.atan(y/x)
    fi = math.atan((math.sqrt(x**2+y**2)/z))
    return r, theta, fi

def sphere2cart(r, theta, fi):
    x = r*math.sin(fi)*math.cos(theta)
    y = r*math.sin(fi)*math.sin(theta)
    z = r*math.cos(fi)
    return x, y, z