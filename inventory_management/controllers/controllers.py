from odoo import http
from odoo.http import request
import json

class InventoryAPI(http.Controller):

    @http.route('/api/inventory/update', type='json', auth='user', methods=['POST'])
    def update_inventory(self, **post):
        try:
            data = post.get('data', [])
            if data:
                request.env['inventory.item'].sudo().update_from_api(data)
                return {"success": True, "message": "Inventory updated successfully"}
            return {"success": False, "message": "No data provided"}
        except Exception as e:
            return {"success": False, "message": str(e)}
