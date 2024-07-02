# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Gokul PI (<https://www.cybrosys.com>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """This class is inheriting the model 'product.product', It contains
    fields  for the model.  """
    _inherit = 'res.config.settings'

    measurement_id_analytics = fields.Char(
        config_parameter=
        'google_analytics_odoo.measurement_id_analytics',
        string='Measurement ID',
        help='Measurement id of the google analytics')
    api_secret = fields.Char(
        config_parameter=
        'google_analytics_odoo.api_secret',
        string='API Secret',
        help='API secret of the google analytics')
    enable_analytics = fields.Boolean(config_parameter=
                                      'google_analytics_odoo.enable_analytics',
                                      string='Enable Analytics',
                                      help='Enable to send events to'
                                           'google analytics')
