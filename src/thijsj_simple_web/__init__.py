## begin license ##
#
# Learn creating a simple website and hosting it using containers.
#
# Copyright (C) 2023 Thijs Janssen https://thijsj.nl
#
# This file is part of "Simple Container Website"
#
# "Simple Container Website" is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "Simple Container Website" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Simple Container Website".  If not, see <http://www.gnu.org/licenses/>.
#
## end license ##

from quart import Quart
from quart.templating import render_template

app = Quart(__name__)

@app.route('/')
async def index():
    return await render_template('index.html', title="Index <pagina>")

