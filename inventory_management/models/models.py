from odoo import models, fields, api

class InventoryItem(models.Model):
    _name = 'inventory.item'
    _description = 'Inventory Item'

    name = fields.Char(string="Item Name", required=True)
    sku = fields.Char(string="SKU", required=True, unique=True)
    quantity = fields.Integer(string="Quantity", default=0)
    price = fields.Float(string="Unit Price")
    supplier = fields.Char(string="Supplier")
    category = fields.Selection([
        ('electronics', 'Electronics'),
        ('furniture', 'Furniture'),
        ('clothing', 'Clothing'),
    ], string="Category")

    @api.model
    def update_from_api(self, data):
        """ Met à jour l'inventaire avec des données externes """
        for item in data:
            existing_item = self.search([('sku', '=', item['sku'])], limit=1)
            if existing_item:
                existing_item.write({'quantity': item['quantity']})
            else:
                self.create({
                    'name': item['name'],
                    'sku': item['sku'],
                    'quantity': item['quantity'],
                    'price': item['price'],
                    'supplier': item['supplier'],
                    'category': item['category']
                })
