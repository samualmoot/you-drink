import sys

# Ensure we import all other settings
# The settings imported below will be flattened into this module, similar
# to `import *` using `flatten_module_attributes`.
import web.settings  # noqa: F401
import web.settings.tests  # noqa: F401
from web.settings.utils import flatten_module_attributes

TEST_RUNNER = "xmlrunner.extra.djangotestrunner.XMLTestRunner"
TEST_OUTPUT_DIR = "test-reports/pyunittest"
TEST_OUTPUT_FILE_NAME = "results.xml"

# Flatten imported settings / attributes from sub-components to make it
# look like one module
flatten_module_attributes(
    module=sys.modules[__name__], imports=list(sys.modules.keys()), prefix="web.settings"
)
