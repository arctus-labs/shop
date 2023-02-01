from . import pcs
from . import flarc
from . import helpers

app = flarc.Flarc(__name__)
db = app.db
from . import models

from arctus.noctus.noctus import noctus
from arctus.accounts.accounts import accounts

app.register_blueprint(noctus)
app.register_blueprint(accounts)

app.run(port=1313, debug=True)
