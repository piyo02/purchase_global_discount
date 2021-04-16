from odoo import api, fields, models, _

import logging
_logger = logging.getLogger(__name__)

class DiscountGlobalSetting(models.TransientModel):
    _name = "discount.global.settings"

    discount_product_id = fields.Many2one(
        'product.product', string='Discount Product',
        help='The product used to model the discount.')
        
    account_payable_id = fields.Many2one(
        'account.account', string='Account Payable',
        help='The product used to model the account payable.')