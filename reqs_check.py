from pip._internal.operations import freeze

DEPENDENCIES = ['selenium', ]

for inst_pkg in freeze.freeze():
    for dep_pkg in DEPENDENCIES:
        if inst_pkg.find(dep_pkg) != -1:
            DEPENDENCIES.remove(dep_pkg)
            break

assert (len(DEPENDENCIES) == 0), "Missing packages: %s" % " ".join(DEPENDENCIES)
