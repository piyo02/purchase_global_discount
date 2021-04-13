from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare
from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class PurchaseConfigSettings(models.TransientModel):
    _inherit = "purchase.config.settings"

    discount_product_id = fields.Many2one(
        'product.product', 
        string='Discount Product',
         help='The product used to model the discount.')
        
    account_payable_id = fields.Many2one(
        'account.account',
        string='Account Payable',
        help='The product used to model the account payable.'
    )