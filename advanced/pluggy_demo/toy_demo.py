import pluggy

hookspec = pluggy.HookspecMarker("myproject")
hookimpl = pluggy.HookimplMarker("myproject")


class MySpec(object):
    """A hook specification namespace."""

    @hookspec
    def myhook(self, arg1, arg2):
        """My special little hook that you can customize."""


class MySpec2(object):
    """A hook specification namespace."""

    @hookspec(firstresult=True)
    def myhook(self, arg1, arg2):
        """My special little hook that you can customize."""


class Plugin_1(object):
    """A hook implementation namespace."""

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_1.myhook()")
        return 1


class Plugin_2(object):
    """A 2nd hook implementation namespace."""

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_2.myhook()")
        return 2


class Plugin_3(object):
    """A 2nd hook implementation namespace."""

    @hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_3.myhook()")
        return 3


# create a manager and add the spec
pm = pluggy.PluginManager("myproject")
pm.add_hookspecs(MySpec)

# register plugins
pm.register(Plugin_1())
pm.register(Plugin_2())
# call our `myhook` hook
results = pm.hook.myhook(arg1=1, arg2=2)
print(results)

pm2 = pluggy.PluginManager("myproject")
pm2.add_hookspecs(MySpec2)
pm2.register(Plugin_1())
pm2.register(Plugin_2())
pm2.register(Plugin_3())
results2 = pm2.hook.myhook(arg1=1, arg2=2)
print(results2)
