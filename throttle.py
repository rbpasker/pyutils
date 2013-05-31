
# in-thread throttle function decorator. 
# only works on void functions 
def throttle(fn, sec):
    ns = Namespace()
    ns.lasttime = time.time()
    ns.interval = sec

    def throttled(*args, **kwargs):
        ns.currenttime = time.time()
        ns.delta = ns.currenttime - ns.lasttime
        if (ns.delta > (ns.interval)):
            ns.lasttime = ns.currenttime
            fn(*args, **kwargs)

    return throttled
